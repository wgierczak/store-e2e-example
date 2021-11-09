from behave import then, when

from store_tests.page_objects.contact_page import ContactPage
from store_tests.string_utilities.random_string import RandomString


@when('user provides correct email')
def provide_correct_email_in_contact_form(context):
    correct_email = 'test_email@example.com'
    ContactPage().provide_email(correct_email)


@when('user provides wrong email')
def provide_wrong_email_in_contact_form(context):
    wrong_email = RandomString().choose_letters_and_numbers(10)
    contact_form = ContactPage()
    contact_form.provide_email(wrong_email)
    contact_form.click_on_blank_space()


@when('user fills rest of form')
def fill_contact_form(context):
    contact_form = ContactPage()
    random_string = RandomString()
    contact_form.select_subject_option()
    contact_form.provide_order_reference(random_string.choose_letters(8))
    contact_form.provide_message(random_string.choose_letters(20))


@when('clicks on send button')
def submit_contact_form(context):
    ContactPage().send_contact_us_form()


@then('warning about wrong email is displayed')
def verify_form_error_is_displayed(context):
    assert ContactPage().is_form_error_visible(), "Form error is not visible"


@then('success message is visible')
def verify_success_message_is_displayed(context):
    assert ContactPage().is_success_message_visible(), "Success message is not visible"


@then('error message is visible')
def verify_error_message_is_displayed(context):
    assert ContactPage().is_error_message_visible(), "Error message is not visible"
