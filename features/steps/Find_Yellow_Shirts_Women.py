from behave import *

import utilities as UT

@when('I search for yellow t shirts in the searchbar')
def step_impl(context):
    searchBox = context.driver.find_element_by_class_name("search-box")
    searchBox.clear()
    searchBox.send_keys("yellow shirt")
    searchBox.send_keys(context.keys.RETURN)



@when('I refine by gender - women')
def step_impl(context):
    women = context.driver.find_element_by_xpath("//div[@class='facetvalue-name' and text()='WOMEN']")
    #TODO - Find this XPath

    actions = context.ActionChains(context.driver)
    actions.click(women)
    actions.perform()




#not convinced this is the best way of confirming the new page but it's a start
#TODO - think of a better method
@then('I should see some yellow t shirts for women')
def step_impl(context):
    #Loop through the items displayed on the page to see if they contain the word Purple
    UT.checkIfItemsArePresent(context.driver, 'name', 'purple', True)





