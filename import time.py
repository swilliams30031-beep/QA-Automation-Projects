import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#1. Start Chrome
driver = webdriver.Chrome()


try:
    # 2. Go to the login page and maximize
    driver.get("https:the-internet.herokuapp.com/login")
    driver.maximize_window()
    time.sleep(2)

    # 3. Enter Username using ID
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # 4. Enter Password using ID
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # 5. Click the Login Button using CSS Selector, "button[type='submit']"
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # 6. Pause so you can see the success banner
    time.sleep(4)

finally:
    # 7. Close browser clean
    driver.quit()
