# from behave import *
# import utilities as UT
#
#
# @given('I want to order a shirt from the australlian store')
# def step_impl(context):
#     context.driver.get("http://www.asos.com/au/")
#     assert "ASOS" in context.driver.title
#
#
#
#
# @when('I search for purple t shirts AUS')
# def step_impl(context):
#     websiteAddress = "http://www.asos.com/au/"
#     UT.clickOnMensShirts(context.driver, context.ActionChains, websiteAddress)
#
#     try:
#         purple = context.driver.find_element_by_xpath('//div[8]/div/div/ul/li[13]/a/span[1]')
#         purple.click()
#     except:
#         raise Exception("Cannot Click on Purple Checkbox")
#
#
# @when('I change the currency to NZ Dollar')
# def step_impl(context):
#     try:
#         dropdown = context.driver.find_element_by_xpath("//section[@id='productlist-results']/div/div[3]/ul/li/a/div/div/div/span")
#         # currency = context.driver.find_element_by_xpath("//div[@id='localisationMenu']/div/div/select")
#         # currency.click()
#         dropdown.click()
#     except:
#         raise Exception("Cannot Click on Currency Checkbox")
#
