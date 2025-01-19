from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

@given('Click on Deals')
def check_deals(context):
    context.driver.find_element(By.XPATH,'[data-test="@web/Header/MainMenuLink"]').click()

@when('Click on Top deals')
def top_deals(context):
    context.driver.find_element(By.XPATH,'//a[data-test="deals-topDeals"]').click()

@then('Verify user is on the Top deals page')
def top_deals_page(context):
    expected_result = 'Top Deals'
    actual_result = context.driver.find_element(By.XPATH,'[data-test="page-title"]')
    print(actual_result)
    sleep(10)










