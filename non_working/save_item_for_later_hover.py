from behave import *
import utilities as UT


# @given('I want to order a shirt from the australlian store')
# def step_impl(context):
#     context.driver.get("http://www.asos.com/au/")
#     assert "ASOS" in context.driver.title




# @when('I search for purple t shirts AUS')
# def step_impl(context):
#     websiteAddress = "http://www.asos.com/au/"
#     UT.clickOnMensShirts(context.driver, context.ActionChains, websiteAddress)
#     import time
#     time.sleep(60)
#     try:
#         purple = context.driver.find_element_by_xpath('//div[8]/div/div/ul/li[13]/a/span[1]')
#         purple.click()
#     except:
#         raise Exception("Cannot Click on Purple Checkbox")
#
#
# @when('I click on the save symbol')
# def step_impl(context):
#     import time
#     time.sleep(1)
#     try:
#         shirtPic = context.driver.find_element_by_xpath("//section[@id='productlist-results']/div/div[3]/ul/li[2]/a/div/img")
#         saveForLater = context.driver.find_element_by_css_selector(".save-later.js-save-later")
#         # dropdown.click()
#         actions = context.ActionChains(driver)
#         actions.move_to_element(shirtPic)
#         actions.click(saveForLater)
#         actions.perform()
#     except:
#         raise Exception("Cannot Click on Save Symbol")
#
#
# @then('I should see saved items in my saved item page')
# def step_impl(context):
#     # #Loop through the items displayed on the page to see if they contain the word Purple
#     # UT.checkSavedItems(context.driver)
#     pass
#
#
#
