import re
import pytest
import pages
from playwright.sync_api import expect

class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        expect(page).to_have_title("Google")
