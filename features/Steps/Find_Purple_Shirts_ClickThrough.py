from behave import *


@given('I want to order a shirt')
def step_impl(context):
    # Go to the asos.com
    context.basePageObject.get()


@when('I search for purple t shirts')
def step_impl(context):
    context.basePageObject.clickOnMensShirts(context.driver.current_url)

    # Click on the purple checkbox
    context.basePageObject.click_element('Xapth', '//div[8]/div/div/ul/li[13]/a/span[1]')


@then('I should see some purple t shirts')
def step_impl(context):
    #Loop through the items displayed on the page to see if they contain the word Purple
    assert context.basePageObject.checkIfItemsArePresent('name', 'purple')




