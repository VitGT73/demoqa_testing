from playwright.sync_api import Page
from config import settings


class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(settings.BASE_URL)
