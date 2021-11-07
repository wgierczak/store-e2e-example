class UrlContains:

    def __init__(self, url: str):
        self.url = url

    def __call__(self, driver) -> bool:
        return self.url.rstrip("/") in driver.current_url
