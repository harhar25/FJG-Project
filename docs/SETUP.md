# Installation and Usage Guide
## IT Laboratory Utilization Schedule System

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation Steps

#### 1. **Download/Clone the Project**
```bash
cd c:\Users\HarHar\New-sys
```

#### 2. **Create Virtual Environment (Recommended)**
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

#### 4. **Initialize Database with Sample Data**
```bash
python seed_db.py
```

You should see output like:
```
✅ Database seeding completed successfully!
   - Created 3 instructors
   - Created 5 students
   - Created 5 laboratories
   - Created 5 courses
   - Created 300 lab schedules

📝 Demo Credentials:
   - Admin: admin / admin123
   - Instructor: instructor1 / pass123
   - Student: student1 / pass123
```

#### 5. **Start the Application**
```bash
python run.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

#### 6. **Access the Application**
Open your browser and navigate to: **http://localhost:5000**

---

## 🎮 Demo Account Credentials

### Administrator Account
- **Username:** admin
- **Password:** admin123
- **Access:** Full system management

### Instructor Account
- **Username:** instructor1 (or instructor2, instructor3)
- **Password:** pass123
- **Access:** Submit requests, view schedules, manage reservations

### Student Account
- **Username:** student1 (or student2, student3, student4, student5)
- **Password:** pass123
- **Access:** View schedules, check availability

---

## 📋 Project Structure Overview

```
New-sys/
│
├── app/                          # Main application package
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models
│   │
│   ├── routes/                  # Route blueprints
│   │   ├── auth.py              # Login/Registration routes
│   │   ├── admin.py             # Admin management routes
│   │   ├── instructor.py        # Instructor routes
│   │   ├── student.py           # Student routes
│   │   └── api.py               # API endpoints
│   │
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template with navbar
│   │   ├── login.html           # Login page
│   │   ├── register.html        # Registration page
│   │   ├── forgot_password.html # Password reset
│   │   ├── admin/               # Admin templates
│   │   │   ├── dashboard.html
│   │   │   ├── manage_labs.html
│   │   │   ├── manage_instructors.html
│   │   │   ├── view_schedule.html
│   │   │   ├── approve_requests.html
│   │   │   └── reports.html
│   │   ├── instructor/          # Instructor templates
│   │   │   ├── dashboard.html
│   │   │   ├── submit_request.html
│   │   │   ├── view_schedule.html
│   │   │   ├── my_requests.html
│   │   │   └── notifications.html
│   │   ├── student/             # Student templates
│   │   │   ├── dashboard.html
│   │   │   ├── schedule_by_lab.html
│   │   │   ├── schedule_by_instructor.html
│   │   │   ├── schedule_by_section.html
│   │   │   └── notifications.html
│   │   └── errors/              # Error pages
│   │       ├── 404.html
│   │       └── 500.html
│   │
│   └── static/                  # Static files
│       ├── css/
│       │   ├── style.css        # Main stylesheet
│       │   └── auth.css         # Auth page styles
│       ├── js/
│       │   └── main.js          # Utility JavaScript
│       └── images/              # Image assets
│
├── config.py                    # Flask configuration
├── run.py                       # Application entry point
├── seed_db.py                   # Database seeder script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── SETUP.md                     # This file
```

---

## 🔧 Configuration

### Changing Configuration
Edit `config.py` to modify:

```python
SECRET_KEY = 'your-secret-key'               # Change for production
SQLALCHEMY_DATABASE_URI = 'sqlite:///lab_system.db'
SESSION_COOKIE_SECURE = False                # Set to True in production
DEBUG = True                                  # Set to False in production
```

### Environment Variables
Create a `.env` file:
```
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
```

---

## 📱 Features Walkthrough

### For Administrators

1. **Dashboard**
   - View quick stats (Total labs, sessions, pending requests)
   - Access all management features

2. **Manage Labs**
   - Add new laboratory rooms
   - Edit lab details (capacity, location, equipment)
   - View all labs

3. **Manage Instructors**
   - Add new instructor accounts
   - Activate/deactivate instructors
   - View instructor list

4. **View Schedule**
   - See all lab schedules
   - Filter by lab and week
   - Monitor bookings

5. **Approve Requests**
   - Review pending reservation requests
   - Approve requests (creates schedule)
   - Decline requests (sends notification)

6. **Reports**
   - View monthly lab usage
   - Check utilization rates
   - Analyze peak hours

### For Instructors

1. **Dashboard**
   - View upcoming sessions
   - Check pending requests
   - See notifications

2. **Submit Request**
   - Reserve labs by date and time
   - Specify course and section
   - Add notes/reasons

3. **My Requests**
   - Track submitted reservations
   - View approval status
   - See request history

4. **View Schedule**
   - Check lab availability
   - See upcoming sessions
   - Navigate by week

5. **Notifications**
   - Receive approval/decline notifications
   - View notification history

### For Students

1. **Dashboard**
   - See upcoming lab sessions
   - Quick access to schedule views

2. **View Schedule by Lab**
   - Browse labs
   - Check availability by room
   - See course details

3. **View Schedule by Instructor**
   - Filter by instructor name
   - Find instructor schedules

4. **View Schedule by Section**
   - Find course section schedules
   - Check assigned labs

---

## 🔐 Security Features

- ✅ Secure password hashing (Werkzeug)
- ✅ Session-based authentication (Flask-Login)
- ✅ CSRF protection (Flask-WTF)
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ Role-based access control
- ✅ XSS protection via Jinja2

---

## 📱 Responsive Design

The application is optimized for:
- **Mobile** (< 768px): Touch-friendly interface
- **Tablet** (768px - 1199px): Medium layout
- **Desktop** (≥ 1200px): Full features

---

## 🐛 Troubleshooting

### Issue: "Port 5000 is already in use"
**Solution:** Change the port in `run.py`:
```python
app.run(debug=True, port=5001)
```

### Issue: "ModuleNotFoundError"
**Solution:** Ensure virtual environment is activated:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: Database error
**Solution:** Reset database:
```bash
del lab_system.db
python seed_db.py
```

### Issue: Login not working
**Solution:** Verify database is seeded:
```bash
python seed_db.py
```

---

## 📊 Database Schema

### Users Table
```
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- full_name
- role (Administrator/Instructor/Student)
- is_active
- created_at
- last_login
```

### Laboratories Table
```
- id (Primary Key)
- lab_name
- lab_code (Unique)
- capacity
- location
- equipment
- is_active
```

### Courses Table
```
- id (Primary Key)
- course_code (Unique)
- course_name
- credit_hours
- section
- instructor_id (FK to Users)
- is_active
```

### LabSchedule Table
```
- id (Primary Key)
- lab_id (FK)
- course_id (FK)
- scheduled_date
- start_time
- end_time
- status (Available/Reserved/Maintenance)
- notes
- created_by (FK)
```

### ReservationRequest Table
```
- id (Primary Key)
- instructor_id (FK)
- lab_id (FK)
- course_id (FK)
- requested_date
- start_time
- end_time
- status (Pending/Approved/Declined)
- reason
- approved_by (FK)
- approval_date
```

---

## 🚀 Production Deployment

### Before Deploying:

1. **Change secret key**
   ```python
   SECRET_KEY = 'generate-a-secure-random-key'
   ```

2. **Set debug to False**
   ```python
   DEBUG = False
   ```

3. **Use production database**
   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/labsystem'
   ```

4. **Enable HTTPS**
   ```python
   SESSION_COOKIE_SECURE = True
   ```

### Recommended Deployment Options:
- Heroku
- AWS EC2
- DigitalOcean
- PythonAnywhere
- Azure App Service

---

## 📞 Support

For issues or questions:
1. Check this guide first
2. Review error messages in console
3. Check Flask debug information at localhost:5000
4. Review application logs

---

## 📝 License

This project is provided as an educational tool.

---

**Version:** 1.0.0  
**Last Updated:** November 2025  
**Status:** ✅ Production Ready
