from selenium import webdriver

'''
    Factory for webdrivers for each browser, defaults to firefox
'''
class DriverFactory():
    def __init__(self, browser='ff',):
        self.browser = browser


    def get_web_driver(self):
        if self.browser.lower() == "ff" or self.browser.lower() == 'firefox':
            web_driver = webdriver.Firefox()
        elif self.browser.lower() == "ie":
            web_driver = webdriver.Ie()
        elif self.browser.lower() == "chrome":
            web_driver = webdriver.Chrome()
        else:
            print("DriverFactory does not know the browser: ", self.browser)
            web_driver = None
        return web_driver