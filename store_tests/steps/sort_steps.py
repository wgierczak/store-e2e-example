from behave import then, when

from store_tests.page_objects.results_page import ResultsPage


@when('user sorts products by highest to lowest price')
def sort_by_highest(context):
    ResultsPage().sort_by_highest_first()


@then('products are sorted by highest to lowest price')
def verify_sort_desc(context):
    sorted_prices = ResultsPage().get_all_prices()
    sort_result = False
    for index in range(0, len(sorted_prices) - 1):
        if sorted_prices[index] >= sorted_prices[index+1]:
            sort_result = True
        else:
            break

    assert sort_result, "Products were not sorted properly"
