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
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3']").click()
sleep(7)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(10)

