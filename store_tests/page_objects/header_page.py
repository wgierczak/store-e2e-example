from store_tests.page_objects.abstract_element import ElementById, ElementByClass
from store_tests.page_objects.abstract_page import AbstractPage


class HeaderPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.search_bar_input = ElementById('search_query_top')
        self.submit_search_button = ElementByClass('button-search')

    def provide_product_name_to_searchbar(self, product_name: str):
        self.search_bar_input.send_value(product_name)

    def submit_search(self):
        self.submit_search_button.click()
