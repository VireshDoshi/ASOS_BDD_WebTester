from behave import *
import utilities as UT




@when('I select a size')
def step_impl(context):
    try:
        # size = context.driver.find_element_by_xpath("//div[@id='product-size']/section/div/div/div[2]/select")
        size = context.Select(context.driver.find_element_by_xpath("//div[@id='product-size']/section/div/div/div[2]/select"))
        size.select_by_index(2)
        selectedSize = size.all_selected_options
        assert selectedSize[0].text == 'S - Chest 91-96 cm'
    except:
        raise Exception("Cannot Click on The Size DropDown Icon")


@when('I Click on add to bag')
def step_impl(context):
    try:
        saveIcon = context.driver.find_element_by_xpath("//div[@id='product-add']/div/a/span[2]")
        saveIcon.click()
    except:
        raise Exception("Cannot Click on The Save Icon")


@then('I should see saved items in my basket item page')
def step_impl(context):
    #Option1
    context.time.sleep(4)

    quantity = context.driver.find_element_by_class_name('bag-link-quantity')
    assert int(quantity.text.strip('(').strip(')')) > 0


    try:
        myBag = context.driver.find_element_by_xpath("//li[@id='miniBagApp']/div/div/a/span")
        myBag.click()

    except:
        raise Exception("Cannot Click on The Bag Icon")
    # #Loop through the items displayed on the page to see if they contain the word Purple
    UT.checkItemsInMyBag(context.driver)
    # # pass
