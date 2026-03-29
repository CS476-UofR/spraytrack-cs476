<!--
Simple English comments version
This documentation file belongs to the CS476 Spray Records project.
-->

# Spray Records Web App (Commented Version)
A full-stack web application for managing pesticide and herbicide spray records with role-based workflows, geospatial tracking, and regulatory compliance support.
HTML / CSS / JavaScript + MySQL + Django

# User Roles
   Operator:
            Create, edit, and submit spray records
            Select spray locations using an interactive map
   Admin / Supervisor:
            Review submitted records
            Approve or flag records
            Search and visualize historical data

## What is included
- Frontend: pure HTML/CSS/JavaScript pages (no frameworks)
- Backend: Django
- Authentication: JWT (token-based)
- Authorization: Role-based (Operator vs Admin)
- Workflow: Draft → Submit → Approve/Flag
- Audit logs for status changes (Observer-like design)
- Export: CSV / JSON / PDF (Factory-like design)

## Live Deployement
Frontend: (VERCEL)
https://spraytrack-cs476-8ye27s9qq-cs476-uofrs-projects.vercel.app/

Backend: (RAILWAY)
https://spraytrack-cs476-production.up.railway.app/

## Core Features
JWT-based authentication
Role-based authorization (Operator vs Admin)
Workflow:
Draft → Submit → Approved / Flagged
Interactive map for spray location (Leaflet + OpenStreetMap)
Audit logging of record changes (Observer pattern)
Export data as:
CSV
JSON
PDF (Factory pattern)

## Run backend
1) Create DB tables (MySQL):
   - Run `schema.sql` in your MySQL client

2) Configure environment:
   - Copy `Backend/.env.example` to `Backend/.env`
   - Fill in DB credentials

3) Install and run:
   - cd Backend
   - python -m venv venv
   - .venv\Scripts\activate
   - pip install -r requirements.txt
   - python manage.py migrate
   - python manage.py runserver
   - API at: http://localhost:4000

4) Seed demo users:
   - POST http://localhost:4000/auth/seed
   - Accounts:
     - operator@test.com / pass123
     - admin@test.com / pass123

## Run frontend
- Open `frontend/login.html` directly in a browser (or host with a static server)
- Make sure `API_BASE` in `frontend/assets/app.js` matches your backend URL

## Pages included
General:
- login.html

Operator:
- operator-dashboard.html
- operator-new-record.html
- operator-map.html
- operator-review.html
- operator-confirm.html
- operator-records.html

Admin:
- admin-dashboard.html
- admin-search.html
- admin-view-record.html
- admin-map.html

## Project Structure
Backend/
Frontend/
  ├── login.html
  ├── operator-*.html
  ├── admin-*.html
  └── Assets/
Database/

## Deployment Architecture
Frontend: Vercel (Static Hosting, CDN)
Backend: Railway (Django + Gunicorn)
Database: Railway MySQL

Communication Flow: 
Browser → Frontend (Vercel)
Frontend → Backend API (Railway)
Backend → Database (MySQL)

## Testing
   1) Open frontend
   2) Click Seed Demo Users
   3) Login as:
         operator@test.com
         admin@test.com
   4) Test: 
         Record Creation
         Submission
         Approval Workflow

## Contributors
         Arpit Gupta 
               Developed the frontend interface using HTML, CSS, and JavaScript
               Managed database integration and structure coordination
               Handled deployment of the application (Vercel + Railway)
               Performed debugging of frontend and integration issues
               Live Demonstration of the Software
         Nolan Gasper
               Designed the backend architecture and wireframes
               Implemented backend functionality using Django framework
               Worked on backend setup, configuration, and scripting (Bash)
               Performed debugging of backend logic and API issues
         Luke Behnam
               Integrated frontend and backend systems
               Implemented API communication between UI and backend
               Integrated Leaflet maps for geospatial functionality
               Performed debugging of API integration and map-related issues
         Wooyoung Jeong
               Managed database design and schema implementation
               Contributed significantly to project report writing and documentation
               Performed debugging of database queries and data-related issues
         Jasdeep Singh Virk
               Contributed to frontend development and UI design
               Assisted in implementing user interface components
         Atharv Yuvraj Bondre
               Conducted system testing and validation
               Assisted with deployment processes and environment setup
         Mehakpreet Singh
               Prepared the presentation slides (PPT)
               Assisted in testing and validation of system features
               
         (Everyone Assisted in Report Writing)
## Notes
   This project was developed as part of CS 476 – Software Development and Demonstration
   Focuses on real-world municipal spray record management
   Designed for scalability, accuracy, and regulatory compliance