from behave import *




@when('I search for purple t shirts via the searchbar')
def step_impl(context):
    searchBox = context.driver.find_element_by_class_name("search-box")
    searchBox.clear()
    searchBox.send_keys("purple shirt")
    searchBox.send_keys(context.keys.RETURN)
