import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Automatically downloads & manages the driver binary via Selenium 4
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()