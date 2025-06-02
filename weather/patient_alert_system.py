"""
Comprehensive patient alert system for weather-based health management
"""
from datetime import datetime, timedelta
from django.utils import timezone
import json

class PatientAlertSystem:
    """Advanced alert system for patients with chronic conditions"""
    
    @staticmethod
    def get_medication_alerts(weather_data, user, health_conditions):
        """Generate weather-triggered medication alerts"""
        alerts = []
        temp = weather_data.get('temperature', 25)
        humidity = weather_data.get('humidity', 50)
        aqi = weather_data.get('air_quality_index', 3)
        weather_condition = weather_data.get('weather_condition', '')
        
        # Parse health conditions
        conditions = health_conditions.lower() if health_conditions else ""
        
        # Respiratory conditions (Asthma, COPD, Bronchitis)
        if any(condition in conditions for condition in ['asthma', 'copd', 'bronchitis', 'respiratory']):
            if aqi >= 4:
                alerts.append({
                    'type': 'critical',
                    'category': 'medication',
                    'icon': '💨',
                    'title': 'INHALER ALERT - Poor Air Quality',
                    'message': f'AQI {aqi}/5 is dangerous for respiratory conditions. Keep rescue inhaler ready. Take preventive medication as prescribed. Avoid outdoor activities.',
                    'action_required': True,
                    'medication': 'Rescue Inhaler',
                    'timing': 'Immediate',
                    'priority': 'critical'
                })
            elif aqi >= 3 or 'dust' in weather_condition:
                alerts.append({
                    'type': 'warning',
                    'category': 'medication',
                    'icon': '🌫️',
                    'title': 'Respiratory Precaution',
                    'message': 'Moderate air pollution detected. Consider preventive inhaler use before going out. Carry rescue medication.',
                    'action_required': True,
                    'medication': 'Preventive Inhaler',
                    'timing': 'Before outdoor activities',
                    'priority': 'high'
                })
        
        # Cardiovascular conditions
        if any(condition in conditions for condition in ['heart', 'cardiac', 'hypertension', 'blood pressure']):
            if temp > 35:
                alerts.append({
                    'type': 'critical',
                    'category': 'medication',
                    'icon': '❤️',
                    'title': 'CARDIAC ALERT - Extreme Heat',
                    'message': f'Temperature {temp}°C dangerous for heart conditions. Take prescribed medications on time. Monitor blood pressure. Stay hydrated but don\'t overdrink.',
                    'action_required': True,
                    'medication': 'Cardiac medications',
                    'timing': 'As prescribed + extra monitoring',
                    'priority': 'critical'
                })
            elif temp > 30 and humidity > 80:
                alerts.append({
                    'type': 'warning',
                    'category': 'medication',
                    'icon': '💊',
                    'title': 'Heart Health Monitoring',
                    'message': 'Hot and humid weather stresses cardiovascular system. Monitor blood pressure twice daily. Take medications on schedule.',
                    'action_required': True,
                    'medication': 'BP medications',
                    'timing': 'Regular schedule + monitoring',
                    'priority': 'high'
                })
        
        # Diabetes
        if any(condition in conditions for condition in ['diabetes', 'diabetic', 'blood sugar']):
            if temp > 35:
                alerts.append({
                    'type': 'warning',
                    'category': 'medication',
                    'icon': '🩸',
                    'title': 'Diabetes Heat Management',
                    'message': f'Extreme heat affects blood sugar control. Check glucose more frequently. Store insulin properly (cool, not frozen). Stay hydrated.',
                    'action_required': True,
                    'medication': 'Insulin/Diabetes medications',
                    'timing': 'Increased monitoring',
                    'priority': 'high'
                })
        
        # Arthritis/Joint conditions
        if any(condition in conditions for condition in ['arthritis', 'joint', 'rheumatoid']):
            if humidity > 80 or 'rain' in weather_condition:
                alerts.append({
                    'type': 'info',
                    'category': 'medication',
                    'icon': '🦴',
                    'title': 'Joint Pain Management',
                    'message': f'High humidity {humidity}% may increase joint pain. Consider anti-inflammatory medication. Apply heat therapy. Gentle exercises recommended.',
                    'action_required': False,
                    'medication': 'Anti-inflammatory',
                    'timing': 'As needed for pain',
                    'priority': 'medium'
                })
        
        # Migraine/Headache conditions
        if any(condition in conditions for condition in ['migraine', 'headache']):
            if abs(weather_data.get('pressure', 1013) - 1013) > 10:
                alerts.append({
                    'type': 'warning',
                    'category': 'medication',
                    'icon': '🧠',
                    'title': 'Migraine Weather Alert',
                    'message': 'Barometric pressure changes detected. Migraine trigger possible. Keep rescue medication ready. Stay hydrated.',
                    'action_required': True,
                    'medication': 'Migraine medication',
                    'timing': 'At first sign of symptoms',
                    'priority': 'medium'
                })
        
        return alerts
    
    @staticmethod
    def get_health_monitoring_alerts(weather_data, user, health_conditions):
        """Generate health monitoring alerts based on weather"""
        alerts = []
        temp = weather_data.get('temperature', 25)
        humidity = weather_data.get('humidity', 50)
        aqi = weather_data.get('air_quality_index', 3)
        
        conditions = health_conditions.lower() if health_conditions else ""
        
        # Blood pressure monitoring
        if any(condition in conditions for condition in ['hypertension', 'blood pressure', 'heart']):
            if temp > 35 or aqi >= 4:
                alerts.append({
                    'type': 'warning',
                    'category': 'monitoring',
                    'icon': '📊',
                    'title': 'Blood Pressure Check Required',
                    'message': 'Extreme weather conditions. Check blood pressure twice today (morning & evening). Record readings.',
                    'action_required': True,
                    'frequency': 'Twice daily',
                    'priority': 'high'
                })
        
        # Blood sugar monitoring
        if any(condition in conditions for condition in ['diabetes', 'diabetic']):
            if temp > 35:
                alerts.append({
                    'type': 'warning',
                    'category': 'monitoring',
                    'icon': '🩸',
                    'title': 'Increased Glucose Monitoring',
                    'message': 'Heat stress affects blood sugar. Check glucose before meals and 2 hours after. Stay hydrated.',
                    'action_required': True,
                    'frequency': 'Before & after meals',
                    'priority': 'high'
                })
        
        # Respiratory monitoring
        if any(condition in conditions for condition in ['asthma', 'copd', 'respiratory']):
            if aqi >= 3:
                alerts.append({
                    'type': 'info',
                    'category': 'monitoring',
                    'icon': '🫁',
                    'title': 'Respiratory Symptom Watch',
                    'message': 'Monitor breathing difficulty, cough, or wheezing. Use peak flow meter if available. Note any changes.',
                    'action_required': True,
                    'frequency': 'Throughout the day',
                    'priority': 'medium'
                })
        
        return alerts
    
    @staticmethod
    def get_appointment_alerts(weather_data, user):
        """Generate appointment-related alerts based on weather"""
        alerts = []
        temp = weather_data.get('temperature', 25)
        aqi = weather_data.get('air_quality_index', 3)
        weather_condition = weather_data.get('weather_condition', '')
        
        # Severe weather conditions
        if temp > 40 or aqi >= 4 or 'storm' in weather_condition:
            alerts.append({
                'type': 'warning',
                'category': 'appointment',
                'icon': '🏥',
                'title': 'Consider Rescheduling Appointments',
                'message': 'Severe weather conditions. Consider rescheduling non-urgent outdoor appointments. Telemedicine options available.',
                'action_required': False,
                'priority': 'medium'
            })
        
        # Monsoon/flooding conditions
        if weather_data.get('monsoon_intensity') == 'heavy':
            alerts.append({
                'type': 'info',
                'category': 'appointment',
                'icon': '🌧️',
                'title': 'Monsoon Travel Advisory',
                'message': 'Heavy rainfall expected. Allow extra travel time. Check for waterlogged routes. Carry emergency contacts.',
                'action_required': False,
                'priority': 'medium'
            })
        
        return alerts
    
    @staticmethod
    def get_emergency_alerts(weather_data, user, health_conditions):
        """Generate emergency health alerts"""
        alerts = []
        temp = weather_data.get('temperature', 25)
        aqi = weather_data.get('air_quality_index', 3)
        dust_storm_risk = weather_data.get('dust_storm_risk', 'low')
        
        conditions = health_conditions.lower() if health_conditions else ""
        
        # Critical temperature for vulnerable patients
        if temp > 42:
            alerts.append({
                'type': 'critical',
                'category': 'emergency',
                'icon': '🚨',
                'title': 'HEAT EMERGENCY ALERT',
                'message': f'DANGEROUS temperature {temp}°C. Risk of heat stroke. Stay indoors with AC. Call doctor if feeling unwell. Emergency: 108',
                'action_required': True,
                'emergency_contact': '108',
                'priority': 'critical'
            })
        
        # Critical air quality for respiratory patients
        if aqi >= 5 and any(condition in conditions for condition in ['asthma', 'copd', 'respiratory']):
            alerts.append({
                'type': 'critical',
                'category': 'emergency',
                'icon': '🚨',
                'title': 'RESPIRATORY EMERGENCY RISK',
                'message': 'HAZARDOUS air quality for respiratory conditions. Stay indoors. Use air purifiers. Seek immediate medical help if breathing difficulty.',
                'action_required': True,
                'emergency_contact': '108',
                'priority': 'critical'
            })
        
        # Dust storm emergency
        if dust_storm_risk == 'high' and any(condition in conditions for condition in ['asthma', 'respiratory', 'eye']):
            alerts.append({
                'type': 'critical',
                'category': 'emergency',
                'icon': '🌪️',
                'title': 'DUST STORM HEALTH EMERGENCY',
                'message': 'Severe dust storm dangerous for respiratory/eye conditions. Stay indoors. Seal windows. Emergency medical help: 108',
                'action_required': True,
                'emergency_contact': '108',
                'priority': 'critical'
            })
        
        return alerts
    
    @staticmethod
    def get_daily_health_tips(weather_data, user, health_conditions):
        """Generate daily health tips based on weather and conditions"""
        tips = []
        temp = weather_data.get('temperature', 25)
        humidity = weather_data.get('humidity', 50)
        comfort_level = weather_data.get('comfort_level', 'moderate')
        
        conditions = health_conditions.lower() if health_conditions else ""
        
        # General tips based on comfort level
        if comfort_level == 'very_hot':
            tips.append({
                'type': 'info',
                'category': 'daily_tip',
                'icon': '💡',
                'title': 'Daily Health Tip',
                'message': 'Very hot day ahead. Start hydrating early. Eat light, cooling foods like cucumber, watermelon. Avoid heavy meals.',
                'priority': 'low'
            })
        
        elif comfort_level == 'hot_humid':
            tips.append({
                'type': 'info',
                'category': 'daily_tip',
                'icon': '🌿',
                'title': 'Humidity Management Tip',
                'message': 'Hot and humid weather. Wear loose, breathable cotton clothes. Use talcum powder to prevent rashes. Take cool showers.',
                'priority': 'low'
            })
        
        # Condition-specific tips
        if 'diabetes' in conditions and temp > 30:
            tips.append({
                'type': 'info',
                'category': 'daily_tip',
                'icon': '🍎',
                'title': 'Diabetes Heat Management',
                'message': 'Hot weather tip: Eat smaller, frequent meals. Avoid sugary drinks. Check feet daily for heat-related injuries.',
                'priority': 'low'
            })
        
        if 'arthritis' in conditions and humidity > 70:
            tips.append({
                'type': 'info',
                'category': 'daily_tip',
                'icon': '🧘‍♀️',
                'title': 'Joint Care in Humidity',
                'message': 'High humidity may increase joint stiffness. Do gentle morning stretches. Apply warm compress before activities.',
                'priority': 'low'
            })
        
        return tips
    
    @staticmethod
    def get_all_patient_alerts(weather_data, user, health_conditions):
        """Get comprehensive patient alerts"""
        all_alerts = []
        
        # Collect all types of alerts
        all_alerts.extend(PatientAlertSystem.get_medication_alerts(weather_data, user, health_conditions))
        all_alerts.extend(PatientAlertSystem.get_health_monitoring_alerts(weather_data, user, health_conditions))
        all_alerts.extend(PatientAlertSystem.get_appointment_alerts(weather_data, user))
        all_alerts.extend(PatientAlertSystem.get_emergency_alerts(weather_data, user, health_conditions))
        all_alerts.extend(PatientAlertSystem.get_daily_health_tips(weather_data, user, health_conditions))
        
        # Sort by priority
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        all_alerts.sort(key=lambda x: priority_order.get(x.get('priority', 'low'), 3))
        
        return all_alerts
