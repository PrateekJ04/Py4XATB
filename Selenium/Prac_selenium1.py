import time

from selenium import webdriver

# Invoking a browser and validating its page source details and printing the current URL
driver = webdriver.Chrome()
driver.get(" https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()
time.sleep(3)
pg_src = driver.page_source
current_url = driver.current_url
print(f"The current URL is : {current_url}")
assert pg_src.__contains__("CURA Healthcare Service")
