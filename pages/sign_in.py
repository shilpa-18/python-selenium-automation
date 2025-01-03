from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignIn(BasePage):
    SIGN_IN_PAGE = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")

    def verify_sign_in_page_opened(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_PAGE)
