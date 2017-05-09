from selenium import webdriver


class SeleniumWrapper(object):
    def __init__(self):
        # base_url = 'http://localhost:8000'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def quit(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def get(self, location=''):
        """
        navigate webdriver to different pages
        """
        self.driver.get(location)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)

    def find_by_class_name(self, className):
        '''
        find a class name in the DOM
        :param className: 
        :return: 
        '''
        return self.driver.find_element_by_class_name(className)

    def title(self):
        print(self.driver.title)
        return self.driver.title
