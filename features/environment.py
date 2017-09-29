from Pages import driverFactory as df
from Pages import basePage as bpo
from Pages import bag
from Pages import savedItem
from Pages import commonPage as cp
import logging

# Context is shared accross all instances of the test.


def before_all(context):
    if not context.config.log_capture:
        context.logging.basicConfig(level=logging.DEBUG)


def before_scenario(context, scenario):
    # Get the browser from the behave.ini file
    browser = context.config.userdata.get("browser", "firefox")

    # Get driver from driver factory
    context.driver = df.DriverFactory(browser=browser).get_web_driver()

    # Create a basePageObject and assign it to context
    context.basePageObject = bpo.BasePage(context.driver)
    context.bagPageObject = bag.Bag(context.driver)
    context.savedItemObject = savedItem.SavedItem(context.driver)
    context.commonPageObject = cp.CommonPage(context.driver)


def after_scenario(context, scenario):

    # Quit the driver after each test has been ran.
    context.driver.quit()