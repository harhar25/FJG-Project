from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, timedelta, timezone
from sqlalchemy import and_, or_
from app import db
from app.models import (
    Laboratory, Course, LabSchedule, 
    ReservationRequest, Notification, UserRole, UserRole
)

instructor_bp = Blueprint('instructor', __name__, url_prefix='/instructor')

def instructor_required(f):
    """Decorator to check if user is instructor"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'Instructor':
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@instructor_bp.route('/dashboard')
@login_required
@instructor_required
def dashboard():
    """Instructor dashboard"""
    today = datetime.now(timezone.utc).date()
    week_end = today + timedelta(days=7)
    
    # Get upcoming sessions
    upcoming_sessions = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= today,
            LabSchedule.scheduled_date <= week_end
        )
    ).order_by(LabSchedule.scheduled_date).all()
    
    # Get pending requests
    pending_requests = ReservationRequest.query.filter_by(
        instructor_id=current_user.id,
        status='Pending'
    ).count()
    
    # Get unread notifications
    unread_notifications = Notification.query.filter_by(
        user_id=current_user.id,
        is_read=False
    ).count()
    
    return render_template('instructor/dashboard.html',
                         upcoming_sessions=upcoming_sessions,
                         pending_requests=pending_requests,
                         unread_notifications=unread_notifications)

@instructor_bp.route('/submit-request', methods=['GET', 'POST'])
@login_required
@instructor_required
def submit_request():
    """Submit reservation request"""
    if request.method == 'POST':
        lab_id = request.form.get('lab_id', type=int)
        course_id = request.form.get('course_id', type=int)
        requested_date = request.form.get('requested_date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        reason = request.form.get('reason')
        
        # Validate
        if not all([lab_id, course_id, requested_date, start_time, end_time, reason]):
            flash('All fields are required.', 'error')
            return redirect(url_for('instructor.submit_request'))
        
        requested_date = datetime.strptime(requested_date, '%Y-%m-%d').date()
        start_time = datetime.strptime(start_time, '%H:%M').time()
        end_time = datetime.strptime(end_time, '%H:%M').time()
        
        # Check for conflicts
        conflicts = LabSchedule.query.filter(
            and_(
                LabSchedule.lab_id == lab_id,
                LabSchedule.scheduled_date == requested_date,
                or_(
                    and_(LabSchedule.start_time <= start_time, LabSchedule.end_time > start_time),
                    and_(LabSchedule.start_time < end_time, LabSchedule.end_time >= end_time),
                    and_(LabSchedule.start_time >= start_time, LabSchedule.end_time <= end_time)
                ),
                LabSchedule.status.in_(['Reserved', 'Maintenance'])
            )
        ).first()
        
        if conflicts:
            flash('The selected time slot is not available.', 'error')
            return redirect(url_for('instructor.submit_request'))
        
        # Create request
        res_request = ReservationRequest(
            instructor_id=current_user.id,
            lab_id=lab_id,
            course_id=course_id,
            requested_date=requested_date,
            start_time=start_time,
            end_time=end_time,
            reason=reason,
            status='Pending'
        )
        db.session.add(res_request)
        db.session.commit()
        
        flash('Reservation request submitted successfully.', 'success')
        return redirect(url_for('instructor.dashboard'))
    
    labs = Laboratory.query.filter_by(is_active=True).all()
    courses = Course.query.all()
    
    return render_template('instructor/submit_request.html', labs=labs, courses=courses)

@instructor_bp.route('/view-schedule')
@login_required
@instructor_required
def view_schedule():
    """View weekly schedule"""
    week_start_str = request.args.get('week_start')
    
    if week_start_str:
        week_start = datetime.strptime(week_start_str, '%Y-%m-%d').date()
    else:
        today = datetime.now(timezone.utc).date()
        week_start = today - timedelta(days=today.weekday())
    
    week_end = week_start + timedelta(days=7)
    
    schedules = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= week_start,
            LabSchedule.scheduled_date < week_end
        )
    ).order_by(LabSchedule.scheduled_date, LabSchedule.start_time).all()
    
    labs = Laboratory.query.filter_by(is_active=True).all()
    
    return render_template('instructor/view_schedule.html',
                         schedules=schedules,
                         labs=labs,
                         week_start=week_start,
                         timedelta=timedelta)

@instructor_bp.route('/my-requests')
@login_required
@instructor_required
def my_requests():
    """View my reservation requests"""
    page = request.args.get('page', 1, type=int)
    
    requests = ReservationRequest.query.filter_by(
        instructor_id=current_user.id
    ).order_by(ReservationRequest.created_at.desc()).paginate(page=page, per_page=10)
    
    return render_template('instructor/my_requests.html', requests=requests)

@instructor_bp.route('/notifications')
@login_required
@instructor_required
def notifications():
    """View notifications"""
    page = request.args.get('page', 1, type=int)
    
    notifications = Notification.query.filter_by(
        user_id=current_user.id
    ).order_by(Notification.created_at.desc()).paginate(page=page, per_page=10)
    
    # Mark as read
    unread = Notification.query.filter_by(user_id=current_user.id, is_read=False).all()
    for notif in unread:
        notif.is_read = True
    db.session.commit()
    
    return render_template('instructor/notifications.html', notifications=notifications)

@instructor_bp.route('/profile', methods=['GET', 'POST'])
@login_required
@instructor_required
def profile():
    """Instructor profile page"""
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        email = request.form.get('email')

        # Validate
        if not all([full_name, username, email]):
            flash('All fields are required.', 'error')
            return redirect(url_for('instructor.profile'))

        # Check for uniqueness
        if User.query.filter(User.id != current_user.id, User.username == username).first():
            flash('Username already exists.', 'error')
            return redirect(url_for('instructor.profile'))
        
        if User.query.filter(User.id != current_user.id, User.email == email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('instructor.profile'))

        current_user.full_name = full_name
        current_user.username = username
        current_user.email = email
        db.session.commit()

        flash('Profile updated successfully.', 'success')
        return redirect(url_for('instructor.profile'))

    return render_template('auth/edit_profile.html')
