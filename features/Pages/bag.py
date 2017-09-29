from basePage import BasePage

'''
    Utility Function
    - checkItemsInMyBag -> Check the subtotal price of your bag is greater than 00.00, this is how we assume that there is an item in your bag.
    - checkBagQuantity -> Check the amount of items in the bag.
    - clickOnBag -> Clicks on the bag icon.
'''
# Inherits base Page and extends functionality


class Bag(BasePage):

    def checkItemsInMyBag(self):
        self.wait(3)
        # Find the Subtotal price and we assume if the item value is >00.00 then there is an item there.
        subTotalPrice = self.get_class("bag-subtotal-price")

        if subTotalPrice.text[1:] != '00.00':
            print('Success!! ---> Found items in bag')
            return True

    def checkBagQuantity(self):
        self.wait(4)
        quantity = self.get_class('bag-link-quantity')
        # Strip the () from the quantity and cast it to an int for compare
        assert int(quantity.text.strip('(').strip(')')) > 0

    def clickOnBag(self):
        self.click_element('Xpath', "//li[@id='miniBagApp']/div/div/a/span")