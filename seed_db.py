from datetime import time#!/usr/bin/env python3#!/usr/bin/env python3#!/usr/bin/env python3

from app import create_app, db

from app.models import User, Laboratory, Course"""



app = create_app()Seed Database Script for IT Lab System""""""



with app.app_context():Quick seed script to populate test data

    db.drop_all()

    db.create_all()"""Comprehensive Database Seeding ScriptSeed Database Script - Enterprise IT Lab System

    

    admin = User(username='admin', email='admin@lab.edu', full_name='Admin', role='Administrator')from datetime import datetime, timedelta, time

    admin.set_password('admin@123456')

    from app import create_app, dbIT Laboratory Utilization Schedule SystemPopulates the database with comprehensive sample data for testing all features.

    instr1 = User(username='instructor1', email='inst1@lab.edu', full_name='Dr. Smith', role='Instructor')

    instr1.set_password('instructor1@123456')from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest, Notification, LabUsageReport

    

    instr2 = User(username='instructor2', email='inst2@lab.edu', full_name='Prof. Davis', role='Instructor')

    instr2.set_password('instructor2@123456')

    app = create_app()

    instr3 = User(username='instructor3', email='inst3@lab.edu', full_name='Dr. Patel', role='Instructor')

    instr3.set_password('instructor3@123456')Creates test data for:Features:

    

    st1 = User(username='student1', email='st1@lab.edu', full_name='Alice', role='Student')with app.app_context():

    st1.set_password('password')

        # Clear and recreate- 1 Admin, 3 Instructors, 5 Students- 9 Users (1 Admin, 3 Instructors, 5 Students)

    st2 = User(username='student2', email='st2@lab.edu', full_name='Bob', role='Student')

    st2.set_password('password')    db.drop_all()

    

    st3 = User(username='student3', email='st3@lab.edu', full_name='Charlie', role='Student')    db.create_all()- 8 Laboratory rooms- 8 Laboratory rooms with equipment

    st3.set_password('password')

        print("✅ Database cleared and recreated\n")

    st4 = User(username='student4', email='st4@lab.edu', full_name='Diana', role='Student')

    st4.set_password('password')    - 10 Courses with instructors- 10 Courses with multiple sections

    

    st5 = User(username='student5', email='st5@lab.edu', full_name='Eve', role='Student')    # Users

    st5.set_password('password')

        admin = User(username='admin', email='admin@lab.edu', full_name='Admin', role='Administrator')- 200+ Lab schedules (next 30 days)- 200+ Lab schedules for next 30 days

    db.session.add_all([admin, instr1, instr2, instr3, st1, st2, st3, st4, st5])

    db.session.commit()    admin.set_password('admin@123456')

    

    labs = [    - 10 Reservation requests- 10 Reservation requests with various statuses

        Laboratory(lab_name='Computer Lab A', lab_code='LAB-A', capacity=30, location='Bldg 1, 101', equipment='PCs'),

        Laboratory(lab_name='Computer Lab B', lab_code='LAB-B', capacity=25, location='Bldg 1, 102', equipment='PCs'),    instr1 = User(username='instructor1', email='inst1@lab.edu', full_name='Dr. Smith', role='Instructor')

        Laboratory(lab_name='Network Lab', lab_code='LAB-NET', capacity=20, location='Bldg 2, 201', equipment='Routers'),

        Laboratory(lab_name='Database Lab', lab_code='LAB-DB', capacity=25, location='Bldg 2, 202', equipment='Servers'),    instr1.set_password('instructor1@123456')- Sample notifications- Sample notifications

        Laboratory(lab_name='Dev Lab', lab_code='LAB-DEV', capacity=30, location='Bldg 3, 301', equipment='Workstations'),

        Laboratory(lab_name='Web Lab', lab_code='LAB-WEB', capacity=28, location='Bldg 3, 302', equipment='Servers'),    

        Laboratory(lab_name='Security Lab', lab_code='LAB-SEC', capacity=20, location='Bldg 4, 401', equipment='Firewall'),

        Laboratory(lab_name='Mobile Lab', lab_code='LAB-MOB', capacity=25, location='Bldg 4, 402', equipment='Devices'),    instr2 = User(username='instructor2', email='inst2@lab.edu', full_name='Prof. Davis', role='Instructor')- Usage reports- Usage reports

    ]

        instr2.set_password('instructor2@123456')

    db.session.add_all(labs)

    db.session.commit()    

    

    courses = [    instr3 = User(username='instructor3', email='inst3@lab.edu', full_name='Dr. Patel', role='Instructor')

        Course(course_code='CS101', course_name='Intro to CS', credit_hours=3, section='A', instructor_id=instr1.id),

        Course(course_code='CS101', course_name='Intro to CS', credit_hours=3, section='B', instructor_id=instr2.id),    instr3.set_password('instructor3@123456')Usage: python seed_db.pyUsage: python seed_db.py

        Course(course_code='CS202', course_name='Data Structures', credit_hours=4, section='A', instructor_id=instr1.id),

        Course(course_code='NET301', course_name='Networks', credit_hours=3, section='A', instructor_id=instr2.id),    

        Course(course_code='DB301', course_name='Databases', credit_hours=3, section='A', instructor_id=instr3.id),

        Course(course_code='WEB302', course_name='Web Dev', credit_hours=3, section='A', instructor_id=instr1.id),    student1 = User(username='student1', email='st1@lab.edu', full_name='Alice', role='Student')""""""

        Course(course_code='SEC401', course_name='Security', credit_hours=3, section='A', instructor_id=instr2.id),

        Course(course_code='MOB301', course_name='Mobile Apps', credit_hours=3, section='A', instructor_id=instr3.id),    student1.set_password('password')

        Course(course_code='ADV401', course_name='Advanced Prog', credit_hours=4, section='A', instructor_id=instr1.id),

        Course(course_code='DEV301', course_name='Software Dev', credit_hours=3, section='A', instructor_id=instr2.id),    

    ]

        student2 = User(username='student2', email='st2@lab.edu', full_name='Bob', role='Student')

    db.session.add_all(courses)

    db.session.commit()    student2.set_password('password')from datetime import datetime, timedelta, timeimport os

    

    print("\n" + "="*60)    

    print("✅ DATABASE SEEDING COMPLETE!")

    print("="*60)    student3 = User(username='student3', email='st3@lab.edu', full_name='Charlie', role='Student')from app import create_app, dbimport sys

    print("\n📋 TEST CREDENTIALS:\n")

    print("Admin: admin / admin@123456")    student3.set_password('password')

    print("Instructors: instructor1,2,3 / instructor1,2,3@123456")

    print("Students: student1-5 / password")    from app.models import (from datetime import datetime, timedelta, time

    print("="*60 + "\n")

    student4 = User(username='student4', email='st4@lab.edu', full_name='Diana', role='Student')

    student4.set_password('password')    User, Laboratory, Course, LabSchedule, from app import create_app, db

    

    student5 = User(username='student5', email='st5@lab.edu', full_name='Eve', role='Student')    ReservationRequest, Notification, LabUsageReportfrom app.models import (

    student5.set_password('password')

    )    User, Laboratory, Course, LabSchedule, 

    db.session.add_all([admin, instr1, instr2, instr3, student1, student2, student3, student4, student5])

    db.session.commit()    ReservationRequest, Notification, LabUsageReport

    print("✅ Created 1 Admin, 3 Instructors, 5 Students")

    def seed_database():)

    # Labs

    labs_info = [    """Main seeding function"""

        ('Computer Lab A', 'LAB-A', 30, 'Bldg 1, Room 101', 'PCs, Projector'),

        ('Computer Lab B', 'LAB-B', 25, 'Bldg 1, Room 102', 'PCs, Board'),    app = create_app()def seed_database():

        ('Network Lab', 'LAB-NET', 20, 'Bldg 2, Room 201', 'Routers, Switches'),

        ('Database Lab', 'LAB-DB', 25, 'Bldg 2, Room 202', 'Servers, DB Software'),        """Seed the database with comprehensive sample data"""

        ('Development Lab', 'LAB-DEV', 30, 'Bldg 3, Room 301', 'Workstations, IDEs'),

        ('Web Lab', 'LAB-WEB', 28, 'Bldg 3, Room 302', 'Web Servers'),    with app.app_context():    app = create_app()

        ('Security Lab', 'LAB-SEC', 20, 'Bldg 4, Room 401', 'Firewall, IDS'),

        ('Mobile Lab', 'LAB-MOB', 25, 'Bldg 4, Room 402', 'Devices, SDKs'),        print("\n" + "="*70)    

    ]

            print("🌱 IT LAB SYSTEM - DATABASE SEEDING")    with app.app_context():

    labs = []

    for name, code, cap, loc, equip in labs_info:        print("="*70 + "\n")        # Clear existing data

        lab = Laboratory(lab_name=name, lab_code=code, capacity=cap, location=loc, equipment=equip)

        labs.append(lab)                print("\n" + "="*60)

    

    db.session.add_all(labs)        try:        print("🗑️  Clearing existing data...")

    db.session.commit()

    print(f"✅ Created {len(labs)} labs")            # Clear        print("="*60)

    

    # Courses            print("🗑️  Clearing existing data...")        db.drop_all()

    courses_info = [

        ('CS101', 'Intro to CS', 3, 'A', instr1),            db.drop_all()        db.create_all()

        ('CS101', 'Intro to CS', 3, 'B', instr2),

        ('CS202', 'Data Structures', 4, 'A', instr1),            db.create_all()        

        ('NET301', 'Networks', 3, 'A', instr2),

        ('DB301', 'Databases', 3, 'A', instr3),            print("✅ Database cleared and recreated\n")        # Create Admin User

        ('WEB302', 'Web Dev', 3, 'A', instr1),

        ('SEC401', 'Security', 3, 'A', instr2),                    print("Creating admin user...")

        ('MOB301', 'Mobile Apps', 3, 'A', instr3),

        ('ADV401', 'Advanced Prog', 4, 'A', instr1),            # Create Users        admin = User(

        ('DEV301', 'Software Dev', 3, 'A', instr2),

    ]            print("👥 Creating users...")            username='admin',

    

    courses = []            admin = User(            email='admin@labsystem.com',

    for code, name, credits, section, instr in courses_info:

        course = Course(course_code=code, course_name=name, credit_hours=credits, section=section, instructor_id=instr.id)                username='admin',            full_name='System Administrator',

        courses.append(course)

                    email='admin@labsystem.edu',            role='Administrator'

    db.session.add_all(courses)

    db.session.commit()                full_name='System Administrator',        )

    print(f"✅ Created {len(courses)} courses")

                    role='Administrator',        admin.set_password('admin123')

    print("\n" + "="*60)

    print("✅ DATABASE SEEDING COMPLETE!")                is_active=True        db.session.add(admin)

    print("="*60)

    print("\n📋 TEST CREDENTIALS:\n")            )        

    print("Admin: admin / admin@123456")

    print("Instructors: instructor{1,2,3} / instructor{1,2,3}@123456")            admin.set_password('admin@123456')        # Create Instructor Users

    print("Students: student{1-5} / password")

    print("="*60 + "\n")            db.session.add(admin)        print("Creating instructors...")


                    instructors = []

            instructors = []        for i in range(1, 4):

            for i in range(1, 4):            instructor = User(

                instructor = User(                username=f'instructor{i}',

                    username=f'instructor{i}',                email=f'instructor{i}@labsystem.com',

                    email=f'instructor{i}@university.edu',                full_name=f'Instructor {i}',

                    full_name=f'Dr. Instructor {i}',                role='Instructor'

                    role='Instructor',            )

                    is_active=True            instructor.set_password('pass123')

                )            db.session.add(instructor)

                instructor.set_password(f'instructor{i}@123456')            instructors.append(instructor)

                db.session.add(instructor)        

                instructors.append(instructor)        # Create Student Users

                    print("Creating students...")

            students = []        students = []

            for i in range(1, 6):        for i in range(1, 6):

                student = User(            student = User(

                    username=f'student{i}',                username=f'student{i}',

                    email=f'student{i}@university.edu',                email=f'student{i}@labsystem.com',

                    full_name=f'Student {i}',                full_name=f'Student {i}',

                    role='Student',                role='Student'

                    is_active=True            )

                )            student.set_password('pass123')

                student.set_password('password')            db.session.add(student)

                db.session.add(student)            students.append(student)

                students.append(student)        

                    db.session.commit()

            db.session.commit()        

            print(f"✅ Created 1 Admin + {len(instructors)} Instructors + {len(students)} Students\n")        # Create Laboratories

                    print("Creating laboratories...")

            # Create Labs        labs_data = [

            print("🏢 Creating laboratory rooms...")            {

            labs_data = [                'lab_name': 'Computer Lab 1',

                ('Computer Lab A', 'LAB-A', 30, 'Building 1, Room 101', 'Desktop PCs, Projector, Printer'),                'lab_code': 'CL-101',

                ('Computer Lab B', 'LAB-B', 25, 'Building 1, Room 102', 'Desktop PCs, Interactive Board'),                'capacity': 30,

                ('Networking Lab', 'LAB-NET', 20, 'Building 2, Room 201', 'Networking Equipment, Routers'),                'location': 'Building A, Floor 1',

                ('Database Lab', 'LAB-DB', 25, 'Building 2, Room 202', 'Servers, Database Software'),                'equipment': 'Desktop Computers, Projector, Network Switches'

                ('Software Dev Lab', 'LAB-DEV', 30, 'Building 3, Room 301', 'Dev Workstations, IDEs'),            },

                ('Web Lab', 'LAB-WEB', 28, 'Building 3, Room 302', 'Web Servers, Development Tools'),            {

                ('Security Lab', 'LAB-SEC', 20, 'Building 4, Room 401', 'Firewall, IDS/IPS, Isolated Network'),                'lab_name': 'Computer Lab 2',

                ('Mobile Lab', 'LAB-MOB', 25, 'Building 4, Room 402', 'Devices, Development Tools'),                'lab_code': 'CL-102',

            ]                'capacity': 25,

                            'location': 'Building A, Floor 2',

            labs = {}                'equipment': 'Desktop Computers, Interactive Board'

            for lab_name, lab_code, capacity, location, equipment in labs_data:            },

                lab = Laboratory(            {

                    lab_name=lab_name,                'lab_name': 'Network Lab',

                    lab_code=lab_code,                'lab_code': 'NL-201',

                    capacity=capacity,                'capacity': 20,

                    location=location,                'location': 'Building B, Floor 1',

                    equipment=equipment,                'equipment': 'Networking Equipment, Switches, Routers'

                    is_active=True            },

                )            {

                db.session.add(lab)                'lab_name': 'Database Lab',

                labs[lab_code] = lab                'lab_code': 'DL-301',

                            'capacity': 25,

            db.session.commit()                'location': 'Building B, Floor 2',

            print(f"✅ Created {len(labs)} laboratory rooms\n")                'equipment': 'Servers, Database Software, Storage Systems'

                        },

            # Create Courses            {

            print("📚 Creating courses...")                'lab_name': 'Electronics Lab',

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
