from behave import *


@when('I search for yellow t shirts in the searchbar')
def step_impl(context):
    #Find , clear and then enter text into the search bar
    context.basePageObject.set_text('Class', "search-box", "yellow shirt")


@when('I refine by "{searchTerm}"')
def step_impl(context, searchTerm):
    if searchTerm == 'women':
        context.basePageObject.click_element('Xpath', "//section[@id='productlist-results']/aside/div/div/div/ul/li[2]/a/span[2]")
    elif searchTerm == 'men':
        context.basePageObject.click_element('Xpath', "//section[@id='productlist-results']/aside/div/div/div/ul/li[2]/a/span")


@then('I should see some yellow t shirts for women')
def step_impl(context):
    # Loop through the items displayed on the page to see if they contain the word yellow
    assert context.basePageObject.checkIfItemsArePresent('name', 'yellow')






