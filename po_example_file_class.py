class Page:

    def click(self, locator):
        print(f'Clicking by {locator}')

    def find_element(self, locator):
        print(f'Searching by {locator}')

    def input_text(self, locator, text):
        print(f'Inputting {text} by {locator}')


page = Page()
page.click()
