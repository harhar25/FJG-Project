from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from datetime import datetime
from app import db
from app.models import Notification, LabSchedule, Laboratory

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/notifications/unread', methods=['GET'])
@login_required
def get_unread_notifications():
    """Get unread notifications count"""
    count = Notification.query.filter_by(
        user_id=current_user.id,
        is_read=False
    ).count()
    
    return jsonify({'unread_count': count})

@api_bp.route('/notifications/mark-read/<int:notification_id>', methods=['POST'])
@login_required
def mark_notification_read(notification_id):
    """Mark notification as read"""
    notification = Notification.query.get_or_404(notification_id)
    
    if notification.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    notification.is_read = True
    db.session.commit()
    
    return jsonify({'success': True})

@api_bp.route('/schedule/time-blocks', methods=['GET'])
@login_required
def get_schedule_time_blocks():
    """Get schedule time blocks for a specific day and lab"""
    lab_id = request.args.get('lab_id', type=int)
    date_str = request.args.get('date')
    
    if not lab_id or not date_str:
        return jsonify({'error': 'Missing parameters'}), 400
    
    schedule_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    schedules = LabSchedule.query.filter_by(
        lab_id=lab_id,
        scheduled_date=schedule_date
    ).order_by(LabSchedule.start_time).all()
    
    time_blocks = []
    for schedule in schedules:
        time_blocks.append({
            'id': schedule.id,
            'start_time': schedule.start_time.strftime('%H:%M'),
            'end_time': schedule.end_time.strftime('%H:%M'),
            'status': schedule.status,
            'course': schedule.course.course_name if schedule.course else '',
            'instructor': schedule.course.instructor_id if schedule.course else '',
            'section': schedule.course.section if schedule.course else ''
        })
    
    return jsonify({
        'lab_id': lab_id,
        'date': date_str,
        'time_blocks': time_blocks
    })

@api_bp.route('/labs', methods=['GET'])
@login_required
def get_labs():
    """Get all active labs"""
    from app.models import Laboratory
    
    labs = Laboratory.query.filter_by(is_active=True).all()
    
    return jsonify([{
        'id': lab.id,
        'name': lab.lab_name,
        'code': lab.lab_code,
        'capacity': lab.capacity,
        'location': lab.location
    } for lab in labs])
