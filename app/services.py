from datetime import datetime
from fastapi import HTTPException
employees = []
next_id = 1
def check_unique_email(email, exclude_id=None):

    email = str(email).strip().lower()
    for employee in employees:
        if (
            employee["email"] == email
            and employee["id"] != exclude_id
        ):
            raise HTTPException(
                status_code=409,
                detail="Email address is already registered"
            )
    return email

def find_employee(employee_id):

    if employee_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Employee ID must be a positive integer"
        )
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(
        status_code=404,
        detail=f"Employee with ID {employee_id} not found"
    )


def create_employee(data):

    global next_id
    email = check_unique_email(data.email)
    employee = {
        "id": next_id,
        "name": data.name,
        "email": email,
        "department": data.department,
        "primary_skill": data.primary_skill,
        "location": data.location,
        "work_mode": data.work_mode.value,
        "is_active": data.is_active,
        "created_at": datetime.now()
    }
    employees.append(employee)
    next_id += 1
    return employee

def get_all_employees():
    return employees


def get_employee_by_id(employee_id):

    return find_employee(employee_id)


def update_employee(employee_id, data):

    employee = find_employee(employee_id)

    email = check_unique_email(
        data.email,
        exclude_id=employee_id
    )

    employee["name"] = data.name
    employee["email"] = email
    employee["department"] = data.department
    employee["primary_skill"] = data.primary_skill
    employee["location"] = data.location
    employee["work_mode"] = data.work_mode.value
    employee["is_active"] = data.is_active

    return employee


def delete_employee(employee_id):

    employee = find_employee(employee_id)

    employees.remove(employee)

    return {
        "message": "Employee deleted successfully"
    }