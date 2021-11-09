from behave import given

from store_tests.data_structures.footer_sections import FooterSection
from store_tests.page_objects.footer_page import FooterPage


@given('user is in "{footer_section}" section')
def navigate_to_section(context, footer_section: str):
    FooterPage(FooterSection[footer_section].value).open_section()
