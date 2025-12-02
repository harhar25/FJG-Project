import os
from flask import render_template
from app import create_app, db
from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Make models available in Flask shell"""
    return {
        'db': db,
        'User': User,
        'Laboratory': Laboratory,
        'Course': Course,
        'LabSchedule': LabSchedule,
        'ReservationRequest': ReservationRequest
    }

@app.before_request
def before_request():
    """Update last login time on every request"""
    from flask_login import current_user
    from datetime import datetime, timezone
    if current_user.is_authenticated:
        try:
            current_user.last_login = datetime.now(timezone.utc)
            db.session.commit()
        except:
            pass

    # Auto-delete past schedules
    try:
        today = datetime.now(timezone.utc).date()
        LabSchedule.query.filter(LabSchedule.scheduled_date < today).delete()
        db.session.commit()
    except:
        db.session.rollback()
        pass

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('errors/500.html'), 500

@app.route('/')
def index():
    """Root route - redirect to login or dashboard"""
    from flask_login import current_user
    if current_user.is_authenticated:
        if current_user.role == 'Administrator':
            return redirect(url_for('admin.dashboard'))
        elif current_user.role == 'Instructor':
            return redirect(url_for('instructor.dashboard'))
    # Not authenticated - go to login page
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    from flask import redirect, url_for
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
