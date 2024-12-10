from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open target main page")
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when("click on the cart icon")
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'.sc-e487bf3b-1.iZzjLF').click()
    sleep(5)

@then("verify your cart is empty message is shown")
def verify_cart_empty(context):
    expected_result = 'cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.fJliSz").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'

