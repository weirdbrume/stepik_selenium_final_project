# task - https://stepik.org/lesson/238819/step/2?unit=211271


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
