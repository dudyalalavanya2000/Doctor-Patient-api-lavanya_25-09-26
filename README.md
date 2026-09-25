# Doctor Patient Management API

A RESTful API built using **FastAPI** for managing doctors and patients. The application includes JWT-based authentication, role-based authorization, patient-doctor assignment, validation, and error handling.

## Project Overview

The Doctor Patient Management API provides functionality for:

* User registration and login
* JWT authentication
* Admin and Doctor roles
* Doctor management
* Patient management
* Assigning patients to doctors
* Role-based patient access
* Pydantic data validation
* Error handling
* Swagger API documentation

## Technologies Used

* Python 3.9+
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* JWT
* Python-Jose
* Pwdlib
* Uvicorn
* Python-Dotenv

## Project Structure

```text
doctor-patient-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── utils.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── doctors.py
│   │   └── patients.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── doctor_service.py
│       └── patient_service.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dudyalalavanya2000/doctor-patient-api.git
```

### 2. Navigate to the project

```bash
cd doctor-patient-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Do not commit the `.env` file to GitHub.

## Run the Application

Start the FastAPI application using:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger can be used to register users, login, authorize using JWT, create doctors and patients, assign patients, and test the APIs.

## Authentication

The application uses **JWT Bearer Token authentication**.

### Register

```http
POST /auth/register
```

Example:

```json
{
  "name": "Admin",
  "email": "admin@gmail.com",
  "password": "admin123456",
  "role": "admin"
}
```

Supported roles:

* `admin`
* `doctor`

### Login

```http
POST /auth/login
```

The login endpoint uses OAuth2 password form authentication.

Use:

```text
grant_type: password
username: registered email
password: registered password
```

The API returns an access token:

```json
{
  "access_token": "your-jwt-token",
  "token_type": "bearer"
}
```

Use this token to authorize protected endpoints.

## API Endpoints

### Authentication

| Method | Endpoint         | Description                  |
| ------ | ---------------- | ---------------------------- |
| POST   | `/auth/register` | Register a new user          |
| POST   | `/auth/login`    | Login and generate JWT token |

### Doctors

| Method | Endpoint               | Description      |
| ------ | ---------------------- | ---------------- |
| GET    | `/doctors/`            | Get all doctors  |
| POST   | `/doctors/`            | Create a doctor  |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID |
| PUT    | `/doctors/{doctor_id}` | Update doctor    |
| DELETE | `/doctors/{doctor_id}` | Delete doctor    |

### Patients

| Method | Endpoint                                           | Description                     |
| ------ | -------------------------------------------------- | ------------------------------- |
| GET    | `/patients/`                                       | Get patients based on user role |
| POST   | `/patients/`                                       | Create a patient                |
| GET    | `/patients/{patient_id}`                           | Get a patient                   |
| PUT    | `/patients/{patient_id}`                           | Update a patient                |
| PUT    | `/patients/{patient_id}/assign-doctor/{doctor_id}` | Assign patient to doctor        |

## Role-Based Access

### Admin

An Admin can:

* View all patients
* Create doctors
* Update doctors
* Delete doctors
* Assign patients to doctors
* Access patient records

### Doctor

A Doctor can:

* View only assigned patients
* View an individual assigned patient
* Update only assigned patients

A Doctor cannot access or update patients assigned to another doctor.

## Patient Assignment

An Admin can assign a patient to a doctor using:

```http
PUT /patients/{patient_id}/assign-doctor/{doctor_id}
```

Example:

```text
PUT /patients/4/assign-doctor/2
```

This assigns Patient ID `4` to Doctor ID `2`.

## Validation

The API uses Pydantic validation for request data.

Examples:

* Patient age must be greater than `0`
* Phone number must contain 10–15 digits
* Email addresses must be valid
* Password must contain at least 6 characters

Invalid input returns an appropriate validation error response.

## Error Handling

The API handles common errors including:

* Invalid login credentials
* Duplicate email
* User not found
* Doctor not found
* Patient not found
* Unauthorized access
* Insufficient permissions
* Invalid request data

HTTP status codes such as `400`, `401`, `403`, `404`, and `422` are used where appropriate.

## Testing

The APIs can be tested using **Swagger UI**.

Recommended testing flow:

```text
Register Admin
      ↓
Register Doctor User
      ↓
Login as Admin
      ↓
Create Doctor
      ↓
Create Patients
      ↓
Assign Patient to Doctor
      ↓
Login as Doctor
      ↓
View Assigned Patients
      ↓
Test Unauthorized Patient Access
      ↓
Test Patient Update Permissions
```

## Example Role-Based Access Test

If Patient `4` is assigned to Doctor `2`:

```text
Doctor 2 → GET /patients/
```

The doctor can see Patient `4`.

If Patient `3` is not assigned to Doctor `2`:

```text
Doctor 2 → GET /patients/3
```

The API returns:

```json
{
  "detail": "You can access only your assigned patients"
}
```

with HTTP status:

```text
403 Forbidden
```

## Security

* Passwords are stored using password hashing.
* JWT tokens are used for authentication.
* Protected endpoints require authentication.
* Role-based authorization restricts access to resources.
* Secret configuration is stored in environment variables.


