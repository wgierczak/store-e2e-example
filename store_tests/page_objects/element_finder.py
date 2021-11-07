from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from store_tests.config.web_driver import WebDriver


class ElementFinder:

    def __init__(self, condition):
        self.driver = WebDriver.get_driver()
        self.timeout = 30
        self.web_driver_wait = WebDriverWait(self.driver, self.timeout)
        self.condition = condition

    def create(self):
        return self.web_driver_wait.until(self.condition)


class VisibilityAllElements(ElementFinder):

    def __init__(self, locator_strategy: By, locator: str):
        super().__init__(ec.visibility_of_any_elements_located((locator_strategy, locator)))


class ClickableElement(ElementFinder):

    def __init__(self, locator_strategy: By, locator: str):
        super().__init__(ec.element_to_be_clickable((locator_strategy, locator)))
