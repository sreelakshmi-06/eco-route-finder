from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

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

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
