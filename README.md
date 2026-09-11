# Employee Management API

## Project Overview

Employee Management API is a backend application developed using Python and FastAPI.

This project is used to manage employee records through REST API operations.

The application supports:

- Create Employee
- View All Employees
- View Employee by ID
- Update Employee
- Delete Employee
- Health Check

Employee records are stored temporarily in an in-memory Python list. No database is used.

---

## What is FastAPI?

FastAPI is a modern and high-performance Python web framework used to build REST APIs and backend applications.

FastAPI provides:

- Fast API development
- Request validation
- Pydantic models
- Automatic API documentation
- Swagger UI
- HTTP status codes
- Easy CRUD API development

---

## Project Objective

The main objectives of this project are:

1. Learn FastAPI.
2. Create REST APIs using Python.
3. Understand CRUD operations.
4. Validate request data using Pydantic.
5. Implement employee management.
6. Handle API errors.
7. Test APIs using Swagger UI.
8. Learn Git and GitHub.

---

## Technologies Used

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Swagger UI
- Git
- Visual Studio Code

---

## Project Structure

```text
employee_fastapi/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── services.py
│
├── requirements.txt
├── README.md
└── .gitignore
