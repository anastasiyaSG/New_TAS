"""
Page Object for Login Page.
"""
from playwright.async_api import Page, Locator

class LoginPage:
    """Page Object Model for the Login page."""
    def __init__(self, page: Page):
        """Initialize LoginPage with Playwright Page object."""
        self.page = page
        self.sign_in = page.get_by_test_id("loginButton")
        self.username = page.get_by_role("textbox", name="Phone, email, or username")
        self.next_button = page.get_by_role("button", name="Next")
        self.password = page.get_by_role("textbox", name="Password Reveal password")
        self.login_button = page.get_by_test_id("LoginForm_Login_Button")
   
        self.error_message: Locator = page.locator(".error-message")

    async def login(self, username: str, password: str) -> None:
        """Perform login action with given credentials."""
        await self.sign_in.click()
        await self.username.fill(username)
        await self.next_button.click()
        await self.password.fill(password)
        await self.login_button.click()

    async def get_error_message(self) -> str:
        """Get error message text if login fails."""
        return await self.error_message.text_content()
