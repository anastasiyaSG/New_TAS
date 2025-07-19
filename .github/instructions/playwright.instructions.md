---
description: 'Playwright test generation instructions for Python'
applyTo: '**'
---

## Test Writing Guidelines

### Code Quality Standards
- **Locators**: Prioritize user-facing, role-based locators (`get_by_role`, `get_by_label`, `get_by_text`, etc.) for resilience and accessibility. Use ` logging.info("Log in to X")` context manager to group interactions and improve test readability and reporting.
- **Assertions**: Use Playwright's auto-retrying web-first assertions (e.g., `expect(locator).to_have_text()`). Avoid `expect(locator).to_be_visible()` unless specifically testing for visibility changes.
- **Timeouts**: Rely on Playwright's built-in auto-waiting. Avoid hard-coded waits or increasing default timeouts.
- **Clarity**: Use descriptive test and logging names that clearly state the intent. Add comments only to explain complex logic or non-obvious interactions.

### Test Structure
- **Imports**: Start with `import pytest` and `from playwright.async_api import expect` for async tests, Use `from playwright.async_api import Page, expect` for page interactions.
- **Test Functions**: Use `async def` for test functions and include `pytest.mark.asyncio` to mark them as async tests.
- **Arrange → Act → Assert**: Structure tests with clear sections:
  - **Arrange**: Set up the test environment, including page navigation and fixture setup.
  - **Act**: Perform actions on the page (e.g., clicking buttons, filling forms).
  - **Assert**: Verify expected outcomes using Playwright's assertions.
- **Organization**: Group related tests for a feature in a class or module.
- **Fixtures**: Use pytest fixtures (e.g., `page`) for setup actions common to all tests.
- **Titles**: Use clear naming conventions, such as `test_feature_specific_action`.

### File Organization
- **Location**: Store all test files in the `tests/` directory.
- **Naming**: Use the convention `test_<feature_or_page>.py` (e.g., `test_login.py`, `test_search.py`).
- **Scope**: Aim for one test file per major application feature or page.

### Assertion Best Practices
- **UI Structure**: Use `to_have_aria_snapshot()` to verify the accessibility tree structure of a component.
- **Element Counts**: Use `to_have_count()` to assert the number of elements found by a locator.
- **Text Content**: Use `to_have_text()` for exact text matches and `to_contain_text()` for partial matches.
- **Navigation**: Use `to_have_url()` to verify the page URL after an action.

## Example Test Structure
```python
import pytest
from playwright.async_api import Page, expect

@pytest.mark.asyncio
async def test_login_success(page: Page):
    # Arrange: Navigate to the login page
    await page.goto("https://example.com/login")

    # Act: Fill in credentials and submit the form
    logging.info("Fill in login form")
    await page.get_by_label("Username").fill("testuser")
    await page.get_by_label("Password").fill("securepassword")
    await page.get_by_role("button", name="Sign in").click()

    # Assert: Verify successful login
    logging.info("Verify successful login")
    await expect(page).to_have_url("https://example.com/dashboard")
    await expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
    
```
or simply:

```python
@pytest.mark.asyncio
async def test_user_can_login_successfully(login_session):
    page = login_session

    home_page = HomePage(page)
    await expect(home_page.user).to_be_visible(timeout=10000)

```
## Quality Checklist

Before finalizing tests, ensure:
- [ ] All locators are accessible and specific and avoid strict mode violations
- [ ] Tests are grouped logically and follow a clear structure
- [ ] Assertions are meaningful and reflect user expectations
- [ ] Tests follow consistent naming conventions
- [ ] Code is properly formatted and commented