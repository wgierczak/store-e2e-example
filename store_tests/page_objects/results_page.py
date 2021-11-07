from store_tests.page_objects.abstract_element import ElementByClass
from store_tests.page_objects.abstract_page import AbstractPage


class ResultsPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.product_container = ElementByClass('product-container')
        self.product_image_container = ElementByClass('lnk_view')
        self.product_link = ElementByClass('product_img_link')

    def is_any_product_visible(self) -> bool:
        return self.product_container.is_visible()

    def open_first_product(self):
        self.product_container.hover_over_element()
        self.product_image_container.click()

    def is_product_valid_type(self, desired_type_of_product: str) -> bool:
        product_full_name = self.product_link.get_element_title()
        return desired_type_of_product in product_full_name

    def get_product_name(self) -> str:
        return self.product_link.get_element_title()
