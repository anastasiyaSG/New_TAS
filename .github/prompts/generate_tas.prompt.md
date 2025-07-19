---
mode: agent
---
# 🚀 Prompt for GitHub Copilot: Generate New E2E Test (Playwright + Python + POM + Async)

## 🔧 Project Rules

You are generating test cases for an async Playwright Python automation project, written using `pytest` and **Page Object Model (POM)**. Each test must be:

- Fully asynchronous using `async def` and `await`.
- Written using the **Playwright Python async API** only.
- Built using POM classes from the `/pages/` directory.
- Clean, maintainable, and production-level.
- Structured with **Arrange → Act → Assert** logic.
- Use `pytest` fixtures for setup and teardown.
- Use `pytest.mark.asyncio` for async tests.
- Use `pytest.mark.parametrize` for data-driven tests.
- Include meaningful assertions to verify application behavior.
- Use `pytest` for test discovery and execution.
- Follow the **naming conventions** outlined below.

## ✨ Naming Conventions

- Test functions: `test_user_can_*`, `test_should_*`, etc.
- Page classes: PascalCase (`LoginPage`, `CheckoutPage`)
- Methods in pages: snake_case (`fill_form`, `submit_login`)
- Use type hints and docstrings for all methods.

## ✅ Copilot Test Generation Prompt

> Use this when asking Copilot to write a new test:

**Prompt:**

