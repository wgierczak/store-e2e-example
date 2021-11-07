from selenium.webdriver import Chrome, ChromeOptions

from store_tests.config.configuration import Configuration


class WebDriver:
    driver = None

    @staticmethod
    def start_driver(configuration: Configuration):
        WebDriver.driver = WebDriverConfigurator(configuration).provide_driver()


class WebDriverConfigurator:

    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def provide_driver(self):
        driver = Chrome(chrome_options=self.__get_chrome_options())
        return driver

    def __get_chrome_options(self) -> ChromeOptions:
        chrome_options = ChromeOptions()
        chrome_options.add_argument(self.configuration.chrome_browser_language)
        chrome_options.add_argument(self.configuration.chrome_window_size)
        chrome_options.add_argument(self.configuration.chrome_enable_logging)
        chrome_options.headless = self.configuration.headless_mode
        return chrome_options
