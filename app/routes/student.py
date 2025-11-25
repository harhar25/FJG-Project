from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from sqlalchemy import and_
from app import db
from app.models import Laboratory, Course, LabSchedule, Notification

student_bp = Blueprint('student', __name__, url_prefix='/student')

def student_required(f):
    """Decorator to check if user is student"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'Student':
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@student_bp.route('/dashboard')
@login_required
@student_required
def dashboard():
    """Student dashboard"""
    today = datetime.utcnow().date()
    week_end = today + timedelta(days=7)
    
    # Get upcoming schedules
    upcoming_schedules = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= today,
            LabSchedule.scheduled_date <= week_end,
            LabSchedule.status == 'Reserved'
        )
    ).order_by(LabSchedule.scheduled_date).limit(5).all()
    
    return render_template('student/dashboard.html', upcoming_schedules=upcoming_schedules)

@student_bp.route('/schedule/by-lab')
@login_required
@student_required
def schedule_by_lab():
    """View schedule filtered by lab room"""
    lab_id = request.args.get('lab_id', type=int)
    week_start_str = request.args.get('week_start')
    
    if week_start_str:
        week_start = datetime.strptime(week_start_str, '%Y-%m-%d').date()
    else:
        today = datetime.utcnow().date()
        week_start = today - timedelta(days=today.weekday())
    
    week_end = week_start + timedelta(days=7)
    
    query = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= week_start,
            LabSchedule.scheduled_date < week_end,
            LabSchedule.status == 'Reserved'
        )
    )
    
    if lab_id:
        query = query.filter_by(lab_id=lab_id)
    
    schedules = query.order_by(LabSchedule.scheduled_date, LabSchedule.start_time).all()
    labs = Laboratory.query.filter_by(is_active=True).all()
    
    return render_template('student/schedule_by_lab.html',
                         schedules=schedules,
                         labs=labs,
                         week_start=week_start,
                         selected_lab_id=lab_id,
                         timedelta=timedelta)

@student_bp.route('/schedule/by-instructor')
@login_required
@student_required
def schedule_by_instructor():
    """View schedule filtered by instructor"""
    instructor_id = request.args.get('instructor_id', type=int)
    week_start_str = request.args.get('week_start')
    
    if week_start_str:
        week_start = datetime.strptime(week_start_str, '%Y-%m-%d').date()
    else:
        today = datetime.utcnow().date()
        week_start = today - timedelta(days=today.weekday())
    
    week_end = week_start + timedelta(days=7)
    
    from app.models import User
    
    query = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= week_start,
            LabSchedule.scheduled_date < week_end,
            LabSchedule.status == 'Reserved'
        )
    )
    
    if instructor_id:
        query = query.filter_by(created_by=instructor_id)
    
    schedules = query.order_by(LabSchedule.scheduled_date, LabSchedule.start_time).all()
    instructors = User.query.filter_by(role='Instructor', is_active=True).all()
    
    return render_template('student/schedule_by_instructor.html',
                         schedules=schedules,
                         instructors=instructors,
                         week_start=week_start,
                         selected_instructor_id=instructor_id,
                         timedelta=timedelta)

@student_bp.route('/schedule/by-section')
@login_required
@student_required
def schedule_by_section():
    """View schedule filtered by course section"""
    course_id = request.args.get('course_id', type=int)
    week_start_str = request.args.get('week_start')
    
    if week_start_str:
        week_start = datetime.strptime(week_start_str, '%Y-%m-%d').date()
    else:
        today = datetime.utcnow().date()
        week_start = today - timedelta(days=today.weekday())
    
    week_end = week_start + timedelta(days=7)
    
    query = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= week_start,
            LabSchedule.scheduled_date < week_end,
            LabSchedule.status == 'Reserved'
        )
    )
    
    if course_id:
        query = query.filter_by(course_id=course_id)
    
    schedules = query.order_by(LabSchedule.scheduled_date, LabSchedule.start_time).all()
    courses = Course.query.filter_by(is_active=True).all()
    
    return render_template('student/schedule_by_section.html',
                         schedules=schedules,
                         courses=courses,
                         week_start=week_start,
                         selected_course_id=course_id,
                         timedelta=timedelta)

@student_bp.route('/notifications')
@login_required
@student_required
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
    
    return render_template('student/notifications.html', notifications=notifications)
