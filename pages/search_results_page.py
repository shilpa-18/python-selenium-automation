from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from target_search_coffee import actual_result


class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def verify_search_results(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

    def verify_cart_empty(self, locator):
        actual_result = self.find_element(*self.CART_ICON).text
        assert actual_result == '', f'Expected cart empty {actual_result}'