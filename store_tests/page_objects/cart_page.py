from time import sleep
from typing import Optional

from behave.runner import Context

from store_tests.exceptions.exceptions import NoItemInCartException
from store_tests.page_objects.abstract_element import ElementByXpath, ElementByClass
from store_tests.page_objects.abstract_page import AbstractPage


class CartPage(AbstractPage):

    def __init__(self, context: Context, default_index: Optional[int] = 0):
        super().__init__()
        self.context = context
        self.index = default_index
        self.item = ElementByClass('cart_item')
        self.remove_item_button = ElementByClass('icon-trash')
        self.increase_item_quantity_button = ElementByClass('icon-plus')
        self.decrease_item_quantity_button = ElementByClass('icon-minus')
        self.number_of_items = ElementByClass('cart_quantity_input')

    def get_number_of_items(self) -> int:
        return len(self.item.get_list_of_elements())

    def get_product_index(self, product_name: str) -> int:
        for item_name in self.context.cart:
            if product_name in item_name.lower():
                return self.context.cart.index(item_name)
        raise NoItemInCartException(product_name)

    def remove_item(self):
        self.remove_item_button.click(self.index)
        sleep(4)

    def increase_item_quantity(self):
        self.increase_item_quantity_button.click(self.index)
        sleep(2)

    def decrease_item_quantity(self):
        self.decrease_item_quantity_button.click(self.index)
        sleep(2)

    def get_item_quantity(self) -> int:
        item_quantity = int(self.number_of_items.get_element_value(self.index))
        return item_quantity

    @staticmethod
    def is_product_visible(product_name: str) -> bool:
        product_visibility = ElementByXpath(f"//div[contains(text(),'{product_name}')]").is_visible()
        return product_visibility
