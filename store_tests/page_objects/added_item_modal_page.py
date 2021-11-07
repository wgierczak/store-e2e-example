from store_tests.page_objects.abstract_element import ElementByClass
from store_tests.page_objects.abstract_page import AbstractPage


class AddedItemModalPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.close_button = ElementByClass('cross')

    def close_modal(self):
        self.close_button.click()
