from behave import *

# Given is located in Find_Purple_Shirts_ClickThrough.py


@when('in the Australian store')
def step_impl(context):

    # Change Country
    context.basePageObject.changeCountry("//div[@id='siteSelectorList']/ul/li[6]/a")

    context.websiteAddress = "http://www.asos.com/au/"
    context.basePageObject.wait(2)
    assert context.websiteAddress in context.driver.current_url

@when('I search for yellow t shirts')
def step_impl(context):

    # Get to the mens shirts page
    try:
        context.basePageObject.clickOnMensShirts(context.websiteAddress)
    except:
        raise Exception("Failed to click on shirts")

    #Click on the yellow shirts checkbox
    try:
        #Click on the yellow checkbox
        context.basePageObject.click_element('Xpath', "//section[@id='productlist-results']/aside/div[8]/div/div/ul/li[19]/a/span[2]")
    except:
        raise Exception("Cannot Click on Yellow Checkbox")

@then('I should see some yellow t shirts')
def step_impl(context):

    #Loop through the items displayed on the page to see if they contain the word yellow
    assert context.basePageObject.checkIfItemsArePresent('name', 'yellow')





