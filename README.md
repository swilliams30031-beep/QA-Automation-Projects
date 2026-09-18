# SauceDemo E2E Test Automation Framework

A modular, maintainable UI automation test suite built with Python, Selenium WebDriver, and PyTest using the Page Object Model (POM) architecture.

## 🚀 Features
- **Page Object Model (POM)** design pattern separating page elements/actions from test logic.
- **PyTest Fixtures** for centralized browser lifecycle management (setup and teardown).
- **Explicit Waits** utilizing `WebDriverWait` and `expected_conditions` to handle dynamic elements reliably.
- Automated valid and invalid login verification against the SauceDemo web application.

## 🛠️ Tech Stack
- **Language:** Python
- **Testing Framework:** PyTest
- **Automation Tool:** Selenium WebDriver (v4)

## 📁 Project Structure
```text
QA Automation Projects/
│
├── pages/
│ ├── base_page.py # Core wrapper for Selenium actions and explicit waits
│ └── login_page.py # Page object containing SauceDemo login locators & actions
│
├── tests/
│ ├── conftest.py # PyTest browser setup and teardown fixtures
│ └── test_login.py # Automated test cases for login scenarios
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation