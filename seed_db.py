#!/usr/bin/env python3#!/usr/bin/env python3#!/usr/bin/env python3from datetime import time#!/usr/bin/env python3#!/usr/bin/env python3#!/usr/bin/env python3

"""IT Lab System - Database Seeding Script"""

"""IT Lab System - Database Seeding Script"""

from datetime import datetime, timedelta, time

from app import create_app, db"""

from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest, Notification, LabUsageReport

from datetime import datetime, timedelta, time



def seed_database():from app import create_app, dbIT Lab System - Database Seeding Scriptfrom app import create_app, db

    """Seed the database with test data"""

    app = create_app()from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest, Notification, LabUsageReport

    

    with app.app_context():Comprehensive Database Seeding Script to populate the system with test data

        print("\n" + "="*70)

        print("🌱 IT LAB SYSTEM - DATABASE SEEDING")

        print("="*70 + "\n")

        def seed_database():"""from app.models import User, Laboratory, Course"""

        try:

            print("🗑️  Clearing existing data...")    """Seed the database with test data"""

            db.drop_all()

            db.create_all()    app = create_app()

            print("✅ Database cleared and recreated\n")

                

            # CREATE USERS

            print("👥 Creating users...")    with app.app_context():from datetime import datetime, timedelta, time

            admin = User(username='admin', email='admin@labsystem.com', full_name='System Administrator', role='Administrator')

            admin.set_password('admin123')        print("\n" + "="*70)

            db.session.add(admin)

                    print("🌱 IT LAB SYSTEM - DATABASE SEEDING")from app import create_app, db

            instructors = []

            for i in range(1, 4):        print("="*70 + "\n")

                instructor = User(

                    username=f'instructor{i}',        from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest, Notification, LabUsageReportapp = create_app()Seed Database Script for IT Lab System""""""

                    email=f'instructor{i}@labsystem.com',

                    full_name=f'Dr. Instructor {i}',        try:

                    role='Instructor'

                )            print("🗑️  Clearing existing data...")

                instructor.set_password('pass123')

                db.session.add(instructor)            db.drop_all()

                instructors.append(instructor)

                        db.create_all()

            students = []

            for i in range(1, 6):            print("✅ Database cleared and recreated\n")

                student = User(

                    username=f'student{i}',            def seed_database():

                    email=f'student{i}@labsystem.com',

                    full_name=f'Student {i}',            # CREATE USERS

                    role='Student'

                )            print("👥 Creating users...")    """Seed the database with comprehensive sample data"""with app.app_context():Quick seed script to populate test data

                student.set_password('pass123')

                db.session.add(student)            admin = User(username='admin', email='admin@labsystem.com', full_name='System Administrator', role='Administrator')

                students.append(student)

                        admin.set_password('admin123')    

            db.session.commit()

            print(f"✅ Created 1 Admin + {len(instructors)} Instructors + {len(students)} Students\n")            db.session.add(admin)

            

            # CREATE LABORATORIES                app = create_app()    db.drop_all()

            print("🏢 Creating laboratories...")

            labs_data = [            instructors = []

                {'lab_name': 'Computer Lab 1', 'lab_code': 'CL-101', 'capacity': 30, 'location': 'Building A, Floor 1', 'equipment': 'Desktop Computers, Projector'},

                {'lab_name': 'Computer Lab 2', 'lab_code': 'CL-102', 'capacity': 25, 'location': 'Building A, Floor 2', 'equipment': 'Desktop Computers, Interactive Board'},            for i in range(1, 4):    

                {'lab_name': 'Network Lab', 'lab_code': 'NL-201', 'capacity': 20, 'location': 'Building B, Floor 1', 'equipment': 'Networking Equipment, Routers'},

                {'lab_name': 'Database Lab', 'lab_code': 'DL-301', 'capacity': 25, 'location': 'Building B, Floor 2', 'equipment': 'Servers, Database Software'},                instructor = User(

                {'lab_name': 'Electronics Lab', 'lab_code': 'EL-401', 'capacity': 20, 'location': 'Building C, Floor 1', 'equipment': 'Oscilloscopes, Multimeters'},

                {'lab_name': 'Web Dev Lab', 'lab_code': 'WDL-402', 'capacity': 28, 'location': 'Building C, Floor 2', 'equipment': 'Workstations, Web Servers'},                    username=f'instructor{i}',    with app.app_context():    db.create_all()"""Comprehensive Database Seeding ScriptSeed Database Script - Enterprise IT Lab System

                {'lab_name': 'Security Lab', 'lab_code': 'SL-501', 'capacity': 20, 'location': 'Building D, Floor 1', 'equipment': 'Firewall, IDS/IPS'},

                {'lab_name': 'Mobile Dev Lab', 'lab_code': 'MDL-502', 'capacity': 25, 'location': 'Building D, Floor 2', 'equipment': 'Mobile Devices, Emulators'},                    email=f'instructor{i}@labsystem.com',

            ]

                                full_name=f'Dr. Instructor {i}',        print("\n" + "="*70)

            labs = []

            for lab_data in labs_data:                    role='Instructor'

                lab = Laboratory(**lab_data)

                db.session.add(lab)                )        print("🌱 IT LAB SYSTEM - DATABASE SEEDING")    

                labs.append(lab)

                            instructor.set_password('pass123')

            db.session.commit()

            print(f"✅ Created {len(labs)} laboratory rooms\n")                db.session.add(instructor)        print("="*70 + "\n")

            

            # CREATE COURSES                instructors.append(instructor)

            print("📚 Creating courses...")

            courses_data = [                        admin = User(username='admin', email='admin@lab.edu', full_name='Admin', role='Administrator')from datetime import datetime, timedelta, time

                {'course_code': 'CS101', 'course_name': 'Intro to CS', 'credit_hours': 3, 'section': 'A1', 'instructor_id': instructors[0].id},

                {'course_code': 'CS101', 'course_name': 'Intro to CS', 'credit_hours': 3, 'section': 'B1', 'instructor_id': instructors[1].id},            students = []

                {'course_code': 'CS201', 'course_name': 'Data Structures', 'credit_hours': 4, 'section': 'A', 'instructor_id': instructors[0].id},

                {'course_code': 'CS301', 'course_name': 'Database Systems', 'credit_hours': 4, 'section': 'A', 'instructor_id': instructors[2].id},            for i in range(1, 6):        try:

                {'course_code': 'NET401', 'course_name': 'Advanced Networking', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[1].id},

                {'course_code': 'WEB301', 'course_name': 'Web Development', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[0].id},                student = User(

                {'course_code': 'SEC401', 'course_name': 'Cybersecurity', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[1].id},

                {'lab_name': 'Mobile Dev Lab', 'lab_code': 'MDL-502', 'capacity': 25, 'location': 'Building D, Floor 2', 'equipment': 'Mobile Devices, Emulators'},                    username=f'student{i}',            print("🗑️  Clearing existing data...")    admin.set_password('admin@123456')

            ]

                                email=f'student{i}@labsystem.com',

            courses = []

            for course_data in courses_data[:-1]:                    full_name=f'Student {i}',            print("="*70)

                course = Course(**course_data)

                db.session.add(course)                    role='Student'

                courses.append(course)

                            )                from app import create_app, dbIT Laboratory Utilization Schedule SystemPopulates the database with comprehensive sample data for testing all features.

            db.session.commit()

            print(f"✅ Created {len(courses)} courses\n")                student.set_password('pass123')

            

            # CREATE LAB SCHEDULES                db.session.add(student)            # Clear existing data

            print("📅 Creating lab schedules...")

            today = datetime.utcnow().date()                students.append(student)

            schedule_times = [('08:00', '10:00'), ('10:00', '12:00'), ('13:00', '15:00'), ('15:00', '17:00'), ('17:00', '19:00')]

                                    db.drop_all()    instr1 = User(username='instructor1', email='inst1@lab.edu', full_name='Dr. Smith', role='Instructor')

            schedule_count = 0

            for offset in range(7):            db.session.commit()

                current_date = today + timedelta(days=offset)

                if current_date.weekday() >= 5:            print(f"✅ Created 1 Admin + {len(instructors)} Instructors + {len(students)} Students\n")            db.create_all()

                    continue

                            

                for lab in labs:

                    for course in courses[:3]:            # CREATE LABORATORIES                instr1.set_password('instructor1@123456')from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest, Notification, LabUsageReport

                        for start_time, end_time in schedule_times:

                            schedule = LabSchedule(            print("🏢 Creating laboratories...")

                                lab_id=lab.id,

                                course_id=course.id,            labs_data = [            print("✅ Database cleared and recreated\n")

                                scheduled_date=current_date,

                                start_time=datetime.strptime(start_time, '%H:%M').time(),                {'lab_name': 'Computer Lab 1', 'lab_code': 'CL-101', 'capacity': 30, 'location': 'Building A, Floor 1', 'equipment': 'Desktop Computers, Projector'},

                                end_time=datetime.strptime(end_time, '%H:%M').time(),

                                status='Reserved' if (offset % 2 == 0) else 'Available',                {'lab_name': 'Computer Lab 2', 'lab_code': 'CL-102', 'capacity': 25, 'location': 'Building A, Floor 2', 'equipment': 'Desktop Computers, Interactive Board'},                

                                created_by=admin.id

                            )                {'lab_name': 'Network Lab', 'lab_code': 'NL-201', 'capacity': 20, 'location': 'Building B, Floor 1', 'equipment': 'Networking Equipment, Routers'},

                            db.session.add(schedule)

                            schedule_count += 1                {'lab_name': 'Database Lab', 'lab_code': 'DL-301', 'capacity': 25, 'location': 'Building B, Floor 2', 'equipment': 'Servers, Database Software'},            # ===== CREATE USERS =====

            

            db.session.commit()                {'lab_name': 'Electronics Lab', 'lab_code': 'EL-401', 'capacity': 20, 'location': 'Building C, Floor 1', 'equipment': 'Oscilloscopes, Multimeters'},

            print(f"✅ Created {schedule_count} lab schedules\n")

                            {'lab_name': 'Web Dev Lab', 'lab_code': 'WDL-402', 'capacity': 28, 'location': 'Building C, Floor 2', 'equipment': 'Workstations, Web Servers'},            print("👥 Creating users...")    instr2 = User(username='instructor2', email='inst2@lab.edu', full_name='Prof. Davis', role='Instructor')

            # CREATE RESERVATION REQUESTS

            print("📋 Creating reservation requests...")                {'lab_name': 'Security Lab', 'lab_code': 'SL-501', 'capacity': 20, 'location': 'Building D, Floor 1', 'equipment': 'Firewall, IDS/IPS'},

            requests = []

            for i in range(10):                {'lab_name': 'Mobile Dev Lab', 'lab_code': 'MDL-502', 'capacity': 25, 'location': 'Building D, Floor 2', 'equipment': 'Mobile Devices, Emulators'},            

                instructor = instructors[i % len(instructors)]

                lab = labs[i % len(labs)]            ]

                course = courses[i % len(courses)]

                request_date = today + timedelta(days=(i % 5) + 1)                        # Admin User    instr2.set_password('instructor2@123456')

                

                if i % 3 == 0:            labs = []

                    status, approved_by, approval_date = 'Pending', None, None

                elif i % 3 == 1:            for lab_data in labs_data:            admin = User(

                    status, approved_by, approval_date = 'Approved', admin.id, datetime.utcnow()

                else:                lab = Laboratory(**lab_data)

                    status, approved_by, approval_date = 'Declined', admin.id, datetime.utcnow()

                                db.session.add(lab)                username='admin',    app = create_app()

                request = ReservationRequest(

                    instructor_id=instructor.id,                labs.append(lab)

                    lab_id=lab.id,

                    course_id=course.id,                            email='admin@labsystem.com',

                    requested_date=request_date,

                    start_time=time(9, 0),            db.session.commit()

                    end_time=time(11, 0),

                    status=status,            print(f"✅ Created {len(labs)} laboratory rooms\n")                full_name='System Administrator',    instr3 = User(username='instructor3', email='inst3@lab.edu', full_name='Dr. Patel', role='Instructor')

                    reason=f'Lab session for {course.course_name} Section {course.section}',

                    approved_by=approved_by,            

                    approval_date=approval_date

                )            # CREATE COURSES                role='Administrator'

                db.session.add(request)

                requests.append(request)            print("📚 Creating courses...")

            

            db.session.commit()            courses_data = [            )    instr3.set_password('instructor3@123456')Creates test data for:Features:

            print(f"✅ Created {len(requests)} reservation requests\n")

                            {'course_code': 'CS101', 'course_name': 'Intro to CS', 'credit_hours': 3, 'section': 'A1', 'instructor_id': instructors[0].id},

            # CREATE NOTIFICATIONS

            print("🔔 Creating notifications...")                {'course_code': 'CS101', 'course_name': 'Intro to CS', 'credit_hours': 3, 'section': 'B1', 'instructor_id': instructors[1].id},            admin.set_password('admin123')

            notifications = []

                            {'course_code': 'CS201', 'course_name': 'Data Structures', 'credit_hours': 4, 'section': 'A', 'instructor_id': instructors[0].id},

            for req in requests[:5]:

                if req.status == 'Approved':                {'course_code': 'CS301', 'course_name': 'Database Systems', 'credit_hours': 4, 'section': 'A', 'instructor_id': instructors[2].id},            db.session.add(admin)    

                    notif = Notification(

                        user_id=req.instructor_id,                {'course_code': 'NET401', 'course_name': 'Advanced Networking', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[1].id},

                        title='Reservation Approved ✅',

                        message=f'Your lab reservation has been approved.',                {'course_code': 'WEB301', 'course_name': 'Web Development', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[0].id},            

                        notification_type='approval',

                        related_request_id=req.id,                {'course_code': 'SEC401', 'course_name': 'Cybersecurity', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[1].id},

                        is_read=False

                    )                {'course_code': 'MOB301', 'course_name': 'Mobile Apps', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[2].id},            # Instructor Users    st1 = User(username='student1', email='st1@lab.edu', full_name='Alice', role='Student')with app.app_context():

                    db.session.add(notif)

                    notifications.append(notif)                {'course_code': 'ADV401', 'course_name': 'Advanced Programming', 'credit_hours': 4, 'section': 'A', 'instructor_id': instructors[0].id},

            

            for student in students[:3]:                {'course_code': 'DEV301', 'course_name': 'Software Development', 'credit_hours': 3, 'section': 'A', 'instructor_id': instructors[1].id},            instructors = []

                notif = Notification(

                    user_id=student.id,            ]

                    title='Schedule Updated 📅',

                    message='Your course lab schedule has been updated.',                        for i in range(1, 4):    st1.set_password('password')

                    notification_type='schedule_update',

                    is_read=False            courses = []

                )

                db.session.add(notif)            for course_data in courses_data:                instructor = User(

                notifications.append(notif)

                            course = Course(**course_data)

            db.session.commit()

            print(f"✅ Created {len(notifications)} notifications\n")                db.session.add(course)                    username=f'instructor{i}',        # Clear and recreate- 1 Admin, 3 Instructors, 5 Students- 9 Users (1 Admin, 3 Instructors, 5 Students)

            

            # SUMMARY                courses.append(course)

            print("="*70)

            print("✅ DATABASE SEEDING COMPLETED!")                                email=f'instructor{i}@labsystem.com',

            print("="*70 + "\n")

                        db.session.commit()

            print("📝 TEST CREDENTIALS:\n")

            print("Admin: admin / admin123")            print(f"✅ Created {len(courses)} courses\n")                    full_name=f'Dr. Instructor {i}',    st2 = User(username='student2', email='st2@lab.edu', full_name='Bob', role='Student')

            print("Instructors: instructor1-3 / pass123")

            print("Students: student1-5 / pass123\n")            

            

        except Exception as e:            # CREATE LAB SCHEDULES                    role='Instructor'

            print(f"❌ ERROR: {str(e)}")

            db.session.rollback()            print("📅 Creating lab schedules...")

            raise

            today = datetime.utcnow().date()                )    st2.set_password('password')    db.drop_all()



if __name__ == '__main__':            schedule_times = [('08:00', '10:00'), ('10:00', '12:00'), ('13:00', '15:00'), ('15:00', '17:00'), ('17:00', '19:00')]

    seed_database()

                            instructor.set_password('pass123')

            schedule_count = 0

            for offset in range(7):                db.session.add(instructor)    

                current_date = today + timedelta(days=offset)

                if current_date.weekday() >= 5:                instructors.append(instructor)

                    continue

                                st3 = User(username='student3', email='st3@lab.edu', full_name='Charlie', role='Student')    db.create_all()- 8 Laboratory rooms- 8 Laboratory rooms with equipment

                for lab in labs:

                    for course in courses[:3]:            # Student Users

                        for start_time, end_time in schedule_times:

                            schedule = LabSchedule(            students = []    st3.set_password('password')

                                lab_id=lab.id,

                                course_id=course.id,            for i in range(1, 6):

                                scheduled_date=current_date,

                                start_time=datetime.strptime(start_time, '%H:%M').time(),                student = User(        print("✅ Database cleared and recreated\n")

                                end_time=datetime.strptime(end_time, '%H:%M').time(),

                                status='Reserved' if (offset % 2 == 0) else 'Available',                    username=f'student{i}',

                                created_by=admin.id

                            )                    email=f'student{i}@labsystem.com',    st4 = User(username='student4', email='st4@lab.edu', full_name='Diana', role='Student')

                            db.session.add(schedule)

                            schedule_count += 1                    full_name=f'Student {i}',

            

            db.session.commit()                    role='Student'    st4.set_password('password')    - 10 Courses with instructors- 10 Courses with multiple sections

            print(f"✅ Created {schedule_count} lab schedules\n")

                            )

            # CREATE RESERVATION REQUESTS

            print("📋 Creating reservation requests...")                student.set_password('pass123')    

            requests = []

            for i in range(10):                db.session.add(student)

                instructor = instructors[i % len(instructors)]

                lab = labs[i % len(labs)]                students.append(student)    st5 = User(username='student5', email='st5@lab.edu', full_name='Eve', role='Student')    # Users

                course = courses[i % len(courses)]

                request_date = today + timedelta(days=(i % 5) + 1)            

                

                if i % 3 == 0:            db.session.commit()    st5.set_password('password')

                    status, approved_by, approval_date = 'Pending', None, None

                elif i % 3 == 1:            print(f"✅ Created 1 Admin + {len(instructors)} Instructors + {len(students)} Students\n")

                    status, approved_by, approval_date = 'Approved', admin.id, datetime.utcnow()

                else:                    admin = User(username='admin', email='admin@lab.edu', full_name='Admin', role='Administrator')- 200+ Lab schedules (next 30 days)- 200+ Lab schedules for next 30 days

                    status, approved_by, approval_date = 'Declined', admin.id, datetime.utcnow()

                            # ===== CREATE LABORATORIES =====

                request = ReservationRequest(

                    instructor_id=instructor.id,            print("🏢 Creating laboratories...")    db.session.add_all([admin, instr1, instr2, instr3, st1, st2, st3, st4, st5])

                    lab_id=lab.id,

                    course_id=course.id,            

                    requested_date=request_date,

                    start_time=time(9, 0),            labs_data = [    db.session.commit()    admin.set_password('admin@123456')

                    end_time=time(11, 0),

                    status=status,                {

                    reason=f'Lab session for {course.course_name} Section {course.section}',

                    approved_by=approved_by,                    'lab_name': 'Computer Lab 1',    

                    approval_date=approval_date

                )                    'lab_code': 'CL-101',

                db.session.add(request)

                requests.append(request)                    'capacity': 30,    labs = [    - 10 Reservation requests- 10 Reservation requests with various statuses

            

            db.session.commit()                    'location': 'Building A, Floor 1',

            print(f"✅ Created {len(requests)} reservation requests\n")

                                'equipment': 'Desktop Computers, Projector, Network Switches'        Laboratory(lab_name='Computer Lab A', lab_code='LAB-A', capacity=30, location='Bldg 1, 101', equipment='PCs'),

            # CREATE NOTIFICATIONS

            print("🔔 Creating notifications...")                },

            notifications = []

                            {        Laboratory(lab_name='Computer Lab B', lab_code='LAB-B', capacity=25, location='Bldg 1, 102', equipment='PCs'),    instr1 = User(username='instructor1', email='inst1@lab.edu', full_name='Dr. Smith', role='Instructor')

            for req in requests[:5]:

                if req.status == 'Approved':                    'lab_name': 'Computer Lab 2',

                    notif = Notification(

                        user_id=req.instructor_id,                    'lab_code': 'CL-102',        Laboratory(lab_name='Network Lab', lab_code='LAB-NET', capacity=20, location='Bldg 2, 201', equipment='Routers'),

                        title='Reservation Approved ✅',

                        message=f'Your lab reservation for {req.course.course_name} has been approved.',                    'capacity': 25,

                        notification_type='approval',

                        related_request_id=req.id,                    'location': 'Building A, Floor 2',        Laboratory(lab_name='Database Lab', lab_code='LAB-DB', capacity=25, location='Bldg 2, 202', equipment='Servers'),    instr1.set_password('instructor1@123456')- Sample notifications- Sample notifications

                        is_read=False

                    )                    'equipment': 'Desktop Computers, Interactive Board'

                    db.session.add(notif)

                    notifications.append(notif)                },        Laboratory(lab_name='Dev Lab', lab_code='LAB-DEV', capacity=30, location='Bldg 3, 301', equipment='Workstations'),

                elif req.status == 'Declined':

                    notif = Notification(                {

                        user_id=req.instructor_id,

                        title='Reservation Declined ❌',                    'lab_name': 'Network Lab',        Laboratory(lab_name='Web Lab', lab_code='LAB-WEB', capacity=28, location='Bldg 3, 302', equipment='Servers'),    

                        message=f'Your lab reservation for {req.course.course_name} has been declined.',

                        notification_type='decline',                    'lab_code': 'NL-201',

                        related_request_id=req.id,

                        is_read=False                    'capacity': 20,        Laboratory(lab_name='Security Lab', lab_code='LAB-SEC', capacity=20, location='Bldg 4, 401', equipment='Firewall'),

                    )

                    db.session.add(notif)                    'location': 'Building B, Floor 1',

                    notifications.append(notif)

                                'equipment': 'Networking Equipment, Switches, Routers'        Laboratory(lab_name='Mobile Lab', lab_code='LAB-MOB', capacity=25, location='Bldg 4, 402', equipment='Devices'),    instr2 = User(username='instructor2', email='inst2@lab.edu', full_name='Prof. Davis', role='Instructor')- Usage reports- Usage reports

            for student in students[:3]:

                notif = Notification(                },

                    user_id=student.id,

                    title='Schedule Updated 📅',                {    ]

                    message='Your course lab schedule has been updated. Please review the new timings.',

                    notification_type='schedule_update',                    'lab_name': 'Database Lab',

                    is_read=False

                )                    'lab_code': 'DL-301',        instr2.set_password('instructor2@123456')

                db.session.add(notif)

                notifications.append(notif)                    'capacity': 25,

            

            db.session.commit()                    'location': 'Building B, Floor 2',    db.session.add_all(labs)

            print(f"✅ Created {len(notifications)} notifications\n")

                                'equipment': 'Servers, Database Software, Storage Systems'

            # CREATE USAGE REPORTS

            print("📊 Creating lab usage reports...")                },    db.session.commit()    

            current_month = datetime.now().replace(day=1).date()

            report_count = 0                {

            

            for i, lab in enumerate(labs):                    'lab_name': 'Electronics Lab',    

                report = LabUsageReport(

                    lab_id=lab.id,                    'lab_code': 'EL-401',

                    report_month=current_month,

                    total_sessions=15 + (i % 10),                    'capacity': 20,    courses = [    instr3 = User(username='instructor3', email='inst3@lab.edu', full_name='Dr. Patel', role='Instructor')

                    total_hours=45 + (i * 5),

                    peak_hour='2:00 PM - 3:00 PM'                    'location': 'Building C, Floor 1',

                )

                db.session.add(report)                    'equipment': 'Oscilloscopes, Multimeters, Power Supplies'        Course(course_code='CS101', course_name='Intro to CS', credit_hours=3, section='A', instructor_id=instr1.id),

                report_count += 1

                            },

            db.session.commit()

            print(f"✅ Created {report_count} usage reports\n")                {        Course(course_code='CS101', course_name='Intro to CS', credit_hours=3, section='B', instructor_id=instr2.id),    instr3.set_password('instructor3@123456')Usage: python seed_db.pyUsage: python seed_db.py

            

            # SUMMARY                    'lab_name': 'Web Development Lab',

            print("="*70)

            print("✅ DATABASE SEEDING COMPLETED!")                    'lab_code': 'WDL-402',        Course(course_code='CS202', course_name='Data Structures', credit_hours=4, section='A', instructor_id=instr1.id),

            print("="*70 + "\n")

                                'capacity': 28,

            print("📝 TEST CREDENTIALS:\n")

            print("👤 ADMIN:")                    'location': 'Building C, Floor 2',        Course(course_code='NET301', course_name='Networks', credit_hours=3, section='A', instructor_id=instr2.id),    

            print("   Username: admin | Password: admin123\n")

                                'equipment': 'Development Workstations, Web Servers'

            print("👨‍🏫 INSTRUCTORS:")

            print("   Username: instructor1,2,3 | Password: pass123\n")                },        Course(course_code='DB301', course_name='Databases', credit_hours=3, section='A', instructor_id=instr3.id),

            

            print("👨‍🎓 STUDENTS:")                {

            print("   Username: student1-5 | Password: pass123\n")

                                'lab_name': 'Security Lab',        Course(course_code='WEB302', course_name='Web Dev', credit_hours=3, section='A', instructor_id=instr1.id),    student1 = User(username='student1', email='st1@lab.edu', full_name='Alice', role='Student')""""""

            print("="*70)

            print("Ready to run: python run.py")                    'lab_code': 'SL-501',

            print("="*70 + "\n")

                                'capacity': 20,        Course(course_code='SEC401', course_name='Security', credit_hours=3, section='A', instructor_id=instr2.id),

        except Exception as e:

            print(f"\n❌ ERROR: {str(e)}")                    'location': 'Building D, Floor 1',

            db.session.rollback()

            raise                    'equipment': 'Firewall, IDS/IPS, Isolated Network'        Course(course_code='MOB301', course_name='Mobile Apps', credit_hours=3, section='A', instructor_id=instr3.id),    student1.set_password('password')



                },

if __name__ == '__main__':

    seed_database()                {        Course(course_code='ADV401', course_name='Advanced Prog', credit_hours=4, section='A', instructor_id=instr1.id),


                    'lab_name': 'Mobile Development Lab',

                    'lab_code': 'MDL-502',        Course(course_code='DEV301', course_name='Software Dev', credit_hours=3, section='A', instructor_id=instr2.id),    

                    'capacity': 25,

                    'location': 'Building D, Floor 2',    ]

                    'equipment': 'Mobile Devices, Development Tools, Emulators'

                },        student2 = User(username='student2', email='st2@lab.edu', full_name='Bob', role='Student')

            ]

                db.session.add_all(courses)

            labs = []

            for lab_data in labs_data:    db.session.commit()    student2.set_password('password')from datetime import datetime, timedelta, timeimport os

                lab = Laboratory(**lab_data)

                db.session.add(lab)    

                labs.append(lab)

                print("\n" + "="*60)    

            db.session.commit()

            print(f"✅ Created {len(labs)} laboratory rooms\n")    print("✅ DATABASE SEEDING COMPLETE!")

            

            # ===== CREATE COURSES =====    print("="*60)    student3 = User(username='student3', email='st3@lab.edu', full_name='Charlie', role='Student')from app import create_app, dbimport sys

            print("📚 Creating courses...")

                print("\n📋 TEST CREDENTIALS:\n")

            courses_data = [

                {    print("Admin: admin / admin@123456")    student3.set_password('password')

                    'course_code': 'CS101',

                    'course_name': 'Introduction to Computer Science',    print("Instructors: instructor1,2,3 / instructor1,2,3@123456")

                    'credit_hours': 3,

                    'section': 'A1',    print("Students: student1-5 / password")    from app.models import (from datetime import datetime, timedelta, time

                    'instructor_id': instructors[0].id

                },    print("="*60 + "\n")

                {

                    'course_code': 'CS101',    student4 = User(username='student4', email='st4@lab.edu', full_name='Diana', role='Student')

                    'course_name': 'Introduction to Computer Science',

                    'credit_hours': 3,    student4.set_password('password')    User, Laboratory, Course, LabSchedule, from app import create_app, db

                    'section': 'B1',

                    'instructor_id': instructors[1].id    

                },

                {    student5 = User(username='student5', email='st5@lab.edu', full_name='Eve', role='Student')    ReservationRequest, Notification, LabUsageReportfrom app.models import (

                    'course_code': 'CS201',

                    'course_name': 'Data Structures',    student5.set_password('password')

                    'credit_hours': 4,

                    'section': 'A',    )    User, Laboratory, Course, LabSchedule, 

                    'instructor_id': instructors[0].id

                },    db.session.add_all([admin, instr1, instr2, instr3, student1, student2, student3, student4, student5])

                {

                    'course_code': 'CS301',    db.session.commit()    ReservationRequest, Notification, LabUsageReport

                    'course_name': 'Database Systems',

                    'credit_hours': 4,    print("✅ Created 1 Admin, 3 Instructors, 5 Students")

                    'section': 'A',

                    'instructor_id': instructors[2].id    def seed_database():)

                },

                {    # Labs

                    'course_code': 'CS202',

                    'course_name': 'Network Administration',    labs_info = [    """Main seeding function"""

                    'credit_hours': 3,

                    'section': 'B2',        ('Computer Lab A', 'LAB-A', 30, 'Bldg 1, Room 101', 'PCs, Projector'),

                    'instructor_id': instructors[1].id

                },        ('Computer Lab B', 'LAB-B', 25, 'Bldg 1, Room 102', 'PCs, Board'),    app = create_app()def seed_database():

                {

                    'course_code': 'NET401',        ('Network Lab', 'LAB-NET', 20, 'Bldg 2, Room 201', 'Routers, Switches'),

                    'course_name': 'Advanced Networking',

                    'credit_hours': 3,        ('Database Lab', 'LAB-DB', 25, 'Bldg 2, Room 202', 'Servers, DB Software'),        """Seed the database with comprehensive sample data"""

                    'section': 'A',

                    'instructor_id': instructors[1].id        ('Development Lab', 'LAB-DEV', 30, 'Bldg 3, Room 301', 'Workstations, IDEs'),

                },

                {        ('Web Lab', 'LAB-WEB', 28, 'Bldg 3, Room 302', 'Web Servers'),    with app.app_context():    app = create_app()

                    'course_code': 'WEB301',

                    'course_name': 'Web Development',        ('Security Lab', 'LAB-SEC', 20, 'Bldg 4, Room 401', 'Firewall, IDS'),

                    'credit_hours': 3,

                    'section': 'A',        ('Mobile Lab', 'LAB-MOB', 25, 'Bldg 4, Room 402', 'Devices, SDKs'),        print("\n" + "="*70)    

                    'instructor_id': instructors[0].id

                },    ]

                {

                    'course_code': 'SEC401',            print("🌱 IT LAB SYSTEM - DATABASE SEEDING")    with app.app_context():

                    'course_name': 'Cybersecurity Fundamentals',

                    'credit_hours': 3,    labs = []

                    'section': 'A',

                    'instructor_id': instructors[1].id    for name, code, cap, loc, equip in labs_info:        print("="*70 + "\n")        # Clear existing data

                },

                {        lab = Laboratory(lab_name=name, lab_code=code, capacity=cap, location=loc, equipment=equip)

                    'course_code': 'MOB301',

                    'course_name': 'Mobile App Development',        labs.append(lab)                print("\n" + "="*60)

                    'credit_hours': 3,

                    'section': 'A',    

                    'instructor_id': instructors[2].id

                },    db.session.add_all(labs)        try:        print("🗑️  Clearing existing data...")

                {

                    'course_code': 'ADV401',    db.session.commit()

                    'course_name': 'Advanced Programming',

                    'credit_hours': 4,    print(f"✅ Created {len(labs)} labs")            # Clear        print("="*60)

                    'section': 'A',

                    'instructor_id': instructors[0].id    

                },

            ]    # Courses            print("🗑️  Clearing existing data...")        db.drop_all()

            

            courses = []    courses_info = [

            for course_data in courses_data:

                course = Course(**course_data)        ('CS101', 'Intro to CS', 3, 'A', instr1),            db.drop_all()        db.create_all()

                db.session.add(course)

                courses.append(course)        ('CS101', 'Intro to CS', 3, 'B', instr2),

            

            db.session.commit()        ('CS202', 'Data Structures', 4, 'A', instr1),            db.create_all()        

            print(f"✅ Created {len(courses)} courses\n")

                    ('NET301', 'Networks', 3, 'A', instr2),

            # ===== CREATE LAB SCHEDULES =====

            print("📅 Creating lab schedules (next 7 days, 8 AM - 7 PM)...")        ('DB301', 'Databases', 3, 'A', instr3),            print("✅ Database cleared and recreated\n")        # Create Admin User

            

            today = datetime.utcnow().date()        ('WEB302', 'Web Dev', 3, 'A', instr1),

            

            schedule_times = [        ('SEC401', 'Security', 3, 'A', instr2),                    print("Creating admin user...")

                ('08:00', '10:00'),

                ('10:00', '12:00'),        ('MOB301', 'Mobile Apps', 3, 'A', instr3),

                ('13:00', '15:00'),

                ('15:00', '17:00'),        ('ADV401', 'Advanced Prog', 4, 'A', instr1),            # Create Users        admin = User(

                ('17:00', '19:00'),

            ]        ('DEV301', 'Software Dev', 3, 'A', instr2),

            

            schedule_count = 0    ]            print("👥 Creating users...")            username='admin',

            for offset in range(7):

                current_date = today + timedelta(days=offset)    

                

                # Skip weekends    courses = []            admin = User(            email='admin@labsystem.com',

                if current_date.weekday() >= 5:

                    continue    for code, name, credits, section, instr in courses_info:

                

                for lab in labs:        course = Course(course_code=code, course_name=name, credit_hours=credits, section=section, instructor_id=instr.id)                username='admin',            full_name='System Administrator',

                    for course in courses[:3]:

                        for start_time, end_time in schedule_times:        courses.append(course)

                            schedule = LabSchedule(

                                lab_id=lab.id,                    email='admin@labsystem.edu',            role='Administrator'

                                course_id=course.id,

                                scheduled_date=current_date,    db.session.add_all(courses)

                                start_time=datetime.strptime(start_time, '%H:%M').time(),

                                end_time=datetime.strptime(end_time, '%H:%M').time(),    db.session.commit()                full_name='System Administrator',        )

                                status='Reserved' if (offset % 2 == 0) else 'Available',

                                created_by=admin.id    print(f"✅ Created {len(courses)} courses")

                            )

                            db.session.add(schedule)                    role='Administrator',        admin.set_password('admin123')

                            schedule_count += 1

                print("\n" + "="*60)

            db.session.commit()

            print(f"✅ Created {schedule_count} lab schedules\n")    print("✅ DATABASE SEEDING COMPLETE!")                is_active=True        db.session.add(admin)

            

            # ===== CREATE RESERVATION REQUESTS =====    print("="*60)

            print("📋 Creating reservation requests...")

                print("\n📋 TEST CREDENTIALS:\n")            )        

            requests = []

            for i in range(10):    print("Admin: admin / admin@123456")

                instructor = instructors[i % len(instructors)]

                lab = labs[i % len(labs)]    print("Instructors: instructor{1,2,3} / instructor{1,2,3}@123456")            admin.set_password('admin@123456')        # Create Instructor Users

                course = courses[i % len(courses)]

                request_date = today + timedelta(days=(i % 5) + 1)    print("Students: student{1-5} / password")

                

                # Vary status    print("="*60 + "\n")            db.session.add(admin)        print("Creating instructors...")

                if i % 3 == 0:

                    status = 'Pending'

                    approved_by = None                    instructors = []

                    approval_date = None

                elif i % 3 == 1:            instructors = []        for i in range(1, 4):

                    status = 'Approved'

                    approved_by = admin.id            for i in range(1, 4):            instructor = User(

                    approval_date = datetime.utcnow()

                else:                instructor = User(                username=f'instructor{i}',

                    status = 'Declined'

                    approved_by = admin.id                    username=f'instructor{i}',                email=f'instructor{i}@labsystem.com',

                    approval_date = datetime.utcnow()

                                    email=f'instructor{i}@university.edu',                full_name=f'Instructor {i}',

                request = ReservationRequest(

                    instructor_id=instructor.id,                    full_name=f'Dr. Instructor {i}',                role='Instructor'

                    lab_id=lab.id,

                    course_id=course.id,                    role='Instructor',            )

                    requested_date=request_date,

                    start_time=time(9, 0),                    is_active=True            instructor.set_password('pass123')

                    end_time=time(11, 0),

                    status=status,                )            db.session.add(instructor)

                    reason=f'Lab session for {course.course_name} Section {course.section}',

                    approved_by=approved_by,                instructor.set_password(f'instructor{i}@123456')            instructors.append(instructor)

                    approval_date=approval_date

                )                db.session.add(instructor)        

                db.session.add(request)

                requests.append(request)                instructors.append(instructor)        # Create Student Users

            

            db.session.commit()                    print("Creating students...")

            print(f"✅ Created {len(requests)} reservation requests\n")

                        students = []        students = []

            # ===== CREATE NOTIFICATIONS =====

            print("🔔 Creating notifications...")            for i in range(1, 6):        for i in range(1, 6):

            

            notifications = []                student = User(            student = User(

            

            for req in requests[:5]:                    username=f'student{i}',                username=f'student{i}',

                if req.status == 'Approved':

                    notif = Notification(                    email=f'student{i}@university.edu',                email=f'student{i}@labsystem.com',

                        user_id=req.instructor_id,

                        title='Reservation Approved ✅',                    full_name=f'Student {i}',                full_name=f'Student {i}',

                        message=f'Your lab reservation for {req.course.course_name} on {req.requested_date} has been approved.',

                        notification_type='approval',                    role='Student',                role='Student'

                        related_request_id=req.id,

                        is_read=False                    is_active=True            )

                    )

                    db.session.add(notif)                )            student.set_password('pass123')

                    notifications.append(notif)

                elif req.status == 'Declined':                student.set_password('password')            db.session.add(student)

                    notif = Notification(

                        user_id=req.instructor_id,                db.session.add(student)            students.append(student)

                        title='Reservation Declined ❌',

                        message=f'Your lab reservation for {req.course.course_name} has been declined.',                students.append(student)        

                        notification_type='decline',

                        related_request_id=req.id,                    db.session.commit()

                        is_read=False

                    )            db.session.commit()        

                    db.session.add(notif)

                    notifications.append(notif)            print(f"✅ Created 1 Admin + {len(instructors)} Instructors + {len(students)} Students\n")        # Create Laboratories

            

            for student in students[:3]:                    print("Creating laboratories...")

                notif = Notification(

                    user_id=student.id,            # Create Labs        labs_data = [

                    title='Schedule Updated 📅',

                    message='Your course lab schedule has been updated. Please review the new timings.',            print("🏢 Creating laboratory rooms...")            {

                    notification_type='schedule_update',

                    is_read=False            labs_data = [                'lab_name': 'Computer Lab 1',

                )

                db.session.add(notif)                ('Computer Lab A', 'LAB-A', 30, 'Building 1, Room 101', 'Desktop PCs, Projector, Printer'),                'lab_code': 'CL-101',

                notifications.append(notif)

                            ('Computer Lab B', 'LAB-B', 25, 'Building 1, Room 102', 'Desktop PCs, Interactive Board'),                'capacity': 30,

            db.session.commit()

            print(f"✅ Created {len(notifications)} notifications\n")                ('Networking Lab', 'LAB-NET', 20, 'Building 2, Room 201', 'Networking Equipment, Routers'),                'location': 'Building A, Floor 1',

            

            # ===== CREATE USAGE REPORTS =====                ('Database Lab', 'LAB-DB', 25, 'Building 2, Room 202', 'Servers, Database Software'),                'equipment': 'Desktop Computers, Projector, Network Switches'

            print("📊 Creating lab usage reports...")

                            ('Software Dev Lab', 'LAB-DEV', 30, 'Building 3, Room 301', 'Dev Workstations, IDEs'),            },

            current_month = datetime.now().replace(day=1).date()

            report_count = 0                ('Web Lab', 'LAB-WEB', 28, 'Building 3, Room 302', 'Web Servers, Development Tools'),            {

            

            for i, lab in enumerate(labs):                ('Security Lab', 'LAB-SEC', 20, 'Building 4, Room 401', 'Firewall, IDS/IPS, Isolated Network'),                'lab_name': 'Computer Lab 2',

                report = LabUsageReport(

                    lab_id=lab.id,                ('Mobile Lab', 'LAB-MOB', 25, 'Building 4, Room 402', 'Devices, Development Tools'),                'lab_code': 'CL-102',

                    report_month=current_month,

                    total_sessions=15 + (i % 10),            ]                'capacity': 25,

                    total_hours=45 + (i * 5),

                    peak_hour='2:00 PM - 3:00 PM'                            'location': 'Building A, Floor 2',

                )

                db.session.add(report)            labs = {}                'equipment': 'Desktop Computers, Interactive Board'

                report_count += 1

                        for lab_name, lab_code, capacity, location, equipment in labs_data:            },

            db.session.commit()

            print(f"✅ Created {report_count} usage reports\n")                lab = Laboratory(            {

            

            # ===== SUMMARY =====                    lab_name=lab_name,                'lab_name': 'Network Lab',

            print("="*70)

            print("✅ DATABASE SEEDING COMPLETED SUCCESSFULLY!")                    lab_code=lab_code,                'lab_code': 'NL-201',

            print("="*70 + "\n")

                                capacity=capacity,                'capacity': 20,

            print("📝 TEST CREDENTIALS:\n")

            print("👤 ADMIN:")                    location=location,                'location': 'Building B, Floor 1',

            print("   Username: admin")

            print("   Password: admin123\n")                    equipment=equipment,                'equipment': 'Networking Equipment, Switches, Routers'

            

            print("👨‍🏫 INSTRUCTORS:")                    is_active=True            },

            print("   Username: instructor1, instructor2, instructor3")

            print("   Password: pass123\n")                )            {

            

            print("👨‍🎓 STUDENTS:")                db.session.add(lab)                'lab_name': 'Database Lab',

            print("   Username: student1, student2, student3, student4, student5")

            print("   Password: pass123\n")                labs[lab_code] = lab                'lab_code': 'DL-301',

            

            print("="*70)                            'capacity': 25,

            print("Ready to run the application!")

            print("="*70 + "\n")            db.session.commit()                'location': 'Building B, Floor 2',

            

        except Exception as e:            print(f"✅ Created {len(labs)} laboratory rooms\n")                'equipment': 'Servers, Database Software, Storage Systems'

            print(f"\n❌ ERROR: {str(e)}")

            db.session.rollback()                        },

            raise

            # Create Courses            {



if __name__ == '__main__':            print("📚 Creating courses...")                'lab_name': 'Electronics Lab',

    seed_database()

            courses = []                'lab_code': 'EL-401',

            course_data = [                'capacity': 20,

                ('CS101', 'Intro to Computer Science', 3, 'A', instructors[0]),                'location': 'Building C, Floor 1',

                ('CS101', 'Intro to Computer Science', 3, 'B', instructors[1]),                'equipment': 'Oscilloscopes, Multimeters, Power Supplies'

                ('CS202', 'Data Structures', 4, 'A', instructors[0]),            },

                ('NET301', 'Computer Networks', 3, 'A', instructors[1]),        ]

                ('DB301', 'Database Systems', 3, 'A', instructors[2]),        

                ('WEB302', 'Web Development', 3, 'A', instructors[0]),        labs = []

                ('SEC401', 'Cybersecurity', 3, 'A', instructors[1]),        for lab_data in labs_data:

                ('MOB301', 'Mobile Apps', 3, 'A', instructors[2]),            lab = Laboratory(**lab_data)

                ('ADV401', 'Advanced Programming', 4, 'A', instructors[0]),            db.session.add(lab)

                ('DEV301', 'Software Development', 3, 'A', instructors[1]),            labs.append(lab)

            ]        

                    db.session.commit()

            for code, name, credits, section, instructor in course_data:        

                course = Course(        # Create Courses

                    course_code=code,        print("Creating courses...")

                    course_name=name,        courses_data = [

                    credit_hours=credits,            {

                    section=section,                'course_code': 'CS101',

                    instructor_id=instructor.id,                'course_name': 'Introduction to Computer Science',

                    description=f'{name} - Section {section}',                'credit_hours': 3,

                    is_active=True                'section': 'A1',

                )                'instructor_id': instructors[0].id

                db.session.add(course)            },

                courses.append(course)            {

                            'course_code': 'CS201',

            db.session.commit()                'course_name': 'Data Structures',

            print(f"✅ Created {len(courses)} courses\n")                'credit_hours': 4,

                            'section': 'B1',

            # Create Lab Schedules                'instructor_id': instructors[1].id

            print("📅 Creating lab schedules (next 30 days, 8 AM - 7 PM)...")            },

            schedules = []            {

            base_date = datetime.now().date()                'course_code': 'CS301',

            labs_list = list(labs.values())                'course_name': 'Database Systems',

                            'credit_hours': 4,

            time_slots = [                'section': 'C1',

                (time(8, 0), time(9, 30)),                'instructor_id': instructors[2].id

                (time(9, 30), time(11, 0)),            },

                (time(11, 0), time(12, 30)),            {

                (time(12, 30), time(14, 0)),                'course_code': 'CS102',

                (time(14, 0), time(15, 30)),                'course_name': 'Introduction to Computer Science',

                (time(15, 30), time(17, 0)),                'credit_hours': 3,

                (time(17, 0), time(18, 30)),                'section': 'A2',

                (time(18, 30), time(20, 0)),                'instructor_id': instructors[0].id

            ]            },

                        {

            schedule_count = 0                'course_code': 'CS202',

            for day_offset in range(30):                'course_name': 'Network Administration',

                schedule_date = base_date + timedelta(days=day_offset)                'credit_hours': 3,

                                'section': 'B2',

                # Skip weekends                'instructor_id': instructors[1].id

                if schedule_date.weekday() >= 5:            },

                    continue        ]

                        

                for lab in labs_list:        courses = []

                    for slot_idx, (start, end) in enumerate(time_slots):        for course_data in courses_data:

                        # Vary status            course = Course(**course_data)

                        if (day_offset + slot_idx) % 3 == 0:            db.session.add(course)

                            status = 'Available'            courses.append(course)

                        elif (day_offset + slot_idx) % 3 == 1:        

                            status = 'Reserved'        db.session.commit()

                        else:        

                            status = 'Available'        # Create Lab Schedules

                                print("Creating lab schedules...")

                        course = courses[slot_idx % len(courses)]        today = datetime.utcnow().date()

                                

                        schedule = LabSchedule(        schedule_times = [

                            lab_id=lab.id,            ('08:00', '10:00'),

                            course_id=course.id,            ('10:00', '12:00'),

                            scheduled_date=schedule_date,            ('13:00', '15:00'),

                            start_time=start,            ('15:00', '17:00'),

                            end_time=end,        ]

                            status=status,        

                            notes=f'Session for {course.course_name}',        schedule_count = 0

                            created_by=admin.id        for offset in range(7):  # Create schedules for next 7 days

                        )            current_date = today + timedelta(days=offset)

                        db.session.add(schedule)            

                        schedule_count += 1            # Skip weekends

                        if current_date.weekday() >= 5:

            db.session.commit()                continue

            print(f"✅ Created {schedule_count} lab schedules\n")            

                        for lab in labs:

            # Create Reservation Requests                for course in courses[:3]:

            print("📋 Creating reservation requests...")                    for start_time, end_time in schedule_times:

            requests = []                        schedule = LabSchedule(

            for i in range(10):                            lab_id=lab.id,

                instructor = instructors[i % len(instructors)]                            course_id=course.id,

                lab = labs_list[i % len(labs_list)]                            scheduled_date=current_date,

                course = courses[i % len(courses)]                            start_time=datetime.strptime(start_time, '%H:%M').time(),

                request_date = base_date + timedelta(days=(i % 20) + 1)                            end_time=datetime.strptime(end_time, '%H:%M').time(),

                                            status='Reserved' if (offset % 2 == 0) else 'Available',

                # Vary status                            created_by=admin.id

                if i % 3 == 0:                        )

                    status = 'Pending'                        db.session.add(schedule)

                    approved_by = None                        schedule_count += 1

                    approval_date = None        

                elif i % 3 == 1:        db.session.commit()

                    status = 'Approved'        

                    approved_by = admin.id        print("\n✅ Database seeding completed successfully!")

                    approval_date = datetime.utcnow()        print(f"   - Created {len(instructors)} instructors")

                else:        print(f"   - Created {len(students)} students")

                    status = 'Declined'        print(f"   - Created {len(labs)} laboratories")

                    approved_by = admin.id        print(f"   - Created {len(courses)} courses")

                    approval_date = datetime.utcnow()        print(f"   - Created {schedule_count} lab schedules")

                        print("\n📝 Demo Credentials:")

                request = ReservationRequest(        print("   - Admin: admin / admin123")

                    instructor_id=instructor.id,        print("   - Instructor: instructor1 / pass123")

                    lab_id=lab.id,        print("   - Student: student1 / pass123")

                    course_id=course.id,

                    requested_date=request_date,if __name__ == '__main__':

                    start_time=time(9, 0),    seed_database()

                    end_time=time(11, 0),
                    status=status,
                    reason=f'Lab session for {course.course_name} Section {course.section}',
                    approved_by=approved_by,
                    approval_date=approval_date
                )
                db.session.add(request)
                requests.append(request)
            
            db.session.commit()
            print(f"✅ Created {len(requests)} reservation requests\n")
            
            # Create Notifications
            print("🔔 Creating notifications...")
            notifications = []
            
            for req in requests[:5]:
                if req.status == 'Approved':
                    notif = Notification(
                        user_id=req.instructor_id,
                        title='Reservation Approved ✅',
                        message=f'Your lab reservation for {req.course.course_name} on {req.requested_date} has been approved.',
                        notification_type='approval',
                        related_request_id=req.id,
                        is_read=False
                    )
                    db.session.add(notif)
                    notifications.append(notif)
                elif req.status == 'Declined':
                    notif = Notification(
                        user_id=req.instructor_id,
                        title='Reservation Declined ❌',
                        message=f'Your lab reservation for {req.course.course_name} has been declined.',
                        notification_type='decline',
                        related_request_id=req.id,
                        is_read=False
                    )
                    db.session.add(notif)
                    notifications.append(notif)
            
            for student in students[:3]:
                notif = Notification(
                    user_id=student.id,
                    title='Schedule Updated 📅',
                    message='Your course lab schedule has been updated. Please review the new timings.',
                    notification_type='schedule_update',
                    is_read=False
                )
                db.session.add(notif)
                notifications.append(notif)
            
            db.session.commit()
            print(f"✅ Created {len(notifications)} notifications\n")
            
            # Create Usage Reports
            print("📊 Creating lab usage reports...")
            current_month = datetime.now().replace(day=1).date()
            report_count = 0
            
            for i, lab in enumerate(labs_list):
                report = LabUsageReport(
                    lab_id=lab.id,
                    report_month=current_month,
                    total_sessions=15 + (i % 10),
                    total_hours=45 + (i * 5),
                    peak_hour='2:00 PM - 3:00 PM'
                )
                db.session.add(report)
                report_count += 1
            
            db.session.commit()
            print(f"✅ Created {report_count} usage reports\n")
            
            # Summary
            print("="*70)
            print("✅ DATABASE SEEDING COMPLETED SUCCESSFULLY!")
            print("="*70 + "\n")
            
            print("📝 TEST CREDENTIALS:\n")
            print("👤 ADMIN:")
            print("   Username: admin")
            print("   Password: admin@123456\n")
            
            print("👨‍🏫 INSTRUCTORS:")
            print("   Username: instructor1, instructor2, instructor3")
            print("   Password: {username}@123456\n")
            
            print("👨‍🎓 STUDENTS:")
            print("   Username: student1, student2, student3, student4, student5")
            print("   Password: password\n")
            
            print("="*70)
            print("Ready to run the application!")
            print("="*70 + "\n")
            
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    seed_database()
