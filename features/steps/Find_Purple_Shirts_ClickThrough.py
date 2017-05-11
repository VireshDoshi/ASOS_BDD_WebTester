from behave import *

import utilities as UT

@given('I want to order a shirt')
def step_impl(context):
    context.driver.get("http://www.asos.com")
    assert "ASOS" in context.driver.title



@when('I search for purple t shirts')
def step_impl(context):
    websiteAddress = "http://www.asos.com/"
    UT.clickOnMensShirts(context.driver, context.ActionChains, websiteAddress)

    try:
        purple = context.driver.find_element_by_xpath('//div[8]/div/div/ul/li[13]/a/span[1]')
        purple.click()
    except:
        raise Exception("Cannot Click on Purple Checkbox")



#not convinced this is the best way of confirming the new page but it's a start
#TODO - think of a better method
@then('I should see some purple t shirts')
def step_impl(context):
    #Loop through the items displayed on the page to see if they contain the word Purple
    UT.checkIfItemsArePresent(context.driver, 'name', 'purple', True)





