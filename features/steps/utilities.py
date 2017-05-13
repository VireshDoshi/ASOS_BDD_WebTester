




def checkIfItemsArePresent(driver, className, termToSearch, stopAtFirstOccurance = False):
    #TODO - cant just search name, needs to be product list
    context.time.sleep(3)
    # Loop through all displayed clothes and see if it contains purple.
    listOfItems = driver.find_elements_by_class_name(className)
    for i in listOfItems:
        name = i.text
        lowerCase = termToSearch.lower()
        firstLetterCapital = termToSearch[0].upper() + termToSearch.lower()
        if lowerCase or firstLetterCapital in name:
            print('Success!! ---> Found {} in product names'.format(termToSearch))
            if stopAtFirstOccurance:
                break


def clickOnMensShirts(driver, actionChains, country):


    shirt = driver.find_element_by_xpath('//a[@href="' + country + 'men/shirts/cat/?cid=3602"]')
    men = driver.find_element_by_xpath('//a[@href="' + country + 'men/"]')


    actions = actionChains(driver)
    actions.move_to_element(men)
    actions.click(shirt)
    actions.perform()

def checkSavedItems(driver):
    context.time.sleep(3)
    # Loop through all displayed clothes and see if it contains purple.
    listOfSavedItems = driver.find_elements_by_class_name('savedItem-item-messages')
    if len(listOfSavedItems) > 0:
        print('Success!! ---> Found saved item in product names')


def checkItemsInMyBag(driver):
    context.time.sleep(3)
    # Find the Subtotal price and we assume if the item value is >00.00 then there is an item there.
    subTotalPrice = driver.find_element_by_class_name("bag-subtotal-price")
    if subTotalPrice.text[1:] != '00.00':
        print('Success!! ---> Found items in bag')