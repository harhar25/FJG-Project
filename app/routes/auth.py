from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import pyotp
import qrcode
import io
import base64
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from datetime import datetime, timezone
from app import db
from app.models import User, UserRole

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Username and password are required.', 'error')
            return redirect(url_for('auth.login'))
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            if not user.is_active:
                flash('Your account has been deactivated.', 'error')
                return redirect(url_for('auth.login'))
            
            if user.otp_enabled:
                session['user_id_2fa'] = user.id
                return redirect(url_for('auth.verify_2fa'))
            
            login_user(user)
            user.last_login = datetime.now(timezone.utc)
            db.session.commit()
            
            # Redirect based on role
            if user.role == 'Administrator':
                return redirect(url_for('admin.dashboard'))
            elif user.role == 'Instructor':
                return redirect(url_for('instructor.dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """Handle user logout"""
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """User profile page"""
    return render_template('profile.html', user=current_user)

@auth_bp.route('/preferences')
@login_required
def preferences():
    """User preferences/settings page"""
    return render_template('preferences.html', user=current_user)

@auth_bp.route('/messages')
@login_required
def messages():
    """User messages page"""
    page = request.args.get('page', 1, type=int)
    # Placeholder for messages functionality
    return render_template('messages.html', page=page)

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Handle forgot password (simplified version)"""
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Password reset instructions have been sent to your email.', 'success')
        else:
            flash('If an account exists with this email, instructions have been sent.', 'info')
        
        return redirect(url_for('auth.login'))
    
    return render_template('forgot_password.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """User self-registration (public signup)"""
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role', 'Instructor')
        terms = request.form.get('terms')
        
        # Validate input
        if not all([full_name, username, email, password, confirm_password, role, terms]):
            flash('All fields are required.', 'error')
            return redirect(url_for('auth.signup'))
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('auth.signup'))
        
        if len(password) < 8:
            flash('Password must be at least 8 characters long.', 'error')
            return redirect(url_for('auth.signup'))
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('An account with this email already exists.', 'error')
            return redirect(url_for('auth.signup'))
        
        if User.query.filter_by(username=username).first():
            flash('An account with this username already exists.', 'error')
            return redirect(url_for('auth.signup'))
        
        try:
            # Map role names
            # Assign role, ensuring 'admin' or 'Administrator' becomes 'Administrator'
            assigned_role = 'Administrator' if role.lower() == 'admin' else 'Instructor'

            # Create new user
            user = User(
                username=username,
                email=email,
                full_name=full_name,
                role=assigned_role,
                is_active=True
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
        
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'error')
            return redirect(url_for('auth.signup'))
    
    return render_template('signup.html')


@auth_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Handle profile editing"""
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        email = request.form.get('email')

        # Validate
        if not all([full_name, username, email]):
            flash('All fields are required.', 'error')
            return redirect(url_for('auth.edit_profile'))

        # Check for uniqueness
        if User.query.filter(User.id != current_user.id, User.username == username).first():
            flash('Username already exists.', 'error')
            return redirect(url_for('auth.edit_profile'))
        
        if User.query.filter(User.id != current_user.id, User.email == email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('auth.edit_profile'))

        current_user.full_name = full_name
        current_user.username = username
        current_user.email = email
        db.session.commit()

        flash('Profile updated successfully.', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/edit_profile.html')

@auth_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    """Handle password change"""
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_new_password = request.form.get('confirm_new_password')

        if not all([current_password, new_password, confirm_new_password]):
            flash('All fields are required.', 'error')
            return redirect(url_for('auth.change_password'))

        if not current_user.check_password(current_password):
            flash('Incorrect current password.', 'error')
            return redirect(url_for('auth.change_password'))

        if new_password != confirm_new_password:
            flash('New passwords do not match.', 'error')
            return redirect(url_for('auth.change_password'))

        current_user.set_password(new_password)
        db.session.commit()

        flash('Password updated successfully.', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('auth/change_password.html')

@auth_bp.route('/setup-2fa', methods=['GET', 'POST'])
@login_required
def setup_2fa():
    """Handle 2FA setup"""
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'enable':
            current_user.otp_enabled = True
            db.session.commit()
            flash('2FA enabled successfully.', 'success')
        elif action == 'disable':
            current_user.otp_enabled = False
            db.session.commit()
            flash('2FA disabled successfully.', 'success')
        return redirect(url_for('auth.setup_2fa'))

    if not current_user.otp_secret:
        current_user.otp_secret = pyotp.random_base32()
        db.session.commit()

    qr_code = None
    if not current_user.otp_enabled:
        uri = current_user.get_totp_uri()
        img = qrcode.make(uri)
        buf = io.BytesIO()
        img.save(buf)
        buf.seek(0)
        qr_code = base64.b64encode(buf.getvalue()).decode('ascii')

    return render_template('auth/setup_2fa.html', qr_code=qr_code)


@auth_bp.route('/verify-2fa', methods=['GET', 'POST'])
def verify_2fa():
    """Handle 2FA verification"""
    user_id = session.get('user_id_2fa')
    if not user_id:
        return redirect(url_for('auth.login'))

    user = User.query.get(user_id)
    if not user:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        token = request.form.get('token')
        if user.verify_totp(token):
            session.pop('user_id_2fa', None)
            login_user(user)
            user.last_login = datetime.now(timezone.utc)
            db.session.commit()

            if user.role == 'Administrator':
                return redirect(url_for('admin.dashboard'))
            elif user.role == 'Instructor':
                return redirect(url_for('instructor.dashboard'))
        else:
            flash('Invalid 2FA token.', 'error')

    return render_template('auth/verify_2fa.html')

