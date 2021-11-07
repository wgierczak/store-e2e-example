from behave.model import Scenario
from behave.runner import Context

from store_tests.config.configuration import Configuration
from store_tests.config.web_driver import WebDriver
from store_tests.page_objects.main_page import MainPage


def before_all(context: Context):
    context.configuration = Configuration()


def before_feature(context: Context):
    WebDriver.start_driver(context.configuration)
    context.driver = WebDriver.get_driver()


def before_scenario(context: Context, scenario: Scenario):
    main_page = MainPage()
    main_page.open()
    main_page.clear_webpage_cookies()
    context.scenario_name = scenario.name


def after_feature():
    WebDriver.stop()
