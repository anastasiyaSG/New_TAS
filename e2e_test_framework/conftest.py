"""
Pytest fixtures for Playwright async browser and login session.
"""
import pathlib
import pytest
from playwright.async_api import async_playwright, Page, expect
import pytest_asyncio
from e2e_test_framework.pages.login_page import LoginPage
import os
from dotenv import load_dotenv
import json

BASE_URL = "https://x.com/i/flow/login"  # Replace with your actual base URL

@pytest_asyncio.fixture()
async def set_up_x(request):
    """Create a new browser page for each test."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)  # Set headless=True for CI
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(BASE_URL)
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        try:
            yield page
        finally:
            test_name = request.node.name
            trace_path = pathlib.Path(f"traces/{test_name}.zip")
            await context.tracing.stop(path=trace_path)
            await context.close()
            await browser.close()

@pytest_asyncio.fixture()
async def login_session(set_up_x):
    """
    Fixture to handle login session for tests.
    This can be used to log in once and reuse the session across tests.
    """
    page = set_up_x
    login_page = LoginPage(page)
    # Load environment variables from .env file
    credentials_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    with open(credentials_path, "r") as f:
        creds = json.load(f)
    username = creds['E2E_USERNAME']
    password = creds['E2E_PASSWORD']
    await expect(login_page.username).to_be_visible(timeout=5000)
    await login_page.username.fill(username)
    await login_page.next_button.click()
    await expect(login_page.password).to_be_visible(timeout=5000)
    await login_page.password.fill(password)
    await login_page.login_button.click()
    yield page
    # Cleanup if needed (e.g., logout)
    # await page.locator("#logout").click()  # Adjust selector as needed
