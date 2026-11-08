# AI-Based Smart Van and Route Scheduling System

An AI-powered logistics management web application that automates vehicle, driver, and route scheduling using **Constraint Satisfaction Problem (CSP)** techniques.

The system uses Python and Django for backend management and a custom CSP engine to generate schedules while considering operational constraints such as driver availability, vehicle capacity, maintenance status, fuel range, and overlapping assignments.

## Project Overview

Managing transportation resources manually can lead to scheduling conflicts, inefficient vehicle utilization, and driver workload issues.

This project addresses these challenges through an intelligent scheduling system that manages vans, drivers, routes, and schedules in a centralized web application.

Its AI scheduling engine uses backtracking search and CSP heuristics to find valid assignments while respecting defined constraints.

## Key Features

### 1. AI-Based Scheduling Engine

The project implements a custom Constraint Satisfaction Problem (CSP) solver.

Algorithms and techniques include:

- Backtracking Search
- Minimum Remaining Values (MRV)
- Least Constraining Value (LCV)
- Forward Checking
- Domain Generation
- Constraint Checking

### 2. Van Management

- Add, view, update, and delete vans.
- Maintain vehicle registration numbers.
- Track passenger capacity.
- Track fuel range.
- Monitor vehicle maintenance status.

### 3. Driver Management

- Add and manage drivers.
- Store driver license information.
- Track driver availability.
- Define maximum working hours.

### 4. Route Management

- Create and manage routes.
- Define source and destination.
- Specify route distance.
- Set estimated travel time.
- Specify passenger requirements.
- Assign route priorities.

### 5. Automatic Schedule Generation

The CSP engine evaluates possible combinations of:

- Vans
- Drivers
- Departure times
- Routes

It checks the constraints before accepting an assignment and saves successful schedules in the database.

### 6. Dashboard

The dashboard provides an overview of:

- Total vans
- Total drivers
- Total routes
- Generated schedules
- Vehicles under maintenance

### 7. Modern User Interface

- Responsive dashboard
- Dark-themed interface
- Glassmorphism-inspired design
- Interactive charts
- Smooth animations
- Bootstrap-based layout

## AI Algorithms and Constraints

### Algorithms

| Algorithm | Purpose |
|---|---|
| Backtracking Search | Searches for a valid combination of assignments |
| MRV | Selects the variable with the fewest remaining possible values |
| LCV | Prioritizes values that restrict other variables the least |
| Forward Checking | Removes inconsistent values from remaining domains |
| Degree Heuristic | Helps select constrained variables |

### Hard Constraints

The scheduling engine considers the following restrictions:

1. A driver cannot handle two overlapping routes.
2. A van cannot be assigned to two overlapping routes.
3. Passenger requirements must not exceed vehicle capacity.
4. Drivers must be available.
5. Vehicles under maintenance cannot be assigned.
6. Fuel range must be sufficient for the route.
7. Driver working hours must remain within their defined limit.

### Soft Constraints

The domain-ordering strategy also considers:

- Earlier departure times to reduce passenger waiting.
- Vehicle fuel capacity when ordering possible assignments.
- Efficient resource utilization.

Note: The current implementation uses heuristic ordering to find a valid schedule; it does not guarantee a globally optimal solution.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML5, CSS3, JavaScript |
| UI Framework | Bootstrap 5 |
| Database | SQLite |
| AI Technique | Constraint Satisfaction Problem |
| Search Algorithm | Backtracking |
| Visualization | Chart.js |
| Animations | GSAP |

## Project Architecture

The project follows Django's Model-View-Template (MVT) architecture.

```text
AI-Smart-Logistics-Scheduler/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── logistics/
│   ├── migrations/
│   ├── services/
│   │   └── csp/
│   │       └── solver.py
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── driver_form.html
│   ├── driver_list.html
│   ├── route_form.html
│   ├── route_list.html
│   ├── schedule_list.html
│   ├── van_form.html
│   └── van_list.html
│
├── manage.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── plan.md
```

## Database Models

The system uses four primary Django models:

**Van**
- Vehicle number
- Passenger capacity
- Fuel capacity
- Vehicle status
- Maintenance status

**Driver**
- Name
- License number
- Availability
- Maximum working hours

**Route**
- Source
- Destination
- Distance
- Estimated time
- Passenger count
- Priority

**Schedule**
- Assigned route
- Assigned van
- Assigned driver
- Departure time

## Installation and Setup

### Prerequisites

- Python 3.11 or later
- pip
- Git
- A modern web browser

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-smart-logistics-scheduler.git
```

### 2. Navigate to the Project Folder

```bash
cd ai-smart-logistics-scheduler
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Django

Configure a secure Django secret key using an environment variable rather than committing it to the repository.

For local development, configure the appropriate settings in `core/settings.py`.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your own credentials.

### 9. Start the Development Server

```bash
python manage.py runserver
```

### 10. Open the Application

Visit:

http://127.0.0.1:8000/

Django Admin:

http://127.0.0.1:8000/admin/

## How to Use

1. Start the Django development server.
2. Open the application dashboard.
3. Navigate to the Vans section and add available vehicles.
4. Navigate to Drivers and add driver information.
5. Navigate to Routes and define transportation routes.
6. Open the Schedules section.
7. Click **Generate with AI (CSP)**.
8. The CSP engine evaluates available assignments and attempts to generate a valid schedule.
9. View the generated schedules.

## Documentation

Additional project documentation is available in:

- `PROJECT_REPORT.md` – Detailed software engineering project report.
- `plan.md` – Project requirements, constraints, design specifications, and implementation plan.

## Future Improvements

- Google Maps integration for route visualization.
- Real-time traffic and distance estimation.
- Advanced multi-day scheduling.
- Improved optimization using cost-based objective functions.
- Automated scheduling analytics and reporting.
- Enhanced authentication and role-based access control.
- PostgreSQL support for production deployment.

## Project Purpose

This project demonstrates the practical application of Artificial Intelligence concepts, particularly Constraint Satisfaction Problems, in a real-world logistics scheduling scenario.

It combines AI algorithms, backend development, database management, and frontend design into one integrated software application.

## License

This project is intended for educational and learning purposes.
