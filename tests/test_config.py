import pytest
from pages import index_page
from playwright.sync_api import expect, BrowserContext, Page


class TestFooter:
    # @pytest.mark.skip
    def test_user_should_be_able_to_open_popup_select_subscription_plan(
        self, context: BrowserContext
    ) -> None:
        page: Page = context.new_page()
        index_page.open_index_page(page)
        expect(page).to_have_title("Google")
