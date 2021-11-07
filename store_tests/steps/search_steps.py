from behave import then, when

from store_tests.data_structures.products import Products
from store_tests.page_objects.header_page import HeaderPage
from store_tests.page_objects.product_page import ProductPage
from store_tests.page_objects.results_page import ResultsPage


@when('user search for "{product_type}"')
def search_for_shirt(context, product_type: str):
    header_elements = HeaderPage()
    header_elements.provide_product_name_to_searchbar(Products[product_type].value)
    header_elements.submit_search()


@when('user click on product')
def open_product_details(context):
    ResultsPage().open_first_product()


@then('shirt is available in results')
def verify_shirt_is_available_in_results(context):
    results = ResultsPage()
    assert results.is_any_product_visible(), "No product is available"
    assert results.is_product_type_valid(Products.SHIRT.value), \
        f"Different product was found - displayed product name: {results.get_product_name()}"


@then('details of product are displayed')
def verify_product_details_page(context):
    assert ProductPage().is_buy_block_visible(), "Product page was not properly loaded"
