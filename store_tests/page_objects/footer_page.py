from store_tests.page_objects.abstract_element import ElementByPartialLink
from store_tests.page_objects.abstract_page import AbstractPage


class FooterPage(AbstractPage):

    def __init__(self, section_name: str):
        super().__init__()
        self.section = ElementByPartialLink(section_name)

    def open_section(self):
        self.section.click()
