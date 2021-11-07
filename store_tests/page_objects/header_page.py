from store_tests.page_objects.abstract_element import ElementById, ElementByClass
from store_tests.page_objects.abstract_page import AbstractPage


class HeaderPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.search_bar_input = ElementById('search_query_top')
        self.submit_search_button = ElementByClass('button-search')
        self.dropdown_cart_checkout_button = ElementById('button_order_cart')
        self.cart_field = ElementByClass('ajax_cart_quantity')

    def provide_product_name_to_searchbar(self, product_name: str):
        self.search_bar_input.send_value(product_name)

    def submit_search(self):
        self.submit_search_button.click()

    def open_cart(self):
        self.cart_field.hover_over_element()
        self.dropdown_cart_checkout_button.click()
