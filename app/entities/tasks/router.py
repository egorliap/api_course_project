from fastapi import APIRouter, Depends, HTTPException, Response

from .service import TaskService
from .schemas import STask, STaskAdd, STaskUpdate
from .rb import RBTask

from typing import List

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.get('/', summary="get all tasks")
async def get_all_tasks(request_body: RBTask = Depends()) -> List[STask]:
    return await TaskService.find_all(**request_body.to_dict())

@router.get('/{id}', summary="get one task by id")
async def get_one_task_by_id(task_id:int) -> STask | dict:
    result = await TaskService.find_one_or_none_by_id(task_id)
    if result is None:
        return {
            "message": f"Task with {task_id} not found"
            }
    return result

@router.post('/add')
async def insert_task(task: STaskAdd) -> dict:
    result = await TaskService.insert(task.model_dump())
    if result:
        return {
            "message": "Successfully added task",
            "task": task
            }
    else:
        return {
            "message": "Error wile adding task"
            }
        
@router.delete('/delete/{id}')
async def delete_task_by_id(task_id: int) -> dict:
    result = await TaskService.delete(task_id)
    if result:
        return {
            "message": f"Successfully delete task with id {task_id}"
            }
    else:
        return {
            "message": "Error while delete task"
            }
        
@router.put('/update')
async def update_task(task: STaskUpdate) -> dict:
    result = await TaskService.update(filter_by={"id": task.id}, **task().model_dump())
    if result:
        return {
            "message": f"Task updated successfully",
            "task": task,
            }
    else:
        return {
            "message": "Error while updating task"
            }