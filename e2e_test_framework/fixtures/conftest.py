"""
Pytest fixtures for Playwright async browser and login session.
"""
import pytest
from playwright.async_api import async_playwright, Page
from e2e_test_framework.pages.login_page import LoginPage
import os
from dotenv import load_dotenv

BASE_URL = "https://x.com"  # Replace with your actual base URL

@pytest.fixture()
async def page() -> Page:
    """Create a new browser page for each test."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(BASE_URL)
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        try:
            yield page
        finally:
            await context.tracing.stop(path="trace.zip")
            await context.close()
            await browser.close()

@pytest.fixture()
async def login_session(page: Page):
    """
    Fixture to handle login session for tests.
    This can be used to log in once and reuse the session across tests.
    """
    login_page = LoginPage(page)
    load_dotenv()
    E2E_USERNAME = os.getenv("E2E_USERNAME")
    E2E_PASSWORD = os.getenv("E2E_PASSWORD")
    await login_page.login(E2E_USERNAME, E2E_PASSWORD)
    yield page
    # Cleanup if needed (e.g., logout)
    # await page.locator("#logout").click()  # Adjust selector as needed
