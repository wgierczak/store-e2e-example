from typing import Optional

from store_tests.page_objects.abstract_element import ElementByClass
from store_tests.page_objects.abstract_page import AbstractPage


class CompareProductsPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.product_block = ElementByClass('product-block')

    def is_product_block_visible(self, index: Optional[int] = None) -> bool:
        return self.product_block.is_visible(index)
