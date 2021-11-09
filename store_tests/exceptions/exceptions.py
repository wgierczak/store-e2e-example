class WrongUrlException(Exception):
    """Loaded page url is different than expected"""

    def __init__(self, current_url: str, expected_url: str):
        self.message = f"Current url is: {current_url}, expected url is: {expected_url}"
        super().__init__(self.message)


class NoItemInCartException(Exception):
    """Item is not in cart"""

    def __init__(self, item_name: str):
        self.message = f"Item - {item_name} - is not in cart"
        super().__init__(self.message)


class NoSectionException(Exception):
    """Section is not in footer"""

    def __init__(self, section_name: str):
        self.message = f"Section - {section_name} - is not in footer"
        super().__init__(self.message)
