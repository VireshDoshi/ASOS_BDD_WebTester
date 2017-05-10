from behave import *


@given('I want to order a shirt')
def step_impl(context):
    context.driver.get("http://www.asos.com")
    context.implicitly_wait(10)
    assert "ASOS" in context.driver.title



@when('I search for purple t shirts')
def step_impl(context):
    searchBox = context.driver.find_element_by_class_name("search-box")
    print(searchBox.text)
    searchBox.clear()
    searchBox.send_keys("purple shirt")
    searchBox.send_keys(context.keys.RETURN)


@then('I should see some purple t shirts')
def step_impl(context):
    # import time
    # time.sleep(2)
    print (context.driver.current_url)
    assert context.driver.current_url == 'http://www.asos.com/search/purple-shirt?q=purple+shirt'
    pass
    # context.driver.quit()