class WrongUrlException(Exception):
    """Loaded page url is different than expected"""

    def __init__(self, current_url: str, expected_url: str):
        self.message = f"Current url is: {current_url}, expected url is: {expected_url}"
        super().__init__(self.message)
