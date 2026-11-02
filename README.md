# Recruitment & Placement Management System

## 1. Project Overview
The Recruitment & Placement Management System is a web-based application developed using Python Flask, HTML, CSS, JavaScript and SQLite.

It helps manage candidate registration, candidate records and placement information through a simple dashboard.

## 2. Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** SQLite
- **IDE:** Visual Studio Code
- **Browser:** Google Chrome

## 3. Main Features
1. Recruiter Login
2. Dashboard
3. Candidate Registration
4. Candidate Details Management
5. Candidates List Display
6. Delete Candidate
7. Total Candidates Count
8. Placed Candidates Count
9. Pending Candidates Count
10. SQLite Database Integration

## 4. Demo Login Details
- Email: recruiter@demo.com
- Password: demo123

## 5. Project Folder Structure

```text
recruitment-placement-ui/
│
├── app.py
├── placement.db
├── login.html
├── dashboard.html
├── candidate-form.html
├── candidates.html
│
├── css/
│   └── style.css
│
└── js/
    └── app.js
```

## 6. Installation and Execution

**Step 1:** Install Python.

**Step 2:** Open the project folder in VS Code.

**Step 3:** Install Flask:

```bash
python -m pip install flask
```

**Step 4:** Run the application:

```bash
python app.py
```

**Step 5:** Open the browser and visit:

```text
http://127.0.0.1:5000/
```

## 7. Database
SQLite is used to store recruiter login details and candidate information.

The candidates table stores:
- Candidate ID
- Full Name
- Email
- Mobile Number
- Qualification
- College
- Passing Year
- Percentage
- Technology
- Placement Status

## 8. Conclusion
The Recruitment & Placement Management System provides a simple way to register and manage candidate information. It reduces manual record management and provides an easy-to-use interface for placement-related activities.

## 9. Future Scope
- Admin and recruiter roles
- Candidate search and filtering
- Edit candidate details
- Resume upload
- Placement reports
- Email notifications
