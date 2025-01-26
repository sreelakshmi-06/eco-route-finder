# ECO ROUTE FINDER 🎯

## Basic Details
### Team Name: Sreelakshmi S K
College-Marian Engineering College

### Hosted Project Link
https://github.com/sreelakshmi-06/eco-route-finder

### Project Description
Eco route finder is a web application which promotes eco-travel by helping users to identify routes and modes of transportation with minimal ecological impact.This application integrates live route data,user preferences and eco-metrics to recommend travel option that reduce carbon footprints while maintaining convenience.

### The Problem statement
Eco-anxiety for indecisive traveler

### The Solution
I'm trying to solve this problem by creating an Eco-route
The key features and their implementation are as follows:
1. User Preferences
User preferences are the settings or choices that allow the system to tailor the eco route recommendations to individual users. These preferences help ensure the routes and metrics provided are relevant and useful.

Key User Preferences:
Vehicle Type:
Users can select their vehicle type (e.g., electric, hybrid, gasoline, diesel, bicycle).
This affects the calculation of fuel efficiency, emissions, and charging/fueling station recommendations.
Fuel Efficiency:
Users can input their vehicle's fuel efficiency (e.g., miles per gallon or kWh per mile).
This data is used to calculate fuel consumption and emissions for different routes.
Priority Settings:
Users can choose their priorities, such as:
Fastest Route: Minimize travel time.
Shortest Route: Minimize distance.
Eco-Friendly Route: Minimize carbon emissions and fuel consumption.
Scenic Route: Prioritize routes with natural beauty or less urban congestion.
Charging/Fueling Needs:
For electric vehicles, users can specify their battery range and preferred charging networks.
For traditional vehicles, users can indicate if they need fueling stations along the route.
Avoidance Preferences:
Users can specify areas or road types to avoid (e.g., toll roads, highways, or congested urban areas).
Accessibility Needs:
Users with disabilities or special needs can specify requirements like wheelchair-accessible routes or minimal elevation changes.
Implementation:
Create a user profile or settings page where users can input and update their preferences.
Use these preferences to filter and customize route recommendations.

2. Routes
Routes are the paths suggested by the system based on user preferences and real-time data. The goal is to provide the most eco-friendly and efficient options.

Key Features of Routes:
Eco-Friendly Route Calculation:
Use AI/ML algorithms to analyze factors like:
Traffic: Avoid congested areas to reduce idling and emissions.
Elevation: Prioritize flatter routes to save fuel
Road Quality: Suggest smoother roads to improve fuel efficiency.
Distance: Balance shorter distances with other eco-friendly factors.
Multi-Modal Routes:
Combine different modes of transportation (e.g., driving to a train station, then taking public transit).
Encourage the use of bicycles or walking for shorter segments.
Real-Time Adjustments:
Update routes dynamically based on real-time traffic, weather, and road conditions.
Charging/Fueling Stops:
For electric vehicles, include charging stations along the route.
For traditional vehicles, suggest eco-friendly fueling options (e.g., biofuel stations).
Scenic and Low-Stress Routes:
Offer routes that are not only eco-friendly but also pleasant and less stressful for drivers.

Implementation:
Use mapping APIs (e.g., Google Maps, OpenStreetMap) to generate and display routes.
Integrate AI/ML models to optimize routes based on user preferences and real-time data.
Provide multiple route options with clear comparisons (e.g., time, distance, emissions).

3. Eco-Metrics
Eco-metrics are the quantitative measurements that help users understand the environmental impact of their chosen routes. These metrics empower users to make informed decisions.

Key Eco-Metrics:
Carbon Footprint:
Estimate the total CO2 emissions for a route based on:
Vehicle type and fuel efficiency.
Distance traveled.
Traffic conditions and elevation changes.
Display the carbon footprint in kilograms or tons of CO2.
Fuel Consumption:
Calculate the amount of fuel (or energy for EVs) required for the route.
Show savings compared to traditional routes.
Emission Savings:
Highlight the reduction in emissions when choosing an eco route over a conventional route.
Compare the eco route to the average emissions for similar trips.
Cost Savings:
Estimate the monetary savings from reduced fuel consumption.
Include potential savings from avoiding tolls or congestion charges.
Health Impact:
Provide data on how the eco route contributes to better air quality and public health.
For example, estimate the reduction in particulate matter (PM2.5) and nitrogen oxides (NOx).

Implementation:
Develop a backend system to calculate eco-metrics based on user inputs and route data.
Use standardized formulas for emissions and fuel consumption (e.g., EPA or DEFRA guidelines).
Display metrics in a user-friendly dashboard with visualizations like charts, graphs, and comparisons.

## Technical Details
### Technologies/Components Used
For Software:
- Languages used-Python, HTML
- Frameworks used-flask
- Libraries used-flask libraries,database libraries
- Tools used-Visual Studio Code,SQLite,Git/Github,Browser developer tools,Python virtual environment(venv)

For Hardware:
-  main components-Development machine,Network connectivity
-  specifications-Development Machine:
Processor: Minimum Intel i5 or equivalent (dual-core or better recommended).
RAM: At least 8 GB (16 GB recommended for smoother multitasking).
Storage: 500 MB to 1 GB free space for project files and dependencies.
Operating System: Windows 10/11, macOS, or Linux.
Display: 1080p resolution or higher (optional for comfortable UI testing).

- List tools required-Development Tools:

Visual Studio Code: For writing and debugging code.
SQLite CLI or MySQL Workbench: For database setup and query testing.
Postman: For API testing.
Git: For version control.
Testing Tools:

Browser Developer Tools: Chrome, Firefox, or Edge DevTools for frontend debugging.
Mobile Device/Emulator: To test responsiveness on mobile screens.


### Implementation
For Software:
# Installation
Installation
Clone the Repository: Use Git to clone the project repository:

bash
Copy
Edit
git clone https://github.com/your-repo-name/eco-route.git
cd eco-route
Set Up a Virtual Environment: Create and activate a virtual environment to isolate project dependencies:

bash
Copy
Edit
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install Dependencies: Install the required Python packages listed in requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Set Up the Database:

For SQLite: The database will be automatically created when running the app.
For MySQL: Update the database connection details in your configuration file (app.py or a separate config file):
python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/database_name"
Migrate the Database: Use Flask-Migrate or SQLAlchemy to initialize the database:

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade


# Run
Run the Application
Start the Flask Server: Run the application locally:

bash
Copy
Edit
python app.py
Access the Application: Open your browser and navigate to:

arduino
Copy
Edit
http://127.0.0.1:5000
Stop the Server: Press Ctrl + C in the terminal to stop the Flask development server.



### Project Documentation
For Software:
Folder Structure:
csharp
Copy
Edit
eco-route/
├── app.py               # Main application file
├── templates/           # HTML templates
│   ├── index.html       # Homepage
│   ├── result.html      # Results page
├── static/              # Static files (CSS, JS, images)
├── models.py            # Database models
├── requirements.txt     # Project dependencies
├── migrations/          # Database migration files
├── venv/                # Virtual environment
└── README.md            # Project documentation
API Endpoints
GET /: Displays the homepage.
POST /route: Accepts user input for route preferences and returns recommended routes.
GET /metrics: Returns user eco-metrics in JSON format.
Configuration
Set environment variables:
bash
Copy
Edit
export FLASK_APP=app.py
export FLASK_ENV=development
Testing
Run unit tests using pytest:
bash
Copy
Edit
pytest

# Diagrams
Workflow/Architecture
1. User Interaction
Users interact with the web application through the frontend (HTML/CSS/JavaScript).
They submit preferences, such as the mode of transport and destination.
2. Backend Processing
The backend, built with Flask, handles the user request and:
Processes input data.
Fetches or calculates route options using algorithms based on eco-metrics (e.g., emissions, distance, time).
3. Database Operations
User data, preferences, routes, and eco-metrics are stored and retrieved from the database (SQLite or MySQL).
The backend uses SQLAlchemy ORM for seamless database interaction.
4. Eco-Metrics Calculation
Based on route data, the backend computes eco-metrics like carbon savings, fuel efficiency, and alternative route comparisons.
This data is dynamically prepared for presentation.
5. Frontend Response
The backend sends route options and eco-metrics to the frontend via API responses.
The frontend renders these options, highlighting the most eco-friendly routes with visuals (charts, icons).
6. Feedback Loop
Users can update preferences or provide feedback on routes.
The system refines suggestions over time based on user patterns and input.
Components in the Architecture
Frontend:

Browser: Displays the app to users.
Static Files: HTML, CSS, JavaScript.
Backend:

Flask Framework: Handles routing, API creation, and business logic.
Database:

SQLite/MySQL: Stores user preferences, route data, and metrics.
Optional Components:

External APIs: For live traffic or route data (e.g., Google Maps API).
Visualization Libraries: Like Chart.js for eco-metrics presentation.





Made with ❤️ at TinkerHub
