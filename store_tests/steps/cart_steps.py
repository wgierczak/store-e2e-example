from typing import Callable

from behave import then, when

from store_tests.data_structures.products import Products
from store_tests.page_objects.added_item_modal_page import AddedItemModalPage
from store_tests.page_objects.cart_page import CartPage
from store_tests.page_objects.header_page import HeaderPage
from store_tests.page_objects.results_page import ResultsPage


@when('user adds product to cart')
def add_product_to_cart(context):
    results = ResultsPage()
    results.add_product_to_cart()
    AddedItemModalPage().close_modal()
    context.cart.append(results.get_product_name())


@when('user opens checkout sections')
def open_cart(context):
    HeaderPage().open_cart()


@when('user change quantity of "{product_name}" to "{quantity:d}"')
def set_item_quantity(context, product_name: str, quantity: int):
    product_index = CartPage(context).get_product_index(Products[product_name].value)
    cart = CartPage(context, product_index)
    __set_number(quantity, cart.get_item_quantity, cart.increase_item_quantity,
                 cart.decrease_item_quantity)


@when('user removes "{product_name}" from cart')
def remove_product_from_cart(context, product_name: str):
    product_to_remove_index = CartPage(context).get_product_index(Products[product_name].value)
    CartPage(context, product_to_remove_index).remove_item()


@then('quantity of "{product_name}" is "{quantity_of_product:d}"')
def verify_quantity_of_product(context, product_name: str, quantity_of_product: int):
    product_to_check_index = CartPage(context).get_product_index(Products[product_name].value)
    actual_item_quantity = CartPage(context, product_to_check_index).get_item_quantity()
    assert actual_item_quantity == quantity_of_product, f"Expected quantity of product is: {quantity_of_product}, " \
                                                        f"displayed quantity is: {actual_item_quantity}"


@then('number of unique products in cart is "{number_of_products:d}"')
def verify_number_of_products_in_cart(context, number_of_products: int):
    displayed_items_quantity = CartPage(context).get_number_of_items()
    assert number_of_products == displayed_items_quantity, \
        f"Invalid number of products in cart - expected quantity: {number_of_products}, " \
        f"displayed items quantity: {displayed_items_quantity}"


def __set_number(expected_number: int, current_number_method: Callable, increase_number_method: Callable,
                 decrease_number_method: Callable):
    current_number = current_number_method()
    while current_number != expected_number:
        if current_number < expected_number:
            increase_number_method()
        else:
            decrease_number_method()
        current_number = current_number_method()
