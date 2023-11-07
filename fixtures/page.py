import pytest
from playwright.sync_api import Playwright, Browser #, Page, sync_playwright
# from config import settings
# from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright



@pytest.fixture(scope='module')
def browser(playwright: Playwright):
    browser: Browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

# fixture для создания страницы
@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()



# @pytest.fixture()
# def page() -> Page:
#     playwright = sync_playwright().start()
#     if settings.playwright.BROWSER == 'firefox':
#         browser = get_firefox_browser(playwright)
#         context = get_context(browser)
#         page_data = context.new_page()
#     elif settings.playwright.BROWSER == 'chrome':
#         browser = get_chrome_browser(playwright)
#         context = get_context(browser)
#         page_data = context.new_page()
#     else:
#         browser = get_chrome_browser(playwright)
#         context = get_context(browser)
#         page_data = context.new_page()
#     yield page_data
#     for context in browser.contexts:
#         context.close()
#     browser.close()
#     playwright.stop()


# def get_firefox_browser(playwright) -> Browser:
#     return playwright.firefox.launch(
#         headless=settings.playwright.IS_HEADLESS,
#         slow_mo=settings.playwright.SLOW_MO,
#     )


# def get_chrome_browser(playwright) -> Browser:
#     return playwright.chromium.launch(
#         headless=settings.playwright.IS_HEADLESS,
#         slow_mo=settings.playwright.SLOW_MO
#     )


# def get_context(browser) -> BrowserContext:
#     context = browser.new_context(
#         viewport=settings.playwright.PAGE_VIEWPORT_SIZE,
#         locale=settings.playwright.LOCALE
#     )
#     context.set_default_timeout(
#         timeout=settings.expectations.DEFAULT_TIMEOUT
#     )
#     return context
