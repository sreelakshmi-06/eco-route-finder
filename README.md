# ECO ROUTE FINDER 🎯


## Basic Details
### Team Name: Sreelakshmi S K


### Team Members
- Member 1: [Name] - [College]
- Member 2: [Name] - [College]
- Member 3: [Name] - [College]

### Hosted Project Link
[mention your project hosted project link here]

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

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Team](Add photo of your team here)


![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub
