from fastapi import APIRouter, Depends

from .schemas import SLesson, SLessonAdd, SLessonUpdate
from .rb import RBLesson
from .service import ScheduleService

from typing import List

router = APIRouter(prefix='/schedule', tags=['schedule'])

@router.get("/" , summary="get full schedule")
async def get_all_schedule(request_body: RBLesson = Depends()) -> List[SLesson]:
    return await ScheduleService.find_all(**request_body.to_dict())

@router.get("/{id}", summary="get lesson by id")
async def get_lesson_by_id(lesson_id:int) -> SLesson | dict:
    result = await ScheduleService.find_by_id(lesson_id)
    if result is None:
        return {
            "message": f"Lesson with {lesson_id} not found"
            }
    return result

@router.post("/add", summary="insert new lesson in schedule")
async def insert_lesson(lesson: SLessonAdd) -> dict:
    result = await ScheduleService.insert_lesson(**lesson.to_dict())
    if result:
        return {
            "message": "Successfully added",
            "lesson": lesson
            }
    else:
        return {
            "message": "Error while adding lesson"
            }
        
@router.delete("/delete/{id}", summary="delete lesson by id")
async def delete_lesson_by_id(lesson_id:int) -> dict:
    result = await ScheduleService.delete_lesson_by_id(lesson_id)
    if result:
        return {
            "message": f"Successfully delete lesson with id {lesson_id}"
            }
    else:
        return {
            "message": "Error while deleting lesson"
            }
        
@router.put("/update", summary="update lesson")
async def update_lesson(lesson: SLessonUpdate) -> dict:
    result = await ScheduleService.update(
        filter_by = {"lesson_id": lesson.id},
        start_at = lesson.start_at,
        duration = lesson.duration,
        task = lesson.task
        )
    if result:
        return {
            "message": "Lesson updated successfully",
            "lesson": lesson
            }
    else:
        return {
            "message": "Error while updating lesson"}