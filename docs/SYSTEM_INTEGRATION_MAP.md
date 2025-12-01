# 🔗 SYSTEM INTEGRATION MAP - Instructor, Admin & Student Connection

**Date:** December 1, 2025  
**Status:** ✅ FULLY INTEGRATED

---

## 📊 COMPLETE DATA FLOW DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       IT LAB SCHEDULE SYSTEM FLOW                        │
└─────────────────────────────────────────────────────────────────────────┘

                          🧑‍🏫 INSTRUCTOR                                   
                      ┌─────────────────────┐                             
                      │ 1. SUBMITS REQUEST  │                             
                      │ - Lab Room          │                             
                      │ - Date & Time       │                             
                      │ - Course & Section  │                             
                      │ - Reason/Notes      │                             
                      └──────────┬──────────┘                             
                                 │                                         
                    ┌────────────▼────────────┐                          
                    │   RESERVATION_REQUEST   │                          
                    │   TABLE (DATABASE)      │                          
                    │ ─────────────────────── │                          
                    │ Request ID: 1           │                          
                    │ Instructor: John        │                          
                    │ Status: PENDING ← ← ┐  │                          
                    │ Lab: Lab 101         │  │                          
                    │ Date: 2025-12-05     │  │                          
                    │ Time: 9AM-11AM       │  │                          
                    └────────────┬─────────┘  │                          
                                 │            │                          
                    ┌────────────▼────────────┐ │                        
                    │   📬 ADMIN DASHBOARD    │ │ ADMIN REVIEWS           
                    │ ─────────────────────── │ │                        
                    │ ✓ Pending: 1            │ │ 2. ADMIN SEES REQUEST   
                    │ ✓ View All Requests     │─ │ - Request Details      
                    │ ✓ Approval Panel        │   │ - Conflict Check       
                    └────────────┬────────────┘   │ - Decision             
                                 │                │                        
                    ┌────────────▼────────────┐  │                        
                    │  3. ADMIN DECISION      │◄─┘                        
                    │ ─────────────────────── │                           
                    │ ✓ APPROVE or DECLINE    │                           
                    └──────┬─────────┬────────┘                           
                           │         │                                    
               ┌───────────┘         └───────────┐                       
               │                                 │                       
        ✅ APPROVED                       ❌ DECLINED                   
        (Status→Approved)                (Status→Declined)              
               │                                 │                       
    ┌──────────▼──────────┐        ┌────────────▼─────────┐            
    │  LAB_SCHEDULE TABLE │        │  NOTIFICATION TABLE  │            
    │  ─────────────────  │        │  ──────────────────  │            
    │ Schedule ID: 1      │        │ To: John (Instructor)│            
    │ Lab: Lab 101        │        │ Type: DECLINE        │            
    │ Date: 2025-12-05    │        │ Message: Declined    │            
    │ Time: 9AM-11AM      │        │ Status: UNREAD       │            
    │ Status: RESERVED    │        └────────┬─────────────┘            
    │ Created: Admin Bob  │                 │                           
    └──────────┬──────────┘                 │                           
               │                            │                           
    ┌──────────▼──────────────────────────────▼───────────┐             
    │         4. 🧑‍🏫 INSTRUCTOR SEES UPDATE                │             
    │    (Notifications Page / Dashboard)                 │             
    │ ──────────────────────────────────────────────     │             
    │ ✓ If APPROVED:                                      │             
    │   - Lab Session Created & Scheduled                 │             
    │   - "Request Approved" Notification (GREEN)         │             
    │   - Lab Now Shows in Calendar                       │             
    │                                                     │             
    │ ✓ If DECLINED:                                      │             
    │   - "Request Declined" Notification (RED)           │             
    │   - Can Resubmit New Request                        │             
    └──────────────┬──────────────────────────────────────┘             
                   │                                                    
        ┌──────────▼─────────────────┐                                
        │  5. 👨‍🎓 STUDENTS BENEFIT       │                                
        │  (View Approved Schedules)  │                                
        │ ─────────────────────────── │                                
        │ Student Dashboard:          │                                
        │ ✓ Upcoming Sessions Display │                                
        │ ✓ Browse by Lab Room        │                                
        │ ✓ Browse by Instructor      │                                
        │ ✓ Browse by Course Section  │                                
        │                             │                                
        │ ⚡ REAL-TIME UPDATES:       │                                
        │ When instructor gets        │                                
        │ approval → students         │                                
        │ immediately see it          │                                
        └─────────────────────────────┘                                
```

---

## 🔄 **COMPLETE DATA CONNECTION MAP**

### **1️⃣ INSTRUCTOR → DATABASE (Submit Request)**
```
INSTRUCTOR
    ↓
Clicks "Submit Request"
    ↓
Fill Form:
├─ Course (Dropdown - from Course table)
├─ Lab Room (Dropdown - from Laboratory table)
├─ Date & Time (Instructor chooses)
├─ Reason/Notes (Free text)
└─ Section (Auto-populated from course)
    ↓
POST /instructor/submit-request
    ↓
CREATE ReservationRequest:
├─ instructor_id = current_user.id
├─ lab_id = selected lab
├─ course_id = selected course
├─ requested_date = selected date
├─ start_time = selected start
├─ end_time = selected end
├─ reason = provided notes
└─ status = 'Pending'
    ↓
Save to DATABASE
    ↓
Flash: "Request submitted successfully!"
```

### **2️⃣ ADMIN → DATABASE (Review & Approve/Decline)**
```
ADMIN
    ↓
Admin Dashboard:
├─ Sees stat: "Pending Requests: X"
└─ Clicks "Approve Requests"
    ↓
GET /admin/approve-requests
    ↓
QUERY ReservationRequest WHERE status='Pending'
    ↓
Display Table:
├─ Request ID
├─ Instructor Name (from User table)
├─ Course Code (from Course table)
├─ Lab Name (from Laboratory table)
├─ Date & Time
├─ Reason
├─ [APPROVE] Button
└─ [DECLINE] Button
    ↓
Admin Clicks APPROVE or DECLINE
    ↓
POST /admin/approve-requests
    ↓
IF APPROVE:
├─ UPDATE ReservationRequest: status='Approved'
├─ CREATE LabSchedule:
│  ├─ lab_id = reservation.lab_id
│  ├─ course_id = reservation.course_id
│  ├─ scheduled_date = reservation.requested_date
│  ├─ start_time = reservation.start_time
│  ├─ end_time = reservation.end_time
│  ├─ status = 'Reserved'
│  └─ created_by = admin.id
└─ CREATE Notification (To Instructor):
   ├─ type = 'approval'
   ├─ title = 'Request Approved'
   └─ message = '[Lab Name] reservation approved'
    ↓
IF DECLINE:
├─ UPDATE ReservationRequest: status='Declined'
└─ CREATE Notification (To Instructor):
   ├─ type = 'decline'
   ├─ title = 'Request Declined'
   └─ message = '[Lab Name] reservation declined'
```

### **3️⃣ INSTRUCTOR → NOTIFICATIONS (Gets Feedback)**
```
INSTRUCTOR
    ↓
Navigates to Notifications page
    ↓
GET /instructor/notifications
    ↓
QUERY Notification WHERE user_id=instructor_id
    ↓
Display Notifications:
├─ If APPROVED:
│  ├─ Green Icon ✅
│  ├─ Title: "Request Approved"
│  ├─ Message: "[Lab Name] reserved"
│  └─ Can now see schedule
│
└─ If DECLINED:
   ├─ Red Icon ❌
   ├─ Title: "Request Declined"
   ├─ Message: "Request declined"
   └─ Can submit new request
    ↓
Instructor Sees Status
```

### **4️⃣ STUDENT → DATABASE (Views Approved Schedules)**
```
STUDENT
    ↓
Student Dashboard
    ↓
GET /student/dashboard
    ↓
QUERY LabSchedule WHERE status='Reserved'
    ↓
Display Upcoming Sessions:
├─ Lab Name (from Laboratory table)
├─ Date & Time (from LabSchedule)
├─ Instructor Name (from User table)
├─ Course Info (from Course table)
└─ Status Badge
    ↓
Student Clicks "Browse by Lab Room"
    ↓
GET /student/schedule/by-lab
    ↓
QUERY Laboratory WHERE is_active=True
    ↓
Student Selects Lab
    ↓
QUERY LabSchedule WHERE lab_id=selected AND date=week
    ↓
Display Calendar:
├─ Days: Mon-Sun
├─ Time Slots: 8AM-7PM
├─ Each slot shows:
│  ├─ Time Range
│  ├─ Course Code
│  ├─ Section
│  ├─ Instructor Name
│  └─ Status
└─ Student Can See Approved Sessions
    ↓
Repeat for:
├─ Browse by Instructor
└─ Browse by Course Section
```

---

## 📋 **DATABASE RELATIONSHIPS**

```
┌──────────────────────────────────────────────────┐
│          DATABASE RELATIONSHIPS                   │
├──────────────────────────────────────────────────┤

USER TABLE (All roles)
├─ id (PK)
├─ username
├─ full_name
├─ role ← Determines what each sees
│   ├─ 'Administrator' → Admin routes only
│   ├─ 'Instructor' → Instructor routes only
│   └─ 'Student' → Student routes only
└─ is_active

LABORATORY TABLE
├─ id (PK)
├─ lab_name
├─ lab_code
├─ capacity
└─ is_active

COURSE TABLE
├─ id (PK)
├─ course_code
├─ course_name
├─ section
├─ instructor_id ← Foreign Key to User
└─ Created By: Admin

RESERVATION_REQUEST TABLE
├─ id (PK)
├─ instructor_id ← Foreign Key to User (Instructor)
├─ lab_id ← Foreign Key to Laboratory
├─ course_id ← Foreign Key to Course
├─ requested_date
├─ start_time
├─ end_time
├─ reason
├─ status: 'Pending' → 'Approved'/'Declined'
├─ approved_by ← Foreign Key to User (Admin)
└─ approval_date

LAB_SCHEDULE TABLE
├─ id (PK)
├─ lab_id ← Foreign Key to Laboratory
├─ course_id ← Foreign Key to Course
├─ scheduled_date
├─ start_time
├─ end_time
├─ status: 'Available'/'Reserved'/'Maintenance'
├─ created_by ← Foreign Key to User (Admin)
└─ Created when: Admin approves request

NOTIFICATION TABLE
├─ id (PK)
├─ user_id ← Foreign Key to User (Recipient)
├─ title
├─ message
├─ notification_type: 'approval'/'decline'/'update'
├─ is_read
├─ created_at
├─ read_at
└─ related_request_id ← Foreign Key to ReservationRequest

Connection Paths:
────────────────
Instructor Request → Admin Review → Approval/Decline
     ↓ (same request_id)
  ReservationRequest → Notification (To Instructor)
     ↓ (when approved)
  LabSchedule → Students See It

Students Can See LabSchedule By:
├─ Lab Room Filter (lab_id)
├─ Instructor Filter (course_id → instructor_id)
└─ Section Filter (course_id → section)
```

---

## 🔗 **COMPLETE USER JOURNEY**

### **Scenario: Lab Booking Workflow**

```
STEP 1: INSTRUCTOR SUBMITS REQUEST
────────────────────────────────────
John (Instructor) needs Lab 101 on Dec 5, 2025
- Logs in → /instructor/dashboard
- Clicks "Submit Request"
- Goes to → /instructor/submit-request (GET)
- Fills Form:
  Course: IT-101 (JavaScript)
  Lab: Lab 101 (Capacity 30)
  Date: 2025-12-05
  Time: 9:00 AM - 11:00 AM
  Notes: "Final Project Demo"
- Clicks "Submit Request" (POST)
- Data Stored in DATABASE:
  ReservationRequest(
    instructor_id=John.id,
    lab_id=101,
    course_id=1,
    requested_date=2025-12-05,
    start_time=09:00,
    end_time=11:00,
    reason="Final Project Demo",
    status='Pending'
  )
- John Sees: "Request submitted successfully!"


STEP 2: ADMIN REVIEWS REQUEST
──────────────────────────────
Bob (Admin) checks dashboard:
- /admin/dashboard Shows:
  - Pending Requests: 1 ← (John's request)
- Clicks "Approve Requests"
- Goes to → /admin/approve-requests (GET)
- Sees Table:
  Request ID: 1
  Instructor: John Smith
  Course: IT-101 / Section A
  Lab: Lab 101
  Date & Time: 12/05/2025 9:00-11:00
  Reason: "Final Project Demo"
  [APPROVE] [DECLINE]
- Bob Checks for Conflicts:
  - Is Lab 101 available? ✅ Yes
  - Any scheduling conflicts? ✅ No
- Bob Clicks [APPROVE]
- Data Updated in DATABASE:
  ReservationRequest status = 'Approved'
  LabSchedule Created:
  LabSchedule(
    lab_id=101,
    course_id=1,
    scheduled_date=2025-12-05,
    start_time=09:00,
    end_time=11:00,
    status='Reserved',
    created_by=Bob.id
  )
  Notification Created:
  Notification(
    user_id=John.id,
    title="Request Approved",
    message="Lab 101 reserved for IT-101",
    type='approval',
    is_read=False
  )
- Bob Sees: "Request approved successfully!"


STEP 3: INSTRUCTOR GETS NOTIFICATION
─────────────────────────────────────
John Gets Notification:
- Dashboard Shows: "Notifications: 1"
- Clicks "Notifications"
- Goes to → /instructor/notifications (GET)
- QUERY: SELECT * FROM Notification WHERE user_id=John.id
- Sees:
  ✅ "Request Approved"
  "Lab 101 reserved for IT-101, Session: Dec 5, 2025 9:00 AM"
  Timestamp: Today 3:45 PM
  [Mark as Read]
- John Clicks [Mark as Read]
- Notification Updated: is_read = True
- John Can Now:
  ✓ See in /instructor/view-schedule
  ✓ See upcoming session on /instructor/dashboard


STEP 4: STUDENTS SEE THE SCHEDULED LAB
──────────────────────────────────────
Student Views Available Labs:
- Logs in → /student/dashboard
- Sees Section A students:
  "Your Upcoming Lab Sessions"
  Lab 101: Dec 5, 2025 9:00-11:00 (IT-101)
- Clicks "Browse by Lab Room"
- Goes to → /student/schedule/by-lab (GET)
- QUERY: SELECT * FROM Laboratory WHERE is_active=True
- Selects "Lab 101"
- QUERY: SELECT * FROM LabSchedule WHERE lab_id=101 AND date >= today
- Sees Calendar:
  Friday, Dec 5:
  9:00-11:00 | IT-101 (Section A) | John Smith
  11:00-1:00 | Available
  1:00-3:00 | Available
- Student Can Also:
  ✓ /student/schedule/by-instructor → See John's sessions
  ✓ /student/schedule/by-section → See Section A sessions


STEP 5: ADMIN GETS REPORTS
──────────────────────────
Admin Reviews System:
- Clicks "View Reports"
- Goes to → /admin/reports
- Sees Monthly Summary:
  Total Labs: 5
  Total Sessions This Month: 12
  Total Hours: 36 hours
  Average Utilization: 72%
  Lab 101: 8 sessions, 24 hours used
- Admin Can Filter by Month and See:
  - Which labs are most used
  - Peak hours
  - Instructor usage patterns
  - Student enrollment trends


DATABASE STATE AFTER COMPLETE WORKFLOW:
────────────────────────────────────────
ReservationRequest Table:
  id=1, instructor=John, lab=101, status='Approved'

LabSchedule Table:
  id=1, lab_id=101, scheduled_date=2025-12-05, status='Reserved'

Notification Table:
  id=1, user=John, type='approval', is_read=True

John's View:
  ✓ Request submitted
  ✓ Approved by admin
  ✓ Notified of approval
  ✓ Can see scheduled session

Students' View:
  ✓ Can see Lab 101 booked on Dec 5
  ✓ Know instructor is John
  ✓ Know time 9:00-11:00
  ✓ Can attend if registered in IT-101
```

---

## ✅ **CONNECTION VERIFICATION CHECKLIST**

### **Instructor ↔ Admin Connection**
- ✅ Instructor submits → stored in DATABASE
- ✅ Admin sees in approval panel
- ✅ Admin approval/decline → updates DATABASE
- ✅ Notification sent to Instructor
- ✅ Instructor sees feedback
- ✅ If approved → LabSchedule created (both see it)

### **Instructor ↔ Student Connection**
- ✅ Instructor's approved request → creates LabSchedule
- ✅ Students query LabSchedule
- ✅ Students see Instructor's name
- ✅ Students see scheduled time
- ✅ Students know which lab
- ✅ Students know which course/section

### **Admin ↔ Student Connection**
- ✅ Admin manages labs (Laboratory table)
- ✅ Admin approves requests (ReservationRequest)
- ✅ Admin approvals create LabSchedule
- ✅ Students query LabSchedule (created by admin)
- ✅ Admin generates reports from student enrollments
- ✅ Admin can see utilization

### **All Three Connected**
- ✅ Single database (source of truth)
- ✅ Role-based access control
- ✅ Data flows in all directions
- ✅ Real-time updates
- ✅ Notifications for changes
- ✅ Audit trail (approval_date, approved_by, etc.)

---

## 🎯 **KEY INTEGRATION POINTS**

| Connection | Data Source | Data Destination | Query/Action |
|-----------|-------------|------------------|--------------|
| Instructor → Admin | ReservationRequest | Approval Panel | SELECT WHERE status='Pending' |
| Admin → Instructor | Notification | Notifications Page | SELECT WHERE user_id=X |
| Admin → LabSchedule | Approval Button | Create Schedule | INSERT LabSchedule |
| LabSchedule → Student | Lab Filter | Schedule Display | SELECT WHERE lab_id=X |
| Instructor → Student | Course Info | Schedule Display | JOIN Course table |
| Student → Admin | Dashboard | Reports | COUNT/SUM queries |

---

## 🔒 **SECURITY IN CONNECTIONS**

```
@login_required              ← All routes require login
├─ @instructor_required      ← Only instructors see instructor routes
├─ @admin_required           ← Only admins see admin routes
└─ @student_required         ← Only students see student routes

Database Security:
├─ SQLAlchemy ORM            ← Prevents SQL injection
├─ Foreign Key Constraints   ← Data integrity
├─ Timestamps                ← Audit trail
├─ User ID Checks            ← Can't access others' data
└─ Role Verification         ← Authorization at route level
```

---

## 📱 **REAL-TIME SYNC OPPORTUNITIES**

Current: Database is single source of truth
Ready for Enhancement:
- WebSocket notifications (instructor gets instant approval alert)
- Email notifications (admin emails instructor)
- SMS reminders (student gets lab session reminders)
- Calendar sync (export to Google Calendar, Outlook)

---

## ✨ **CONCLUSION**

The system is **FULLY INTEGRATED** with all three roles:

✅ **Instructor** - Submits requests, views approvals, teaches sessions  
✅ **Admin** - Reviews requests, approves/declines, manages system  
✅ **Student** - Views schedules, attends sessions, gets notifications  

All data flows correctly through the **single database** with proper relationships and role-based access control.

**Status:** 🟢 FULLY CONNECTED AND OPERATIONAL

