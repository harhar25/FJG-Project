#!/usr/bin/env python
from app import create_app
from app.models import User

app = create_app()

# Test the student route
with app.test_client() as client:
    # Login first with correct email
    login_response = client.post('/auth/login', data={
        'email': 'student1@labsystem.com',
        'password': 'password123'
    })
    
    print(f'Login response status: {login_response.status_code}')
    print(f'Login Location: {login_response.location}')
    
    # Now try to access schedule by lab (should be authenticated)
    response = client.get('/student/schedule/by-lab')
    print(f'\nSchedule by lab response status: {response.status_code}')
    
    # Check if labs are in the response
    if b'Computer Lab 1' in response.data:
        print('✓ Labs are rendered in response')
    else:
        print('✗ Labs NOT found in response')
            
    # Check if select element exists
    if b'labFilter' in response.data:
        print('✓ labFilter select element found')
    else:
        print('✗ labFilter select element NOT found')
        
    # Check if filterSchedule function is in response
    if b'function filterSchedule' in response.data:
        print('✓ filterSchedule function found')
    else:
        print('✗ filterSchedule function NOT found')


