from pydantic import BaseModel, Field, field_validator


class Category(BaseModel):
    name: str = Field(..., description="Название категории")
    color: str = Field(..., description="Цвет категории")


class Task(BaseModel):
    title: str = Field(..., description="Название задачи")
    description: str = Field("", description="Описание задачи")
    is_completed: bool = Field(False, description="Признак выполнения")
    category: Category = Field(..., description="Категория задачи")
    internal_note: str = Field("", description="Служебное поле")

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        cleaned = value.strip()
        if len(cleaned) < 3:
            raise ValueError(
                "Название задачи должно содержать не менее 3 символов"
            )
        return cleaned


class TaskOut(BaseModel):
    id: int = Field(..., description="Идентификатор задачи")
    title: str
    description: str
    is_completed: bool
    category: Category