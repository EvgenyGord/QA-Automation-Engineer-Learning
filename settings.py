import os

from dotenv import load_dotenv

load_dotenv()

API_USERNAME = os.getenv("API_USERNAME")
API_PASSWORD = os.getenv("API_PASSWORD")

if not API_USERNAME or not API_PASSWORD:
    raise RuntimeError(
        "API_USERNAME and API_PASSWORD must be set in .env"
    )
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings:
    @property
    def base_url(self) -> str:
        """
        Возвращает основной URL для API.

        Этот URL используется для всех API-запросов в системе.
        Его можно легко изменить для использования с другим окружением.
        """
        return "https://demoqa.com"

