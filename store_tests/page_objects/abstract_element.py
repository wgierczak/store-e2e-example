from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from store_tests.config.web_driver import WebDriver
from store_tests.page_objects.element_finder import VisibilityElement, ClickableElement


class AbstractElement:

    def __init__(self, locator_strategy: By, locator: str):
        self.locator_strategy = locator_strategy
        self.locator = locator
        self.driver = WebDriver.get_driver()

    def get_element(self) -> WebElement:
        return VisibilityElement(self.locator_strategy, self.locator).create()

    def get_clickable_element(self) -> WebElement:
        return ClickableElement(self.locator_strategy, self.locator).create()

    def click(self):
        self.get_element().click()

    def send_value(self, text_to_send: str, typing_speed: float = 0.05):
        selected_input = self.get_element()
        selected_input.click()
        selected_input.clear()
        for char in text_to_send:
            sleep(typing_speed)
            selected_input.send_keys(char)
