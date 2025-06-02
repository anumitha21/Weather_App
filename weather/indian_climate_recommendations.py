"""
Enhanced weather recommendations specifically for Indian climate conditions
"""
from datetime import datetime, timedelta
import random

class IndianClimateRecommendations:
    """Enhanced recommendations for Indian weather conditions"""
    
    @staticmethod
    def get_temperature_recommendations(weather_data, user_role):
        """Get temperature-based recommendations for Indian climate"""
        recommendations = []
        temp = weather_data.get('temperature', 25)
        heat_index = weather_data.get('heat_index', temp)
        humidity = weather_data.get('humidity', 50)
        
        # Extreme heat (>40°C) - Common in North India
        if temp > 40:
            recommendations.extend([
                {
                    'type': 'danger',
                    'category': 'health',
                    'icon': '🔥',
                    'title': 'EXTREME HEAT ALERT',
                    'message': f'Temperature {temp}°C is dangerous. STAY INDOORS between 10 AM - 6 PM. Drink water every 10 minutes (300ml/hour). Use ORS if sweating heavily. Wear light cotton clothes. Avoid outdoor work.',
                    'priority': 'critical',
                    'savings': None
                },
                {
                    'type': 'warning',
                    'category': 'energy',
                    'icon': '❄️',
                    'title': 'AC Optimization for Extreme Heat',
                    'message': f'Set AC to 26°C (not lower) to prevent power cuts. Use ceiling fans with AC. Close all curtains. Run AC during off-peak hours when possible.',
                    'priority': 'high',
                    'savings': '₹200-400/day'
                }
            ])
        
        # Very hot (35-40°C) - Common in summer
        elif temp > 35:
            recommendations.extend([
                {
                    'type': 'warning',
                    'category': 'health',
                    'icon': '🌡️',
                    'title': 'Very Hot Weather',
                    'message': f'Temperature {temp}°C with {humidity}% humidity. Drink 4-5 liters water daily. Avoid 11 AM - 4 PM outdoors. Wear sunscreen SPF 50+. Take cool showers.',
                    'priority': 'high',
                    'savings': None
                },
                {
                    'type': 'info',
                    'category': 'automation',
                    'icon': '🏠',
                    'title': 'Smart Home Heat Management',
                    'message': 'Automatically close curtains, set AC to 25°C, and activate fans. Pre-cool rooms before peak hours.',
                    'priority': 'medium',
                    'savings': '₹150-250/day'
                }
            ])
        
        # Hot and humid (30-35°C with high humidity) - Coastal cities
        elif temp > 30 and humidity > 70:
            recommendations.extend([
                {
                    'type': 'warning',
                    'category': 'health',
                    'icon': '💧',
                    'title': 'Hot & Humid Conditions',
                    'message': f'Heat index feels like {heat_index}°C. High humidity prevents cooling. Use dehumidifiers. Wear breathable cotton. Avoid heavy meals.',
                    'priority': 'medium',
                    'savings': None
                },
                {
                    'type': 'info',
                    'category': 'energy',
                    'icon': '💨',
                    'title': 'Humidity Control',
                    'message': 'Use AC in dry mode. Run exhaust fans. Dehumidify rooms to 50-60%. This improves comfort and reduces AC load.',
                    'priority': 'medium',
                    'savings': '₹100-200/day'
                }
            ])
        
        # Pleasant weather (22-30°C)
        elif 22 <= temp <= 30:
            recommendations.append({
                'type': 'success',
                'category': 'general',
                'icon': '🌤️',
                'title': 'Pleasant Weather',
                'message': f'Perfect {temp}°C weather! Great for outdoor activities. Natural ventilation recommended. Minimal AC needed.',
                'priority': 'low',
                'savings': '₹300-500/day'
            })
        
        # Cool weather (<22°C) - Winter/Hill stations
        elif temp < 22:
            if temp < 10:
                recommendations.append({
                    'type': 'info',
                    'category': 'health',
                    'icon': '🧥',
                    'title': 'Cold Weather',
                    'message': f'Temperature {temp}°C. Dress in layers. Protect extremities. Warm beverages help. Check on elderly family members.',
                    'priority': 'medium',
                    'savings': None
                })
            else:
                recommendations.append({
                    'type': 'info',
                    'category': 'general',
                    'icon': '🌬️',
                    'title': 'Cool Weather',
                    'message': f'Pleasant {temp}°C weather. Perfect for outdoor activities. Natural ventilation sufficient. Heating may be needed at night.',
                    'priority': 'low',
                    'savings': None
                })
        
        return recommendations
    
    @staticmethod
    def get_monsoon_recommendations(weather_data, user_role):
        """Get monsoon-specific recommendations"""
        recommendations = []
        monsoon_intensity = weather_data.get('monsoon_intensity', 'none')
        humidity = weather_data.get('humidity', 50)
        weather_condition = weather_data.get('weather_condition', '')
        
        if monsoon_intensity == 'heavy':
            recommendations.extend([
                {
                    'type': 'warning',
                    'category': 'health',
                    'icon': '🌧️',
                    'title': 'Heavy Monsoon Alert',
                    'message': 'Heavy rainfall expected. Avoid waterlogged areas. Boil drinking water. Watch for mosquito breeding. Keep emergency supplies ready.',
                    'priority': 'high',
                    'savings': None
                },
                {
                    'type': 'info',
                    'category': 'automation',
                    'icon': '🏠',
                    'title': 'Monsoon Home Protection',
                    'message': 'Auto-close windows and awnings. Activate dehumidifiers. Check drainage systems. Protect electronics from moisture.',
                    'priority': 'high',
                    'savings': None
                }
            ])
        
        elif monsoon_intensity == 'moderate':
            recommendations.append({
                'type': 'info',
                'category': 'health',
                'icon': '☔',
                'title': 'Moderate Rainfall',
                'message': 'Carry umbrella. Wear waterproof footwear. Drive carefully. Increase vitamin C intake to prevent infections.',
                'priority': 'medium',
                'savings': None
            })
        
        elif monsoon_intensity == 'pre_monsoon' and humidity > 85:
            recommendations.append({
                'type': 'info',
                'category': 'health',
                'icon': '🌫️',
                'title': 'Pre-Monsoon Humidity',
                'message': f'Very high humidity {humidity}%. Monsoon approaching. Prepare rain gear. Service AC and drainage. Stock medicines.',
                'priority': 'medium',
                'savings': None
            })
        
        return recommendations
    
    @staticmethod
    def get_air_quality_recommendations(weather_data, user_role):
        """Get air quality recommendations for Indian cities"""
        recommendations = []
        aqi = weather_data.get('air_quality_index', 3)
        city = weather_data.get('city', '').lower()
        dust_storm_risk = weather_data.get('dust_storm_risk', 'low')
        
        # Severe air pollution (AQI 4-5)
        if aqi >= 4:
            recommendations.extend([
                {
                    'type': 'danger',
                    'category': 'health',
                    'icon': '😷',
                    'title': 'SEVERE AIR POLLUTION',
                    'message': 'AQI is hazardous. Wear N95 masks outdoors. Avoid morning walks. Use air purifiers indoors. Limit outdoor activities for children and elderly.',
                    'priority': 'critical',
                    'savings': None
                },
                {
                    'type': 'warning',
                    'category': 'automation',
                    'icon': '🌪️',
                    'title': 'Air Purification Mode',
                    'message': 'Activate all air purifiers. Close windows. Use HEPA filters. Avoid outdoor drying of clothes.',
                    'priority': 'high',
                    'savings': None
                }
            ])
        
        # Moderate pollution (AQI 3)
        elif aqi == 3:
            recommendations.append({
                'type': 'warning',
                'category': 'health',
                'icon': '🌫️',
                'title': 'Moderate Air Pollution',
                'message': 'Air quality is moderate. Sensitive people should limit outdoor activities. Consider masks for morning exercise.',
                'priority': 'medium',
                'savings': None
            })
        
        # Dust storm risk
        if dust_storm_risk == 'high':
            recommendations.append({
                'type': 'danger',
                'category': 'health',
                'icon': '🌪️',
                'title': 'DUST STORM WARNING',
                'message': 'High dust storm risk. Stay indoors. Close all windows. Cover water tanks. Avoid driving. Protect eyes and respiratory system.',
                'priority': 'critical',
                'savings': None
            })
        elif dust_storm_risk == 'moderate':
            recommendations.append({
                'type': 'warning',
                'category': 'health',
                'icon': '💨',
                'title': 'Dust Storm Possible',
                'message': 'Moderate dust storm risk. Keep windows closed. Carry protective gear if going out. Check air filters.',
                'priority': 'medium',
                'savings': None
            })
        
        return recommendations
    
    @staticmethod
    def get_uv_recommendations(weather_data, user_role):
        """Get UV protection recommendations for Indian climate"""
        recommendations = []
        uv_index = weather_data.get('uv_index', 5)
        
        if uv_index >= 11:
            recommendations.append({
                'type': 'danger',
                'category': 'health',
                'icon': '☀️',
                'title': 'EXTREME UV RADIATION',
                'message': f'UV Index {uv_index} is extreme. AVOID sun 10 AM - 4 PM. Use SPF 50+ sunscreen every hour. Wear full-sleeve clothes, hat, sunglasses.',
                'priority': 'critical',
                'savings': None
            })
        elif uv_index >= 8:
            recommendations.append({
                'type': 'warning',
                'category': 'health',
                'icon': '🕶️',
                'title': 'Very High UV Radiation',
                'message': f'UV Index {uv_index} is very high. Use SPF 30+ sunscreen. Seek shade 11 AM - 3 PM. Wear protective clothing.',
                'priority': 'high',
                'savings': None
            })
        elif uv_index >= 6:
            recommendations.append({
                'type': 'info',
                'category': 'health',
                'icon': '🧴',
                'title': 'High UV Radiation',
                'message': f'UV Index {uv_index} is high. Apply SPF 30 sunscreen. Wear sunglasses and hat. Limit midday sun exposure.',
                'priority': 'medium',
                'savings': None
            })
        
        return recommendations
    
    @staticmethod
    def get_role_specific_recommendations(weather_data, user_role):
        """Get role-specific recommendations for Indian context"""
        recommendations = []
        temp = weather_data.get('temperature', 25)
        humidity = weather_data.get('humidity', 50)
        aqi = weather_data.get('air_quality_index', 3)
        
        if user_role == 'athlete':
            if temp > 35:
                recommendations.append({
                    'type': 'warning',
                    'category': 'health',
                    'icon': '🏃‍♂️',
                    'title': 'Exercise Safety Alert',
                    'message': f'Temperature {temp}°C too hot for outdoor training. Exercise indoors 5-7 AM or after 7 PM. Hydrate 500ml before, 250ml every 15 min during exercise.',
                    'priority': 'high',
                    'savings': None
                })
            elif temp > 30 and humidity > 70:
                recommendations.append({
                    'type': 'info',
                    'category': 'health',
                    'icon': '💪',
                    'title': 'Modified Training Schedule',
                    'message': 'Hot and humid conditions. Reduce intensity by 20%. Exercise in shaded areas. Monitor heart rate closely.',
                    'priority': 'medium',
                    'savings': None
                })
        
        elif user_role == 'elderly':
            if temp > 35 or aqi >= 4:
                recommendations.append({
                    'type': 'danger',
                    'category': 'health',
                    'icon': '👴',
                    'title': 'Elderly Safety Alert',
                    'message': 'Extreme conditions dangerous for elderly. Stay indoors with AC. Drink water regularly. Have emergency contacts ready. Monitor for heat exhaustion.',
                    'priority': 'critical',
                    'savings': None
                })
        
        elif user_role == 'patient':
            if aqi >= 4:
                recommendations.append({
                    'type': 'danger',
                    'category': 'health',
                    'icon': '🏥',
                    'title': 'Patient Health Alert',
                    'message': 'Poor air quality dangerous for chronic conditions. Use prescribed inhalers. Avoid outdoor activities. Monitor symptoms closely.',
                    'priority': 'critical',
                    'savings': None
                })
        
        return recommendations
