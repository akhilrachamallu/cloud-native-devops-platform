from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user_id
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate


router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Create a new task for the authenticated user.
    """

    task = Task(
        title=task_data.title,
        description=task_data.description,
        user_id=current_user_id,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.get(
    "/",
    response_model=list[TaskResponse],
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Return all tasks belonging to the authenticated user.
    """

    tasks = db.scalars(
        select(Task).where(
            Task.user_id == current_user_id
        )
    ).all()

    return tasks


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Return a specific task belonging to the authenticated user.
    """

    task = db.scalar(
        select(Task).where(
            Task.id == task_id,
            Task.user_id == current_user_id,
        )
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.patch(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Update a task belonging to the authenticated user.
    """

    task = db.scalar(
        select(Task).where(
            Task.id == task_id,
            Task.user_id == current_user_id,
        )
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    updates = task_data.model_dump(
        exclude_unset=True
    )

    for field, value in updates.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Delete a task belonging to the authenticated user.
    """

    task = db.scalar(
        select(Task).where(
            Task.id == task_id,
            Task.user_id == current_user_id,
        )
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()

    return None