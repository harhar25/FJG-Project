# 🏢 IT Laboratory Utilization Schedule System - Enterprise Implementation Plan

**Date:** November 26, 2025  
**Project:** FJG-Project  
**Status:** Full Reconstruction with Enterprise Standards  
**SDLC Model:** Agile with Iterative Development  

---

## 📋 Executive Summary

This document outlines the complete rebuild of the IT Laboratory Utilization Schedule System to meet **ENTERPRISE-LEVEL** standards. The system will serve three distinct user types:

1. **Administrators** - Laboratory & Instructor management, request approval, reporting
2. **Instructors** - Laboratory reservation, schedule viewing, request submission
3. **Students** - Schedule viewing, section-based filtering

---

## 🎯 Core Requirements

### TOOLS & TECHNOLOGIES
✅ **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.3  
✅ **Backend:** Python Flask  
✅ **Database:** SQLite (upgradeable to PostgreSQL)  
✅ **SDLC:** Agile Model with 2-week sprints  
✅ **Responsiveness:** Mobile, Tablet, Desktop  

### REQUIREMENT BREAKDOWN

#### 1️⃣ LOGIN PAGE
- **Fields:** Username, Password
- **Buttons:** Login, Forgot Password, Sign Up
- **Features:**
  - Session management
  - Password hashing (werkzeug)
  - Remember me option
  - Account activation status check
  - Role-based redirects
  
#### 2️⃣ DASHBOARDS (Role-Based)

**2.1 ADMIN DASHBOARD**
- Quick view cards:
  - Total Labs (with link to details)
  - Total Scheduled Sessions (with calendar)
  - Pending Requests (with approval panel)
- Navigation buttons:
  - Manage Labs → Full CRUD operations
  - Manage Instructors → Full CRUD operations
  - View Schedule → Calendar view
  - Approve Requests → Approval interface

**2.2 INSTRUCTOR DASHBOARD**
- Upcoming Lab Sessions (table with next 30 days)
- Submit Reservation Request (modal form)
- View Weekly Schedule (calendar)
- Request Status History
- Notifications center

**2.3 STUDENT DASHBOARD**
- View Schedule filtered by:
  - Lab Room (dropdown)
  - Instructor (dropdown)
  - Course Section (dropdown)
- Enrolled Courses (quick access)
- Schedule notifications
- Download calendar option

#### 3️⃣ LABORATORY SCHEDULE PAGE
- **Calendar Layout:** Weekly view, 8 AM - 7 PM
- **Filters:**
  - Select Lab Room (dropdown)
  - Select Date/Week (date picker)
  - Filter by Section/Instructor (multi-select)
- **Time Blocks:**
  - Green: Available
  - Blue: Reserved
  - Red: Conflict/Maintenance
- **Click Interaction:** Popup showing:
  - Section
  - Instructor
  - Course
  - Duration
  - Status

#### 4️⃣ RESERVATION REQUEST FORM
- **Fields:**
  - Instructor Name (auto-filled)
  - Course/Subject (dropdown)
  - Section (dropdown)
  - Preferred Lab Room (dropdown)
  - Date & Time (datetime picker)
  - Duration (select)
  - Notes (textarea)
- **Buttons:** Submit, Reset
- **Validation:** All required fields, conflict checking

#### 5️⃣ APPROVAL PANEL (Admin Only)
- **Table Columns:**
  - Request ID
  - Instructor Name
  - Section
  - Requested Lab
  - Date & Time
  - Reason/Notes
  - Actions (Approve/Decline buttons)
- **Features:**
  - Search/filter
  - Bulk actions
  - Approval confirmation modal
  - Automatic notifications

#### 6️⃣ NOTIFICATION SYSTEM
- **For Instructors:**
  - Request approved notification
  - Request declined notification
  - Schedule conflict warnings
- **For Students:**
  - Section lab schedule updated
  - Schedule changes
  - Important announcements
- **Features:**
  - Notification bell (header)
  - Notification center modal
  - Email notifications (optional)
  - Mark as read functionality

#### 7️⃣ REPORTS PAGE (Admin Only)
- **Report Types:**
  1. Monthly Lab Usage Report
     - Labs used vs available
     - Usage hours by lab
     - Peak hours analysis
  2. Instructor Usage Summary
     - Sessions taught
     - Labs used most
     - Request approval rate
  3. Peak Hours & Demand Chart
     - Hourly usage graph
     - Daily trends
     - Seasonal patterns
- **Export Options:** PDF, CSV, Excel

#### 8️⃣ RESPONSIVE DESIGN
- **Mobile (< 768px):**
  - Hamburger menu navigation
  - Simplified schedule viewer
  - Tap-to-view time blocks
  - Quick reservation button
  - Single column layouts
  
- **Tablet (768px - 1024px):**
  - Side-by-side layouts
  - Touch-optimized buttons
  - Simplified calendar
  
- **Desktop (> 1024px):**
  - Full calendar view
  - Multi-column layouts
  - Advanced filtering
  - Detailed reports

---

## 🏗️ PROJECT STRUCTURE

```
app/
├── __init__.py              # App initialization, DB setup
├── models.py                # ✅ Database models (AUDIT NEEDED)
├── routes/
│   ├── __init__.py
│   ├── auth.py              # ✅ Login/Logout (ENHANCE)
│   ├── admin.py             # 🔄 Admin dashboard & management
│   ├── instructor.py        # 🔄 Instructor dashboard & forms
│   ├── student.py           # 🔄 Student dashboard & schedule
│   └── api.py               # 🆕 AJAX endpoints for live data
├── static/
│   ├── css/
│   │   ├── base.css         # 🔄 Base styles
│   │   ├── admin.css        # 🆕 Admin-specific styles
│   │   ├── instructor.css   # 🆕 Instructor-specific styles
│   │   ├── student.css      # 🆕 Student-specific styles
│   │   └── responsive.css   # 🆕 Mobile/Tablet/Desktop
│   ├── js/
│   │   ├── base.js          # 🔄 Shared functionality
│   │   ├── calendar.js      # 🆕 Calendar logic
│   │   ├── modals.js        # 🆕 Modal management
│   │   ├── notifications.js # 🆕 Notification handling
│   │   └── api.js           # 🆕 API calls
│   └── images/
├── templates/
│   ├── base.html            # 🔄 Base template (UPDATE)
│   ├── login.html           # ✅ Login page (ENHANCE)
│   ├── admin/
│   │   ├── dashboard.html   # 🆕 Admin dashboard
│   │   ├── labs.html        # 🆕 Manage labs
│   │   ├── instructors.html # 🆕 Manage instructors
│   │   ├── requests.html    # 🆕 Approval panel
│   │   ├── schedule.html    # 🆕 Schedule view
│   │   └── reports.html     # 🆕 Reports page
│   ├── instructor/
│   │   ├── dashboard.html   # 🆕 Instructor dashboard
│   │   ├── schedule.html    # 🆕 Weekly schedule
│   │   ├── reservation.html # 🆕 Reservation form
│   │   └── requests.html    # 🆕 Request history
│   └── student/
│       ├── dashboard.html   # 🆕 Student dashboard
│       └── schedule.html    # 🆕 Schedule view

config.py                   # 🔄 Configuration (UPDATE)
run.py                      # 🔄 Application entry point
requirements.txt            # 🔄 Dependencies
seed_db.py                  # 🆕 Sample data generator
```

---

## 📊 Database Schema (Models Overview)

✅ **Already Defined:**
- User (with roles: Admin, Instructor, Student)
- Laboratory
- Course
- LabSchedule
- ReservationRequest
- Notification
- LabUsageReport

🔄 **Needs Enhancement:**
- Add course enrollment for students
- Add request status history/audit trail
- Add notification preferences
- Add lab maintenance schedule

---

## 🔄 IMPLEMENTATION PHASES

### Phase 1: Backend Foundation (Week 1)
- [ ] Audit & enhance database models
- [ ] Fix model relationships
- [ ] Create seed data script
- [ ] Build admin routes (CRUD)
- [ ] Build instructor routes
- [ ] Build student routes
- [ ] Build API endpoints

### Phase 2: Frontend - Authentication (Week 1-2)
- [ ] Enhance login page
- [ ] Implement forgot password
- [ ] Add session management
- [ ] Create error pages

### Phase 3: Frontend - Admin (Week 2-3)
- [ ] Build admin dashboard
- [ ] Lab management interface
- [ ] Instructor management interface
- [ ] Approval panel
- [ ] Reports page

### Phase 4: Frontend - Instructor (Week 3-4)
- [ ] Instructor dashboard
- [ ] Reservation form
- [ ] Weekly schedule view
- [ ] Request history

### Phase 5: Frontend - Student (Week 4)
- [ ] Student dashboard
- [ ] Schedule viewer with filters
- [ ] Notification center

### Phase 6: Shared Features (Week 4-5)
- [ ] Notification system
- [ ] Calendar component
- [ ] Reports generation
- [ ] Data export (CSV, PDF)

### Phase 7: Responsive Design (Week 5-6)
- [ ] Mobile optimization
- [ ] Tablet optimization
- [ ] Desktop polish
- [ ] Touch interactions

### Phase 8: Testing & Deployment (Week 6-7)
- [ ] Unit tests
- [ ] Integration tests
- [ ] User acceptance testing
- [ ] Performance optimization
- [ ] Deployment

---

## ✅ ENTERPRISE STANDARDS CHECKLIST

### Security
- [ ] Password hashing (werkzeug)
- [ ] CSRF protection (Flask-WTF)
- [ ] SQL injection prevention (SQLAlchemy ORM)
- [ ] XSS prevention (Jinja2 auto-escaping)
- [ ] Session security
- [ ] Role-based access control (RBAC)

### Performance
- [ ] Database indexing
- [ ] Query optimization
- [ ] Caching strategy
- [ ] Lazy loading relationships
- [ ] Pagination for large datasets
- [ ] Minified assets

### Code Quality
- [ ] PEP 8 compliance
- [ ] Docstrings for all functions
- [ ] Error handling
- [ ] Logging
- [ ] Comments for complex logic
- [ ] Modular, DRY code

### UX/UI
- [ ] Responsive design (mobile-first)
- [ ] Accessibility (WCAG 2.1)
- [ ] Consistent styling
- [ ] Loading indicators
- [ ] Error messages
- [ ] Success confirmations

### Maintainability
- [ ] Clear file structure
- [ ] Configuration management
- [ ] Database migrations ready
- [ ] Documentation
- [ ] Version control
- [ ] Environment separation (dev/prod)

---

## 🚀 QUICK START COMMANDS

```bash
# Setup
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Database
python seed_db.py

# Run
python run.py

# Testing
pytest tests/
```

---

## 📞 TESTING CREDENTIALS

**Admin Account:**
- Username: `admin`
- Password: `admin@123456`

**Instructor Account:**
- Username: `instructor1`
- Password: `instr@123456`

**Student Account:**
- Username: `student1`
- Password: `stud@123456`

---

## 📝 NEXT STEPS

1. ✅ Review this plan
2. 🔄 Audit models (see models.py review needed)
3. 🔄 Enhance authentication system
4. 🔄 Build admin backend routes
5. 🔄 Create admin dashboard frontend
6. 🔄 Continue with instructor and student sections

---

**Status:** Ready for implementation  
**Estimated Completion:** 7-8 weeks (full enterprise-grade system)  
**Current Phase:** Phase 1 - Backend Foundation
