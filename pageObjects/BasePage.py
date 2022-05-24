class BasePage(object):
    url = None

    def __init__(self,driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    @property
    def title(self):
        return self.driver.title

    def quit(self):
        self.driver.close()
        return None