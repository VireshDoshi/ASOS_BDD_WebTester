from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


'''
    Factory for webdrivers for each browser, defaults to firefox
'''


class DriverFactory():

    def __init__(self, browser='firefox',):
        self.browser = browser

    def get_web_driver(self):
        if self.browser.lower() == "ff" or self.browser.lower() == 'firefox':
            web_driver = webdriver.Firefox()
        elif self.browser.lower() == "ie":
            web_driver = webdriver.Ie()
        elif self.browser.lower() == "chrome":
            web_driver = webdriver.Chrome()
        elif self.browser.lower() == "remote":
            desired_caps = {'platform': 'LINUX', 'browserName': 'chrome'} 
      	    web_driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=desired_caps )
        else:
            print("DriverFactory does not know the browser: ", self.browser)
            web_driver = None
        return web_driver
