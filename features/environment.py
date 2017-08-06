from Page_Objects import driverFactory as DF
from Page_Objects import basePage as BPO
from Page_Objects import bag
from Page_Objects import savedItem

# Context is shared accross all instances of the test so we assing certain variable to it here.


def before_scenario(context, scenario):
    # Get driver from driver factory
    context.driver = DF.DriverFactory().get_web_driver()
    # Create a basePageObject and assign it to context
    context.basePageObject = BPO.BasePage(context.driver)
    context.bagPageObject = bag.Bag(context.driver)
    context.savedItemObject = savedItem.SavedItem(context.driver)


def after_scenario(context, scenario):
    # Quit the driver after each test has been ran.
    context.driver.quit()