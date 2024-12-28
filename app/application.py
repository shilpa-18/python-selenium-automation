from css_homework import driver
from pages.header import Header
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
