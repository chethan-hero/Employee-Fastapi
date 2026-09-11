from fastapi import FastAPI

from .schemas import Employee, EmployeeCreate

from .services import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)


app = FastAPI(
    title="Employee Management API",
    description="FastAPI backend for managing employee records",
    version="1.0.0"
)


# Health Check
@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "message": "Application is running"
    }


# Create Employee
@app.post(
    "/employees",
    response_model=Employee,
    status_code=201
)
def create(data: EmployeeCreate):

    return create_employee(data)


# List All Employees
@app.get(
    "/employees",
    response_model=list[Employee]
)
def get_all():

    return get_all_employees()


# Get Employee By ID
@app.get(
    "/employees/{employee_id}",
    response_model=Employee
)
def get_by_id(employee_id: int):

    return get_employee_by_id(employee_id)


# Update Employee
@app.put(
    "/employees/{employee_id}",
    response_model=Employee
)
def update(
    employee_id: int,
    data: EmployeeCreate
):

    return update_employee(
        employee_id,
        data
    )


# Delete Employee
@app.delete("/employees/{employee_id}")
def delete(employee_id: int):

    return delete_employee(employee_id)