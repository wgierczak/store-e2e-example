from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from store_tests.conditions.custom_expected_conditions import UrlContains
from store_tests.config.web_driver import WebDriver
from store_tests.exceptions.exceptions import WrongUrlException


class AbstractPage:

    def __init__(self):
        self.driver = WebDriver.get_driver()

    def go_to_url(self, url: str):
        self.driver.get(url)

    def get_url(self) -> str:
        return self.driver.current_url

    def wait_for_url_contains(self, part_of_url: str, timeout: int = 20, raise_exception: bool = False) -> bool:
        return self.__wait_for_url(UrlContains, part_of_url, timeout, raise_exception)

    def clear_cookies(self, domain: str):
        self.go_to_url(domain)
        self.wait_for_url_contains(domain)
        self.driver.delete_all_cookies()

    def run_javascript(self, script: str):
        self.driver.execute_script(script)

    def click_on_blank_space(self):
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()

    def __wait_for_url(self, expected_condition: ec, url: str, timeout: int, raise_exception: bool) -> bool:
        try:
            return WebDriverWait(self.driver, timeout).until(expected_condition(url))
        except TimeoutException as timeout_exception:
            if raise_exception:
                raise WrongUrlException(self.get_url(), url) from timeout_exception
            return False
