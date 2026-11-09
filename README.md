# Smart Van and Route Scheduling System

Welcome to the **Smart Van and Route Scheduling System**! This is an AI-powered logistics scheduling web application designed to automate and optimize the assignment of vans and drivers to specific routes using Constraint Satisfaction Problem (CSP) algorithms.

## Purpose
The primary purpose of this project is to eliminate manual scheduling conflicts, reduce human error, and optimize logistics operations through intelligent constraint solving and resource management.

## Goals
- Automate van and driver assignments.
- Ensure 100% compliance with operational constraints (working hours, vehicle capacity, maintenance).
- Provide a responsive, premium, and intuitive user interface for logistics administrators.
- Offer actionable analytics and real-time dashboard reporting.

## Features
- **AI Scheduling Engine:** Uses CSP (Backtracking, Forward Checking, MRV, LCV) to generate conflict-free schedules.
- **Van Management (CRUD):** Manage vehicles, capacities, fuel ranges, and maintenance status.
- **Driver Management (CRUD):** Track driver availability, licensing, and maximum daily working hours.
- **Route Management (CRUD):** Define routes with specific distances, passenger loads, time estimates, and priorities.
- **Analytics Dashboard:** Visualize vehicle usage, driver workload, and overall system status with Chart.js.
- **Modern SaaS UI:** Features a dark theme with glassmorphism effects and GSAP-powered smooth animations.

---

## Screenshots
> [!NOTE]
> *(Placeholder for actual screenshots)*
> - `Dashboard Overview`
> - `Manage Vans`
> - `Manage Drivers`
> - `Manage Routes`
> - `Generated AI Schedules`

---

## Project Architecture
The system follows a standard Django MVT (Model-View-Template) architecture integrated with a custom Python-based AI microservice logic layer. 
- **Frontend (Templates):** Bootstrap 5, custom CSS (Glassmorphism), Vanilla JS (GSAP).
- **Backend (Views/Models):** Django handling HTTP requests, database transactions, and context rendering.
- **AI Engine (Services):** A decoupled module (`services/csp/solver.py`) that applies CSP logic on the Django QuerySets.

---

## Technology Stack

### Frontend
- **Languages:** HTML5, CSS3, Vanilla JavaScript
- **Framework:** Bootstrap 5.3
- **Libraries:** Chart.js, GSAP (GreenSock Animation Platform)
- **Icons:** Bootstrap Icons
- **Fonts:** Google Fonts (Inter, Poppins)

### Backend
- **Language:** Python 3.11+
- **Framework:** Django 5.x
- **Architecture:** MVT (Model-View-Template)

### Database
- **Engine:** SQLite3 (Default for development)
- **ORM:** Django ORM

---

## Software Requirements

### Operating System
- Windows / macOS / Linux

### Required Software
- **Python Version:** 3.10 or higher
- **Package Manager:** pip (comes with Python)
- **Git:** For version control and cloning
- **Browser:** Modern web browser (Chrome, Firefox, Edge, Safari)

---

## Installation Guide

Follow these steps to set up the project on your local machine.

### Step 1: Clone repository
```bash
git clone <your-repository-url>
```

### Step 2: Navigate into project
```bash
cd "Smart Van and Route Scheduling System"
```

### Step 3: Create virtual environment
```bash
python -m venv venv
```

### Step 4: Activate virtual environment
**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```
**Windows (Command Prompt):**
```cmd
.\venv\Scripts\activate.bat
```
**Linux / Mac:**
```bash
source venv/bin/activate
```

### Step 5: Install dependencies
```bash
pip install -r requirements.txt
# Alternatively, if requirements.txt is missing:
# pip install django
```

### Step 6: Install frontend packages
*(No Node.js/npm required. Frontend packages are imported via CDNs in `base.html`.)*

### Step 7: Install backend packages
*(Handled in Step 5 using pip).*

### Step 8: Database setup
Run the following commands to create the SQLite database and run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 9: Environment Variables
Create a `.env` file in the root directory (where `manage.py` is located) for production.
> [!NOTE]
> Currently, the system uses default Django settings. For production, define:
> `SECRET_KEY=your-super-secret-key`
> `DEBUG=False`
> `ALLOWED_HOSTS=127.0.0.1,localhost`

### Step 10: Run backend
```bash
python manage.py runserver
```

### Step 11: Run frontend
*(Frontend is served automatically by Django through the backend server).*

### Step 12: Open browser
Open `http://127.0.0.1:8000/` in your browser.

### Step 13: Login
To access the admin panel at `http://127.0.0.1:8000/admin/`, first create a superuser:
```bash
python manage.py createsuperuser
```
Enter a username, email, and password. Log in using these credentials.

### Step 14: Use the application
Navigate using the sidebar to add Vans, Drivers, and Routes. Then go to "Schedules" and click "Generate with AI (CSP)".

---

## Commands Section

| Command | Explanation |
|---|---|
| `python -m venv venv` | Creates a completely isolated Python virtual environment. |
| `.\venv\Scripts\Activate.ps1` | Activates the virtual environment on Windows PowerShell. |
| `pip install -r requirements.txt` | Installs all required Python dependencies. |
| `python manage.py makemigrations` | Detects changes in `models.py` and creates migration files. |
| `python manage.py migrate` | Applies the migration files to the database schema. |
| `python manage.py createsuperuser` | Creates an administrator account for the Django backend. |
| `python manage.py runserver` | Starts the local Django development server on port 8000. |

---

## Project Structure

```text
/
├── core/                   # Main Django project configuration (settings, wsgi, urls)
├── logistics/              # Main application logic
│   ├── migrations/         # Database migration history
│   ├── services/           # Custom business logic
│   │   └── csp/            # AI Constraint Satisfaction Problem Engine
│   │       ├── __init__.py
│   │       └── solver.py   # CSP Backtracking Algorithm
│   ├── admin.py            # Admin panel configuration
│   ├── models.py           # Database schemas (Van, Driver, Route, Schedule)
│   ├── urls.py             # Route mappings for the logistics app
│   └── views.py            # Class-Based Views for CRUD and Dashboard
├── static/                 # Static assets
│   ├── css/                # Custom stylesheets (style.css)
│   ├── js/                 # Custom scripts (main.js)
│   └── img/                # Image assets
├── templates/              # HTML templates (base.html, dashboard, forms, lists)
├── venv/                   # Python Virtual Environment
├── db.sqlite3              # Local SQLite database file
└── manage.py               # Django execution script
```

---

## How to Run
**Beginner Tutorial:**
1. **What to install:** Download and install Python 3.11+. Make sure to check "Add Python to PATH" during installation.
2. **What command to run:** Open Terminal/Command Prompt in the project folder and type `python -m venv venv`.
3. Activate it: `venv\Scripts\activate`.
4. Install Django: `pip install django`.
5. Prepare the database: `python manage.py migrate`.
6. Start the server: `python manage.py runserver`.
7. **Expected output:** The terminal will show `Starting development server at http://127.0.0.1:8000/`.
8. **What to click:** Open your web browser and click or type `http://127.0.0.1:8000/`.
9. **Possible errors:** "python is not recognized". **How to fix:** Reinstall Python and ensure "Add to PATH" is checked.

---

## Troubleshooting

- **Python errors (ModuleNotFoundError):**
  Ensure your virtual environment is activated before running the server. Run `pip install django`.
- **Database errors (no such table):**
  You forgot to migrate. Run `python manage.py makemigrations` followed by `python manage.py migrate`.
- **Port already in use (Error: That port is already in use.):**
  Another process is using port 8000. Stop it or run the server on a different port: `python manage.py runserver 8001`.
- **Permission denied (Windows Scripts):**
  Running scripts is disabled on your system. Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted` in PowerShell as Administrator.

---

## FAQ

1. **What is CSP?** Constraint Satisfaction Problem, an AI methodology to find solutions matching strict rules.
2. **Can I use PostgreSQL instead of SQLite?** Yes. Update `DATABASES` in `core/settings.py`.
3. **Is Node.js required?** No, the frontend relies on CDN links.
4. **How do I add a new Van?** Navigate to the Vans tab and click "Add Van".
5. **How does the AI optimize schedules?** It sorts domains to minimize distance/fuel ratio and prioritizes earlier departures.
6. **What happens if a driver exceeds max hours?** The CSP engine rejects the assignment.
7. **What if no solution exists?** The AI will inform you that no valid assignment can be found under current constraints.
8. **How do I change the color theme?** Edit CSS variables in `:root` inside `static/css/style.css`.
9. **How do I create an admin?** Use `python manage.py createsuperuser`.
10. **Where are the database models located?** In `logistics/models.py`.
11. **Where is the AI logic stored?** In `logistics/services/csp/solver.py`.
12. **Can I deploy this to Heroku?** Yes, but you will need to add `gunicorn` and `psycopg2`.
13. **Why do the animations look choppy?** Ensure hardware acceleration is enabled in your browser.
14. **How do I run tests?** Run `python manage.py test`.
15. **Does the AI use neural networks?** No, it uses classic AI search algorithms (Backtracking).
16. **How do I restart the server?** Press `Ctrl+C` in the terminal and run `python manage.py runserver` again.
17. **Where do I add new URLs?** In `logistics/urls.py`.
18. **Is this open-source?** Yes, under the MIT license.
19. **How do I clear all schedules?** Clicking "Generate with AI" clears the current schedule and creates a new one.
20. **Who do I contact for support?** Open an issue on the GitHub repository.

---

## License
MIT License. See `LICENSE` file for more details.

---

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -m 'Add awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Open a Pull Request.

---

## Author
Developed with ❤️ by Senior Software Engineer & AI Coding Assistant.
