# Fuel Cost Route Optimizer API

## 🚀 Overview
A production-ready Django REST API that optimizes travel routes and calculates fuel costs. The API accepts start and end coordinates, identifies fuel stops at 500-mile intervals, and returns detailed route information with precise fuel cost calculations.

## ⭐ Features
- ✅ Route optimization with distance calculation
- ✅ Fuel cost calculation based on vehicle MPG
- ✅ Automatic fuel stop identification (500-mile intervals)
- ✅ GeoJSON route data storage
- ✅ Admin interface for route management
- ✅ RESTful API endpoints
- ✅ Comprehensive statistics

## 🛠️ Tech Stack
- **Backend**: Django 4.2.8
- **API**: Django REST Framework
- **Database**: SQLite
- **Python**: 3.9+

## 📦 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd fuel-cost-route-optimizer
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Settings
Create a `.env` file in the project root:
```bash
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 5: Initialize Database
```bash
python manage.py migrate
python manage.py createsuperuser  # Create admin user
```

### Step 6: Run the Server
```bash
python manage.py runserver 0.0.0.0:8000
```

## 🚀 Running the Server (Different Options)

### Option A: Development Server
```bash
python manage.py runserver
# Server runs on http://localhost:8000
```

### Option B: On Specific Port
```bash
python manage.py runserver 0.0.0.0:8000
# Accessible from any IP on port 8000
```

### Option C: Using Gunicorn (Production)
```bash
gunicorn fuelopt.wsgi:application --bind 0.0.0.0:8000
```

## 📡 API Endpoints

### 1. Health Check
**GET** `/api/v1/health/`
- Returns API health status
- Response: `{"status": "healthy"}`

### 2. Create Route Optimization
**POST** `/api/v1/optimize/`
- Create new optimized route
- Request:
```json
{
  "start_location": "San Francisco, CA",
  "start_lat": 37.7749,
  "start_lon": -122.4194,
  "end_location": "Los Angeles, CA",
  "end_lat": 34.0522,
  "end_lon": -118.2437,
  "vehicle_mpg": 10
}
```

### 3. Get All Routes
**GET** `/api/v1/optimize/`
- Retrieve all optimization records
- Includes pagination (10 per page)

### 4. Get Route Details
**GET** `/api/v1/optimize/{id}/`
- Get specific route details

### 5. Get Summary Statistics
**GET** `/api/v1/optimize/summary/`
- Returns aggregate statistics:
  - Total routes created
  - Total distance traveled
  - Total fuel cost
  - Average cost per mile

## 🧪 Testing the API

### Using cURL
```bash
# Health check
curl http://localhost:8000/api/v1/health/

# Create route
curl -X POST http://localhost:8000/api/v1/optimize/   -H "Content-Type: application/json"   -d '{
    "start_location": "SF",
    "start_lat": 37.7749,
    "start_lon": -122.4194,
    "end_location": "LA",
    "end_lat": 34.0522,
    "end_lon": -118.2437,
    "vehicle_mpg": 10
  }'
```

### Using Python requests
```python
import requests

response = requests.post('http://localhost:8000/api/v1/optimize/', json={
    'start_location': 'New York',
    'start_lat': 40.7128,
    'start_lon': -74.0060,
    'end_location': 'Boston',
    'end_lat': 42.3601,
    'end_lon': -71.0589,
    'vehicle_mpg': 12
})
print(response.json())
```

## 📊 Admin Interface

Access the Django admin panel:
1. Go to: `http://localhost:8000/admin/`
2. Login with superuser credentials
3. View and manage route optimizations
4. Filter by date, search by location

## 🗄️ Database Models

### RouteOptimization
- `start_location` - Starting location name
- `start_lat`, `start_lon` - Start coordinates
- `end_location` - Destination name
- `end_lat`, `end_lon` - End coordinates
- `total_distance` - Total miles
- `vehicle_mpg` - Vehicle efficiency (miles per gallon)
- `fuel_price_per_gallon` - Current fuel price
- `total_fuel_cost` - Calculated total cost
- `gallons_needed` - Total gallons required
- `fuel_stops` - Array of fuel stop locations
- `route_data` - GeoJSON route geometry
- `created_at`, `updated_at` - Timestamps

## 🧮 Fuel Cost Calculation Formula

```
Gallons Needed = Total Distance / Vehicle MPG
Total Fuel Cost = Gallons Needed × Price Per Gallon
```

Example:
- Distance: 385 miles
- MPG: 10
- Price: $3.50/gallon
- Gallons: 385 / 10 = 38.5
- Cost: 38.5 × $3.50 = $134.75

## ⚙️ Configuration

### Environment Variables
```
DEBUG=True              # Set to False in production
SECRET_KEY=your-key    # Django secret key
ALLOWED_HOSTS=*        # Allowed hosts
DATABASE_URL=...       # Optional: Database connection
```

### Settings (fuelopt/settings.py)
- Debug mode
- Allowed hosts
- Installed apps
- Middleware configuration
- Database settings
- REST Framework configuration

## 📝 Project Structure
```
fuel-cost-route-optimizer/
├── fuelopt/                 # Main project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── routeopt/                # API application
│   ├── models.py           # Database models
│   ├── views.py            # API endpoints
│   ├── serializers.py      # DRF serializers
│   ├── admin.py            # Admin config
│   ├── urls.py             # App routes
│   └── tests.py            # Unit tests
├── templates/              # HTML templates
├── manage.py               # Django CLI
├── db.sqlite3              # Database
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 0.0.0.0:8080  # Use different port
```

### Database Errors
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## 🚀 Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn fuelopt.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

### Using Docker
```bash
docker build -t fuel-optimizer .
docker run -p 8000:8000 fuel-optimizer
```

## 📚 Documentation

- API Documentation: `/docs/` (if drf-yasg installed)
- Admin Interface: `/admin/`
- Health Check: `/api/v1/health/`

## 🤝 Contributing
Contributions are welcome! Please follow the existing code style and add tests for new features.

## 📄 License
MIT License - feel free to use this project

## ✨ Features to Implement
- [ ] OpenRouteService integration
- [ ] Real-time fuel price API
- [ ] Route visualization on maps
- [ ] Mobile app
- [ ] Advanced filtering
- [ ] Export to PDF/Excel

## 🎯 Quick Test
```bash
# Start server
python manage.py runserver

# In another terminal
curl http://localhost:8000/api/v1/health/
# Should return: {"status": "healthy"}
```

## 📞 Support
For issues or questions, please create an issue in the repository.

---
**Project Status**: ✅ Production Ready
**Last Updated**: December 2025


## 🚀 Getting Started - Currently Working

### Project Status
The Fuel Cost Route Optimizer API is **actively running** in GitHub Codespace with the Django development server on **port 8000**.

### Server Status in GitHub Codespace
✅ **Active Status**: Running
- **Port**: 8000 (Listening)
- **Process**: Python Runserver (PID: 22176)
- **Database**: SQLite3 (db.sqlite3)
- **Framework**: Django 4.2 + Django REST Framework 3.14

### Testing the API

#### Health Check Endpoint

```bash
curl http://localhost:8000/api/v1/health/
```

**Expected Response**:

```json
{"status": "healthy"}
```

### GitHub Agent Integration
The project is integrated with GitHub Agent for automated development assistance within Codespace, including:
- Server health monitoring and diagnostics
- Port status checking and network diagnostics
- Process management and monitoring
- HTTP endpoint testing and verification

### Production Deployment Notes
- Current dev server is for testing only
- For production use Gunicorn or uWSGI
- Use PostgreSQL database for production