from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify at least 10 benefit cells are shown')
def verify_benefit_cells(context):
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components/CellsComponent/Link']")
    print('\nFind Elements')
    print(cells)
    print(len(cells))
    #assert len(cells) == int(expected_cells), f'Expected {expected_cells} links but got {len(cells)}'
