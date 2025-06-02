#!/usr/bin/env python
"""
Create demo data for enterprise facilities
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
from enterprise.models import Facility, Department, FacilityAlert, EnergyTariff
from smarthome.models import SmartDevice, AutomationRule, EnergyUsage, DeviceAction

User = get_user_model()

def create_enterprise_users():
    """Create enterprise demo users"""
    print("Creating enterprise demo users...")
    
    # Hospital users
    hospital_manager = User.objects.create_user(
        username='hospital_manager',
        email='manager@cityhospital.com',
        password='password123',
        first_name='Dr. Sarah',
        last_name='Johnson',
        role='facility_manager',
        facility_type='hospital',
        facility_name='City General Hospital',
        department='Administration',
        employee_id='HM001',
        access_level=5
    )
    
    medical_staff = User.objects.create_user(
        username='medical_staff',
        email='nurse@cityhospital.com',
        password='password123',
        first_name='Nurse',
        last_name='Williams',
        role='medical_staff',
        facility_type='hospital',
        facility_name='City General Hospital',
        department='ICU',
        employee_id='MS001',
        access_level=2
    )
    
    # Factory users
    factory_manager = User.objects.create_user(
        username='factory_manager',
        email='manager@techfactory.com',
        password='password123',
        first_name='Raj',
        last_name='Patel',
        role='facility_manager',
        facility_type='factory',
        facility_name='TechManufacturing Industries',
        department='Operations',
        employee_id='FM001',
        access_level=5
    )
    
    production_manager = User.objects.create_user(
        username='production_manager',
        email='production@techfactory.com',
        password='password123',
        first_name='Priya',
        last_name='Sharma',
        role='production_manager',
        facility_type='factory',
        facility_name='TechManufacturing Industries',
        department='Production',
        employee_id='PM001',
        access_level=3
    )
    
    # Office users
    office_manager = User.objects.create_user(
        username='office_manager',
        email='manager@techcorp.com',
        password='password123',
        first_name='Amit',
        last_name='Kumar',
        role='facility_manager',
        facility_type='office',
        facility_name='TechCorp Office Complex',
        department='Facilities',
        employee_id='OM001',
        access_level=4
    )
    
    energy_manager = User.objects.create_user(
        username='energy_manager',
        email='energy@techcorp.com',
        password='password123',
        first_name='Sunita',
        last_name='Reddy',
        role='energy_manager',
        facility_type='office',
        facility_name='TechCorp Office Complex',
        department='Sustainability',
        employee_id='EM001',
        access_level=4
    )
    
    print(f"Created {User.objects.filter(facility_type__in=['hospital', 'factory', 'office']).count()} enterprise users")
    return [hospital_manager, medical_staff, factory_manager, production_manager, office_manager, energy_manager]

def create_facilities():
    """Create demo facilities"""
    print("Creating demo facilities...")
    
    # Hospital
    hospital = Facility.objects.create(
        name='City General Hospital',
        facility_type='hospital',
        facility_size='large',
        address='123 Medical Center Drive',
        city='Mumbai',
        state='Maharashtra',
        country='India',
        postal_code='400001',
        total_area=150000,
        number_of_buildings=3,
        number_of_floors=8,
        occupancy_capacity=500,
        electrical_capacity=2000,
        backup_power_capacity=1500,
        energy_tariff_type='hospital',
        peak_demand_charge=150,
        certifications=['JCI', 'NABH', 'ISO 14001'],
        compliance_standards=['HIPAA', 'Medical Device Regulations'],
        facility_manager=User.objects.get(username='hospital_manager')
    )
    
    # Factory
    factory = Facility.objects.create(
        name='TechManufacturing Industries',
        facility_type='factory',
        facility_size='enterprise',
        address='Industrial Area, Plot 45-50',
        city='Chennai',
        state='Tamil Nadu',
        country='India',
        postal_code='600001',
        total_area=250000,
        number_of_buildings=5,
        number_of_floors=2,
        occupancy_capacity=800,
        electrical_capacity=5000,
        backup_power_capacity=2000,
        energy_tariff_type='industrial',
        peak_demand_charge=200,
        certifications=['ISO 9001', 'ISO 14001', 'OHSAS 18001'],
        compliance_standards=['Factory Act', 'Environmental Clearance'],
        facility_manager=User.objects.get(username='factory_manager')
    )
    
    # Office
    office = Facility.objects.create(
        name='TechCorp Office Complex',
        facility_type='office',
        facility_size='large',
        address='IT Park, Sector 5',
        city='Bangalore',
        state='Karnataka',
        country='India',
        postal_code='560001',
        total_area=100000,
        number_of_buildings=2,
        number_of_floors=12,
        occupancy_capacity=1200,
        electrical_capacity=1500,
        backup_power_capacity=500,
        energy_tariff_type='commercial',
        peak_demand_charge=120,
        certifications=['LEED Gold', 'IGBC Green Building'],
        compliance_standards=['Building Code', 'Fire Safety'],
        facility_manager=User.objects.get(username='office_manager')
    )
    
    print(f"Created {Facility.objects.count()} facilities")
    return [hospital, factory, office]

def create_departments(facilities):
    """Create departments for each facility"""
    print("Creating departments...")
    
    hospital, factory, office = facilities
    
    # Hospital departments
    hospital_depts = [
        ('Emergency Department', 'emergency', 4, 5000, 20, 24, 40, 60),
        ('ICU', 'icu', 5, 3000, 18, 22, 45, 55),
        ('Operating Room 1', 'operating_room', 5, 1500, 18, 22, 45, 55),
        ('Operating Room 2', 'operating_room', 5, 1500, 18, 22, 45, 55),
        ('Patient Ward A', 'patient_room', 3, 8000, 20, 26, 40, 60),
        ('Laboratory', 'laboratory', 4, 2000, 20, 24, 40, 60),
        ('Pharmacy', 'pharmacy', 3, 1000, 18, 25, 40, 60),
        ('Administration', 'administration', 2, 3000, 22, 26, 40, 60),
    ]
    
    for name, dept_type, criticality, area, temp_min, temp_max, hum_min, hum_max in hospital_depts:
        Department.objects.create(
            facility=hospital,
            name=name,
            department_type=dept_type,
            floor_number=random.randint(1, 8),
            area=area,
            temperature_min=temp_min,
            temperature_max=temp_max,
            humidity_min=hum_min,
            humidity_max=hum_max,
            criticality_level=criticality,
            operates_24_7=dept_type in ['emergency', 'icu', 'operating_room'],
            department_head=User.objects.get(username='medical_staff') if dept_type == 'icu' else None
        )
    
    # Factory departments
    factory_depts = [
        ('Production Floor A', 'production', 4, 15000, 18, 28, 30, 70),
        ('Production Floor B', 'production', 4, 15000, 18, 28, 30, 70),
        ('Assembly Line 1', 'assembly', 3, 8000, 20, 26, 40, 60),
        ('Assembly Line 2', 'assembly', 3, 8000, 20, 26, 40, 60),
        ('Quality Control', 'quality_control', 4, 3000, 20, 24, 40, 55),
        ('Warehouse', 'warehouse', 2, 20000, 15, 30, 30, 80),
        ('Maintenance Shop', 'maintenance', 2, 2000, 18, 30, 30, 70),
        ('Office Area', 'office', 2, 5000, 22, 26, 40, 60),
    ]
    
    for name, dept_type, criticality, area, temp_min, temp_max, hum_min, hum_max in factory_depts:
        Department.objects.create(
            facility=factory,
            name=name,
            department_type=dept_type,
            floor_number=random.randint(1, 2),
            area=area,
            temperature_min=temp_min,
            temperature_max=temp_max,
            humidity_min=hum_min,
            humidity_max=hum_max,
            criticality_level=criticality,
            operates_24_7=dept_type in ['production'],
            department_head=User.objects.get(username='production_manager') if 'production' in dept_type else None
        )
    
    # Office departments
    office_depts = [
        ('Reception', 'reception', 2, 1000, 22, 26, 40, 60),
        ('Conference Rooms', 'conference', 2, 2000, 20, 24, 40, 60),
        ('Floor 5 Workstations', 'workstation', 2, 8000, 22, 26, 40, 60),
        ('Floor 8 Workstations', 'workstation', 2, 8000, 22, 26, 40, 60),
        ('Server Room', 'server_room', 5, 500, 18, 22, 40, 50),
        ('Cafeteria', 'cafeteria', 1, 3000, 20, 28, 40, 70),
        ('Executive Floor', 'office', 3, 5000, 22, 25, 40, 55),
    ]
    
    for name, dept_type, criticality, area, temp_min, temp_max, hum_min, hum_max in office_depts:
        Department.objects.create(
            facility=office,
            name=name,
            department_type=dept_type,
            floor_number=random.randint(1, 12),
            area=area,
            temperature_min=temp_min,
            temperature_max=temp_max,
            humidity_min=hum_min,
            humidity_max=hum_max,
            criticality_level=criticality,
            operates_24_7=dept_type == 'server_room',
            department_head=User.objects.get(username='office_manager') if dept_type == 'office' else None
        )
    
    print(f"Created {Department.objects.count()} departments")

def create_enterprise_devices():
    """Create enterprise smart devices"""
    print("Creating enterprise devices...")
    
    facilities = Facility.objects.all()
    device_count = 0
    
    for facility in facilities:
        departments = facility.departments.all()
        
        for dept in departments:
            # Create devices based on facility and department type
            if facility.facility_type == 'hospital':
                if dept.department_type == 'operating_room':
                    devices = [
                        ('OR Climate Control', 'or_climate', 5),
                        ('Medical HVAC', 'medical_hvac', 5),
                        ('UV Sterilizer', 'uv_sterilizer', 4),
                        ('Backup Power', 'backup_power', 5),
                    ]
                elif dept.department_type == 'icu':
                    devices = [
                        ('ICU HVAC', 'medical_hvac', 5),
                        ('Patient Monitor', 'patient_monitor', 5),
                        ('Oxygen System', 'oxygen_concentrator', 5),
                        ('Medical Fridge', 'medical_fridge', 4),
                    ]
                elif dept.department_type == 'pharmacy':
                    devices = [
                        ('Pharmacy Storage', 'pharmacy_storage', 4),
                        ('Medical Fridge', 'medical_fridge', 4),
                        ('HVAC System', 'medical_hvac', 3),
                    ]
                else:
                    devices = [
                        ('HVAC System', 'medical_hvac', 3),
                        ('Smart Lighting', 'lights', 2),
                        ('Air Purifier', 'air_purifier', 3),
                    ]
            
            elif facility.facility_type == 'factory':
                if dept.department_type == 'production':
                    devices = [
                        ('Production Line Control', 'production_line', 4),
                        ('Industrial HVAC', 'industrial_hvac', 4),
                        ('Conveyor System', 'conveyor_system', 4),
                        ('Industrial Fan', 'industrial_fan', 3),
                        ('Safety System', 'safety_system', 5),
                    ]
                elif dept.department_type == 'quality_control':
                    devices = [
                        ('Quality Monitor', 'quality_monitor', 4),
                        ('HVAC System', 'industrial_hvac', 3),
                        ('Air Purifier', 'air_purifier', 3),
                    ]
                else:
                    devices = [
                        ('HVAC System', 'industrial_hvac', 3),
                        ('Smart Lighting', 'lights', 2),
                        ('Industrial Fan', 'industrial_fan', 2),
                    ]
            
            else:  # office
                if dept.department_type == 'server_room':
                    devices = [
                        ('Server Cooling', 'server_cooling', 5),
                        ('UPS System', 'ups_system', 5),
                        ('Environmental Monitor', 'energy_meter', 4),
                    ]
                elif dept.department_type == 'conference':
                    devices = [
                        ('Conference AV', 'conference_av', 2),
                        ('HVAC System', 'bms', 3),
                        ('Smart Lighting', 'lights', 2),
                    ]
                else:
                    devices = [
                        ('BMS System', 'bms', 3),
                        ('Smart Lighting', 'lights', 2),
                        ('HVAC Control', 'thermostat', 3),
                    ]
            
            # Create devices for this department
            for device_name, device_type, criticality in devices:
                user = facility.facility_manager
                
                device = SmartDevice.objects.create(
                    user=user,
                    name=f"{dept.name} - {device_name}",
                    device_type=device_type,
                    brand=random.choice(['Siemens', 'Honeywell', 'Johnson Controls', 'Schneider', 'ABB']),
                    model=f"Model-{random.randint(1000, 9999)}",
                    location=dept.name,
                    status=random.choice(['online', 'online', 'online', 'offline']),  # 75% online
                    facility=facility,
                    department=dept,
                    asset_tag=f"{facility.name[:3].upper()}-{dept.name[:3].upper()}-{device_count:04d}",
                    criticality_level=criticality,
                    max_power_consumption=random.randint(500, 5000),
                    capabilities={
                        'remote_control': True,
                        'energy_monitoring': True,
                        'automation_support': True,
                        'maintenance_alerts': True
                    },
                    current_state={
                        'power': random.choice([True, False]),
                        'temperature': random.randint(18, 28),
                        'last_maintenance': '2024-01-15'
                    }
                )
                device.save_to_mongodb()
                device_count += 1
    
    print(f"Created {device_count} enterprise devices")

def create_energy_tariffs():
    """Create energy tariff structures"""
    print("Creating energy tariffs...")
    
    tariffs = [
        {
            'name': 'Mumbai Hospital Tariff',
            'tariff_type': 'hospital',
            'utility_company': 'BEST Mumbai',
            'region': 'Mumbai',
            'base_rate': 6.5,
            'peak_rate': 9.2,
            'off_peak_rate': 4.8,
            'demand_charge': 150,
        },
        {
            'name': 'Chennai Industrial Tariff',
            'tariff_type': 'industrial',
            'utility_company': 'TNEB',
            'region': 'Chennai',
            'base_rate': 7.2,
            'peak_rate': 10.5,
            'off_peak_rate': 5.2,
            'demand_charge': 200,
        },
        {
            'name': 'Bangalore Commercial Tariff',
            'tariff_type': 'commercial',
            'utility_company': 'BESCOM',
            'region': 'Bangalore',
            'base_rate': 6.8,
            'peak_rate': 9.8,
            'off_peak_rate': 5.0,
            'demand_charge': 120,
        }
    ]
    
    for tariff_data in tariffs:
        EnergyTariff.objects.create(
            **tariff_data,
            effective_date=datetime.now().date() - timedelta(days=30),
            is_active=True
        )
    
    print(f"Created {EnergyTariff.objects.count()} energy tariffs")

def main():
    """Main function to create all enterprise demo data"""
    print("Creating enterprise demo data...")
    
    # Create users
    users = create_enterprise_users()
    
    # Create facilities
    facilities = create_facilities()
    
    # Create departments
    create_departments(facilities)
    
    # Create devices
    create_enterprise_devices()
    
    # Create energy tariffs
    create_energy_tariffs()
    
    print("\n✅ Enterprise demo data creation completed!")
    print(f"Created:")
    print(f"  - {User.objects.filter(facility_type__in=['hospital', 'factory', 'office']).count()} enterprise users")
    print(f"  - {Facility.objects.count()} facilities")
    print(f"  - {Department.objects.count()} departments")
    print(f"  - {SmartDevice.objects.filter(facility__isnull=False).count()} enterprise devices")
    print(f"  - {EnergyTariff.objects.count()} energy tariffs")
    
    print("\nEnterprise Demo Accounts:")
    print("  Hospital Manager: hospital_manager / password123")
    print("  Medical Staff: medical_staff / password123")
    print("  Factory Manager: factory_manager / password123")
    print("  Production Manager: production_manager / password123")
    print("  Office Manager: office_manager / password123")
    print("  Energy Manager: energy_manager / password123")

if __name__ == '__main__':
    main()
