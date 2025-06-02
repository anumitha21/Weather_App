#!/usr/bin/env python
"""
Create sample advice templates for different user roles
"""
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_health_app.settings')
django.setup()

from advice.models import AdviceTemplate

def create_athlete_templates():
    """Create advice templates for athletes"""
    templates = [
        {
            'role': 'athlete',
            'category': 'activity',
            'title_template': 'Optimal Training Time - {temperature}°C',
            'content_template': 'Perfect conditions for outdoor training! Temperature is {temperature}°C with {humidity}% humidity. Recommended training duration: 45-60 minutes. Stay hydrated with 250ml water every 15 minutes.',
            'min_temperature': 20,
            'max_temperature': 30,
            'max_humidity': 70,
            'max_air_quality': 3,
            'priority': 'medium',
            'icon': 'fas fa-running'
        },
        {
            'role': 'athlete',
            'category': 'health',
            'title_template': 'DANGER: Extreme Heat Alert - {temperature}°C',
            'content_template': 'Temperature {temperature}°C is dangerous for outdoor exercise. Move training indoors or postpone until evening. If you must exercise outdoors, limit to 15-20 minutes with frequent breaks.',
            'min_temperature': 35,
            'priority': 'critical',
            'icon': 'fas fa-thermometer-full'
        },
        {
            'role': 'athlete',
            'category': 'health',
            'title_template': 'Air Quality Warning - Training Modifications Required',
            'content_template': 'Air quality index {air_quality}/5 requires training modifications. Reduce intensity by 20%, avoid high-intensity intervals, and consider wearing a sports mask.',
            'min_air_quality': 3,
            'max_air_quality': 4,
            'priority': 'high',
            'icon': 'fas fa-mask'
        },
        {
            'role': 'athlete',
            'category': 'health',
            'title_template': 'Enhanced Hydration Protocol Required',
            'content_template': 'Hot and humid conditions (T:{temperature}°C, H:{humidity}%) require enhanced hydration. Drink 500ml before exercise, 250ml every 15 minutes during, and 500ml after. Consider electrolyte supplements.',
            'min_temperature': 28,
            'min_humidity': 70,
            'priority': 'high',
            'icon': 'fas fa-tint'
        }
    ]
    
    for template_data in templates:
        AdviceTemplate.objects.get_or_create(
            role=template_data['role'],
            category=template_data['category'],
            title_template=template_data['title_template'],
            defaults=template_data
        )

def create_patient_templates():
    """Create advice templates for patients"""
    templates = [
        {
            'role': 'patient',
            'category': 'health',
            'title_template': 'CRITICAL: Respiratory Alert - AQI {air_quality}',
            'content_template': 'Air quality {air_quality}/5 is dangerous for respiratory conditions. Stay indoors, keep rescue inhaler ready, use air purifiers. Seek medical help if breathing difficulty occurs.',
            'min_air_quality': 4,
            'priority': 'critical',
            'icon': 'fas fa-lungs'
        },
        {
            'role': 'patient',
            'category': 'health',
            'title_template': 'Cardiac Heat Alert - {temperature}°C',
            'content_template': 'Temperature {temperature}°C dangerous for heart conditions. Stay in AC, take medications on time, monitor blood pressure twice daily. Avoid outdoor activities.',
            'min_temperature': 35,
            'priority': 'critical',
            'icon': 'fas fa-heartbeat'
        },
        {
            'role': 'patient',
            'category': 'health',
            'title_template': 'Diabetes Heat Management Required',
            'content_template': 'Extreme heat affects blood sugar control. Check glucose more frequently (before meals + 2 hours after). Store insulin properly (cool, not frozen). Stay hydrated.',
            'min_temperature': 35,
            'priority': 'high',
            'icon': 'fas fa-syringe'
        },
        {
            'role': 'patient',
            'category': 'health',
            'title_template': 'Joint Pain Management - High Humidity',
            'content_template': 'High humidity {humidity}% may increase joint pain. Apply heat therapy before activities. Take anti-inflammatory as needed. Do gentle stretching exercises.',
            'min_humidity': 80,
            'priority': 'medium',
            'icon': 'fas fa-bone'
        }
    ]
    
    for template_data in templates:
        AdviceTemplate.objects.get_or_create(
            role=template_data['role'],
            category=template_data['category'],
            title_template=template_data['title_template'],
            defaults=template_data
        )

def create_elderly_templates():
    """Create advice templates for elderly users"""
    templates = [
        {
            'role': 'elderly',
            'category': 'health',
            'title_template': 'Elderly Heat Safety Alert - {temperature}°C',
            'content_template': 'Temperature {temperature}°C is dangerous for elderly. Stay indoors with AC/fan. Drink water every hour. Wear light, loose clothing. Have emergency contacts ready.',
            'min_temperature': 35,
            'priority': 'critical',
            'icon': 'fas fa-user-shield'
        },
        {
            'role': 'elderly',
            'category': 'activity',
            'title_template': 'Safe Indoor Activities Recommended',
            'content_template': 'Weather conditions not suitable for outdoor activities. Try: gentle yoga, indoor walking, reading, puzzles, or video calls with family. Stay mentally and physically active indoors.',
            'min_temperature': 30,
            'priority': 'medium',
            'icon': 'fas fa-home'
        },
        {
            'role': 'elderly',
            'category': 'health',
            'title_template': 'Air Quality Safety for Elderly',
            'content_template': 'Poor air quality (AQI {air_quality}/5) dangerous for elderly. Stay indoors, use air purifiers, wear N95 mask if must go out. Monitor for breathing difficulty.',
            'min_air_quality': 4,
            'priority': 'critical',
            'icon': 'fas fa-mask'
        }
    ]
    
    for template_data in templates:
        AdviceTemplate.objects.get_or_create(
            role=template_data['role'],
            category=template_data['category'],
            title_template=template_data['title_template'],
            defaults=template_data
        )

def create_facility_manager_templates():
    """Create advice templates for facility managers"""
    templates = [
        {
            'role': 'facility_manager',
            'category': 'facility',
            'title_template': 'Facility Heat Management Protocol - {temperature}°C',
            'content_template': 'Extreme heat {temperature}°C detected. Activate cooling protocols: Increase HVAC capacity, check backup power systems, monitor critical equipment temperatures, ensure staff hydration stations.',
            'min_temperature': 35,
            'priority': 'high',
            'icon': 'fas fa-building'
        },
        {
            'role': 'facility_manager',
            'category': 'facility',
            'title_template': 'Air Quality Emergency Protocol',
            'content_template': 'Hazardous air quality (AQI {air_quality}/5). Activate air filtration systems, seal building, limit outdoor activities, provide masks to staff, monitor vulnerable occupants.',
            'min_air_quality': 4,
            'priority': 'critical',
            'icon': 'fas fa-wind'
        },
        {
            'role': 'facility_manager',
            'category': 'energy',
            'title_template': 'Peak Hour Energy Management',
            'content_template': 'Peak hours (2-6 PM) approaching. Implement load shedding: reduce non-essential lighting, optimize HVAC settings, defer heavy equipment usage. Potential savings: 20-30%.',
            'time_of_day': ['afternoon'],
            'priority': 'medium',
            'icon': 'fas fa-bolt',
            'estimated_savings': '₹500-1000/day'
        }
    ]
    
    for template_data in templates:
        AdviceTemplate.objects.get_or_create(
            role=template_data['role'],
            category=template_data['category'],
            title_template=template_data['title_template'],
            defaults=template_data
        )

def create_energy_manager_templates():
    """Create advice templates for energy managers"""
    templates = [
        {
            'role': 'energy_manager',
            'category': 'energy',
            'title_template': 'Demand Response Event Active',
            'content_template': 'Utility demand response event in effect. Reduce facility load by 20%. Priority actions: Adjust HVAC setpoints, reduce lighting, defer non-critical equipment.',
            'priority': 'high',
            'icon': 'fas fa-chart-line',
            'estimated_savings': '₹2000-5000'
        },
        {
            'role': 'energy_manager',
            'category': 'energy',
            'title_template': 'Optimal Natural Ventilation Window',
            'content_template': 'Perfect weather {temperature}°C for natural ventilation! Reduce HVAC load by opening windows and using fans. Estimated savings: ₹1000-3000 today.',
            'min_temperature': 22,
            'max_temperature': 28,
            'priority': 'medium',
            'icon': 'fas fa-wind',
            'estimated_savings': '₹1000-3000/day'
        }
    ]
    
    for template_data in templates:
        AdviceTemplate.objects.get_or_create(
            role=template_data['role'],
            category=template_data['category'],
            title_template=template_data['title_template'],
            defaults=template_data
        )

def create_general_templates():
    """Create advice templates for general public"""
    templates = [
        {
            'role': 'public',
            'category': 'health',
            'title_template': 'Heat Wave Precautions - {temperature}°C',
            'content_template': 'Temperature {temperature}°C requires precautions. Stay hydrated, avoid midday sun, wear light colors, use AC/fans, check on elderly neighbors.',
            'min_temperature': 35,
            'priority': 'medium',
            'icon': 'fas fa-thermometer-three-quarters'
        },
        {
            'role': 'public',
            'category': 'activity',
            'title_template': 'Perfect Weather for Outdoor Activities',
            'content_template': 'Excellent weather conditions! Temperature {temperature}°C with good air quality. Great time for outdoor activities, walking, or sports. Remember sun protection.',
            'min_temperature': 20,
            'max_temperature': 28,
            'max_air_quality': 2,
            'priority': 'low',
            'icon': 'fas fa-sun'
        }
    ]
    
    for template_data in templates:
        AdviceTemplate.objects.get_or_create(
            role=template_data['role'],
            category=template_data['category'],
            title_template=template_data['title_template'],
            defaults=template_data
        )

def main():
    """Create all advice templates"""
    print("Creating advice templates...")
    
    create_athlete_templates()
    print("✅ Created athlete templates")
    
    create_patient_templates()
    print("✅ Created patient templates")
    
    create_elderly_templates()
    print("✅ Created elderly templates")
    
    create_facility_manager_templates()
    print("✅ Created facility manager templates")
    
    create_energy_manager_templates()
    print("✅ Created energy manager templates")
    
    create_general_templates()
    print("✅ Created general public templates")
    
    total_templates = AdviceTemplate.objects.count()
    print(f"\n🎉 Successfully created {total_templates} advice templates!")

if __name__ == '__main__':
    main()
