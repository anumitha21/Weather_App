#!/usr/bin/env python
"""
Script to create demo users for the Weather Health Advisor application
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_health_app.settings')
django.setup()

from authentication.models import CustomUser

def create_demo_users():
    """Create demo users for testing"""
    
    # Demo users data
    demo_users = [
        {
            'username': 'athlete_demo',
            'email': 'athlete@demo.com',
            'first_name': 'Alex',
            'last_name': 'Runner',
            'password': 'demo123',
            'role': 'athlete',
            'age': 28,
            'location': 'London',
            'health_conditions': 'None'
        },
        {
            'username': 'patient_demo',
            'email': 'patient@demo.com',
            'first_name': 'Sarah',
            'last_name': 'Johnson',
            'password': 'demo123',
            'role': 'patient',
            'age': 45,
            'location': 'Manchester',
            'health_conditions': 'asthma, diabetes'
        },
        {
            'username': 'elderly_demo',
            'email': 'elderly@demo.com',
            'first_name': 'Robert',
            'last_name': 'Smith',
            'password': 'demo123',
            'role': 'elderly',
            'age': 72,
            'location': 'Birmingham',
            'health_conditions': 'arthritis, high blood pressure'
        },
        {
            'username': 'doctor_demo',
            'email': 'doctor@demo.com',
            'first_name': 'Dr. Emily',
            'last_name': 'Wilson',
            'password': 'demo123',
            'role': 'doctor',
            'age': 38,
            'location': 'Edinburgh',
            'health_conditions': 'None'
        },
        {
            'username': 'pharmacist_demo',
            'email': 'pharmacist@demo.com',
            'first_name': 'Michael',
            'last_name': 'Brown',
            'password': 'demo123',
            'role': 'pharmacist',
            'age': 35,
            'location': 'Glasgow',
            'health_conditions': 'None'
        },
        {
            'username': 'public_demo',
            'email': 'public@demo.com',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'password': 'demo123',
            'role': 'public',
            'age': 30,
            'location': 'Liverpool',
            'health_conditions': 'None'
        }
    ]
    
    print("Creating demo users...")
    
    for user_data in demo_users:
        username = user_data['username']
        
        # Check if user already exists
        if CustomUser.objects.filter(username=username).exists():
            print(f"User {username} already exists, skipping...")
            continue
        
        # Create user
        user = CustomUser.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            password=user_data['password'],
            role=user_data['role'],
            age=user_data['age'],
            location=user_data['location'],
            health_conditions=user_data['health_conditions']
        )
        
        print(f"Created user: {username} ({user_data['role']})")
    
    print("\nDemo users created successfully!")
    print("\nLogin credentials:")
    print("=" * 50)
    for user_data in demo_users:
        print(f"Username: {user_data['username']}")
        print(f"Password: {user_data['password']}")
        print(f"Role: {user_data['role'].title()}")
        print("-" * 30)

if __name__ == '__main__':
    create_demo_users()
