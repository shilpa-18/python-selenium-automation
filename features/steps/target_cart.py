from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open target main page")
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when("click Sign In")
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@when("click on cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()
    sleep(5)


@then("verify Sign In form opened")
def verify_sign_in(context):
    sleep(5)
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'h1 span').text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@then("verify 'your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected text {expected_result} did not match {actual_result}'


