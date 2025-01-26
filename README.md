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
