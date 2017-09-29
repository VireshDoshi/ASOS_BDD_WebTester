"""
Page class that all page models can inherit from
There are useful wrappers for common Selenium operations
"""

import unittest
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class BasePage(unittest.TestCase):
    "Page class that all page models can inherit from"

    def __init__(self, selenium_driver):
        "Constructor"
        self.driver = selenium_driver
        self.driver.implicitly_wait(10)

    def get(self, base_url='http://www.asos.com/'):
        # Append a / if there isn't one
        if base_url[-1] != '/':
            base_url += '/'
        "Visit the page"
        self.base_url = self.driver.get(base_url)
        assert(base_url == str(self.driver.current_url))

    def open(self, url):

        "Visit the page base_url + url"
        url = self.base_url + url
        if self.driver.current_url != url:
            self.driver.get(url)
        self.assertEqual(url, self.driver.current_url)

    def get_xpath(self, xpath):

        "Return the DOM element of the xpath OR the 'None' object if the element is not found"
        dom_element = None
        dom_element = self.driver.find_element_by_xpath(xpath)
        return dom_element

    def get_class(self, className):

        "Return the DOM element of the class OR the 'None' object if the element is not found"
        dom_element = None
        dom_element = self.driver.find_element_by_class_name(className)
        return dom_element

    def get_class_elements(self, className):

        "Return the DOM element of the class elements OR the 'None' object if the element is not found"
        dom_element = None
        dom_element = self.driver.find_elements_by_class_name(className)
        return dom_element

    def get_css(self, css):
        """
        Return the DOM element of the css OR the 'None' object if the element is not found
        :param css:
        :return:
        """

        dom_element = None
        dom_element = self.driver.find_element_by_css_selector(css)
        return dom_element

    def click_element(self, arg, path):

        "Click the button supplied"
        link = self.returnElement(arg, path)
        if link is not None:
            try:
                link.click()
            except Exception as e:
                print('Exception when clicking link with xpath: %s' % path)
                print(e)
            else:
                return True

        return False

    def set_text(self, arg, path, value):
        "Set the value of the text field"
        text_field = self.returnElement(arg, path)
        try:
            text_field.clear()
        except Exception as e:
            print('ERROR: Could not clear the text field: %s' % path)

        text_field.send_keys(value)
        text_field.send_keys(Keys.RETURN)

    def returnElement(self, arg, path):
        if arg == 'Xpath':
            return self.get_xpath(path)
        elif arg == 'Css':
            return self.get_css(path)
        elif arg == 'Class':
            return self.get_class(path)
        else:
            return None

    def get_dom_text(self, dom_element):
        "Return the text of a given DOM element or the 'None' object if the element has no attribute called text"
        text = ''
        try:
            text = dom_element.text
        except Exception as e:
            print(e)
            return None
        else:
            return str(text)

    def select_dropdown_option(self, select_locator, option_text):
        """
        Selects the option in the drop-down

        :param select_locator:
        :param option_text:
        :return:
        """
        # dropdown = self.driver.find_element_by_id(select_locator)
        dropdown = self.driver.find_element_by_xpath(select_locator)

        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break


    def select_Item(self, xpath):
        selectedItem = Select(self.get_xpath(xpath))
        print(selectedItem)
        return selectedItem

    def changeCountry(self, countryXPath):
        countryMenu = self.get_class('selected-currency')
        country = self.get_xpath(countryXPath)

        actions = ActionChains(self.driver)
        actions.click(countryMenu)
        actions.click(country)
        actions.perform()


    def wait(self, wait_seconds=5):
        " Performs wait for time provided"
        time.sleep(wait_seconds)

    def teardown(self):
        " Tears down the driver"
        self.driver.quit()






    '''
    
        Utility Functions
        - checkIfItemsArePresent -> Gets a list of all products displayed and searches the text attached to them.
                                    If the text has our variable termToSearch in it then we can assume that the correct results are displayed.
        - clickOnMensShirts -> Takes the country to make the correct URL and then click on Men -> Shirts. This is used across many tests so makes it
                               in utilities.
        - checkSavedItems -> Checks if there is more than 0 items in the saved item list.
        - checkItemsInMyBag -> Check the subtotal price of your bag is greater than 00.00, this is how we assume that there is an item in your bag.
    
    
    '''


    def checkIfItemsArePresent(self, className, termToSearch):
        #TODO - cant just search name, needs to be product list
        self.wait(3)
        # Loop through all displayed clothes and see if it contains purple.
        listOfItems = self.get_class_elements(className)
        for i in listOfItems:
            name = i.text
            lowerCase = termToSearch.lower()
            firstLetterCapital = termToSearch[0].upper() + termToSearch.lower()
            if lowerCase or firstLetterCapital in name:
                print('Success!! ---> Found {} in product names'.format(termToSearch))
                return True

    def clickOnMensShirts(self, country):
        shirt = self.get_xpath('//a[@href="' + country + 'men/shirts/cat/?cid=3602"]')
        men = self.get_xpath('//a[@href="' + country + 'men/"]')

        actions = ActionChains(self.driver)
        actions.move_to_element(men)
        actions.click(shirt)
        actions.perform()



