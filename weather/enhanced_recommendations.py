"""
Enhanced weather-based recommendations including energy and smart home features with Indian climate support
"""
from datetime import datetime
import random
from .indian_climate_recommendations import IndianClimateRecommendations
from .patient_alert_system import PatientAlertSystem

class EnhancedRecommendationEngine:
    """Enhanced recommendation engine with energy and smart home features"""
    
    @staticmethod
    def get_enhanced_temperature_recommendations(temp):
        """Enhanced temperature-based recommendations"""
        recommendations = []
        
        if temp >= 35:
            recommendations.append({
                'type': 'danger',
                'title': 'Extreme Heat Alert',
                'message': f'Temperature is {temp}°C - STAY INDOORS during peak hours (11 AM - 4 PM). Drink water every 15 minutes, wear light-colored loose clothing, use sunscreen SPF 50+, seek immediate medical attention if experiencing heat exhaustion symptoms.',
                'icon': '🌡️',
                'category': 'health',
                'priority': 'high',
                'actions': ['stay_indoors', 'hydrate_frequently', 'use_ac', 'wear_light_clothing']
            })
        elif temp >= 30:
            recommendations.append({
                'type': 'warning',
                'title': 'High Temperature Warning',
                'message': f'Temperature is {temp}°C - Stay hydrated (drink 250ml water every hour), wear light clothing, use sunscreen SPF 30+, avoid outdoor activities between 11 AM - 4 PM. Take cool showers and use fans for air circulation.',
                'icon': '☀️',
                'category': 'health',
                'priority': 'medium',
                'actions': ['hydrate_regularly', 'avoid_peak_sun', 'use_cooling', 'light_clothing']
            })
        elif temp >= 25:
            recommendations.append({
                'type': 'info',
                'title': 'Warm Weather Tips',
                'message': f'Temperature is {temp}°C - Stay comfortable with light clothing, drink plenty of fluids, use sunscreen when outdoors. Good weather for outdoor activities with proper precautions.',
                'icon': '🌤️',
                'category': 'health',
                'priority': 'low',
                'actions': ['stay_hydrated', 'use_sunscreen', 'enjoy_outdoors']
            })
        elif temp <= 0:
            recommendations.append({
                'type': 'danger',
                'title': 'Freezing Temperature Alert',
                'message': f'Temperature is {temp}°C - DRESS IN LAYERS, protect extremities (hands, feet, face), limit outdoor exposure, watch for signs of hypothermia and frostbite. Ensure heating systems are working properly.',
                'icon': '🥶',
                'category': 'health',
                'priority': 'high',
                'actions': ['dress_warmly', 'limit_exposure', 'protect_extremities', 'check_heating']
            })
        elif temp <= 5:
            recommendations.append({
                'type': 'warning',
                'title': 'Cold Weather Precautions',
                'message': f'Temperature is {temp}°C - Dress in layers, protect extremities, warm up indoors before going out. Increase caloric intake and stay dry. Check on elderly neighbors and pets.',
                'icon': '❄️',
                'category': 'health',
                'priority': 'medium',
                'actions': ['layer_clothing', 'warm_up_indoors', 'increase_calories', 'check_others']
            })
        
        return recommendations
    
    @staticmethod
    def get_enhanced_humidity_recommendations(humidity):
        """Enhanced humidity-based recommendations"""
        recommendations = []
        
        if humidity >= 85:
            recommendations.append({
                'type': 'warning',
                'title': 'Very High Humidity Alert',
                'message': f'Humidity is {humidity}% - Reduce physical activity intensity, stay in air-conditioned spaces, monitor for heat exhaustion symptoms. Use dehumidifiers indoors and wear moisture-wicking fabrics.',
                'icon': '💧',
                'category': 'health',
                'priority': 'medium',
                'actions': ['reduce_activity', 'use_ac', 'use_dehumidifier', 'moisture_wicking_clothes']
            })
        elif humidity >= 70:
            recommendations.append({
                'type': 'info',
                'title': 'High Humidity Notice',
                'message': f'Humidity is {humidity}% - Take frequent breaks during outdoor activities, stay hydrated, and use fans for air circulation. Consider indoor alternatives for intense exercise.',
                'icon': '🌫️',
                'category': 'health',
                'priority': 'low',
                'actions': ['take_breaks', 'use_fans', 'indoor_exercise']
            })
        elif humidity <= 30:
            recommendations.append({
                'type': 'info',
                'title': 'Low Humidity Alert',
                'message': f'Humidity is {humidity}% - Use moisturizers for skin, drink extra water, consider using a humidifier indoors. Protect nasal passages and eyes from dryness.',
                'icon': '🏜️',
                'category': 'health',
                'priority': 'low',
                'actions': ['use_moisturizer', 'drink_water', 'use_humidifier', 'protect_airways']
            })
        
        return recommendations
    
    @staticmethod
    def get_enhanced_uv_recommendations(uv_index):
        """Enhanced UV index recommendations"""
        recommendations = []
        
        if uv_index >= 11:
            recommendations.append({
                'type': 'danger',
                'title': 'Extreme UV Exposure Risk',
                'message': f'UV Index is {uv_index} - AVOID outdoor exposure between 10 AM - 4 PM. If you must go out: use SPF 50+ sunscreen (reapply every hour), wear protective clothing, wide-brimmed hat, and UV-blocking sunglasses.',
                'icon': '☀️',
                'category': 'health',
                'priority': 'high',
                'actions': ['avoid_sun', 'spf_50_plus', 'protective_clothing', 'uv_sunglasses']
            })
        elif uv_index >= 8:
            recommendations.append({
                'type': 'warning',
                'title': 'Very High UV Exposure',
                'message': f'UV Index is {uv_index} - Use SPF 30+ sunscreen, wear protective clothing and sunglasses, seek shade during peak hours (10 AM - 4 PM). Reapply sunscreen every 2 hours.',
                'icon': '🌞',
                'category': 'health',
                'priority': 'medium',
                'actions': ['spf_30_plus', 'seek_shade', 'reapply_sunscreen', 'protective_gear']
            })
        elif uv_index >= 6:
            recommendations.append({
                'type': 'warning',
                'title': 'High UV Exposure',
                'message': f'UV Index is {uv_index} - Apply SPF 30 sunscreen, wear sunglasses and a hat. Limit midday sun exposure and seek shade when possible.',
                'icon': '🕶️',
                'category': 'health',
                'priority': 'medium',
                'actions': ['spf_30', 'wear_hat', 'limit_midday_sun']
            })
        elif uv_index >= 3:
            recommendations.append({
                'type': 'info',
                'title': 'Moderate UV Exposure',
                'message': f'UV Index is {uv_index} - Use sunscreen and wear sunglasses during extended outdoor activities. Good conditions for outdoor exercise with basic sun protection.',
                'icon': '🧴',
                'category': 'health',
                'priority': 'low',
                'actions': ['basic_sunscreen', 'sunglasses', 'outdoor_activities_ok']
            })
        
        return recommendations
    
    @staticmethod
    def get_energy_recommendations(weather_data):
        """Energy saving recommendations based on weather"""
        recommendations = []
        temp = weather_data.get('temperature', 20)
        humidity = weather_data.get('humidity', 50)
        wind_speed = weather_data.get('wind_speed', 5)
        description = weather_data.get('description', '').lower()
        
        # Hot weather energy tips
        if temp >= 28:
            recommendations.append({
                'type': 'success',
                'title': 'Hot Weather Energy Savings',
                'message': f'Temperature {temp}°C - Set AC to 24-26°C (saves 6-8% per degree), use ceiling fans to circulate air, close curtains during peak sun hours (11 AM - 4 PM), run dishwasher and laundry during off-peak hours (10 PM - 6 AM) to reduce costs by 20-30%.',
                'icon': '💡',
                'category': 'energy',
                'priority': 'medium',
                'savings': '20-30%',
                'actions': ['set_ac_optimal', 'use_fans', 'close_curtains', 'off_peak_appliances']
            })
        
        # Cold weather energy tips
        elif temp <= 15:
            recommendations.append({
                'type': 'success',
                'title': 'Cold Weather Energy Savings',
                'message': f'Temperature {temp}°C - Lower thermostat by 2°C when away (saves 10% on heating), use natural sunlight for heating during day, seal windows and doors, use programmable thermostats. Wear layers indoors to stay comfortable at lower temperatures.',
                'icon': '🏠',
                'category': 'energy',
                'priority': 'medium',
                'savings': '10-15%',
                'actions': ['lower_thermostat', 'use_sunlight', 'seal_gaps', 'wear_layers']
            })
        
        # High humidity energy tips
        if humidity >= 70:
            recommendations.append({
                'type': 'info',
                'title': 'High Humidity Energy Tips',
                'message': f'Humidity {humidity}% - Use dehumidifiers to reduce AC load (saves 5-10%), ensure proper ventilation, clean AC filters for efficiency. Set AC to "dry" mode when cooling is not needed.',
                'icon': '💨',
                'category': 'energy',
                'priority': 'low',
                'savings': '5-10%',
                'actions': ['use_dehumidifier', 'clean_filters', 'dry_mode', 'ventilate']
            })
        
        # Windy weather energy tips
        if wind_speed >= 15:
            recommendations.append({
                'type': 'info',
                'title': 'Windy Weather Energy Tips',
                'message': f'Wind speed {wind_speed} km/h - Use natural ventilation instead of AC when possible, secure outdoor items to prevent damage, check for air leaks around windows and doors.',
                'icon': '🌬️',
                'category': 'energy',
                'priority': 'low',
                'actions': ['natural_ventilation', 'secure_items', 'check_leaks']
            })
        
        # Peak hour recommendations
        current_hour = datetime.now().hour
        if 14 <= current_hour <= 18:  # Peak hours
            recommendations.append({
                'type': 'warning',
                'title': 'Peak Energy Hours',
                'message': 'Currently in peak electricity hours (2 PM - 6 PM) - Delay running dishwasher, washing machine, and dryer until after 6 PM to save 30-50% on electricity costs. Use minimal lighting and avoid unnecessary appliance use.',
                'icon': '⚡',
                'category': 'energy',
                'priority': 'high',
                'savings': '30-50%',
                'actions': ['delay_appliances', 'minimal_lighting', 'avoid_unnecessary_use']
            })
        
        return recommendations
    
    @staticmethod
    def get_smart_home_recommendations(weather_data, user_devices):
        """Smart home automation recommendations"""
        recommendations = []
        temp = weather_data.get('temperature', 20)
        humidity = weather_data.get('humidity', 50)
        uv_index = weather_data.get('uv_index', 5)
        wind_speed = weather_data.get('wind_speed', 5)
        description = weather_data.get('description', '').lower()
        
        device_types = [device.device_type for device in user_devices] if user_devices else []
        
        # Temperature-based automation
        if temp >= 28 and 'ac' in device_types:
            recommendations.append({
                'type': 'info',
                'title': 'Smart AC Automation',
                'message': f'Temperature {temp}°C - Automatically set AC to 24°C and activate energy-saving mode. Schedule to turn off when no one is home.',
                'icon': '❄️',
                'category': 'automation',
                'priority': 'medium',
                'devices': ['ac'],
                'actions': ['set_ac_24', 'energy_mode', 'schedule_off']
            })
        
        if temp >= 30 and 'curtains' in device_types:
            recommendations.append({
                'type': 'warning',
                'title': 'Smart Curtain Control',
                'message': f'High temperature {temp}°C - Automatically close curtains on south-facing windows to block heat. Open during evening for natural cooling.',
                'icon': '🏠',
                'category': 'automation',
                'priority': 'medium',
                'devices': ['curtains'],
                'actions': ['close_curtains', 'evening_open']
            })
        
        # UV-based automation
        if uv_index >= 7 and 'curtains' in device_types:
            recommendations.append({
                'type': 'warning',
                'title': 'UV Protection Automation',
                'message': f'High UV index {uv_index} - Automatically close all curtains and activate outdoor shade systems to protect furniture and reduce indoor heat.',
                'icon': '☀️',
                'category': 'automation',
                'priority': 'medium',
                'devices': ['curtains', 'awning'],
                'actions': ['close_all_curtains', 'activate_shades']
            })
        
        # Rain detection automation
        if 'rain' in description and 'window' in device_types:
            recommendations.append({
                'type': 'warning',
                'title': 'Rain Detection Automation',
                'message': 'Rain detected - Automatically close all windows and retract awnings to prevent water damage. Activate indoor air circulation.',
                'icon': '🌧️',
                'category': 'automation',
                'priority': 'high',
                'devices': ['window', 'awning', 'fan'],
                'actions': ['close_windows', 'retract_awnings', 'indoor_circulation']
            })
        
        # Wind-based automation
        if wind_speed >= 25:
            recommendations.append({
                'type': 'danger',
                'title': 'High Wind Automation',
                'message': f'High wind speed {wind_speed} km/h - Automatically secure outdoor furniture, close storm shutters, and retract awnings. Monitor for power outages.',
                'icon': '💨',
                'category': 'automation',
                'priority': 'high',
                'devices': ['awning', 'security_system'],
                'actions': ['secure_furniture', 'close_shutters', 'monitor_power']
            })
        
        # Energy optimization automation
        current_hour = datetime.now().hour
        if 14 <= current_hour <= 18 and temp >= 26:  # Peak hours + hot weather
            recommendations.append({
                'type': 'success',
                'title': 'Peak Hour Energy Optimization',
                'message': 'Peak electricity hours + hot weather - Automatically adjust AC temperature +2°C, dim non-essential lights, and delay smart appliance operations until off-peak hours.',
                'icon': '⚡',
                'category': 'automation',
                'priority': 'high',
                'devices': ['ac', 'lights', 'smart_plug'],
                'actions': ['adjust_ac_temp', 'dim_lights', 'delay_appliances'],
                'savings': '25-40%'
            })
        
        return recommendations

    @staticmethod
    def get_comprehensive_recommendations(weather_data, user_role, health_conditions, user_devices=None, user=None):
        """Get comprehensive recommendations including Indian climate and patient alerts"""
        all_recommendations = []

        # Get Indian climate specific recommendations
        all_recommendations.extend(
            IndianClimateRecommendations.get_temperature_recommendations(weather_data, user_role)
        )
        all_recommendations.extend(
            IndianClimateRecommendations.get_monsoon_recommendations(weather_data, user_role)
        )
        all_recommendations.extend(
            IndianClimateRecommendations.get_air_quality_recommendations(weather_data, user_role)
        )
        all_recommendations.extend(
            IndianClimateRecommendations.get_uv_recommendations(weather_data, user_role)
        )
        all_recommendations.extend(
            IndianClimateRecommendations.get_role_specific_recommendations(weather_data, user_role)
        )

        # Get patient-specific alerts if user is a patient
        if user_role == 'patient' and health_conditions:
            patient_alerts = PatientAlertSystem.get_all_patient_alerts(weather_data, user, health_conditions)
            all_recommendations.extend(patient_alerts)

        # Get energy recommendations
        all_recommendations.extend(
            EnhancedRecommendationEngine.get_energy_recommendations(weather_data)
        )

        # Get smart home recommendations if devices available
        if user_devices and user_devices.exists():
            all_recommendations.extend(
                EnhancedRecommendationEngine.get_smart_home_recommendations(weather_data, user_devices)
            )

        # Remove duplicates and sort by priority
        unique_recommendations = []
        seen_titles = set()

        for rec in all_recommendations:
            if rec.get('title') not in seen_titles:
                unique_recommendations.append(rec)
                seen_titles.add(rec.get('title'))

        # Sort by priority
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        unique_recommendations.sort(key=lambda x: priority_order.get(x.get('priority', 'low'), 3))

        return unique_recommendations
