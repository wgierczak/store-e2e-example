from store_tests.page_objects.abstract_element import ElementById, ElementByClass, ElementByXpath
from store_tests.page_objects.abstract_page import AbstractPage


class ContactPage(AbstractPage):

    def __init__(self):
        super().__init__()
        self.subject_dropdown = ElementById('uniform-id_contact')
        self.subject_dropdown_options = ElementByXpath('//*[@id="id_contact"]')
        self.email_input = ElementById('email')
        self.order_reference_input = ElementById('id_order')
        self.message_input = ElementById('message')
        self.send_button = ElementById('submitMessage')
        self.success_message = ElementByClass('alert-success')
        self.error_message = ElementByClass('alert-danger')
        self.form_error = ElementByClass('form-error')

    def provide_email(self, email: str):
        self.email_input.send_value(email)

    def provide_order_reference(self, order_reference: str):
        self.order_reference_input.send_value(order_reference)

    def provide_message(self, message: str):
        self.message_input.send_value(message)

    def click_on_subject_dropdown(self):
        self.subject_dropdown.click()

    def select_subject_option(self):
        self.run_javascript('document.querySelector("#id_contact").options.remove(0)')
        self.subject_dropdown.click()

    def send_contact_us_form(self):
        self.send_button.click()

    def is_form_error_visible(self) -> bool:
        return self.form_error.is_visible()

    def is_error_message_visible(self) -> bool:
        return self.error_message.is_visible()

    def is_success_message_visible(self) -> bool:
        return self.success_message.is_visible()
