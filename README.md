# IT Laboratory Utilization Schedule System

A comprehensive, enterprise-level Flask web application for managing laboratory room schedules and reservations in educational institutions.

## 🎯 Features

### 1. **Authentication & Authorization**
- Secure login system with role-based access control
- Three user types: Administrator, Instructor, Student
- Password hashing and session management
- Forgot password functionality

### 2. **Administrator Dashboard**
- **Quick Stats**: Total labs, scheduled sessions, pending requests
- **Manage Labs**: Add, edit, and deactivate laboratory rooms
- **Manage Instructors**: Create and manage instructor accounts
- **View Schedule**: Monitor all lab schedules with filters
- **Approve Requests**: Review and approve/decline reservation requests
- **Reports**: Generate monthly lab usage reports with utilization metrics

### 3. **Instructor Dashboard**
- **Submit Requests**: Reserve labs with date, time, and course details
- **View Schedule**: Check availability and upcoming sessions
- **My Requests**: Track submitted reservations and their status
- **Notifications**: Receive updates on request approvals/declines

### 4. **Student Dashboard**
- **View Schedule by Lab**: Browse lab availability by room
- **View Schedule by Instructor**: Filter by instructor name
- **View Schedule by Section**: Check course-specific schedules
- **Notifications**: Stay updated on schedule changes

### 5. **Laboratory Schedule Management**
- Weekly calendar view (8 AM to 7 PM)
- Color-coded status indicators:
  - 🟢 Green: Available
  - 🔵 Blue: Reserved
  - 🔴 Red: Maintenance/Conflict
- Clickable time blocks for details
- Conflict detection system

### 6. **Notification System**
- Real-time notifications for request approvals/declines
- Schedule update notifications
- Unread notification counter
- Notification history

### 7. **Reports & Analytics**
- Monthly lab usage reports
- Instructor usage summary
- Peak hours analysis
- Utilization rate calculations
- Export capabilities

### 8. **Responsive Design**
- Mobile-optimized interface
- Tablet view support
- Desktop view with full features
- Touch-friendly on mobile devices

## 🛠️ Tech Stack

- **Backend**: Python Flask 2.3.3
- **Database**: SQLite (with SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5.3
- **Icons**: Font Awesome 6.4
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)

## 🚀 Installation

### 1. Clone or Download the Project
```bash
cd c:\Users\HarHar\New-sys
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database with Sample Data
```bash
python seed_db.py
```

### 5. Run the Application
```bash
python run.py
```

The application will be available at: **http://localhost:5000**

## 📱 Demo Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Instructor | instructor1 | pass123 |
| Student | student1 | pass123 |

## 📁 Project Structure

```
New-sys/
├── app/
│   ├── __init__.py           # App factory
│   ├── models.py             # Database models
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   ├── login.html        # Login page
│   │   ├── admin/            # Admin templates
│   │   ├── instructor/       # Instructor templates
│   │   └── student/          # Student templates
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css     # Main styles
│   │   │   └── auth.css      # Auth page styles
│   │   ├── js/
│   │   │   └── main.js       # JavaScript utilities
│   │   └── images/
│   └── routes/
│       ├── __init__.py
│       ├── auth.py           # Authentication routes
│       ├── admin.py          # Admin routes
│       ├── instructor.py     # Instructor routes
│       ├── student.py        # Student routes
│       └── api.py            # API endpoints
├── config.py                 # Configuration
├── run.py                    # Application entry point
├── seed_db.py                # Database seeder
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## 🔄 SDLC Methodology

This project follows the **Agile Model** with:
- Iterative development cycles
- Incremental feature implementation
- Responsive requirements handling
- Continuous integration of components

## 🎨 Design Patterns

- **Factory Pattern**: Flask app factory (`create_app()`)
- **Blueprint Pattern**: Modular route organization
- **MVC Architecture**: Models, Views, Templates
- **DAO Pattern**: Database access through models

## 📋 Database Schema

### Users Table
- Stores user credentials, roles, and metadata
- Relationships: Notifications, Requests

### Laboratories Table
- Lab details, capacity, equipment
- Relationships: Schedules, Requests

### Courses Table
- Course information and instructor mapping
- Relationships: Schedules, Requests

### LabSchedule Table
- Scheduled lab sessions
- Status tracking (Available, Reserved, Maintenance)

### ReservationRequest Table
- Instructor reservation requests
- Status tracking (Pending, Approved, Declined)

### Notifications Table
- User notifications with types and timestamps
- Unread status tracking

### LabUsageReport Table
- Monthly analytics and utilization metrics

## 🔒 Security Features

- Password hashing with Werkzeug
- Session-based authentication
- CSRF protection (Flask-WTF)
- SQL injection prevention (SQLAlchemy)
- XSS protection via Jinja2 templating
- Role-based access control

## 📱 Responsive Breakpoints

| Device | Breakpoint | Features |
|--------|-----------|----------|
| Mobile | < 768px | Simplified layout, touch-friendly |
| Tablet | 768px - 1199px | Medium layout |
| Desktop | ≥ 1200px | Full features |

## 🎯 Key Functionalities by Role

### Administrator
✅ Add/edit/delete labs
✅ Manage instructor accounts
✅ Approve/decline requests
✅ View all schedules
✅ Generate usage reports
✅ Monitor system statistics

### Instructor
✅ Submit lab reservations
✅ View lab schedules
✅ Track request status
✅ Receive notifications
✅ View schedule availability

### Student
✅ View schedules by lab
✅ Filter by instructor
✅ Filter by course section
✅ Check lab availability
✅ Receive schedule updates

## 🔧 Configuration

Edit `config.py` to customize:
- Database URI
- Secret key
- Session timeout
- Pagination settings
- Debug mode

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed
- Check all dependencies in requirements.txt
- Verify port 5000 is available

### Database errors
- Delete `lab_system.db` and run `seed_db.py` again
- Check file permissions in the project directory

### Login issues
- Ensure database is seeded with users
- Check browser cookies are enabled

## 📝 Future Enhancements

- [ ] Email notifications integration
- [ ] Calendar view improvements
- [ ] Advanced search and filters
- [ ] API rate limiting
- [ ] User profile management
- [ ] Lab maintenance scheduling
- [ ] Student enrollment system
- [ ] Analytics dashboard
- [ ] Mobile app (React Native/Flutter)
- [ ] WebSocket for real-time updates

## 📄 License

This project is provided as an educational tool.

## 👨‍💼 Author
Harold jey N. M., co. Francis jick O. Gabionza

IT Laboratory Utilization Schedule System
Developed as an enterprise-level Flask application

## 📞 Support

For issues or questions, please refer to the documentation or contact the system administrator.

---

**Version**: 1.0.0  
**Last Updated**: December 2025  
**Status**: Production Ready ✅
