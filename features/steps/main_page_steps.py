from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SIGN_IN = (By.XPATH, "//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3']")
SIGN_IN_PAGE = (By.XPATH, "//button[@data-test='accountNav-signIn']")


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(10)
    context.app.main_page.search_product(product)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Click on Sign in')
def click_sign_in(context):
    context.app.header.click_sign_in()

@when('Click on Sign in page')
def click_sign_in_page(context):
    context.app.header.click_sign_in_page()

@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)

@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'