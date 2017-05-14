'''

    Utility Functions
    - checkIfItemsArePresent -> Gets a list of all products displayed and searches the text attached to them.
                                If the text has our variable termToSearch in it then we can assume that the correct results are displayed.
    - clickOnMensShirts -> Takes the country to make the correct URL and then click on Men -> Shirts. This is used across many tests so makes it
                           in utilities.
    - checkSavedItems -> Checks if there is more than 0 items in the saved item list.
    - checkItemsInMyBag -> Check the subtotal price of your bag is greater than 00.00, this is how we assume that there is an item in your bag.


'''

import time



def checkIfItemsArePresent(driver, className, termToSearch):
    #TODO - cant just search name, needs to be product list
    time.sleep(3)
    # Loop through all displayed clothes and see if it contains purple.
    listOfItems = driver.find_elements_by_class_name(className)
    for i in listOfItems:
        name = i.text
        lowerCase = termToSearch.lower()
        firstLetterCapital = termToSearch[0].upper() + termToSearch.lower()
        if lowerCase or firstLetterCapital in name:
            print('Success!! ---> Found {} in product names'.format(termToSearch))
            return True

def clickOnMensShirts(driver, actionChains, country):
    shirt = driver.find_element_by_xpath('//a[@href="' + country + 'men/shirts/cat/?cid=3602"]')
    men = driver.find_element_by_xpath('//a[@href="' + country + 'men/"]')

    actions = actionChains(driver)
    actions.move_to_element(men)
    actions.click(shirt)
    actions.perform()

def checkSavedItems(driver):
    savedItemsLink = driver.find_element_by_xpath("//body[@id='BodyTag']/div[4]/div/header/div[5]/ul/li[3]/a")
    savedItemsLink.click()
    time.sleep(3)

    #Find all the saved items in a list
    listOfSavedItems = driver.find_elements_by_class_name('savedItem-item-messages')
    if len(listOfSavedItems) > 0:
        print('Success!! ---> Found saved item in product names')
        return True

def checkItemsInMyBag(driver):
    time.sleep(3)
    # Find the Subtotal price and we assume if the item value is >00.00 then there is an item there.
    subTotalPrice = driver.find_element_by_class_name("bag-subtotal-price")
    if subTotalPrice.text[1:] != '00.00':
        print('Success!! ---> Found items in bag')
        return True
