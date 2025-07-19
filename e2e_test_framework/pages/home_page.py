"""
Page Object for Home Page.
"""
from playwright.async_api import Page, Locator

class HomePage:
    """Page Object Model for the Home page."""
    def __init__(self, page: Page):
        """Initialize HomePage with Playwright Page object."""
        self.page = page
        self.user= page.get_by_role("link", name="mindfullQAafirmations")
        self.tweet_button = page.get_by_test_id("tweetButtonInline")
        self.tweet_textbox =  page.get_by_test_id("tweetTextarea_0")
        self.navigate_my_profile = page.get_by_label("mindfullQAafirmations@").get_by_role("link", name="mindfullQAafirmations")
    async def get_welcome_message(self) -> str:
        """Get the welcome message text."""
        return await self.welcome_message.text_content()

    async def logout(self) -> None:
        """Perform logout action."""
        await self.logout_button.click()
