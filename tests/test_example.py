import re
import pytest
from playwright.sync_api import expect
# from fixtures import page_no_auth
# @pytest.mark.skip
def test_has_title(page) -> None:

    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page) -> None:

    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
# Running test with arguments: --rootdir /home/vit/devlopment/demoqa_testing/tests --override-ini junit_family=xunit1 --junit-xml=/tmp/tmp-4192HxSu93lGFRSN.xml ./test_example.py::test_has_title
