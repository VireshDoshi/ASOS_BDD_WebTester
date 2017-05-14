from behave import *
import utilities as UT




@given('I want to order a shirt')
def step_impl(context):
    context.webAddress = "http://www.asos.com/"
    context.driver.get(context.webAddress)
    assert context.webAddress in context.driver.current_url

@when('I search for purple t shirts')
def step_impl(context):
    UT.clickOnMensShirts(context.driver, context.ActionChains, context.webAddress)

    #Click on the purple checkbox
    try:
        purple = context.driver.find_element_by_xpath('//div[8]/div/div/ul/li[13]/a/span[1]')
        purple.click()
    except:
        raise Exception("Cannot Click on Purple Checkbox")

@then('I should see some purple t shirts')
def step_impl(context):
    #Loop through the items displayed on the page to see if they contain the word Purple
    assert UT.checkIfItemsArePresent(context.driver, 'name', 'purple')





