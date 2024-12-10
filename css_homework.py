from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Damazoncombr%26hvadid%3D707411630105%26hvdev%3Dc%26hvlocphy%3D9067608%26hvnetw%3Dg%26hvqmt%3Db%26hvrand%3D10348232344390084205%26hvtargid%3Dkwd-341221644399%26hydadcr%3D15247_13597165%26tag%3Dgooghydr-20%26ref%3Dnav_ya_signin&prevRID=BFEPX01BMZDSWE0SP8A4&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute.nav-input')

driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

driver.find_element(By.CSS_SELECTOR, 'a-row.a-spacing-base')

driver.find_element(By.CSS_SELECTOR, "label[for='ap_password']")

driver.find_element(By.CSS_SELECTOR, "label[for='ap_password_check']")

driver.find_element(By.CSS_SELECTOR, ".a-button-input")

driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")



