from typing import Optional, List

from store_tests.conditions.wait_until import wait_until
from store_tests.page_objects.abstract_element import ElementByClass, ElementByXpath
from store_tests.page_objects.abstract_page import AbstractPage


class ResultsPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.product_container = ElementByClass('product-container')
        self.more_details_button = ElementByClass('lnk_view')
        self.add_to_cart_button = ElementByClass('ajax_add_to_cart_button')
        self.product_link = ElementByClass('product_img_link')
        self.add_to_compare_button = ElementByClass('add_to_compare')
        self.compare_button = ElementByClass('bt_compare')
        self.quantity_of_products_to_compare = ElementByClass('total-compare-val')
        self.sort_options_desc = "#selectProductSort > option:nth-child(3)"
        self.product_price = ElementByXpath('//div[@class="product-container"]//span[@class="price product-price"]')

    def is_any_product_visible(self) -> bool:
        return self.product_container.is_visible()

    def get_number_of_products(self) -> len:
        return len(self.product_container.get_list_of_elements())

    def open_product(self, index: Optional[int] = None):
        self.product_container.hover_over_element(index)
        self.more_details_button.click(index)

    def add_product_to_cart(self, index: Optional[int] = None):
        self.product_container.hover_over_element(index)
        self.add_to_cart_button.click(index)

    def is_product_type_valid(self, desired_type_of_product: str) -> bool:
        product_full_name = self.product_link.get_element_title()
        return desired_type_of_product in product_full_name

    def get_product_name(self, index: Optional[int] = None) -> str:
        return self.product_link.get_element_title(index)

    def add_product_to_compare(self, index: Optional[int] = None):
        self.product_container.hover_over_element(index)
        products_to_compare_before_click = self.get_quantity_of_products_to_compare()
        self.add_to_compare_button.click(index=0)
        wait_until(lambda: self.get_quantity_of_products_to_compare() == products_to_compare_before_click + 1,
                   timeout=10, raise_exception=False)

    def get_quantity_of_products_to_compare(self) -> int:
        return int(self.quantity_of_products_to_compare.get_text())

    def open_compare_page(self):
        self.compare_button.click()

    def sort_by_highest_first(self):
        sorted_url = self.get_url() + '&orderby=price&orderway=desc'
        self.go_to_url(sorted_url)

    def get_price_without_currency(self, index: Optional[int] = None) -> float:
        string_price = self.product_price.get_text(index)
        price = float(string_price.replace("$", ''))
        return price

    def get_all_prices(self) -> List[float]:
        number_of_products = self.get_number_of_products()
        all_prices = []
        for index in range(0, number_of_products):
            self.get_price_without_currency(index)
            all_prices.append(self.get_price_without_currency(index))
        return all_prices
