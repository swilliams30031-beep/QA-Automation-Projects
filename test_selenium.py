from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Launch Chrome browser with anti-bot arguments
driver = webdriver.Chrome()

# 2. Navigate to Google
driver.get('https://www.google.com')

# 3. Locate the search bar element by its name attribute
search_box = driver.find_element(By.NAME, "q")

# 4. Action: Type query and press Enter
search_box.send_keys('Selenium QA Automation')
search_box.send_keys(Keys.RETURN)

# 5. Brief pause so you can visually watch the results page load
time.sleep(3)

# 6. Verification / Assertion check
if "Selenium" in driver.title:
    print("Test Passed: Search results page loaded successfully!")
else:
    print("Test FAILED: Title does not match search query.")

# 7. Clean teardown
driver.quit()