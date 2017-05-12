from behave import *
import time
import utilities as UT

#TODO - remove time.sleep


#Given is located in Find_Purple_Shirts_ClickThrough.py

@when('in the Australian store')
def step_impl(context):
    countryMenu = context.driver.find_element_by_class_name('selected-currency')
    aus = context.driver.find_element_by_xpath("//div[@id='siteSelectorList']/ul/li[6]/a")


    actions = context.ActionChains(context.driver)
    actions.click(countryMenu)
    actions.click(aus)
    actions.perform()

@when('I search for yellow t shirts')
def step_impl(context):
    websiteAddress = "http://www.asos.com/"
    time.sleep(2)
    assert websiteAddress in context.driver.current_url

    try:
        UT.clickOnMensShirts(context.driver, context.ActionChains, websiteAddress)
    except:
        raise Exception("Failed to click on shirts")

    try:
        yellow = context.driver.find_element_by_xpath("//section[@id='productlist-results']/aside/div[8]/div/div/ul/li[19]/a/span[2]")
        yellow.click()
    except:
        raise Exception("Cannot Click on Yellow Checkbox")



#not convinced this is the best way of confirming the new page but it's a start
#TODO - think of a better method
@when('I should see some yellow t shirts')
def step_impl(context):
    #Loop through the items displayed on the page to see if they contain the word Purple
    UT.checkIfItemsArePresent(context.driver, 'name', 'yellow', True)





