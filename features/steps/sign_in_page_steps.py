from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify Sign in form opened")
def verify_sign_in_page_opened(context):
    context.app.sign_in_page.open()