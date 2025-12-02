from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone
from app import db, login_manager
from enum import Enum

class UserRole(Enum):
    ADMIN = 'Administrator'
    INSTRUCTOR = 'Instructor'

class User(UserMixin, db.Model):
    """User model for authentication"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='Instructor')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    last_login = db.Column(db.DateTime)
    otp_secret = db.Column(db.String(16))
    otp_enabled = db.Column(db.Boolean, default=False)
    
    # Relationships
    notifications = db.relationship('Notification', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    submitted_requests = db.relationship('ReservationRequest', foreign_keys='ReservationRequest.instructor_id', backref='instructor', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if password matches hash"""
        return check_password_hash(self.password_hash, password)
    
    def get_totp_uri(self):
        return f'otpauth://totp/ITLabScheduler:{self.username}?secret={self.otp_secret}&issuer=ITLabScheduler'

    def verify_totp(self, token):
        import pyotp
        totp = pyotp.TOTP(self.otp_secret)
        return totp.verify(token)

    def __repr__(self):
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID"""
    return User.query.get(int(user_id))

class Laboratory(db.Model):
    """Laboratory/Lab room model"""
    __tablename__ = 'laboratories'
    
    id = db.Column(db.Integer, primary_key=True)
    lab_name = db.Column(db.String(100), nullable=False, unique=True)
    lab_code = db.Column(db.String(20), nullable=False, unique=True)
    capacity = db.Column(db.Integer, default=30)
    location = db.Column(db.String(150))
    equipment = db.Column(db.Text)  # Comma-separated or JSON
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships
    schedules = db.relationship('LabSchedule', backref='laboratory', lazy='dynamic', cascade='all, delete-orphan')
    requests = db.relationship('ReservationRequest', backref='lab', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Laboratory {self.lab_code}>'

class Course(db.Model):
    """Course model"""
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), nullable=False, unique=True)
    course_name = db.Column(db.String(150), nullable=False)
    credit_hours = db.Column(db.Integer)
    section = db.Column(db.String(20), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships
    schedules = db.relationship('LabSchedule', backref='course', lazy='dynamic', cascade='all, delete-orphan')
    requests = db.relationship('ReservationRequest', backref='course', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Course {self.course_code}>'

class LabSchedule(db.Model):
    """Laboratory schedule model"""
    __tablename__ = 'lab_schedules'
    
    id = db.Column(db.Integer, primary_key=True)
    lab_id = db.Column(db.Integer, db.ForeignKey('laboratories.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False, index=True)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default='Available')  # Available, Reserved, Maintenance, Conflict
    notes = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<LabSchedule {self.lab_id} on {self.scheduled_date}>'

class ReservationRequest(db.Model):
    """Reservation request model"""
    __tablename__ = 'reservation_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lab_id = db.Column(db.Integer, db.ForeignKey('laboratories.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    requested_date = db.Column(db.Date, nullable=False, index=True)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), default='Pending')  # Pending, Approved, Declined
    reason = db.Column(db.Text, nullable=False)
    approved_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    approval_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<ReservationRequest {self.id}>'

class Notification(db.Model):
    """Notification model"""
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(50))  # approval, decline, schedule_update
    related_request_id = db.Column(db.Integer, db.ForeignKey('reservation_requests.id'))
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True)
    
    def __repr__(self):
        return f'<Notification {self.id}>'

class LabUsageReport(db.Model):
    """Lab usage report/analytics model"""
    __tablename__ = 'lab_usage_reports'
    
    id = db.Column(db.Integer, primary_key=True)
    lab_id = db.Column(db.Integer, db.ForeignKey('laboratories.id'), nullable=False)
    report_month = db.Column(db.Date, nullable=False)
    total_sessions = db.Column(db.Integer, default=0)
    total_hours = db.Column(db.Float, default=0)
    peak_hour = db.Column(db.String(20))  # e.g., "2:00 PM - 3:00 PM"
    utilization_rate = db.Column(db.Float, default=0)  # Percentage
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<LabUsageReport {self.lab_id}>'
