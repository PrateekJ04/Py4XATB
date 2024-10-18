import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Invoking a browser and validating url change and log in into application
driver = webdriver.Chrome()
driver.get(" https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()
time.sleep(3)
curnt_url = driver.current_url
print(f"This is current url: {curnt_url}")
mk_apmt_btn = driver.find_element(By.ID, "btn-make-appointment")
mk_apmt_btn.click()
time.sleep(3)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("John Doe")
password.send_keys("ThisIsNotAPassword")
submit = driver.find_element(By.ID, "btn-login")
submit.click()
changed_url = driver.current_url
print(f"This is changed url: {changed_url}")
assert curnt_url is not changed_url
