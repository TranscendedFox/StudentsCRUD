from fastapi import APIRouter, HTTPException
from starlette import status

from model.student import Student

from service import student_service

router = APIRouter(
    prefix="/student",
    tags=["student"]
)

students = {}

@router.get("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
async def get_student(student_id: int) -> Student:
    student = await student_service.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id: {student_id} not found")
    return student


@router.post("/", response_model=Student, status_code=status.HTTP_200_OK)
async def create_student(student: Student):
    await student_service.create_student(student)



@router.put("/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
async def update_student(student_id: int, student: Student):
    existing_student = await student_service.get_by_id(student_id)
    if not existing_student:
        raise HTTPException(status_code=404, detail=f"Can't update student with id: {student_id}, not found")
    await student_service.update_student(student_id, student)


@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student(student_id: int):
    await student_service.delete_student(student_id)