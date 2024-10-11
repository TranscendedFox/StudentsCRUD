from typing import  Optional
from model.student import Student
from repository import students_repository

async def get_by_id(id: int) -> Optional[Student]:
    return await students_repository.get_by_id(id)

async def create_student(student: Student):
    return await students_repository.create_student(student)

async def update_student(student_id: int, student: Student):
    return await students_repository.update_student(student_id, student)

async def delete_student(student_id):
    return await students_repository.delete_student(student_id)