from behave import *
import utilities as UT




#Given is located in Find_Purple_Shirts_ClickThrough.py

@when('in the Australian store')
def step_impl(context):
    countryMenu = context.driver.find_element_by_class_name('selected-currency')
    aus = context.driver.find_element_by_xpath("//div[@id='siteSelectorList']/ul/li[6]/a")


    actions = context.ActionChains(context.driver)
    actions.click(countryMenu)
    actions.click(aus)
    actions.perform()

    context.websiteAddress = "http://www.asos.com/au/"
    context.time.sleep(2)
    assert context.websiteAddress in context.driver.current_url

@when('I search for yellow t shirts')
def step_impl(context):
    #Get to the mens shirts page
    try:
        UT.clickOnMensShirts(context.driver, context.ActionChains, context.websiteAddress)
    except:
        raise Exception("Failed to click on shirts")

    #Click on the yellow shirts checkbox
    try:
        yellow = context.driver.find_element_by_xpath("//section[@id='productlist-results']/aside/div[8]/div/div/ul/li[19]/a/span[2]")
        yellow.click()
    except:
        raise Exception("Cannot Click on Yellow Checkbox")

@then('I should see some yellow t shirts')
def step_impl(context):
    #Loop through the items displayed on the page to see if they contain the word yellow
    assert UT.checkIfItemsArePresent(context.driver, 'name', 'yellow', True)





