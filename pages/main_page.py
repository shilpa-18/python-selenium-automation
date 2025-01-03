from pages.base_page import BasePage


class MainPage(BasePage):

    def open_main_page(self):
        self.open_url('https://www.target.com/')

    def search_product(self, product):
        self.input_text(self, 'christmas ornament santa')
        self.click()