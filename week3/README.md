# Week 3 - FastAPI Login Management System

A FastAPI application with PostgreSQL/MySQL connectivity for user authentication.

## Features

- User Registration API
- User Login API with JWT Authentication
- Protected Routes with Token Validation

## Project Structure

```
week3/
├── main.py          # FastAPI application entry point
├── config.py        # Database and JWT configuration
├── database.py      # Database connection setup
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic schemas for validation
├── auth.py          # Authentication utilities
├── routes.py        # API route handlers
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
cd week3
pip install -r requirements.txt
```

### 2. Configure Database

Update `config.py` with your database credentials:

```python
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "fastapi_db",
    "username": "postgres",
    "password": "your_password"
}
```

### 3. Create Database

For PostgreSQL:
```sql
CREATE DATABASE fastapi_db;
```

For MySQL:
```sql
CREATE DATABASE fastapi_db;
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

Or:
```bash
python main.py
```

### 5. Access the API

- API Documentation: http://127.0.0.1:8000/docs
- Alternative Docs: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint    | Description                  | Auth Required |
|--------|-------------|------------------------------|---------------|
| POST   | /register   | Register a new user          | No            |
| POST   | /login      | Login and get access token   | No            |
| GET    | /me         | Get current user info        | Yes           |

## Usage Examples

### Register a User

```bash
curl -X POST "http://127.0.0.1:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "secretpassword",
    "full_name": "John Doe"
  }'
```

### Login

```bash
curl -X POST "http://127.0.0.1:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=johndoe&password=secretpassword"
```

### Access Protected Route

```bash
curl -X GET "http://127.0.0.1:8000/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

