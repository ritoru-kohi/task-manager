from fastapi import APIRouter, HTTPException, status

from models.task import Category, Task, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

_tasks_db: dict[int, dict] = {}
_next_id: int = 1


def _seed() -> None:
    global _next_id
    if _tasks_db:
        return
    sample = Task(
        title="Подготовить отчёт",
        description="Квартальный отчёт по проекту",
        is_completed=False,
        category=Category(name="Работа", color="blue"),
        internal_note="Согласовать с руководителем",
    )
    _tasks_db[_next_id] = {"id": _next_id, **sample.model_dump()}
    _next_id += 1


_seed()


@router.get("", response_model=list[TaskOut], summary="Список задач")
def get_tasks() -> list[TaskOut]:
    return [TaskOut(**task) for task in _tasks_db.values()]


@router.post(
    "",
    response_model=TaskOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создать задачу",
)
def create_task(payload: Task) -> TaskOut:
    global _next_id
    task_data = {"id": _next_id, **payload.model_dump()}
    _tasks_db[_next_id] = task_data
    _next_id += 1
    return TaskOut(**task_data)


@router.get(
    "/{task_id}",
    response_model=TaskOut,
    summary="Получить задачу по ID",
)
def get_task(task_id: int) -> TaskOut:
    task = _tasks_db.get(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с id={task_id} не найдена",
        )
    return TaskOut(**task)