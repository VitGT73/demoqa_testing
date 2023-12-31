from typing import Any, Generator
import pytest
from playwright.sync_api import (
    Playwright,
    Browser,
    Page,
    BrowserContext, BrowserType
)
from config import settings


# from typing import Dict


# @pytest.fixture(scope="function")
# def browser(playwright: Playwright) -> Generator[Browser, Any, None]:
#     headless: bool = settings.playwright.IS_HEADLESS
#     slow_mo: int = settings.playwright.SLOW_MO
#     if settings.playwright.BROWSER == "firefox":
#         browser: Browser = playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
#     elif settings.playwright.BROWSER == "webkit":
#         browser: Browser = playwright.webkit.launch(headless=headless, slow_mo=slow_mo)
#     else:
#         browser: Browser = playwright.chromium.launch(
#             headless=headless, slow_mo=slow_mo
#         )
#     yield browser
#     browser.close()

@pytest.fixture(scope="function")
def context(
    browser_type: BrowserType,
    browser_type_launch_args: dict,
    browser_context_args: dict,
) -> Generator[BrowserContext, Any, None]:
    context: BrowserContext = browser_type.launch_persistent_context(
        "./foobar",
        **{
            **browser_type_launch_args,
            **browser_context_args,
            "locale": "en-US",
        }
    )
    yield context
    context.close()



@pytest.fixture(scope="function")
def page_auth(context) -> Generator[Page, Any, None]:
    # context: BrowserContext = get_context(browser)
    # context.storage_state(path="state.json")
    page: Page = context.new_page()
    yield page
    context.close()
    page.close()

@pytest.fixture(scope="function")
def page(context) -> Generator[Page, Any, None]:

    page: Page = context.new_page()
    yield page
    page.close()
    context.close()


# @pytest.fixture(scope="function")
# def page(browser) -> Generator[Page, Any, None]:
#     context: BrowserContext = get_context(browser)
#     page: Page = context.new_page()
#     yield page
#     context.close()
#     page.close()


# def get_context(browser) -> BrowserContext:
#     context: BrowserContext = browser.new_context(
#         viewport=settings.playwright.PAGE_VIEWPORT_SIZE,
#         locale=settings.playwright.LOCALE,
#     )
#     context.set_default_timeout(timeout=settings.exception.DEFAULT_TIMEOUT)
#     return context
