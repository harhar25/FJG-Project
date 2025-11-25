"""
Database seeder script for initial data population
"""
import os
from datetime import datetime, timedelta
from app import create_app, db
from app.models import User, Laboratory, Course, LabSchedule

def seed_database():
    """Seed the database with sample data"""
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create Admin User
        print("Creating admin user...")
        admin = User(
            username='admin',
            email='admin@labsystem.com',
            full_name='System Administrator',
            role='Administrator'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Create Instructor Users
        print("Creating instructors...")
        instructors = []
        for i in range(1, 4):
            instructor = User(
                username=f'instructor{i}',
                email=f'instructor{i}@labsystem.com',
                full_name=f'Instructor {i}',
                role='Instructor'
            )
            instructor.set_password('pass123')
            db.session.add(instructor)
            instructors.append(instructor)
        
        # Create Student Users
        print("Creating students...")
        students = []
        for i in range(1, 6):
            student = User(
                username=f'student{i}',
                email=f'student{i}@labsystem.com',
                full_name=f'Student {i}',
                role='Student'
            )
            student.set_password('pass123')
            db.session.add(student)
            students.append(student)
        
        db.session.commit()
        
        # Create Laboratories
        print("Creating laboratories...")
        labs_data = [
            {
                'lab_name': 'Computer Lab 1',
                'lab_code': 'CL-101',
                'capacity': 30,
                'location': 'Building A, Floor 1',
                'equipment': 'Desktop Computers, Projector, Network Switches'
            },
            {
                'lab_name': 'Computer Lab 2',
                'lab_code': 'CL-102',
                'capacity': 25,
                'location': 'Building A, Floor 2',
                'equipment': 'Desktop Computers, Interactive Board'
            },
            {
                'lab_name': 'Network Lab',
                'lab_code': 'NL-201',
                'capacity': 20,
                'location': 'Building B, Floor 1',
                'equipment': 'Networking Equipment, Switches, Routers'
            },
            {
                'lab_name': 'Database Lab',
                'lab_code': 'DL-301',
                'capacity': 25,
                'location': 'Building B, Floor 2',
                'equipment': 'Servers, Database Software, Storage Systems'
            },
            {
                'lab_name': 'Electronics Lab',
                'lab_code': 'EL-401',
                'capacity': 20,
                'location': 'Building C, Floor 1',
                'equipment': 'Oscilloscopes, Multimeters, Power Supplies'
            },
        ]
        
        labs = []
        for lab_data in labs_data:
            lab = Laboratory(**lab_data)
            db.session.add(lab)
            labs.append(lab)
        
        db.session.commit()
        
        # Create Courses
        print("Creating courses...")
        courses_data = [
            {
                'course_code': 'CS101',
                'course_name': 'Introduction to Computer Science',
                'credit_hours': 3,
                'section': 'A1',
                'instructor_id': instructors[0].id
            },
            {
                'course_code': 'CS201',
                'course_name': 'Data Structures',
                'credit_hours': 4,
                'section': 'B1',
                'instructor_id': instructors[1].id
            },
            {
                'course_code': 'CS301',
                'course_name': 'Database Systems',
                'credit_hours': 4,
                'section': 'C1',
                'instructor_id': instructors[2].id
            },
            {
                'course_code': 'CS102',
                'course_name': 'Introduction to Computer Science',
                'credit_hours': 3,
                'section': 'A2',
                'instructor_id': instructors[0].id
            },
            {
                'course_code': 'CS202',
                'course_name': 'Network Administration',
                'credit_hours': 3,
                'section': 'B2',
                'instructor_id': instructors[1].id
            },
        ]
        
        courses = []
        for course_data in courses_data:
            course = Course(**course_data)
            db.session.add(course)
            courses.append(course)
        
        db.session.commit()
        
        # Create Lab Schedules
        print("Creating lab schedules...")
        today = datetime.utcnow().date()
        
        schedule_times = [
            ('08:00', '10:00'),
            ('10:00', '12:00'),
            ('13:00', '15:00'),
            ('15:00', '17:00'),
        ]
        
        schedule_count = 0
        for offset in range(7):  # Create schedules for next 7 days
            current_date = today + timedelta(days=offset)
            
            # Skip weekends
            if current_date.weekday() >= 5:
                continue
            
            for lab in labs:
                for course in courses[:3]:
                    for start_time, end_time in schedule_times:
                        schedule = LabSchedule(
                            lab_id=lab.id,
                            course_id=course.id,
                            scheduled_date=current_date,
                            start_time=datetime.strptime(start_time, '%H:%M').time(),
                            end_time=datetime.strptime(end_time, '%H:%M').time(),
                            status='Reserved' if (offset % 2 == 0) else 'Available',
                            created_by=admin.id
                        )
                        db.session.add(schedule)
                        schedule_count += 1
        
        db.session.commit()
        
        print("\n✅ Database seeding completed successfully!")
        print(f"   - Created {len(instructors)} instructors")
        print(f"   - Created {len(students)} students")
        print(f"   - Created {len(labs)} laboratories")
        print(f"   - Created {len(courses)} courses")
        print(f"   - Created {schedule_count} lab schedules")
        print("\n📝 Demo Credentials:")
        print("   - Admin: admin / admin123")
        print("   - Instructor: instructor1 / pass123")
        print("   - Student: student1 / pass123")

if __name__ == '__main__':
    seed_database()
