from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Search for and add {items} to the cart')
def search_items(context, items):
    context.driver.find_element(By.ID, 'search').send_keys(items)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='product-title']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()

@then('Verify that the search results shown for {items}')
def verify_search_results(context, items):
    context.driver.find_element(By.ID,'cart-summary-heading').text
    sleep(5)
    #assert items in actual_result, f'Expected text {items} not in actual {actual_result}'

