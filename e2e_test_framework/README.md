# E2E Test Framework (Playwright Python Async)

A modern, scalable end-to-end (E2E) test automation framework using Playwright (Python, async), pytest, and Page Object Model (POM).

## Structure

- `tests/`: E2E test cases
- `pages/`: Page Object Model classes
- `fixtures/`: Pytest fixtures (browser, login session, etc.)
- `utils/`: Utilities (data generation, logging)
- `configs/`: Environment configs, URLs, credentials
- `prompts/`: Prompts for Copilot test generation

## Getting Started

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run tests:
   ```sh
   pytest tests/
   ```

---

- Follows Playwright, pytest, and POM best practices.
- Async/await everywhere.
- No hardcoded credentials in code.
