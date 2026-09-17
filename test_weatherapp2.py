from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Hide the "Chrome is being controlled by automated test software" infobar
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    yield driver.quit()

def test_google_atlanta_weather(driver):
    #1. Open Google Chrome to Google.com
    driver.get("https://www.google.com")

    #2. Find the search bar and type "Atlanta weather"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Atlanta weather")
    search_box.send_keys(Keys.RETURN)

    #3. Verify the search executed
    WebDriverWait(driver,10).until(EC.title_contains("Atlanta weather"))
    assert "Atlanta weather" in driver.title
    print("\n[SUCCESS] Chrome launched, searched Google, and verified!")
