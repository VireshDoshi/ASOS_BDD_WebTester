from behave import *
import utilities as UT




@when('I select a size')
def step_impl(context):
    try:
        # size = context.driver.find_element_by_xpath("//div[@id='product-size']/section/div/div/div[2]/select")
        size = context.Select(context.driver.find_element_by_xpath("//div[@id='product-size']/section/div/div/div[2]/select")).select_by_value("label=XXS - Chest 32-34in (81-86cm)").click()
        # shirtPic.click()
    except:
        raise Exception("Cannot Click on The Shirt Image")


@when('I Click on add to bag')
def step_impl(context):
    try:
        saveIcon = context.driver.find_element_by_xpath("//div[@id='product-add']/div/a/span[2]")
        saveIcon.click()
    except:
        raise Exception("Cannot Click on The Save Icon")


@then('Then I should see saved items in my saved item page')
def step_impl(context):
    myBag = context.driver.find_element_by_xpath("//li[@id='miniBagApp']/div/div/a/span[2]")
    myBag.click()
    # #Loop through the items displayed on the page to see if they contain the word Purple
    UT.checkItemsInMyBag(context.driver)
    # pass
