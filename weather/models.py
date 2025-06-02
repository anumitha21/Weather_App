from django.db import models
from weather_health_app.mongodb import get_collection
from datetime import datetime, timedelta
import random
import json

class WeatherService:
    """Service class for weather data management"""

    @staticmethod
    def get_current_weather(city="London"):
        """Get current weather data from API or demo data"""
        try:
            import requests
            from django.conf import settings

            # Try to get real weather data
            if settings.WEATHER_API_KEY != 'demo_key':
                url = f"{settings.WEATHER_API_URL}/weather"
                params = {
                    'q': city,
                    'appid': settings.WEATHER_API_KEY,
                    'units': 'metric'
                }
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    return WeatherService._format_weather_data(data)

            # Fallback to demo data
            return WeatherService._get_demo_current_weather(city)

        except Exception as e:
            print(f"Error fetching weather: {e}")
            return WeatherService._get_demo_current_weather(city)

    @staticmethod
    def _format_weather_data(api_data):
        """Format API weather data with enhanced Indian climate support"""
        # Extract basic weather data
        weather_data = {
            'city': api_data.get('name', 'Unknown'),
            'country': api_data.get('sys', {}).get('country', 'Unknown'),
            'temperature': round(api_data.get('main', {}).get('temp', 20)),
            'feels_like': round(api_data.get('main', {}).get('feels_like', 20)),
            'humidity': api_data.get('main', {}).get('humidity', 50),
            'pressure': api_data.get('main', {}).get('pressure', 1013),
            'description': api_data.get('weather', [{}])[0].get('description', 'Clear sky'),
            'icon': api_data.get('weather', [{}])[0].get('icon', '01d'),
            'wind_speed': round(api_data.get('wind', {}).get('speed', 5) * 3.6),  # Convert m/s to km/h
            'wind_direction': api_data.get('wind', {}).get('deg', 180),
            'visibility': api_data.get('visibility', 10000) / 1000,  # Convert to km
            'cloudiness': api_data.get('clouds', {}).get('all', 0),
            'weather_condition': api_data.get('weather', [{}])[0].get('main', 'Clear').lower(),
            'timestamp': datetime.now().isoformat()
        }

        # Add enhanced UV index based on location and conditions
        weather_data['uv_index'] = WeatherService._calculate_uv_index(weather_data)

        # Add enhanced air quality index for Indian cities
        weather_data['air_quality_index'] = WeatherService._calculate_air_quality(weather_data)

        # Add Indian climate specific indicators
        weather_data.update(WeatherService._get_indian_climate_indicators(weather_data))

        return weather_data

    @staticmethod
    def _get_demo_current_weather(city="London"):
        """Generate demo current weather data"""
        weather_conditions = [
            {'desc': 'Clear sky', 'icon': '01d'},
            {'desc': 'Few clouds', 'icon': '02d'},
            {'desc': 'Scattered clouds', 'icon': '03d'},
            {'desc': 'Broken clouds', 'icon': '04d'},
            {'desc': 'Light rain', 'icon': '10d'},
            {'desc': 'Overcast', 'icon': '04d'}
        ]

        condition = random.choice(weather_conditions)
        temp = random.randint(15, 30)

        return {
            'city': city,
            'country': 'Demo',
            'temperature': temp,
            'feels_like': temp + random.randint(-3, 3),
            'humidity': random.randint(40, 80),
            'pressure': random.randint(1000, 1025),
            'description': condition['desc'],
            'icon': condition['icon'],
            'wind_speed': random.randint(2, 15),
            'wind_direction': random.randint(0, 360),
            'visibility': random.randint(5, 15),
            'uv_index': random.randint(1, 11),
            'air_quality_index': random.randint(1, 5),
            'pollen_count': random.randint(1, 5),
            'timestamp': datetime.now().isoformat()
        }

    @staticmethod
    def get_historical_weather(city="London", days_back=7):
        """Get historical weather data (demo data for past days)"""
        historical_data = []

        for i in range(days_back):
            date = datetime.now() - timedelta(days=i+1)

            # Generate consistent demo data based on date
            random.seed(date.day + date.month * 31)

            weather_conditions = [
                {'desc': 'Clear sky', 'icon': '01d'},
                {'desc': 'Few clouds', 'icon': '02d'},
                {'desc': 'Scattered clouds', 'icon': '03d'},
                {'desc': 'Broken clouds', 'icon': '04d'},
                {'desc': 'Light rain', 'icon': '10d'},
                {'desc': 'Overcast', 'icon': '04d'}
            ]

            condition = random.choice(weather_conditions)
            temp = random.randint(12, 28)

            weather_data = {
                'date': date.strftime('%Y-%m-%d'),
                'city': city,
                'temperature': temp,
                'feels_like': temp + random.randint(-3, 3),
                'humidity': random.randint(35, 85),
                'pressure': random.randint(995, 1030),
                'description': condition['desc'],
                'icon': condition['icon'],
                'wind_speed': random.randint(1, 18),
                'wind_direction': random.randint(0, 360),
                'visibility': random.randint(3, 20),
                'uv_index': random.randint(1, 10),
                'air_quality_index': random.randint(1, 5),
                'pollen_count': random.randint(1, 5),
                'timestamp': date.isoformat()
            }

            historical_data.append(weather_data)

        # Reset random seed
        random.seed()
        return historical_data

    @staticmethod
    def save_weather_to_mongodb(weather_data):
        """Save weather data to MongoDB"""
        try:
            collection = get_collection('weather_data')
            if collection is not None:
                weather_data['saved_at'] = datetime.now()
                collection.insert_one(weather_data)
                return True
        except Exception as e:
            print(f"Error saving weather to MongoDB: {e}")
        return False

    @staticmethod
    def get_weather_from_mongodb(city, date=None):
        """Get weather data from MongoDB"""
        try:
            collection = get_collection('weather_data')
            if collection is not None:
                query = {'city': city}
                if date:
                    query['date'] = date
                return collection.find_one(query, sort=[('saved_at', -1)])
        except Exception as e:
            print(f"Error fetching weather from MongoDB: {e}")
        return None

    @staticmethod
    def _calculate_uv_index(weather_data):
        """Calculate UV index based on weather conditions and location"""
        # Base UV index calculation
        base_uv = 6  # Default moderate UV

        # Adjust for cloudiness
        cloudiness = weather_data.get('cloudiness', 0)
        if cloudiness > 80:
            base_uv = max(1, base_uv - 3)  # Heavy clouds
        elif cloudiness > 50:
            base_uv = max(2, base_uv - 2)  # Moderate clouds
        elif cloudiness > 20:
            base_uv = max(3, base_uv - 1)  # Light clouds

        # Adjust for Indian cities (higher UV generally)
        indian_cities = ['mumbai', 'delhi', 'bangalore', 'chennai', 'kolkata', 'hyderabad', 'pune', 'ahmedabad', 'coimbatore']
        city_lower = weather_data.get('city', '').lower()

        if any(indian_city in city_lower for indian_city in indian_cities):
            base_uv = min(11, base_uv + 2)  # Higher UV in Indian cities

        # Adjust for time of day (simplified)
        current_hour = datetime.now().hour
        if 10 <= current_hour <= 16:
            base_uv = min(11, base_uv + 1)  # Peak UV hours
        elif current_hour < 8 or current_hour > 18:
            base_uv = max(1, base_uv - 2)  # Low UV hours

        return max(1, min(11, base_uv))

    @staticmethod
    def _calculate_air_quality(weather_data):
        """Calculate air quality index for Indian cities"""
        # Base AQI
        base_aqi = 3  # Moderate

        # Indian cities typically have higher pollution
        indian_cities = {
            'delhi': 4, 'mumbai': 3, 'kolkata': 4, 'chennai': 3,
            'bangalore': 3, 'hyderabad': 3, 'pune': 3, 'ahmedabad': 4,
            'coimbatore': 2, 'kochi': 2, 'thiruvananthapuram': 2
        }

        city_lower = weather_data.get('city', '').lower()

        # Check for specific Indian cities
        for city, aqi in indian_cities.items():
            if city in city_lower:
                base_aqi = aqi
                break

        # Adjust for weather conditions
        humidity = weather_data.get('humidity', 50)
        wind_speed = weather_data.get('wind_speed', 10)

        # High humidity can trap pollutants
        if humidity > 80:
            base_aqi = min(5, base_aqi + 1)

        # Low wind speed means less dispersion
        if wind_speed < 5:
            base_aqi = min(5, base_aqi + 1)
        elif wind_speed > 15:
            base_aqi = max(1, base_aqi - 1)

        return max(1, min(5, base_aqi))

    @staticmethod
    def _get_indian_climate_indicators(weather_data):
        """Get Indian climate specific indicators"""
        indicators = {}

        temp = weather_data.get('temperature', 25)
        humidity = weather_data.get('humidity', 50)

        # Heat index calculation for Indian climate
        if temp >= 27 and humidity >= 40:
            heat_index = temp + (0.5 * (humidity - 40))
            indicators['heat_index'] = round(heat_index)
        else:
            indicators['heat_index'] = temp

        # Monsoon indicators
        weather_condition = weather_data.get('weather_condition', '')
        humidity_level = weather_data.get('humidity', 50)

        if 'rain' in weather_condition.lower() and humidity_level > 80:
            indicators['monsoon_intensity'] = 'heavy'
        elif 'rain' in weather_condition.lower() and humidity_level > 60:
            indicators['monsoon_intensity'] = 'moderate'
        elif humidity_level > 85:
            indicators['monsoon_intensity'] = 'pre_monsoon'
        else:
            indicators['monsoon_intensity'] = 'none'

        # Comfort level for Indian climate
        if temp > 35:
            indicators['comfort_level'] = 'very_hot'
        elif temp > 30 and humidity > 70:
            indicators['comfort_level'] = 'hot_humid'
        elif temp > 28 and humidity > 80:
            indicators['comfort_level'] = 'uncomfortable'
        elif 22 <= temp <= 28 and 40 <= humidity <= 60:
            indicators['comfort_level'] = 'comfortable'
        elif temp < 15:
            indicators['comfort_level'] = 'cold'
        else:
            indicators['comfort_level'] = 'moderate'

        # Dust storm indicator (common in North India)
        wind_speed = weather_data.get('wind_speed', 0)
        visibility = weather_data.get('visibility', 10)

        if wind_speed > 25 and visibility < 2:
            indicators['dust_storm_risk'] = 'high'
        elif wind_speed > 15 and visibility < 5:
            indicators['dust_storm_risk'] = 'moderate'
        else:
            indicators['dust_storm_risk'] = 'low'

        # Pollen count estimation
        if weather_condition in ['clear', 'sunny'] and wind_speed > 10:
            indicators['pollen_count'] = random.randint(3, 5)
        elif 'rain' in weather_condition:
            indicators['pollen_count'] = random.randint(1, 2)
        else:
            indicators['pollen_count'] = random.randint(2, 4)

        return indicators
