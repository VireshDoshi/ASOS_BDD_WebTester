from behave import *


@given('I want to order a shirt')
def step_impl(context):
    context.driver.get("http://www.asos.com")
    assert "ASOS" in context.driver.title



@when('I search for purple t shirts')
def step_impl(context):
    # searchBox = context.driver.find_element_by_class_name("search-box")
    # searchBox.clear()
    # searchBox.send_keys("purple shirt")
    # searchBox.send_keys(context.keys.RETURN)
    test = context.driver.find_element_by_xpath('//a[@href="http://www.asos.com/men/shirts/cat/?cid=3602"]')
    men = context.driver.find_element_by_xpath('//a[@href="http://www.asos.com/men/"]')
    actions = context.ActionChains(context.driver)
    actions.move_to_element(men)
    actions.click(test)
    actions.perform()
    purple = context.driver.find_element_by_xpath('//div[8]/div/div/ul/li[13]/a/span[1]')
    purple.click()
    print(purple.is_selected())

#not convinced this is the best way of confirming the new page but it's a start
#TODO - think of a better method
@then('I should see some purple t shirts')
def step_impl(context):
    try:
        context.WebDriverWait(context.driver, 3).until(
            context.EC.title_contains("purple shirt"))
    except context.TimeoutException:
        raise Exception("Loading took too much time!")

