import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Verify login success by checking the target URL
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    #Verify error message for locked out user
    error_msg = login_page.get_error_text()
    assert "Epic sadface: Sorry, this user has been locked out." in error_msg