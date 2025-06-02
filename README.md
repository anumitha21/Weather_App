# Weather Health Advisor - Enhanced Smart Home Edition

A comprehensive Django-based web application that provides personalized weather-based health recommendations, smart home automation, and energy optimization for different user types including athletes, patients, elderly individuals, healthcare providers, pharmacists, and the general public.

## 🚀 **MAJOR ENHANCEMENTS - NEW FEATURES**

### 📍 **Global Location Management**
- **Manual Location Selection**: Search and select any city worldwide
- **Saved Locations**: Save favorite locations for quick access
- **Real-time Weather**: Live weather data for any selected location
- **Location-based Automation**: Smart home rules based on location weather

### 🏠 **Smart Home Automation**
- **Device Management**: Register and control smart thermostats, AC units, lights, curtains, and more
- **Weather-based Automation**: Automatic device control based on weather conditions
- **Energy Optimization**: Intelligent energy saving with cost reduction
- **Real-time Control**: Manual override and instant device control

### 💡 **Enhanced Recommendations**
- **Detailed Health Advice**: Specific actionable recommendations for all weather conditions
- **Energy Saving Tips**: Real-time cost reduction suggestions with savings estimates
- **Smart Home Integration**: Automated device suggestions based on weather
- **Peak Hour Optimization**: Electricity cost optimization during peak hours

## 🌟 Features

### Multi-Role Support
- **Athletes/Sports Enthusiasts**: Smart workout planning, route optimization, UV monitoring
- **Patients (Chronic Conditions)**: Health forecasts, air quality alerts, medication reminders
- **Elderly/Vulnerable Adults**: Safety alerts, fall prevention, simplified interface
- **Healthcare Providers**: Patient risk dashboard, appointment scheduling insights
- **Pharmacists**: Inventory forecasting, demand predictions, supply chain alerts
- **General Public**: All-in-one dashboard, energy tips, emergency alerts

### Core Functionality
- **Real-time Weather Data**: Current weather conditions with API integration
- **Historical Weather Calendar**: Navigate through past weather data (demo data for previous days)
- **Health Recommendations Engine**: Personalized advice based on weather and user profile
- **MongoDB Integration**: User profiles and additional data storage
- **Responsive Design**: Mobile-first approach with professional UI
- **Role-based Dashboard**: Customized interface for each user type

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 4.2.7
- MongoDB (optional - falls back to demo data)

### Installation

1. **Clone and Setup**
   ```bash
   cd "d:\final python project for semester"
   pip install -r requirements.txt
   ```

2. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Demo Users**
   ```bash
   python create_demo_users.py
   ```

4. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

6. **Run Server**
   ```bash
   python manage.py runserver
   ```

7. **Access Application**
   Open http://127.0.0.1:8000 in your browser

## 👥 Demo Accounts

The application comes with pre-created demo accounts for testing:

| Username | Password | Role | Description |
|----------|----------|------|-------------|
| `athlete_demo` | `demo123` | Athlete | Sports enthusiast with workout recommendations |
| `patient_demo` | `demo123` | Patient | Chronic conditions (asthma, diabetes) |
| `elderly_demo` | `demo123` | Elderly | Senior citizen with safety alerts |
| `doctor_demo` | `demo123` | Doctor | Healthcare provider dashboard |
| `pharmacist_demo` | `demo123` | Pharmacist | Inventory and demand insights |
| `public_demo` | `demo123` | Public | General user with basic features |

## 🏗️ Project Structure

```
weather_health_app/
├── authentication/          # User management and authentication
├── dashboard/              # Main dashboard and calendar views
├── weather/               # Weather data and recommendations
├── templates/             # HTML templates
├── static/               # CSS, JavaScript, images
├── weather_health_app/   # Main project settings
└── requirements.txt      # Python dependencies
```

## 🔧 Configuration

### Environment Variables (.env)
```env
# Weather API Configuration
WEATHER_API_KEY=your_openweather_api_key_here
WEATHER_API_URL=https://api.openweathermap.org/data/2.5

# MongoDB Configuration (optional)
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/weather_health_db
MONGODB_DB_NAME=weather_health_db

# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Weather API Setup
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Update the `WEATHER_API_KEY` in your `.env` file
3. The app will fall back to demo data if no API key is provided

### MongoDB Setup (Optional)
1. Create a MongoDB Atlas account or use local MongoDB
2. Update the `MONGODB_URI` in your `.env` file
3. The app works with SQLite by default and uses MongoDB for additional features

## 📱 User Interface

### Login Page
- Clean, professional design with weather-themed animations
- Quick demo account selection
- Responsive layout for all devices

### Dashboard
- Role-specific interface with personalized recommendations
- Real-time weather data display
- Health and energy tips based on current conditions
- Quick access to calendar and profile

### Calendar View
- Interactive calendar with weather history
- Click on any date to view detailed weather information
- Demo data for previous days, real data for current day
- Smooth animations and transitions

### Profile Management
- User information display
- MongoDB synchronization status
- Account statistics and quick actions

## 🎨 Design Features

### Visual Elements
- **Weather-themed color scheme**: Sky blues, sun yellows, leaf greens
- **Animated weather icons**: Floating animations for visual appeal
- **Role-based badges**: Color-coded user role indicators
- **Gradient backgrounds**: Modern glass-morphism effects
- **Responsive cards**: Hover effects and smooth transitions

### Accessibility
- **Large text options**: Especially for elderly users
- **High contrast mode**: Better visibility
- **Keyboard navigation**: Full accessibility compliance
- **Screen reader support**: Semantic HTML structure

## 🔍 Technical Details

### Backend
- **Django 4.2.7**: Web framework
- **SQLite**: Primary database for user data
- **MongoDB**: Additional data storage (optional)
- **Weather API**: Real-time weather data
- **Custom User Model**: Extended user profiles

### Frontend
- **Bootstrap 5.3**: Responsive CSS framework
- **jQuery**: JavaScript interactions
- **Font Awesome**: Icon library
- **Custom CSS**: Weather-themed styling
- **Progressive Enhancement**: Works without JavaScript

### Security
- **CSRF Protection**: All forms protected
- **User Authentication**: Secure login/logout
- **Input Validation**: Server and client-side validation
- **SQL Injection Prevention**: Django ORM protection

## 🌡️ Weather Features

### Current Weather
- Temperature, humidity, wind speed
- Weather description and icons
- UV index and air quality
- Pressure and visibility

### Historical Data
- Past 30 days of weather data (demo)
- Consistent data generation for testing
- Calendar navigation interface

### Health Recommendations
- Role-specific advice based on weather
- Condition-specific alerts (asthma, arthritis, etc.)
- Energy-saving tips
- Safety warnings for extreme weather

## 🚀 Deployment

### Development
The application is ready to run in development mode with:
```bash
python manage.py runserver
```

### Production Considerations
- Set `DEBUG=False` in production
- Use a production database (PostgreSQL recommended)
- Configure static file serving
- Set up proper MongoDB connection
- Use environment variables for sensitive data

## 🤝 Contributing

This is a semester project for educational purposes. The application demonstrates:
- Django web development
- MongoDB integration
- Weather API usage
- Responsive web design
- User role management
- Health recommendation systems

## 📄 License

This project is created for educational purposes as part of a Python semester project.

## 🆘 Troubleshooting

### Common Issues

1. **MongoDB Connection Failed**
   - This is normal if MongoDB is not configured
   - The app will work with SQLite and demo data

2. **Weather API Errors**
   - Check your API key in `.env` file
   - The app falls back to demo weather data

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic --noinput`
   - Check `STATIC_URL` and `STATICFILES_DIRS` in settings

4. **Migration Errors**
   - Delete `db.sqlite3` and migration files
   - Run `python manage.py makemigrations` and `python manage.py migrate`

## 📞 Support

For issues or questions about this educational project, please refer to the Django documentation or create an issue in the project repository.

---

**Built with ❤️ using Django and MongoDB for Weather Health Advisory**
