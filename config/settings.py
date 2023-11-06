import os
from environs import Env


class Project:
    BASE_URL = 'https://demoqa.com/'

class Expectations:
    DEFAULT_TIMEOUT = 30 * 1000

class PlayWright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    ENV = os.getenv('ENV',default="stage")
    BROWSER = os.getenv('BROWSER', default="chrome")
    IS_HEADLESS = os.getenv('HEADLESS', default="False")
    SLOW_MO = int(os.getenv('SLOW_MO', default=50))
    LOCALE = 'en-US'

class Settings():
    env = Env()              # Создаем экземпляр класса Env
    env.read_env(".env")
    project: Project = Project()
    exception: Expectations = Expectations()
    playwright: PlayWright = PlayWright()

settings = Settings()
          # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
