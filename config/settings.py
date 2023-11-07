import os
from environs import Env


class Expectations:
    DEFAULT_TIMEOUT = 30 * 1000


class PlayWright:
    PAGE_VIEWPORT_SIZE: dict[str, int] = {"width": 1920, "height": 1080}
    ENV: str = os.getenv("ENV", default="stage")
    BROWSER: str = os.getenv("BROWSER", default="chrome")
    IS_HEADLESS: str = os.getenv("HEADLESS", default="False")
    SLOW_MO = int(os.getenv("SLOW_MO", default=50))
    LOCALE = "en-US"


class Settings:
    env = Env()  # Создаем экземпляр класса Env
    env.read_env(".env")
    BASE_URL = "https://demoqa.com/"
    exception: Expectations = Expectations()
    playwright: PlayWright = PlayWright()


settings = Settings()
# Методом read_env() читаем файл .env и загружаем из него переменные в окружение
