from behave import *


@when('I select a size')
def step_impl(context):
    try:
        #Select a size, in this case we want S - Chest 91-96 cm which is located at index 2 of the dropdown.
        size = context.bagPageObject.select_Item("//div[@id='product-size']/section/div/div/div[2]/select")

        size.select_by_visible_text('S - Chest 91-96 cm')
        selectedSize = size.all_selected_options
        assert selectedSize[0].text == 'S - Chest 91-96 cm'
    except:
        raise Exception("Cannot Click on The Size DropDown Icon")

@when('I Click on add to bag')
def step_impl(context):
    try:
        context.bagPageObject.click_element('Xpath', "//div[@id='product-add']/div/a/span[2]")
    except:
        raise Exception("Cannot Click on The Add To Bag Icon")

@then('I should see saved items in my basket item page')
def step_impl(context):

    #Option1 -> Check the quantity in next to the checkout/ basket icon
    #-------------------------------------------------------------------------
    context.bagPageObject.checkBagQuantity()


    #Option2 -> Go to the checkout / basket page and check if there are items in the bag
    # -------------------------------------------------------------------------
    try:
        context.bagPageObject.clickOnBag()
    except:
        raise Exception("Cannot Click on The Bag Icon")

    #Checks if there are items in the bag
    assert context.bagPageObject.checkItemsInMyBag()

