from store_tests.data_structures.store_urls import TestUrl
from store_tests.page_objects.abstract_page import AbstractPage


class MainPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.base_url = TestUrl.STORE_BASE.value

    def open(self):
        self.go_to_url(self.base_url)

    def clear_webpage_cookies(self):
        self.clear_cookies(self.base_url)
