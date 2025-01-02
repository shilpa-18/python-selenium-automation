from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN = (By.XPATH, "//span[@class='sc-58ad44c0-3 kkWqdY h-margin-r-x3']")
    SIGN_IN_PAGE = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self, *locator):
        self.click(*self.CART_ICON)
        sleep(10)

    def click_sign_in(self, *locator):
        self.click(*self.SIGN_IN)
        sleep(10)

    def click_sign_in_page(self, *locator):
        self.click(*self.SIGN_IN_PAGE)
        sleep(10)
