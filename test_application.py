#!/usr/bin/env python
"""
Test script for Weather Health Advisor application
"""
import os
import sys
import django
import requests
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_health_app.settings')
django.setup()

from authentication.models import CustomUser
from weather.models import WeatherService
from weather.health_recommendations import HealthRecommendationEngine

def test_user_creation():
    """Test user creation and retrieval"""
    print("Testing User Creation...")
    
    # Check if demo users exist
    roles = ['athlete', 'patient', 'elderly', 'doctor', 'pharmacist', 'public']
    for role in roles:
        username = f"{role}_demo"
        try:
            user = CustomUser.objects.get(username=username)
            print(f"✓ {role.title()} demo user exists: {user.username}")
        except CustomUser.DoesNotExist:
            print(f"✗ {role.title()} demo user not found")
    
    print()

def test_weather_service():
    """Test weather service functionality"""
    print("Testing Weather Service...")
    
    try:
        # Test current weather
        current_weather = WeatherService.get_current_weather("London")
        print(f"✓ Current weather retrieved: {current_weather['temperature']}°C, {current_weather['description']}")
        
        # Test historical weather
        historical_weather = WeatherService.get_historical_weather("London", 7)
        print(f"✓ Historical weather retrieved: {len(historical_weather)} days")
        
        # Test MongoDB save (will fail gracefully if MongoDB not available)
        saved = WeatherService.save_weather_to_mongodb(current_weather)
        if saved:
            print("✓ Weather data saved to MongoDB")
        else:
            print("⚠ MongoDB not available, using demo data")
            
    except Exception as e:
        print(f"✗ Weather service error: {e}")
    
    print()

def test_recommendations():
    """Test health recommendation engine"""
    print("Testing Health Recommendations...")
    
    try:
        # Sample weather data
        weather_data = {
            'temperature': 25,
            'humidity': 70,
            'uv_index': 8,
            'air_quality_index': 3,
            'pollen_count': 4,
            'wind_speed': 10,
            'description': 'sunny'
        }
        
        # Test recommendations for different roles
        roles = ['athlete', 'patient', 'elderly', 'doctor', 'pharmacist', 'public']
        
        for role in roles:
            health_conditions = "asthma, diabetes" if role == 'patient' else ""
            recommendations = HealthRecommendationEngine.get_recommendations(
                weather_data, role, health_conditions
            )
            print(f"✓ {role.title()}: {len(recommendations)} recommendations generated")
            
    except Exception as e:
        print(f"✗ Recommendation engine error: {e}")
    
    print()

def test_web_server():
    """Test if web server is accessible"""
    print("Testing Web Server...")
    
    try:
        response = requests.get('http://127.0.0.1:8000', timeout=5)
        if response.status_code == 200:
            print("✓ Web server is accessible")
            print(f"✓ Response status: {response.status_code}")
        else:
            print(f"⚠ Web server returned status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("✗ Web server is not running")
        print("  Run: python manage.py runserver")
    except Exception as e:
        print(f"✗ Web server test error: {e}")
    
    print()

def test_database():
    """Test database connectivity"""
    print("Testing Database...")
    
    try:
        # Test SQLite database
        user_count = CustomUser.objects.count()
        print(f"✓ SQLite database accessible: {user_count} users")
        
        # Test MongoDB (optional)
        from weather_health_app.mongodb import get_db
        db = get_db()
        if db is not None:
            print("✓ MongoDB connection available")
        else:
            print("⚠ MongoDB not available (using demo data)")
            
    except Exception as e:
        print(f"✗ Database test error: {e}")
    
    print()

def main():
    """Run all tests"""
    print("=" * 60)
    print("WEATHER HEALTH ADVISOR - APPLICATION TEST")
    print("=" * 60)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    test_user_creation()
    test_weather_service()
    test_recommendations()
    test_database()
    test_web_server()
    
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print("✓ = Test passed")
    print("⚠ = Test passed with warnings")
    print("✗ = Test failed")
    print()
    print("If all tests show ✓ or ⚠, the application is working correctly!")
    print()
    print("To access the application:")
    print("1. Make sure the server is running: python manage.py runserver")
    print("2. Open http://127.0.0.1:8000 in your browser")
    print("3. Use demo accounts (username: role_demo, password: demo123)")
    print()

if __name__ == '__main__':
    main()
