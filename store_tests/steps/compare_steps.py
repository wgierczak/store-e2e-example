from behave import then, when

from store_tests.conditions.wait_until import wait_until
from store_tests.page_objects.compare_products_page import CompareProductsPage
from store_tests.page_objects.results_page import ResultsPage


@when('user adds "{product_display_index:d}" displayed product from list for comparison')
def add_product_to_cart(context, product_display_index: int):
    index_to_click = product_display_index - 1
    ResultsPage().add_product_to_compare(index_to_click)


@when('user clicks on compare button')
def open_compare_page(context):
    ResultsPage().open_compare_page()


@then('number of products to compare is "{products_to_compare:d}"')
def verify_number_of_products_to_compare(context, products_to_compare: int):
    wait_until(lambda: ResultsPage().get_quantity_of_products_to_compare() == products_to_compare, timeout=10,
               raise_exception=False)
    actual_number_of_products_to_compare = ResultsPage().get_quantity_of_products_to_compare()
    assert actual_number_of_products_to_compare == products_to_compare, \
        f"Wrong number of products to compare, expected quantity: {actual_number_of_products_to_compare}, " \
        f"expected number: {products_to_compare}"


@then('two products are available in comparison page')
def verify_number_of_products_in_comparison_page(context):
    compare_products = CompareProductsPage()
    assert compare_products.is_product_block_visible() and compare_products.is_product_block_visible(1), \
        "One of products is not available for comparison"
