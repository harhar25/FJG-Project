from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timedelta, timezone
from sqlalchemy import func, and_, or_
from app import db
from app.models import (
    User, Laboratory, LabSchedule, ReservationRequest, Notification, LabUsageReport, UserRole, Course
)

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    """Decorator to check if user is admin"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'Administrator':
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    # Admin dashboard
    """Admin dashboard with quick stats"""
    total_labs = Laboratory.query.filter_by(is_active=True).count()
    total_sessions = LabSchedule.query.count()
    pending_requests = ReservationRequest.query.filter_by(status='Pending').count()

    # Chart data: Reservation requests in the last 7 days
    today = datetime.now(timezone.utc).date()
    last_7_days = [today - timedelta(days=i) for i in range(7)]
    chart_data = []
    for day in reversed(last_7_days):
        count = ReservationRequest.query.filter(
            func.date(ReservationRequest.created_at) == day
        ).count()
        chart_data.append({'date': day.strftime('%a, %b %d'), 'count': count})

    return render_template('admin/dashboard.html',
                         total_labs=total_labs,
                         total_sessions=total_sessions,
                         pending_requests=pending_requests,
                         chart_data=chart_data)

@admin_bp.route('/manage-labs', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_labs():
    """Manage laboratory rooms"""
    page = request.args.get('page', 1, type=int)
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'add':
            lab_name = request.form.get('lab_name')
            lab_code = request.form.get('lab_code')
            capacity = request.form.get('capacity', type=int)
            location = request.form.get('location')
            equipment = request.form.get('equipment')
            
            if Laboratory.query.filter_by(lab_code=lab_code).first():
                flash('Lab code already exists.', 'error')
                return redirect(url_for('admin.manage_labs'))
            
            lab = Laboratory(
                lab_name=lab_name,
                lab_code=lab_code,
                capacity=capacity,
                location=location,
                equipment=equipment
            )
            db.session.add(lab)
            db.session.commit()
            flash('Laboratory added successfully.', 'success')
        
        elif action == 'edit':
            lab_id = request.form.get('lab_id', type=int)
            lab = Laboratory.query.get_or_404(lab_id)
            lab.lab_name = request.form.get('lab_name')
            lab.capacity = request.form.get('capacity', type=int)
            lab.location = request.form.get('location')
            lab.equipment = request.form.get('equipment')
            db.session.commit()
            flash('Laboratory updated successfully.', 'success')
        
        elif action == 'delete':
            lab_id = request.form.get('lab_id', type=int)
            lab = Laboratory.query.get_or_404(lab_id)
            lab.is_active = False
            db.session.commit()
            flash('Laboratory deactivated successfully.', 'success')
        
        return redirect(url_for('admin.manage_labs'))
    
    labs = Laboratory.query.paginate(page=page, per_page=10)
    return render_template('admin/manage_labs.html', labs=labs)

@admin_bp.route('/manage-instructors', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_instructors():
    """Manage instructors"""
    page = request.args.get('page', 1, type=int)
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'add':
            username = request.form.get('username')
            email = request.form.get('email')
            full_name = request.form.get('full_name')
            password = request.form.get('password')
            
            if User.query.filter_by(username=username).first():
                flash('Username already exists.', 'error')
                return redirect(url_for('admin.manage_instructors'))
            
            user = User(
                username=username,
                email=email,
                full_name=full_name,
                role='Instructor'
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Instructor added successfully.', 'success')
        
        elif action == 'deactivate':
            user_id = request.form.get('user_id', type=int)
            user = User.query.get_or_404(user_id)
            user.is_active = not user.is_active
            db.session.commit()
            flash(f'Instructor {"activated" if user.is_active else "deactivated"} successfully.', 'success')
        
        return redirect(url_for('admin.manage_instructors'))
    
    instructors = User.query.filter_by(role='Instructor').paginate(page=page, per_page=10)
    return render_template('admin/manage_instructors.html', instructors=instructors)

@admin_bp.route('/add-instructor', methods=['GET', 'POST'])
@login_required
@admin_required
def add_instructor():
    """Add a new instructor"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return redirect(url_for('admin.add_instructor'))
        
        user = User(
            username=username,
            email=email,
            full_name=full_name,
            role='Instructor'
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Instructor added successfully.', 'success')
        return redirect(url_for('admin.manage_instructors'))
    
    return render_template('admin/add_instructor.html')

# New route for viewing instructor details
@admin_bp.route('/instructor/<int:user_id>', methods=['GET'])
@login_required
@admin_required
def view_instructor(user_id):
    """View instructor details"""
    instructor = User.query.get_or_404(user_id)
    return render_template('admin/instructor_details.html', instructor=instructor)

# Updated routes to use POST method
@admin_bp.route('/instructor/<int:user_id>/activate', methods=['POST'])
@login_required
@admin_required
def activate_instructor(user_id):
    """Activate an instructor account"""
    user = User.query.get_or_404(user_id)
    user.is_active = True
    db.session.commit()
    flash(f'Instructor {user.username} has been activated.', 'success')
    return redirect(url_for('admin.view_instructor', user_id=user_id))

@admin_bp.route('/instructor/<int:user_id>/deactivate', methods=['POST'])
@login_required
@admin_required
def deactivate_instructor(user_id):
    """Deactivate an instructor account"""
    user = User.query.get_or_404(user_id)
    user.is_active = False
    db.session.commit()
    flash(f'Instructor {user.username} has been deactivated.', 'warning')
    return redirect(url_for('admin.view_instructor', user_id=user_id))

@admin_bp.route('/instructor/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_instructor(user_id):
    """Delete an instructor account"""
    user = User.query.get_or_404(user_id)
    username = user.username
    db.session.delete(user)
    db.session.commit()
    flash(f'Instructor {username} has been deleted.', 'success')
    return redirect(url_for('admin.manage_instructors'))

@admin_bp.route('/instructor/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_instructor(user_id):
    """Edit an instructor's details"""
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.full_name = request.form.get('full_name')
        
        # Only update password if provided
        new_password = request.form.get('password')
        if new_password:
            user.set_password(new_password)
        
        db.session.commit()
        flash('Instructor updated successfully.', 'success')
        return redirect(url_for('admin.view_instructor', user_id=user_id))
    
    return render_template('admin/edit_instructor.html', instructor=user)

@admin_bp.route('/view-schedule')
@login_required
@admin_required
def view_schedule():
    """View all schedules"""
    lab_id = request.args.get('lab_id', type=int)
    week_start = request.args.get('week_start')
    
    if week_start:
        week_start = datetime.strptime(week_start, '%Y-%m-%d').date()
    else:
        today = datetime.now(timezone.utc).date()
        week_start = today - timedelta(days=today.weekday())
    
    week_end = week_start + timedelta(days=7)
    
    query = LabSchedule.query.filter(
        and_(
            LabSchedule.scheduled_date >= week_start,
            LabSchedule.scheduled_date < week_end
        )
    )
    
    if lab_id:
        query = query.filter_by(lab_id=lab_id)
    
    schedules = query.order_by(LabSchedule.scheduled_date, LabSchedule.start_time).all()
    labs = Laboratory.query.filter_by(is_active=True).all()
    
    return render_template('admin/view_schedule.html',
                         schedules=schedules,
                         labs=labs,
                         week_start=week_start,
                         week_end=week_end,
                         selected_lab_id=lab_id,
                         timedelta=timedelta,
                         datetime=datetime)

@admin_bp.route('/approve-requests', methods=['GET', 'POST'])
@login_required
@admin_required
def approve_requests():
    """Approve or decline reservation requests"""
    page = request.args.get('page', 1, type=int)
    
    if request.method == 'POST':
        request_id = request.form.get('request_id', type=int)
        action = request.form.get('action')
        
        reservation_request = ReservationRequest.query.get_or_404(request_id)
        
        if action == 'approve':
            reservation_request.status = 'Approved'
            reservation_request.approved_by = current_user.id
            reservation_request.approval_date = datetime.now(timezone.utc)
            
            # Create schedule entry
            schedule = LabSchedule(
                lab_id=reservation_request.lab_id,
                course_id=reservation_request.course_id,
                scheduled_date=reservation_request.requested_date,
                start_time=reservation_request.start_time,
                end_time=reservation_request.end_time,
                status='Reserved',
                created_by=current_user.id
            )
            db.session.add(schedule)
            
            # Create notification
            notification = Notification(
                user_id=reservation_request.instructor_id,
                title='Reservation Approved',
                message=f'Your lab reservation for {reservation_request.requested_date} has been approved.',
                notification_type='approval',
                related_request_id=request_id
            )
            db.session.add(notification)
            
            flash('Request approved successfully.', 'success')
        
        elif action == 'decline':
            reservation_request.status = 'Declined'
            reservation_request.approved_by = current_user.id
            reservation_request.approval_date = datetime.now(timezone.utc)
            
            # Create notification
            notification = Notification(
                user_id=reservation_request.instructor_id,
                title='Reservation Declined',
                message=f'Your lab reservation for {reservation_request.requested_date} has been declined.',
                notification_type='decline',
                related_request_id=request_id
            )
            db.session.add(notification)
            
            flash('Request declined successfully.', 'success')
        
        db.session.commit()
        return redirect(url_for('admin.approve_requests'))
    
    requests = ReservationRequest.query.filter_by(status='Pending').paginate(page=page, per_page=15)
    return render_template('admin/approve_requests.html', requests=requests)

@admin_bp.route('/manage-courses', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_courses():
    """Manage courses"""
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            course_code = request.form.get('course_code')
            course_name = request.form.get('course_name')
            if course_code and course_name:
                new_course = Course(course_code=course_code, course_name=course_name)
                db.session.add(new_course)
                db.session.commit()
                flash('Course added successfully.', 'success')
        elif action == 'delete':
            course_id = request.form.get('course_id')
            course = Course.query.get(course_id)
            if course:
                db.session.delete(course)
                db.session.commit()
                flash('Course deleted successfully.', 'success')
        return redirect(url_for('admin.manage_courses'))

    page = request.args.get('page', 1, type=int)
    courses = Course.query.paginate(page=page, per_page=10)
    return render_template('admin/manage_courses.html', courses=courses)

@admin_bp.route('/reports')
@login_required
@admin_required
def reports():
    """Generate and view reports"""
    report_type = request.args.get('type', 'monthly')
    month = request.args.get('month')
    
    if month:
        report_date = datetime.strptime(month, '%Y-%m').date()
    else:
        report_date = datetime.now(timezone.utc).date().replace(day=1)
    
    month_start = report_date
    month_end = (month_start + timedelta(days=32)).replace(day=1)
    
    # Get all labs with their usage stats
    labs_stats = []
    labs = Laboratory.query.filter_by(is_active=True).all()
    
    for lab in labs:
        sessions = LabSchedule.query.filter(
            and_(
                LabSchedule.lab_id == lab.id,
                LabSchedule.scheduled_date >= month_start,
                LabSchedule.scheduled_date < month_end,
                LabSchedule.status == 'Reserved'
            )
        ).all()
        
        total_hours = sum(
            (datetime.combine(datetime.min.date(), s.end_time) - 
             datetime.combine(datetime.min.date(), s.start_time)).total_seconds() / 3600
            for s in sessions
        )
        
        lab_hours_per_day = 11  # 8 AM to 7 PM
        max_hours_per_month = lab_hours_per_day * 30
        utilization_rate = (total_hours / max_hours_per_month * 100) if max_hours_per_month > 0 else 0
        
        labs_stats.append({
            'lab': lab,
            'sessions': len(sessions),
            'total_hours': round(total_hours, 2),
            'utilization_rate': round(utilization_rate, 2)
        })
    
    return render_template('admin/reports.html',
                         labs_stats=labs_stats,
                         report_month=month_start,
                         report_type=report_type)

@admin_bp.route('/notifications')
@login_required
@admin_required
def notifications():
    """Admin notifications"""
    page = request.args.get('page', 1, type=int)
    notifications = Notification.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=20)
    
    return render_template('admin/notifications.html', notifications=notifications)

@admin_bp.route('/schedule-history')
@login_required
@admin_required
def schedule_history():
    """View past schedules"""
    page = request.args.get('page', 1, type=int)
    today = datetime.now(timezone.utc).date()
    
    schedules = LabSchedule.query.filter(
        LabSchedule.scheduled_date < today
    ).order_by(LabSchedule.scheduled_date.desc()).paginate(page=page, per_page=15)
    
    return render_template('admin/schedule_history.html', schedules=schedules)