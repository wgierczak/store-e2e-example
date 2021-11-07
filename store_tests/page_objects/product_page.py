from store_tests.page_objects.abstract_element import ElementById
from store_tests.page_objects.abstract_page import AbstractPage


class ProductPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.buy_block = ElementById('buy_block')

    def is_buy_block_visible(self) -> bool:
        return self.buy_block.is_visible()
