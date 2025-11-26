# Role-Based Navigation - Quick Test Guide

## How to Test the Fix

The application is now running at **http://127.0.0.1:5000**

### Test Credentials

| Role | Username | Password | Purpose |
|------|----------|----------|---------|
| **Administrator** | admin | (from seed data) | Full system control |
| **Instructor** | instructor1 | (from seed data) | Teaching/Lab requests |
| **Student** | student1 | (from seed data) | Learning/Browse schedules |

### What to Check

#### ✅ Check 1: Admin Dashboard
1. **Login** as `admin`
2. **Sidebar should show:**
   - Administration: Dashboard, Laboratories, Instructors, Approvals, Schedule
   - Analytics: Reports
3. **Should NOT show:**
   - Student schedule browsing options
   - Instructor request submission
4. **Dashboard displays:**
   - Total Labs stat card
   - Scheduled Sessions stat card
   - Pending Requests stat card
   - Quick action buttons for admin features

#### ✅ Check 2: Instructor Dashboard
1. **Login** as `instructor1`
2. **Sidebar should show:**
   - Teaching: Dashboard, New Request, My Requests, Schedule
   - Notifications: Notifications
3. **Should NOT show:**
   - Admin management options (Manage Labs, Manage Instructors, Approvals)
   - Student schedule browsing (By Lab, By Instructor, By Course)
4. **Dashboard displays:**
   - Pending Requests stat card (number awaiting approval)
   - Notifications stat card (unread messages)
   - Upcoming Lab Sessions section
   - Quick action buttons for instructor features

#### ✅ Check 3: Student Dashboard
1. **Login** as `student1`
2. **Sidebar should show:**
   - Learning: Dashboard, Schedule by Lab, By Instructor, By Course
   - Communications: Notifications
3. **Should NOT show:**
   - Admin features (Labs, Instructors, Approvals, Reports)
   - Instructor features (New Request, My Requests)
4. **Dashboard displays:**
   - Your Upcoming Lab Sessions
   - Browse Lab Schedules section with 3 filters:
     - By Lab Room
     - By Instructor
     - By Course Section

---

## Feature Comparison

### Before the Fix ❌
```
Every user saw:
├── Main Navigation
│   ├── Dashboard
│   ├── Laboratories
│   ├── Instructors
│   ├── Approvals
│   └── Analytics
├── Management
│   ├── Instructors
│   ├── Laboratories
│   └── Approvals
└── Analytics
    ├── Reports
    └── Statistics
```
**Problem**: A student could see "Manage Instructors" and "Approvals" options, 
even though they don't have permission to access them.

### After the Fix ✅
```
ADMIN sees:
├── Administration
│   ├── Dashboard
│   ├── Laboratories
│   ├── Instructors
│   ├── Approvals
│   └── Schedule
└── Analytics
    └── Reports

INSTRUCTOR sees:
├── Teaching
│   ├── Dashboard
│   ├── New Request
│   ├── My Requests
│   └── Schedule
└── Notifications
    └── Notifications

STUDENT sees:
├── Learning
│   ├── Dashboard
│   ├── Schedule by Lab
│   ├── By Instructor
│   └── By Course
└── Communications
    └── Notifications
```
**Solution**: Each role only sees their own features!

---

## Technical Details

### File Modified
- `app/templates/base.html` - Lines 1378-1502 (sidebar navigation)

### Changes Made
1. **Added Jinja2 conditional blocks** - `{% if current_user.role == '...' %}`
2. **Role-specific navigation sections** - Separate nav structures for each role
3. **Proper routing** - Using `url_for()` for Flask routes
4. **Mobile optimization** - Different quick menus for small screens
5. **Dynamic logout** - Linked to `auth.logout` route

### Security Layers
1. **Frontend**: Sidebar only shows what user should see
2. **Backend**: Each route has `@admin_required`, `@instructor_required`, or `@student_required` decorator
3. **Database**: Role stored in User model
4. **Session**: Flask-Login manages authentication

---

## Expected Behavior

### When Opening Each Dashboard

#### **Admin Dashboard**
```
Hero Banner: "Administrator Dashboard"
Stats Section:
  - Total Labs: [number]
  - Sessions: [number]
  - Pending Requests: [number]
Quick Actions:
  [Manage Labs] [Manage Instructors] [View Schedule] [View Reports]
```

#### **Instructor Dashboard**
```
Hero Banner: "Instructor Dashboard"
Stats Section:
  - Pending Requests: [number] "Awaiting approval"
  - Notifications: [number] "Unread messages"
Upcoming Lab Sessions (next 7 days):
  [Session Cards with details]
Quick Actions:
  [Submit Request] [My Requests] [View Schedule] [Notifications]
```

#### **Student Dashboard**
```
Hero Banner: "Student Dashboard"
Your Upcoming Lab Sessions:
  [Session Cards if any]
Browse Lab Schedules:
  [By Lab Room] [By Instructor] [By Course Section]
```

---

## Troubleshooting

### Issue: Still seeing admin options as student
**Solution**: Clear browser cache and reload, or use Ctrl+Shift+R

### Issue: Logout not working
**Solution**: Check that `auth.logout` route exists in `app/routes/auth.py`

### Issue: Blank sidebar
**Solution**: Make sure you're logged in (check for `current_user.is_authenticated`)

### Issue: Wrong options showing
**Solution**: Verify your `current_user.role` matches one of:
- `'Administrator'`
- `'Instructor'`
- `'Student'`

---

## Next Steps After Testing

After confirming the role-based navigation works:

1. **Fix seed_db.py** - Create test data properly
2. **Complete admin routes** - All CRUD operations
3. **Build instructor features** - Request submission and approvals
4. **Implement student schedules** - All filter options
5. **Add calendar integration** - Display schedules visually
6. **Create notifications UI** - Real-time updates
7. **Add reports** - Analytics and charts
8. **Mobile testing** - Responsive design verification

---

**Status**: 🟢 Ready for Testing  
**Last Updated**: November 26, 2025  
**Commit**: d6e911f  
