from behave import *
import utilities as UT



@when('I search for yellow t shirts in the searchbar')
def step_impl(context):
    #Find , clear and then enter text into the search bar
    searchBox = context.driver.find_element_by_class_name("search-box")
    searchBox.clear()
    searchBox.send_keys("yellow shirt")
    searchBox.send_keys(context.keys.RETURN)



@when('I refine by "{searchTerm}"')
def step_impl(context, searchTerm):
    if searchTerm == 'women':
        gender = context.driver.find_element_by_xpath("//section[@id='productlist-results']/aside/div/div/div/ul/li[2]/a/span[2]")
    elif searchTerm == 'men':
        gender = context.driver.find_element_by_xpath("//section[@id='productlist-results']/aside/div/div/div/ul/li[2]/a/span")

    actions = context.ActionChains(context.driver)
    actions.click(gender)
    actions.perform()

@then('I should see some yellow t shirts for women')
def step_impl(context):
    # Loop through the items displayed on the page to see if they contain the word yellow
    assert UT.checkIfItemsArePresent(context.driver, 'name', 'yellow', True)






