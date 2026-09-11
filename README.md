# Employee Management API

A beginner-friendly REST API project built using Python and FastAPI.

## About FastAPI

FastAPI is a modern Python web framework used to build APIs and backend applications.

This project demonstrates how to create and manage employee records using CRUD operations.

## Technologies Used

- Python 3.14
- FastAPI
- Pydantic
- Uvicorn
- Swagger UI
- Git

## Project Structure

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

## Employee Fields

- id
- name
- email
- department
- primary_skill
- location
- work_mode
- is_active
- created_at

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Check application status |
| POST | /employees | Create employee |
| GET | /employees | Get all employees |
| GET | /employees/{id} | Get employee by ID |
| PUT | /employees/{id} | Update employee |
| DELETE | /employees/{id} | Delete employee |

## Installation

Create a virtual environment:

```bash
python -m venv .venv
