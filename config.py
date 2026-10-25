import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    APP_TITLE: str = os.getenv("APP_TITLE", "Task Manager API")
    APP_DESCRIPTION: str = os.getenv(
        "APP_DESCRIPTION",
        "API для управления задачами (React-клиент)",
    )


settings = Settings()