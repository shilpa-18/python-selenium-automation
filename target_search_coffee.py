from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#search and click
driver.get("https://www.target.com/")
driver.find_element(By.ID, "search" ).send_keys('coffee')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(10)

#verifiction
expected_result = 'coffee'
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

print(actual_result)

sleep(10)