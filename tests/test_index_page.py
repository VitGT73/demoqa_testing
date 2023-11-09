import re
import pytest
import pages
from playwright.sync_api import expect
import time

class TestFooter:
    # @pytest.mark.skip
    def test_user_should_be_ablen(self, page):
        pages.index_page.open_index_page(page)
        expect(page).to_have_title("Google")
