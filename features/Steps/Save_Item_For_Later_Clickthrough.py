from behave import *


@given('I want to order a shirt from the australlian store')
def step_impl(context):
    context.savedItemObject.get("http://www.asos.com/au/")

@when('I search for purple t shirts AUS')
def step_impl(context):
    context.savedItemObject.clickOnMensShirts(context.driver.current_url)

    # Click on the purple checkbox
    context.savedItemObject.click_element('Xpath', '//div[8]/div/div/ul/li[13]/a/span[1]')

@when('I click on an image of a shirt to take me to the product page')
def step_impl(context):
    try:
        context.savedItemObject.click_element('Xpath', "//section[@id='productlist-results']/div/div[3]/ul/li/a/div/img")
    except:
        raise Exception("Cannot Click on The Shirt Image")

@when('I click the save symbol')
def step_impl(context):
    try:
        context.savedItemObject.click_element('Css', ".heartSecondary")
        context.savedItemObject.wait(3)
    except:
        raise Exception("Cannot Click on The Save Icon")

@then('I should see saved items in my saved item page')
def step_impl(context):

    # Check that saved items are in the saved items page.
    assert context.savedItemObject.checkSavedItems()



