from basePage import BasePage
import logging

class CommonPage(BasePage):

    def selectCountryFromDropdown(self):
        """
        Method that selects the country from the dropdown which is located at the top right webpage
        """
        countryMenu = self.get_class('selected-currency')
        logging.debug("viresh debug")

        print countryMenu.get_attribute('innertHTML')

        # country = self.get_xpath(countryXPath)
        #
        # actions = ActionChains(self.driver)
        # actions.click(countryMenu)
        # actions.click(country)
        # actions.perform()

