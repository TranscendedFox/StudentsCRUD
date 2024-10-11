from typing import Optional
from model.student import Student
from repository.database import database

TABLE_NAME = "students"


async def get_by_id(student_id: int) -> Optional[Student]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:id"
    result = await database.fetch_one(query, values={"id": student_id})
    if result:
        return Student(**result)
    else:
        return None


async def create_student(student: Student):
    query = f"""
        INSERT INTO {TABLE_NAME} (first_name, last_name, email)
        VALUES(:first_name, :last_name, :email)
"""
    values = {"first_name": student.first_name, "last_name": student.last_name, "email": student.email}

    await database.execute(query, values)


async def update_student(student_id: int, student: Student):
    query = f"""
        UPDATE {TABLE_NAME}
        SET first_name = :first_name,
        last_name = :last_name,
        email = :email 
        WHERE id = :student_id
"""
    values = {"student_id": student_id, "first_name": student.first_name, "last_name": student.last_name, "email": student.email}

    await database.execute(query, values)


async def delete_student(student_id):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = :student_id"
    await database.execute(query, values={"student_id": student_id})
