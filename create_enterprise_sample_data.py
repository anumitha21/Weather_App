#!/usr/bin/env python
"""
Create sample data for enterprise facilities (alerts, energy usage, etc.)
"""
import os
import sys
import django
from datetime import datetime, timedelta
import random

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_health_app.settings')
django.setup()

from django.contrib.auth import get_user_model
from enterprise.models import Facility, Department, FacilityAlert
from smarthome.models import SmartDevice, EnergyUsage, DeviceAction

User = get_user_model()

def create_facility_alerts():
    """Create sample facility alerts"""
    print("Creating facility alerts...")
    
    facilities = Facility.objects.all()
    alert_count = 0
    
    for facility in facilities:
        departments = facility.departments.all()
        
        # Create various types of alerts
        alert_templates = []
        
        if facility.facility_type == 'hospital':
            alert_templates = [
                {
                    'alert_type': 'environmental',
                    'severity': 'warning',
                    'title': 'ICU Temperature Alert',
                    'message': 'ICU temperature has exceeded optimal range (24°C). Patient comfort may be affected.',
                    'department_type': 'icu'
                },
                {
                    'alert_type': 'equipment',
                    'severity': 'critical',
                    'title': 'Backup Power System Check Required',
                    'message': 'Backup power system requires immediate inspection. Last test failed.',
                    'department_type': None
                },
                {
                    'alert_type': 'safety',
                    'severity': 'warning',
                    'title': 'Air Quality Monitoring',
                    'message': 'Operating room air quality sensors indicate elevated particle count.',
                    'department_type': 'operating_room'
                },
                {
                    'alert_type': 'energy',
                    'severity': 'info',
                    'title': 'Peak Hour Energy Usage',
                    'message': 'Energy consumption 15% above normal during peak hours. Consider load balancing.',
                    'department_type': None
                }
            ]
        
        elif facility.facility_type == 'factory':
            alert_templates = [
                {
                    'alert_type': 'safety',
                    'severity': 'critical',
                    'title': 'Production Line Safety Alert',
                    'message': 'Safety system detected anomaly on Production Floor A. Immediate inspection required.',
                    'department_type': 'production'
                },
                {
                    'alert_type': 'environmental',
                    'severity': 'warning',
                    'title': 'High Humidity in Quality Control',
                    'message': 'Humidity levels (85%) exceed acceptable range for quality control processes.',
                    'department_type': 'quality_control'
                },
                {
                    'alert_type': 'energy',
                    'severity': 'warning',
                    'title': 'Demand Response Event',
                    'message': 'Utility demand response event active. Reduce non-essential loads by 20%.',
                    'department_type': None
                },
                {
                    'alert_type': 'equipment',
                    'severity': 'info',
                    'title': 'Conveyor System Maintenance Due',
                    'message': 'Scheduled maintenance for conveyor system due within 48 hours.',
                    'department_type': 'assembly'
                }
            ]
        
        else:  # office
            alert_templates = [
                {
                    'alert_type': 'environmental',
                    'severity': 'warning',
                    'title': 'Server Room Temperature Alert',
                    'message': 'Server room temperature approaching critical threshold (26°C).',
                    'department_type': 'server_room'
                },
                {
                    'alert_type': 'energy',
                    'severity': 'info',
                    'title': 'HVAC Optimization Opportunity',
                    'message': 'HVAC system running at 85% capacity. Consider schedule optimization.',
                    'department_type': None
                },
                {
                    'alert_type': 'equipment',
                    'severity': 'warning',
                    'title': 'UPS Battery Check Required',
                    'message': 'UPS system battery capacity below 80%. Schedule replacement.',
                    'department_type': 'server_room'
                }
            ]
        
        # Create alerts
        for template in alert_templates:
            # Find appropriate department
            department = None
            if template['department_type']:
                department = departments.filter(department_type=template['department_type']).first()
            
            # Create alert with random timing
            created_time = datetime.now() - timedelta(
                hours=random.randint(1, 72),
                minutes=random.randint(0, 59)
            )
            
            alert = FacilityAlert.objects.create(
                facility=facility,
                department=department,
                alert_type=template['alert_type'],
                severity=template['severity'],
                title=template['title'],
                message=template['message'],
                source_system=f"{facility.facility_type.title()} Management System",
                created_at=created_time
            )
            
            # Randomly acknowledge or resolve some alerts
            if random.random() < 0.3:  # 30% chance of being acknowledged
                alert.acknowledge(facility.facility_manager)
                
                if random.random() < 0.5:  # 50% chance of being resolved if acknowledged
                    actions = [
                        "Maintenance team dispatched and issue resolved.",
                        "System parameters adjusted to normal range.",
                        "Equipment inspection completed, no issues found.",
                        "Preventive measures implemented to prevent recurrence.",
                        "Temporary workaround applied, permanent fix scheduled."
                    ]
                    alert.resolve(facility.facility_manager, random.choice(actions))
            
            alert_count += 1
    
    print(f"Created {alert_count} facility alerts")

def create_energy_usage_data():
    """Create sample energy usage data"""
    print("Creating energy usage data...")
    
    devices = SmartDevice.objects.filter(facility__isnull=False)
    usage_count = 0
    
    # Create data for last 30 days
    for days_back in range(30):
        date = datetime.now().date() - timedelta(days=days_back)
        
        for device in devices:
            # Create hourly data for each device
            for hour in range(24):
                # Determine if it's peak hour (2 PM - 6 PM)
                is_peak = 14 <= hour <= 18
                
                # Base energy consumption based on device type
                base_consumption = {
                    'medical_hvac': random.uniform(15, 25),
                    'or_climate': random.uniform(8, 12),
                    'industrial_hvac': random.uniform(25, 40),
                    'production_line': random.uniform(50, 80),
                    'bms': random.uniform(10, 15),
                    'server_cooling': random.uniform(5, 8),
                }.get(device.device_type, random.uniform(2, 8))
                
                # Add variations based on time and conditions
                if device.facility.facility_type == 'hospital':
                    # Hospitals operate 24/7 with less variation
                    energy_consumed = base_consumption * random.uniform(0.8, 1.2)
                elif device.facility.facility_type == 'factory':
                    # Factories have higher usage during work hours
                    if 6 <= hour <= 22:  # Work hours
                        energy_consumed = base_consumption * random.uniform(0.9, 1.3)
                    else:
                        energy_consumed = base_consumption * random.uniform(0.3, 0.6)
                else:  # office
                    # Offices have usage mainly during business hours
                    if 8 <= hour <= 18:  # Business hours
                        energy_consumed = base_consumption * random.uniform(0.8, 1.2)
                    else:
                        energy_consumed = base_consumption * random.uniform(0.2, 0.4)
                
                # Calculate cost based on tariff
                if is_peak:
                    rate = 9.5  # Peak rate
                else:
                    rate = 5.5  # Off-peak rate
                
                cost = energy_consumed * rate
                
                # Determine if automation was triggered
                automation_triggered = random.random() < 0.4  # 40% automation
                
                # Create energy usage record
                EnergyUsage.objects.create(
                    user=device.user,
                    device=device,
                    facility=device.facility,
                    department=device.department,
                    date=date,
                    hour=hour,
                    energy_consumed=round(energy_consumed, 2),
                    cost=round(cost, 2),
                    weather_temperature=random.randint(20, 35),
                    weather_humidity=random.randint(40, 80),
                    is_peak_hour=is_peak,
                    automation_triggered=automation_triggered,
                    tariff_rate=rate,
                    power_factor=random.uniform(0.85, 0.98),
                    carbon_footprint=round(energy_consumed * 0.82, 2),  # 0.82 kg CO2/kWh
                    renewable_percentage=random.randint(10, 30)
                )
                
                usage_count += 1
    
    print(f"Created {usage_count} energy usage records")

def create_device_actions():
    """Create sample device action history"""
    print("Creating device actions...")
    
    devices = SmartDevice.objects.filter(facility__isnull=False)
    action_count = 0
    
    # Create actions for last 7 days
    for days_back in range(7):
        date = datetime.now() - timedelta(days=days_back)
        
        for device in devices:
            # Random number of actions per device per day
            num_actions = random.randint(2, 8)
            
            for _ in range(num_actions):
                action_time = date + timedelta(
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )
                
                actions = ['turn_on', 'turn_off', 'set_temperature', 'set_mode', 'maintenance_mode']
                action_type = random.choice(actions)
                
                source = random.choice(['manual', 'automation', 'schedule'])
                
                DeviceAction.objects.create(
                    device=device,
                    action_type=action_type,
                    action_value={'temperature': 22, 'mode': 'auto'} if action_type == 'set_temperature' else {},
                    action_source=source,
                    triggered_by_rule=None,  # Would link to automation rule in real implementation
                    timestamp=action_time,
                    success=random.random() < 0.95  # 95% success rate
                )
                
                action_count += 1
    
    print(f"Created {action_count} device actions")

def main():
    """Main function to create all sample data"""
    print("Creating enterprise sample data...")
    
    # Create facility alerts
    create_facility_alerts()
    
    # Create energy usage data
    create_energy_usage_data()
    
    # Create device actions
    create_device_actions()
    
    print("\n✅ Enterprise sample data creation completed!")
    print(f"Summary:")
    print(f"  - {FacilityAlert.objects.count()} facility alerts")
    print(f"  - {EnergyUsage.objects.filter(facility__isnull=False).count()} energy usage records")
    print(f"  - {DeviceAction.objects.filter(device__facility__isnull=False).count()} device actions")

if __name__ == '__main__':
    main()
