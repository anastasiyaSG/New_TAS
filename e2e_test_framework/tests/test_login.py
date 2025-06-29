"""
E2E test case for login functionality using Playwright async, POM, and secure credentials.
"""
import pytest
from playwright.async_api import expect
from e2e_test_framework.pages.home_page import HomePage
from e2e_test_framework.pages.login_page import LoginPage
from e2e_test_framework.fixtures.conftest import login_session


@pytest.mark.asyncio
async def test_user_can_login_successfully(login_session):
    page = login_session
    home_page = HomePage(page)
    await expect(home_page.tweet_textbox).to_be_visible(timeout=5000)
   