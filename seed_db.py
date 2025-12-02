#!/usr/bin/env python3
"""IT Lab System - Database Seeding Script"""
from datetime import datetime, timedelta, time
from app import create_app, db
from app.models import User, Laboratory, Course, LabSchedule, ReservationRequest, Notification, LabUsageReport

def seed_database():
    """Seed database with test data"""
    app = create_app()
    with app.app_context():
        print("\n=== SEEDING DATABASE ===\n")
        try:
            # Clear existing data
            db.drop_all()
            db.create_all()
            
            # Create Admin
            admin = User(username='admin', email='admin@lab.com', full_name='Admin User', role='Administrator')
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Create Instructors
            instructors = []
            for i in range(1, 4):
                instr = User(
                    username=f'instructor{i}',
                    email=f'instructor{i}@lab.com',
                    full_name=f'Instructor {i}',
                    role='Instructor'
                )
                instr.set_password('pass123')
                db.session.add(instr)
                instructors.append(instr)
            
            db.session.commit()
            print(f" Created 1 admin, {len(instructors)} instructors")
            
            # Create Laboratories
            labs = [
                Laboratory(lab_name='Computer Lab 1', lab_code='CL-101', capacity=30, location='Building A, Room 101', equipment='30x PCs'),
                Laboratory(lab_name='Computer Lab 2', lab_code='CL-102', capacity=25, location='Building A, Room 102', equipment='25x PCs'),
                Laboratory(lab_name='Network Lab', lab_code='NL-201', capacity=20, location='Building B, Room 201', equipment='Network Equipment'),
                Laboratory(lab_name='Database Lab', lab_code='DL-301', capacity=25, location='Building B, Room 301', equipment='Servers'),
                Laboratory(lab_name='Electronics Lab', lab_code='EL-401', capacity=20, location='Building C, Room 401', equipment='Electronic Equipment'),
                Laboratory(lab_name='Web Development Lab', lab_code='WDL-402', capacity=28, location='Building C, Room 402', equipment='Web Servers'),
                Laboratory(lab_name='Cybersecurity Lab', lab_code='SL-501', capacity=20, location='Building D, Room 501', equipment='Firewall, IDS'),
                Laboratory(lab_name='Mobile Development Lab', lab_code='MDL-502', capacity=25, location='Building D, Room 502', equipment='Devices'),
            ]
            db.session.add_all(labs)
            db.session.commit()
            print(f" Created {len(labs)} laboratories")
            
            # Create Courses
            courses = [
                Course(course_code='CS101', course_name='Introduction to Computer Science', credit_hours=3, section='A', instructor_id=instructors[0].id),
                Course(course_code='CS201', course_name='Data Structures', credit_hours=4, section='A', instructor_id=instructors[0].id),
                Course(course_code='NET301', course_name='Computer Networks', credit_hours=3, section='A', instructor_id=instructors[1].id),
                Course(course_code='DB301', course_name='Database Management Systems', credit_hours=3, section='A', instructor_id=instructors[2].id),
                Course(course_code='WEB201', course_name='Web Development', credit_hours=3, section='A', instructor_id=instructors[0].id),
                Course(course_code='SEC401', course_name='Cybersecurity Fundamentals', credit_hours=3, section='A', instructor_id=instructors[1].id),
                Course(course_code='MOB301', course_name='Mobile Application Development', credit_hours=3, section='A', instructor_id=instructors[2].id),
                Course(course_code='ADV401', course_name='Advanced Programming', credit_hours=4, section='A', instructor_id=instructors[0].id),
                Course(course_code='DEV301', course_name='Software Development', credit_hours=3, section='A', instructor_id=instructors[1].id),
                Course(course_code='ELE201', course_name='Electronics and Circuits', credit_hours=3, section='A', instructor_id=instructors[2].id),
            ]
            db.session.add_all(courses)
            db.session.commit()
            print(f" Created {len(courses)} courses")
            
            print("\n=== DATABASE SEEDING COMPLETE ===")
            print("\nTest Credentials:")
            print("  Admin:       admin / admin123")
            print("  Instructors: instructor1-3 / pass123")
            print()
            
        except Exception as e:
            print(f"ERROR: {e}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    seed_database()
