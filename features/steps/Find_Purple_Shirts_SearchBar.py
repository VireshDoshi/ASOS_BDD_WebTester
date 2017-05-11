# from behave import *
#
#
# @given('I want to order a shirt')
# def step_impl(context):
#     context.driver.get("http://www.asos.com")
#     assert "ASOS" in context.driver.title
#
#
#
# @when('I search for purple t shirts')
# def step_impl(context):
#     searchBox = context.driver.find_element_by_class_name("search-box")
#     searchBox.clear()
#     searchBox.send_keys("purple shirt")
#     searchBox.send_keys(context.keys.RETURN)
#
#
# #not convinced this is the best way of confirming the new page but it's a start
# #TODO - think of a better method
# @then('I should see some purple t shirts')
# def step_impl(context):
#     try:
#         context.WebDriverWait(context.driver, 3).until(
#             context.EC.title_contains("purple shirt"))
#     except context.TimeoutException:
#         raise Exception("Loading took too much time!")
#
