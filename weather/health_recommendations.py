"""
Enhanced health and energy recommendations based on weather conditions and user roles
"""
from datetime import datetime
import random
from .enhanced_recommendations import EnhancedRecommendationEngine

class HealthRecommendationEngine:
    """Generate health and energy recommendations based on weather and user profile"""
    
    @staticmethod
    def get_recommendations(weather_data, user_role, health_conditions=None):
        """Get personalized recommendations based on weather and user profile"""
        recommendations = []
        
        # Extract weather parameters
        temp = weather_data.get('temperature', 20)
        humidity = weather_data.get('humidity', 50)
        uv_index = weather_data.get('uv_index', 5)
        air_quality = weather_data.get('air_quality_index', 3)
        pollen = weather_data.get('pollen_count', 3)
        wind_speed = weather_data.get('wind_speed', 5)
        description = weather_data.get('description', '').lower()
        
        # Role-specific recommendations
        if user_role == 'athlete':
            recommendations.extend(HealthRecommendationEngine._get_athlete_recommendations(
                temp, humidity, uv_index, air_quality, pollen, wind_speed, description
            ))
        elif user_role == 'patient':
            recommendations.extend(HealthRecommendationEngine._get_patient_recommendations(
                temp, humidity, uv_index, air_quality, pollen, health_conditions
            ))
        elif user_role == 'elderly':
            recommendations.extend(HealthRecommendationEngine._get_elderly_recommendations(
                temp, humidity, uv_index, air_quality, description
            ))
        elif user_role == 'doctor':
            recommendations.extend(HealthRecommendationEngine._get_doctor_recommendations(
                temp, humidity, air_quality, pollen
            ))
        elif user_role == 'pharmacist':
            recommendations.extend(HealthRecommendationEngine._get_pharmacist_recommendations(
                temp, humidity, air_quality, pollen, description
            ))
        else:  # public
            recommendations.extend(HealthRecommendationEngine._get_public_recommendations(
                temp, humidity, uv_index, air_quality, description
            ))
        
        # General weather-based recommendations
        recommendations.extend(HealthRecommendationEngine._get_general_recommendations(
            temp, humidity, uv_index, air_quality, description
        ))
        
        return recommendations
    
    @staticmethod
    def _get_athlete_recommendations(temp, humidity, uv_index, air_quality, pollen, wind_speed, description):
        """Recommendations for athletes"""
        recommendations = []
        
        if temp > 30:
            recommendations.append({
                'type': 'warning',
                'title': 'High Temperature Alert',
                'message': 'Consider early morning or evening workouts. Increase hydration and take frequent breaks.',
                'icon': '🌡️'
            })
        elif temp < 5:
            recommendations.append({
                'type': 'info',
                'title': 'Cold Weather Training',
                'message': 'Warm up thoroughly and wear layered clothing. Extend your warm-up routine.',
                'icon': '❄️'
            })
        
        if humidity > 80:
            recommendations.append({
                'type': 'warning',
                'title': 'High Humidity',
                'message': 'Reduce workout intensity and stay extra hydrated. Consider indoor alternatives.',
                'icon': '💧'
            })
        
        if uv_index > 7:
            recommendations.append({
                'type': 'warning',
                'title': 'High UV Exposure',
                'message': 'Wear sunscreen (SPF 30+), sunglasses, and protective clothing. Avoid midday sun.',
                'icon': '☀️'
            })
        
        if air_quality > 3:
            recommendations.append({
                'type': 'danger',
                'title': 'Poor Air Quality',
                'message': 'Consider indoor workouts. If exercising outside, wear a mask and avoid high-intensity activities.',
                'icon': '😷'
            })
        
        if pollen > 3:
            recommendations.append({
                'type': 'warning',
                'title': 'High Pollen Count',
                'message': 'Take antihistamines if needed. Consider indoor training or exercise after rain.',
                'icon': '🌸'
            })
        
        return recommendations
    
    @staticmethod
    def _get_patient_recommendations(temp, humidity, uv_index, air_quality, pollen, health_conditions):
        """Recommendations for patients with chronic conditions"""
        recommendations = []
        conditions = health_conditions.split(',') if health_conditions else []
        
        # Asthma/COPD recommendations
        if any(condition.strip().lower() in ['asthma', 'copd', 'respiratory'] for condition in conditions):
            if air_quality > 2:
                recommendations.append({
                    'type': 'danger',
                    'title': 'Respiratory Alert',
                    'message': 'Poor air quality detected. Keep inhaler handy and avoid outdoor activities.',
                    'icon': '🫁'
                })
            if pollen > 3:
                recommendations.append({
                    'type': 'warning',
                    'title': 'High Pollen Alert',
                    'message': 'Take preventive medication 15 minutes before going outside. Keep windows closed.',
                    'icon': '🌿'
                })
        
        # Arthritis recommendations
        if any(condition.strip().lower() in ['arthritis', 'joint pain'] for condition in conditions):
            if temp < 10 or humidity > 70:
                recommendations.append({
                    'type': 'info',
                    'title': 'Joint Care Reminder',
                    'message': 'Cold/damp weather may increase joint stiffness. Apply heat therapy and gentle stretching.',
                    'icon': '🦴'
                })
        
        # Diabetes recommendations
        if any(condition.strip().lower() in ['diabetes'] for condition in conditions):
            if temp > 28:
                recommendations.append({
                    'type': 'warning',
                    'title': 'Diabetes Heat Alert',
                    'message': 'Monitor blood sugar more frequently. Stay hydrated and avoid prolonged sun exposure.',
                    'icon': '🩸'
                })
        
        return recommendations
    
    @staticmethod
    def _get_elderly_recommendations(temp, humidity, uv_index, air_quality, description):
        """Recommendations for elderly users"""
        recommendations = []
        
        if temp > 32:
            recommendations.append({
                'type': 'danger',
                'title': 'Heat Warning',
                'message': 'Stay indoors during peak hours (11am-4pm). Use AC and drink water regularly.',
                'icon': '🌡️'
            })
        elif temp < 2:
            recommendations.append({
                'type': 'danger',
                'title': 'Cold Warning',
                'message': 'Dress warmly in layers. Check heating system and avoid going out if possible.',
                'icon': '🧥'
            })
        
        if 'rain' in description or 'snow' in description:
            recommendations.append({
                'type': 'warning',
                'title': 'Slip Hazard Alert',
                'message': 'Wear non-slip shoes and use handrails. Consider postponing non-essential trips.',
                'icon': '⚠️'
            })
        
        return recommendations
    
    @staticmethod
    def _get_doctor_recommendations(temp, humidity, air_quality, pollen):
        """Recommendations for healthcare providers"""
        recommendations = []
        
        if temp > 30 or air_quality > 3:
            recommendations.append({
                'type': 'info',
                'title': 'Patient Care Alert',
                'message': 'Expect increased visits from heat-related illnesses and respiratory issues.',
                'icon': '🏥'
            })
        
        if pollen > 3:
            recommendations.append({
                'type': 'info',
                'title': 'Allergy Season Alert',
                'message': 'High pollen count may increase allergy-related appointments. Stock antihistamines.',
                'icon': '💊'
            })
        
        return recommendations
    
    @staticmethod
    def _get_pharmacist_recommendations(temp, humidity, air_quality, pollen, description):
        """Recommendations for pharmacists"""
        recommendations = []
        
        if temp > 28:
            recommendations.append({
                'type': 'info',
                'title': 'Hot Weather Demand',
                'message': 'Stock up on sunscreen, electrolyte solutions, and cooling gels.',
                'icon': '🧴'
            })
        
        if pollen > 3:
            recommendations.append({
                'type': 'info',
                'title': 'Allergy Medication Alert',
                'message': 'High pollen count - expect increased demand for antihistamines and nasal sprays.',
                'icon': '💊'
            })
        
        if 'rain' in description:
            recommendations.append({
                'type': 'info',
                'title': 'Cold & Flu Season',
                'message': 'Rainy weather may increase cold/flu cases. Stock relevant medications.',
                'icon': '🤧'
            })
        
        return recommendations
    
    @staticmethod
    def _get_public_recommendations(temp, humidity, uv_index, air_quality, description):
        """General recommendations for public users"""
        recommendations = []
        
        if temp > 25:
            recommendations.append({
                'type': 'info',
                'title': 'Stay Cool',
                'message': 'Drink plenty of water and seek shade during peak hours.',
                'icon': '💧'
            })
        
        if uv_index > 6:
            recommendations.append({
                'type': 'warning',
                'title': 'UV Protection',
                'message': 'Apply sunscreen and wear protective clothing when outdoors.',
                'icon': '☀️'
            })
        
        return recommendations
    
    @staticmethod
    def _get_general_recommendations(temp, humidity, uv_index, air_quality, description):
        """General recommendations for all users"""
        recommendations = []
        
        if air_quality > 4:
            recommendations.append({
                'type': 'danger',
                'title': 'Air Quality Alert',
                'message': 'Air quality is unhealthy. Limit outdoor activities and consider wearing a mask.',
                'icon': '🏭'
            })
        
        # Energy saving tips
        if temp > 26:
            recommendations.append({
                'type': 'success',
                'title': 'Energy Saving Tip',
                'message': 'Set AC to 24-26°C and use fans to circulate air efficiently.',
                'icon': '💡'
            })
        elif temp < 15:
            recommendations.append({
                'type': 'success',
                'title': 'Energy Saving Tip',
                'message': 'Open curtains during sunny hours to naturally warm your home.',
                'icon': '🏠'
            })
        
        return recommendations

    @staticmethod
    def get_enhanced_recommendations(weather_data, user_role, health_conditions=None, user_devices=None, user=None):
        """Get enhanced recommendations including Indian climate support and patient alerts"""
        from .enhanced_recommendations import EnhancedRecommendationEngine

        # Use the comprehensive recommendation system
        return EnhancedRecommendationEngine.get_comprehensive_recommendations(
            weather_data, user_role, health_conditions, user_devices, user
        )
