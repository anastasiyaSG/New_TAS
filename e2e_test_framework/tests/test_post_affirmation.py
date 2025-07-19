import pytest
from playwright.async_api import Page, expect
from e2e_test_framework.pages.home_page import HomePage
from e2e_test_framework.pages.login_page import LoginPage
from e2e_test_framework.fixtures.affirmation_fixture import nice_affirmation
import json
import pathlib
import logging

@pytest.mark.asyncio
async def test_post_affirmation_to_x(login_session, nice_affirmation):
    page = login_session
    home_page = HomePage(page)
    # Act: Post a tweet with the affirmation
    logging.info("Post affirmation tweet")
    await home_page.tweet_textbox.fill(nice_affirmation)
    await home_page.tweet_button.click()
    await page.get_by_test_id("app-bar-close").click()

    # Assert: Confirm tweet appears in timeline
    logging.info("Verify tweet posted")
    await home_page.navigate_my_profile.click()
    await page.wait_for_load_state("domcontentloaded")

    await expect(page.get_by_text(nice_affirmation)).to_be_visible()
