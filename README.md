# FastAPI Doctor and Patient Management API

This project is a simple REST API built using FastAPI to manage doctors and patients.

## Objective

The objective of this project is to build a REST API using FastAPI with:

* Doctor management
* Patient management
* Pydantic validation
* Error handling
* In-memory data storage
* API testing using Swagger UI

## Technologies Used

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
doctor-patient-api/
│
├── main.py
├── requirements.txt
└── README.md
```

## API Endpoints

### Doctors

| Method | Endpoint               | Description        |
| ------ | ---------------------- | ------------------ |
| POST   | `/doctors`             | Create a doctor    |
| GET    | `/doctors`             | Get all doctors    |
| GET    | `/doctors/{doctor_id}` | Get a doctor by ID |

### Patients

| Method | Endpoint    | Description      |
| ------ | ----------- | ---------------- |
| POST   | `/patients` | Create a patient |
| GET    | `/patients` | Get all patients |

## Installation

Open the project folder in VS Code.

Open the terminal and install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements File

The `requirements.txt` file contains:

```text
fastapi
uvicorn
pydantic[email]
```

## Execute the Project

### Step 1: Open the Project

Open the project in VS Code.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Start the Server

```bash
uvicorn main:app --reload
```

### Step 4: Server Output

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

## Swagger Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* View all API endpoints
* Test POST and GET requests
* Test validation
* Test error handling
* View API responses

## Swagger Execution Flow

```text
Start FastAPI Server
        ↓
Open Swagger UI
        ↓
http://127.0.0.1:8000/docs
        ↓
Select API Endpoint
        ↓
Click "Try it out"
        ↓
Enter Request Data
        ↓
Click "Execute"
        ↓
View API Response
```

# Doctor APIs

## Create Doctor

**Method:** `POST`

**Endpoint:**

```text
/doctors
```

Enter the following JSON in Swagger:

```json
{
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "rathi@gmail.com",
  "is_active": true
}
```

### Output

```json
{
  "doctor_id": 1,
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "rathi@gmail.com",
  "is_active": true
}
```

## Get All Doctors

**Method:** `GET`

**Endpoint:**

```text
/doctors
```

### Output

```json
[
  {
    "doctor_id": 1,
    "name": "Dr. Rathi",
    "specialization": "Cardiology",
    "email": "rathi@gmail.com",
    "is_active": true
  }
]
```

## Get Doctor by ID

**Method:** `GET`

**Endpoint:**

```text
/doctors/{doctor_id}
```

Enter:

```text
1
```

### Output

```json
{
  "doctor_id": 1,
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "rathi@gmail.com",
  "is_active": true
}
```

# Patient APIs

## Create Patient

**Method:** `POST`

**Endpoint:**

```text
/patients
```

Enter the following JSON in Swagger:

```json
{
  "name": "Meena",
  "age": 25,
  "phone": "8688094563"
}
```

### Output

```json
{
  "patient_id": 1,
  "name": "Meena",
  "age": 25,
  "phone": "8688094563"
}
```

## Get All Patients

**Method:** `GET`

**Endpoint:**

```text
/patients
```

### Output

```json
[
  {
    "patient_id": 1,
    "name": "Meena",
    "age": 25,
    "phone": "8688094563"
  }
]
```

# Validation

The project uses **Pydantic** to validate request data.

## Doctor Email Validation

The doctor email must be in a valid email format.

### Valid Input

```json
{
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "rathi@gmail.com",
  "is_active": true
}
```

### Invalid Input

```json
{
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "wrong-email",
  "is_active": true
}
```

The API rejects the request because the email format is invalid.

## Patient Age Validation

The patient age must be greater than `0`.

### Valid Input

```json
{
  "name": "Meena",
  "age": 25,
  "phone": "8688094563"
}
```

### Invalid Input

```json
{
  "name": "Meena",
  "age": 0,
  "phone": "8688094563"
}
```

The API rejects the request because the patient age must be greater than `0`.

## Patient Phone Validation

The patient phone number must contain exactly 10 characters.

### Valid Input

```json
{
  "name": "Meena",
  "age": 25,
  "phone": "8688094563"
}
```

### Invalid Input

```json
{
  "name": "Meena",
  "age": 25,
  "phone": "123"
}
```

The API rejects the request because the phone number does not contain 10 characters.

# Error Handling

The API uses `HTTPException` to handle errors.

## Doctor Not Found

For example:

```text
GET /doctors/100
```

### Output

```text
404 Not Found
```

```json
{
  "detail": "Doctor not found"
}
```

# Data Storage

The project uses **in-memory storage**.

Doctors and patients are stored in Python lists.

```python
doctors = []
patients = []
```

The data is available only while the FastAPI application is running.

The data will be lost when the application is restarted.

# Complete Execution Flow

```text
1. Open project in VS Code
          ↓
2. Open Terminal
          ↓
3. Install dependencies
   pip install -r requirements.txt
          ↓
4. Start FastAPI server
   uvicorn main:app --reload
          ↓
5. Open Swagger UI
   http://127.0.0.1:8000/docs
          ↓
6. Create Doctor
   POST /doctors
          ↓
7. Get Doctors
   GET /doctors
          ↓
8. Get Doctor by ID
   GET /doctors/{doctor_id}
          ↓
9. Create Patient
   POST /patients
          ↓
10. Get Patients
    GET /patients
          ↓
11. Test Email Validation
          ↓
12. Test Age Validation
          ↓
13. Test Phone Validation
          ↓
14. Test Doctor Not Found Error
```

# API Summary

| Method | Endpoint               | Description      |
| ------ | ---------------------- | ---------------- |
| POST   | `/doctors`             | Create a doctor  |
| GET    | `/doctors`             | Get all doctors  |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID |
| POST   | `/patients`            | Create a patient |
| GET    | `/patients`            | Get all patients |

# API Documentation URLs

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

# Expected Output

### Successful Doctor Creation

```text
201 Created
```

```json
{
  "doctor_id": 1,
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "rathi@gmail.com",
  "is_active": true
}
```

### Successful Patient Creation

```text
201 Created
```

```json
{
  "patient_id": 1,
  "name": "Meena",
  "age": 25,
  "phone": "8688094563"
}
```

### Invalid Input

```text
422 Unprocessable Entity
```

### Doctor Not Found

```text
404 Not Found
```

