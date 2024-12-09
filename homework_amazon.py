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

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
#driver.find_element(By.ID, "twotabsearchtextbox" ).send_keys('coffee')
#driver.find_element(By.XPATH, "//class[@aria-label='Amazon']").click()
driver.find_element(By.ID, "ap_email").click()
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "legalTextRow").click()
driver.find_element(By.ID, "auth-fpp-link-bottom").click()
driver.find_element(By.ID, "ap-other-signin-issues-link").click()
driver.find_element(By.ID, "createAccountSubmit").click()

sleep(20)