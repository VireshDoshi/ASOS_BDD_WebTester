# Selenium Testing with Behave in Python


To get started, we'll need to ensure that Behave is installed. The easiest means of doing so is with Pip:

```
pip install Behave
```

Alternatively you can read [installation documenation](http://pythonhosted.org/behave/install.html) on the Behave website. 


Next, we'll need to install Selenium:

```
pip install selenium
```

Finally, we'll need to install gekodriver from :
https://github.com/mozilla/geckodriver/releases
 (place this in your python directory).



Tests start with writing "Feature" files that use plain english to describe the steps of your test. Features use keywords to form the actual steps being taken in the test:

* **Given** we put the system in a known state before the user (or external system) starts interacting with the system (in the When steps). Avoid talking about user interaction in givens.

* **When** we take key actions the user (or external system) performs. This is the interaction with your system which should (or perhaps should not) cause some state to change.

* **Then** we observe outcomes.

Within the 'Feature_Files' directory are all of the feature scenarios used for testing. They describe interactions with the website and map directly to functions to perform the actions.

These feature files are name the same as the python files located in the 'steps' directory. The python files are where the functions to perform website operations are stored. They are mainly using basic selenium opertaions to locate elements on the screen and perform actions on them to emulate a user e.g()
```
    #Search "purple shirt" in the search box by typing in the text and pressing enter. 
    searchBox = context.driver.find_element_by_class_name("search-box")
    searchBox.clear()
    searchBox.send_keys("purple shirt")
    searchBox.send_keys(context.keys.RETURN)
    
```

Finally there is a Utilities .py file that holds some utility functions to help with tests:
'''

    Utility Functions
    - checkIfItemsArePresent -> Gets a list of all products displayed and searches the text attached to them.
                                If the text has our variable termToSearch in it then we can assume that the correct results are displayed.
    - clickOnMensShirts -> Takes the country to make the correct URL and then click on Men -> Shirts. This is used across many tests so makes it
                           in utilities.
    - checkSavedItems -> Checks if there is more than 0 items in the saved item list.
    - checkItemsInMyBag -> Check the subtotal price of your bag is greater than 00.00, this is how we assume that there is an item in your bag.


'''

Note: Some of these functions seem slow and clunky to me (checkSavedItems, checkItemsInMyBag) but with the idea of them I feel could be adapted to be quite useful.
