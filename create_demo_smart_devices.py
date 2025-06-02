#!/usr/bin/env python
"""
Script to create demo smart devices and automation rules
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_health_app.settings')
django.setup()

from authentication.models import CustomUser
from smarthome.models import SmartDevice, AutomationRule
from smarthome.services import SmartHomeService
from locations.models import UserLocation

def create_demo_smart_devices():
    """Create demo smart devices for testing"""
    
    # Get demo users
    demo_users = CustomUser.objects.filter(username__endswith='_demo')
    
    if not demo_users.exists():
        print("No demo users found. Please run create_demo_users.py first.")
        return
    
    print("Creating demo smart devices and automation rules...")
    
    for user in demo_users:
        print(f"\nCreating devices for {user.username} ({user.get_role_display()})...")
        
        # Create demo devices based on user role
        if user.role == 'athlete':
            devices_data = [
                {
                    'name': 'Gym AC',
                    'device_type': 'ac',
                    'location': 'Home Gym',
                    'brand': 'Samsung',
                    'model': 'WindFree Elite',
                    'capabilities': {'temperature_range': [16, 30], 'modes': ['cool', 'heat', 'auto']},
                    'max_power_consumption': 2000
                },
                {
                    'name': 'Smart Fan',
                    'device_type': 'fan',
                    'location': 'Bedroom',
                    'brand': 'Dyson',
                    'model': 'Pure Cool',
                    'capabilities': {'speed_levels': 10, 'oscillation': True},
                    'max_power_consumption': 75
                },
                {
                    'name': 'UV Protection Curtains',
                    'device_type': 'curtains',
                    'location': 'Living Room',
                    'brand': 'Somfy',
                    'model': 'Motorized Blinds',
                    'capabilities': {'position_control': True, 'timer': True},
                    'max_power_consumption': 50
                }
            ]
        elif user.role == 'patient':
            devices_data = [
                {
                    'name': 'Air Purifier',
                    'device_type': 'air_purifier',
                    'location': 'Bedroom',
                    'brand': 'Philips',
                    'model': 'Series 3000i',
                    'capabilities': {'auto_mode': True, 'allergen_filter': True},
                    'max_power_consumption': 50
                },
                {
                    'name': 'Smart Humidifier',
                    'device_type': 'humidifier',
                    'location': 'Living Room',
                    'brand': 'Levoit',
                    'model': 'LV600HH',
                    'capabilities': {'humidity_control': True, 'essential_oils': True},
                    'max_power_consumption': 300
                },
                {
                    'name': 'Climate Control',
                    'device_type': 'thermostat',
                    'location': 'Main',
                    'brand': 'Nest',
                    'model': 'Learning Thermostat',
                    'capabilities': {'learning': True, 'remote_control': True},
                    'max_power_consumption': 5
                }
            ]
        elif user.role == 'elderly':
            devices_data = [
                {
                    'name': 'Main Thermostat',
                    'device_type': 'thermostat',
                    'location': 'Living Room',
                    'brand': 'Honeywell',
                    'model': 'T9 Smart',
                    'capabilities': {'simple_controls': True, 'voice_control': True},
                    'max_power_consumption': 5
                },
                {
                    'name': 'Bedroom Heater',
                    'device_type': 'heater',
                    'location': 'Bedroom',
                    'brand': 'Dyson',
                    'model': 'Hot+Cool',
                    'capabilities': {'safety_shutoff': True, 'timer': True},
                    'max_power_consumption': 1500
                },
                {
                    'name': 'Security System',
                    'device_type': 'security_system',
                    'location': 'Main',
                    'brand': 'Ring',
                    'model': 'Alarm Pro',
                    'capabilities': {'motion_detection': True, 'emergency_alerts': True},
                    'max_power_consumption': 20
                }
            ]
        else:  # doctor, pharmacist, public
            devices_data = [
                {
                    'name': 'Smart AC',
                    'device_type': 'ac',
                    'location': 'Office',
                    'brand': 'LG',
                    'model': 'Dual Inverter',
                    'capabilities': {'energy_saving': True, 'wifi_control': True},
                    'max_power_consumption': 1800
                },
                {
                    'name': 'Smart Lights',
                    'device_type': 'lights',
                    'location': 'Office',
                    'brand': 'Philips Hue',
                    'model': 'White and Color',
                    'capabilities': {'dimming': True, 'color_changing': True},
                    'max_power_consumption': 60
                },
                {
                    'name': 'Window Blinds',
                    'device_type': 'curtains',
                    'location': 'Office',
                    'brand': 'IKEA',
                    'model': 'FYRTUR',
                    'capabilities': {'wireless_control': True, 'battery_powered': True},
                    'max_power_consumption': 30
                }
            ]
        
        # Create devices
        created_devices = []
        for device_data in devices_data:
            device = SmartDevice.objects.create(
                user=user,
                **device_data
            )
            # Initialize device
            SmartHomeService.initialize_device(device)
            created_devices.append(device)
            print(f"  Created: {device.name} ({device.get_device_type_display()})")
        
        # Create automation rules
        automation_rules = [
            {
                'name': 'Hot Weather AC Control',
                'description': 'Automatically turn on AC when temperature exceeds 28°C',
                'trigger_type': 'temperature',
                'trigger_value': 28,
                'condition_operator': 'gt',
                'action_type': 'set_temperature',
                'action_value': {'temperature': 24, 'mode': 'cool'},
                'target_device_types': ['ac', 'thermostat']
            },
            {
                'name': 'High UV Curtain Control',
                'description': 'Close curtains when UV index is high',
                'trigger_type': 'uv_index',
                'trigger_value': 7,
                'condition_operator': 'gte',
                'action_type': 'close',
                'action_value': {'position': 0},
                'target_device_types': ['curtains']
            },
            {
                'name': 'Energy Peak Hour Optimization',
                'description': 'Optimize energy usage during peak hours',
                'trigger_type': 'energy_peak',
                'trigger_value': 1,
                'condition_operator': 'eq',
                'action_type': 'set_mode',
                'action_value': {'mode': 'eco'},
                'target_device_types': ['ac', 'heater', 'lights']
            }
        ]
        
        for rule_data in automation_rules:
            target_device_types = rule_data.pop('target_device_types')
            
            rule = AutomationRule.objects.create(
                user=user,
                **rule_data
            )
            
            # Add target devices
            target_devices = [d for d in created_devices if d.device_type in target_device_types]
            rule.target_devices.set(target_devices)
            
            print(f"  Created rule: {rule.name}")
        
        # Create a demo location for the user
        if not UserLocation.objects.filter(user=user).exists():
            demo_locations = [
                {'name': 'London, UK', 'city': 'London', 'country': 'GB', 'lat': 51.5074, 'lon': -0.1278},
                {'name': 'New York, US', 'city': 'New York', 'country': 'US', 'lat': 40.7128, 'lon': -74.0060},
                {'name': 'Tokyo, JP', 'city': 'Tokyo', 'country': 'JP', 'lat': 35.6762, 'lon': 139.6503},
                {'name': 'Sydney, AU', 'city': 'Sydney', 'country': 'AU', 'lat': -33.8688, 'lon': 151.2093},
            ]
            
            import random
            location_data = random.choice(demo_locations)
            
            UserLocation.objects.create(
                user=user,
                name=location_data['name'],
                city=location_data['city'],
                country=location_data['country'],
                latitude=location_data['lat'],
                longitude=location_data['lon'],
                is_primary=True
            )
            print(f"  Created location: {location_data['name']}")
    
    print("\nDemo smart devices and automation rules created successfully!")
    print("\nSummary:")
    print(f"Total devices: {SmartDevice.objects.count()}")
    print(f"Total automation rules: {AutomationRule.objects.count()}")
    print(f"Total locations: {UserLocation.objects.count()}")
    
    print("\nYou can now:")
    print("1. Login with demo accounts")
    print("2. Visit the Smart Home dashboard")
    print("3. Control devices and test automation")
    print("4. View energy analytics")
    print("5. Manage locations and weather data")

if __name__ == '__main__':
    create_demo_smart_devices()
