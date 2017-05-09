from behave import *


@given('I want to order a shirt')
def step_impl(context):
    context.driver.get("http://www.asos.com")
    print(context.driver.title)
    assert "ASOS" in context.driver.title



@when('I search for purple t shirts')
def step_impl(context):
    searchBox = context.driver.find_element_by_class_name("search-box")
    searchBox.clear()
    searchBox.send_keys("purple shirt")
    searchBox.send_keys(context.keys.RETURN)


@then('I should see some purple t shirts')
def step_impl(context):
    pass
    # context.driver.quit()