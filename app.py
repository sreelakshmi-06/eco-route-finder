from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_routes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    vehicle_type = db.Column(db.String(50), nullable=False)
    fuel_efficiency = db.Column(db.Float, nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    avoid_tolls = db.Column(db.Boolean, default=False)
    avoid_highways = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Route(db.Model):
    __tablename__ = 'routes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_location = db.Column(db.String(255), nullable=False)
    end_location = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    route_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', backref=db.backref('routes', lazy=True))

class EcoMetrics(db.Model):
    __tablename__ = 'eco_metrics'
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'), nullable=False)
    carbon_footprint = db.Column(db.Float, nullable=False)
    fuel_consumption = db.Column(db.Float, nullable=False)
    cost_savings = db.Column(db.Float, nullable=False)
    emission_savings = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    route = db.relationship('Route', backref=db.backref('eco_metrics', lazy=True))

# Create Tables
@app.before_request
def create_tables():
    db.create_all()

# Homepage Route
@app.route('/')
def home():
    return render_template("index.html")

# Route Optimization Page
@app.route('/route', methods=['POST'])
def route():
    start = request.form.get('start')
    end = request.form.get('end')
    
    # Simulate route data
    eco_distance = round(random.uniform(10, 50), 2)  # Example: random distance in km
    eco_time = round(random.uniform(15, 120), 2)     # Example: random time in minutes
    co2_savings = round(random.uniform(1, 5), 2)     # Example: random CO2 savings in kg
    
    result = {
        "start": start,
        "end": end,
        "eco_distance": eco_distance,
        "eco_time": eco_time,
        "co2_savings": co2_savings
    }
    
    return f'''
    <h1>Eco Route Details</h1>
    <p><strong>From:</strong> {result['start']}</p>
    <p><strong>To:</strong> {result['end']}</p>
    <p><strong>Eco Distance:</strong> {result['eco_distance']} km</p>
    <p><strong>Eco Time:</strong> {result['eco_time']} minutes</p>
    <p><strong>CO2 Savings:</strong> {result['co2_savings']} kg</p>
    <a href="/">Back to Home</a>
    '''

# API Endpoints
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    user = User(
        username=data["username"],
        vehicle_type=data["vehicle_type"],
        fuel_efficiency=data["fuel_efficiency"],
        priority=data["priority"],
        avoid_tolls=data.get("avoid_tolls", False),
        avoid_highways=data.get("avoid_highways", False)
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added", "user_id": user.id})

@app.route("/add_route", methods=["POST"])
def add_route():
    data = request.json
    route = Route(
        user_id=data["user_id"],
        start_location=data["start_location"],
        end_location=data["end_location"],
        distance=data["distance"],
        duration=data["duration"],
        route_type=data["route_type"]
    )
    db.session.add(route)
    db.session.commit()
    return jsonify({"message": "Route added", "route_id": route.id})

@app.route("/get_user_routes/<int:user_id>", methods=["GET"])
def get_user_routes(user_id):
    routes = Route.query.filter_by(user_id=user_id).all()
    route_list = [
        {
            "start_location": route.start_location,
            "end_location": route.end_location,
            "distance": route.distance,
            "duration": route.duration,
            "route_type": route.route_type
        }
        for route in routes
    ]
    return jsonify(route_list)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)