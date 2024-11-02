import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()


@pytest.mark.registration
@allure.title("Create Account/Register new User")
@allure.description("Verify if User is getting registered and Success response is notified")
def test_validate_registration():
    # optns = Options()
    driver = webdriver.Chrome()
    # optns.add_argument('--start-maximized')
    # optns.add_argument("--disable-extensions")
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    first_name.send_keys(fake.first_name())
    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.send_keys(fake.first_name())
    email_id = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
    email_id.send_keys(fake.email())
    telephone = driver.find_element(By.NAME, "telephone")
    telephone.send_keys(fake.random_int(000000, 999999, 5))
    pswd = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    pswd.send_keys("test123")
    cnfrm_pswd = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    cnfrm_pswd.send_keys("test123")
    subscribe_newsletter = driver.find_element(By.XPATH, "(.//input[@value='1'])[2]")
    subscribe_newsletter.click()
    privacy_checkbox = driver.find_element(By.NAME, "agree")
    privacy_checkbox.click()
    continue_button = driver.find_element(By.XPATH, "//*[@type='submit']")
    continue_button.click()
    success_message = driver.find_element(By.XPATH, "//div/h1").text
    print("Title of the Page is: ", driver.title)
    print("Text to be validated is: ", success_message)
    assert success_message.__eq__("Your Account Has Been Created!")

@pytest.mark.signin
@allure.title("Error message validation in VWO log in page ")
@allure.description("Verify if proper error message is displayed in Vwo login page when entered invalid creds")
def test_vwo_login_with_invalid_creds():
    choptions = Options()
    choptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    choptions.add_experimental_option("useAutomationExtension", "False")
    choptions.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=choptions)

    driver.maximize_window()
    time.sleep(3)
    driver.get("https://app.vwo.com/")
    username = driver.find_element(By.NAME, "username")
    username.send_keys("xyzabc@test.com")
    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys("test123")
    time.sleep(2)
    signin_btn = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    signin_btn.click()
    time.sleep(5)
    alert_message = driver.find_element(By.ID, "js-notification-box-msg").text
    print(alert_message)
    assert alert_message.__eq__("Your email, password, IP address or location did not match")

