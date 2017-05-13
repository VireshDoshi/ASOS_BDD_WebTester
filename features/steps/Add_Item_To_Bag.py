from behave import *
import utilities as UT




@when('I select a size')
def step_impl(context):
    try:
        #Select a size, in this case we want S - Chest 91-96 cm which is located at index 2 of the dropdown.
        size = context.Select(context.driver.find_element_by_xpath("//div[@id='product-size']/section/div/div/div[2]/select"))
        size.select_by_index(2)
        selectedSize = size.all_selected_options
        assert selectedSize[0].text == 'S - Chest 91-96 cm'
    except:
        raise Exception("Cannot Click on The Size DropDown Icon")

@when('I Click on add to bag')
def step_impl(context):
    try:
        addToBagIcon = context.driver.find_element_by_xpath("//div[@id='product-add']/div/a/span[2]")
        addToBagIcon.click()
    except:
        raise Exception("Cannot Click on The Add To Bag Icon")

@then('I should see saved items in my basket item page')
def step_impl(context):

    #Option1 -> Check the quantity in next to the checkout/ basket icon
    #-------------------------------------------------------------------------
    context.time.sleep(4)
    quantity = context.driver.find_element_by_class_name('bag-link-quantity')
    #Strip the () from the quantity and cast it to an int for compare
    assert int(quantity.text.strip('(').strip(')')) > 0


    #Option2 -> Go to the checkout / basket page and check if there are items in the bag
    # -------------------------------------------------------------------------
    try:
        myBag = context.driver.find_element_by_xpath("//li[@id='miniBagApp']/div/div/a/span")
        myBag.click()

    except:
        raise Exception("Cannot Click on The Bag Icon")

    #Checks if there are items in the bag
    assert UT.checkItemsInMyBag(context.driver)

