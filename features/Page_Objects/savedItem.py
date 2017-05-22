
from Page_Objects.basePage import BasePage

'''

    Utility Function
     - checkSavedItems -> Checks if there is more than 0 items in the saved item list.


'''
#Inherits base Page and extends functionality
class SavedItem(BasePage):

    def checkSavedItems(self):
        self.click_element('Xpath', "//body[@id='BodyTag']/div[4]/div/header/div[5]/ul/li[3]/a")
        self.wait(3)

        #Find all the saved items in a list
        listOfSavedItems = self.get_class_elements('savedItem-item-messages')
        if len(listOfSavedItems) > 0:
            print('Success!! ---> Found saved item in product names')
            return True


