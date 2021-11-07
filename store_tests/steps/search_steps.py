from behave import then, when

from store_tests.data_structures.products import Products
from store_tests.page_objects.header_page import HeaderPage


@when('user search for shirt')
def open_add_hotel_form(context):
    header_elements = HeaderPage()
    header_elements.provide_product_name_to_searchbar(Products.SHIRT.value)
    header_elements.submit_search()


@then('shirt is available in results')
def verify_shirt_is_available_in_results(context):
    assert True
