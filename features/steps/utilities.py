import time




def checkIfItemsArePresent(driver, className, termToSearch, stopAtFirstOccurance = False):
    #TODO - cant just search name, needs to be product list
    time.sleep(1)
    # Loop through all displayed clothes and see if it contains purple.
    listOfItems = driver.find_elements_by_class_name(className)
    for i in listOfItems:
        name = i.text
        lowerCase = termToSearch.lower()
        firstLetterCapital = termToSearch[0].upper() + termToSearch.lower()
        if lowerCase or firstLetterCapital in name:
            print('Success!!')
            if stopAtFirstOccurance:
                break