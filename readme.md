# Selenium Testing with Behave in Python

![behave output](files/behave_console_output.png?raw=true)
Note: The instructions provided will work on Centos 7. ( I have moved all dev work to Centos 7 from a MAC )
New changes in this forked version contain information on how to run this project in an isolated python virtual environment and dockerised Selenium Grid

## Pre-requisites
You will need to have python installed. In my case, I have python 2.7.10 installed.
Docker and Docker-compose installed.

## Python Virtual environment 

For more details, take a look at http://virtualenvwrapper.readthedocs.io/en/latest/install.html
```
$ sudo pip install virtualenvwrapper


$ export WORKON_HOME=$HOME/.virtualenvs
$ export PROJECT_HOME=$HOME/Devel
$ source /bin/virtualenvwrapper.sh ( use which command to locate this on your linux distro)

$ mkvirtualenv bdd_env1
$ workon bdd_env1
$ pip install -r requirements.txt
```

The following pip packages are required which are shown here for information.
```
$ pip freeze 
 
behave==1.2.5
page-objects==1.1.0
selenium==3.4.3

```
## Selenium Grid Setup
Selenium Grid activation is done via docker using docker-compose files. This selenium grid contains a Chrome and Firefox browser.
```
$ cd env/
$ docker-compose up  ( with -d for detached mode)

# to shutdown selenium grid
$ docker-compose down 
```
Navigate to http://localhost:4444/grid/console to see the selenium Grid frontend
## Execution

In terminal / cmd
```
cd into ASOS_BDD_WebTester
$ behave
```

## Expected outcome
```
(env1) vireshdoshi@vireshs-MacBook-Air:~/py_projects/ASOS_BDD_WebTester$ behave
Feature: Use the website to add an item to my bag # features/Feature_Files/Add_Item_To_Bag.feature:1
  So that I can order a shirt
  As a customer
  I want to be able to add an item to my bag
  Scenario: Search for t shirts and add one to my bag                 # features/Feature_Files/Add_Item_To_Bag.feature:6
    Given I want to order a shirt from the australlian store          # features/steps/Save_Item_For_Later_Clickthrough.py:4 7.530s
    When I search for purple t shirts AUS                             # features/steps/Save_Item_For_Later_Clickthrough.py:9 9.503s
    And I click on an image of a shirt to take me to the product page # features/steps/Save_Item_For_Later_Clickthrough.py:17 4.688s
    And I select a size                                               # features/steps/Add_Item_To_Bag.py:4 0.796s
    And I Click on add to bag                                         # features/steps/Add_Item_To_Bag.py:15 0.282s
    Then I should see saved items in my basket item page              # features/steps/Add_Item_To_Bag.py:22 8.946s

Feature: Use the website to find products in the Australian store # features/Feature_Files/Find_AUS_Shirts.feature:1
  So that I can order a shirt
  As an Australian customer
  I want to be able to find t shirts in my store
  Scenario: Search for t shirts in Australian store  # features/Feature_Files/Find_AUS_Shirts.feature:6
    Given I want to order a shirt                    # features/steps/Find_Purple_Shirts_ClickThrough.py:4 4.018s
    When in the Australian store                     # features/steps/Find_AUS_Shirts.py:6 2.888s
    When I search for yellow t shirts                # features/steps/Find_AUS_Shirts.py:15 11.972s
      Traceback (most recent call last):
        File "/Users/vireshdoshi/.virtualenvs/env1/lib/python2.7/site-packages/behave/model.py", line 1456, in run
          match.run(runner.context)
        File "/Users/vireshdoshi/.virtualenvs/env1/lib/python2.7/site-packages/behave/model.py", line 1903, in run
          self.func(context, *args, **kwargs)
        File "features/steps/Find_AUS_Shirts.py", line 28, in step_impl
          raise Exception("Cannot Click on Yellow Checkbox")
      Exception: Cannot Click on Yellow Checkbox

    Then I should see some yellow t shirts           # None

Feature: Use the website to find shirts # features/Feature_Files/Find_Purple_Shirts_ClickThrough.feature:1
  So that I can order a shirt
  As a customer
  I want to be able to find t shirts
  Scenario: Search for t shirts            # features/Feature_Files/Find_Purple_Shirts_ClickThrough.feature:6
    Given I want to order a shirt          # features/steps/Find_Purple_Shirts_ClickThrough.py:4 7.984s
    When I search for purple t shirts      # features/steps/Find_Purple_Shirts_ClickThrough.py:10 0.797s
    Then I should see some purple t shirts # features/steps/Find_Purple_Shirts_ClickThrough.py:18 9.383s

Feature: Use the website to find shirts # features/Feature_Files/Find_Purple_Shirts_SearchBar.feature:1
  So that I can order a shirt
  As a customer
  I want to be able to find t shirts
  Scenario: Search for t shirts                         # features/Feature_Files/Find_Purple_Shirts_SearchBar.feature:6
    Given I want to order a shirt                       # features/steps/Find_Purple_Shirts_ClickThrough.py:4 3.631s
    When I search for purple t shirts via the searchbar # features/steps/Find_Purple_Shirts_SearchBar.py:4 0.340s
    Then I should see some purple t shirts              # features/steps/Find_Purple_Shirts_ClickThrough.py:18 3.066s

Feature: Use the website to change how search results are displayed # features/Feature_Files/Find_Yellow_Shirts_Women.feature:1
  So that I can select my yellow t shirts
  I want to be able to refine search by gender
  Scenario: Display search results of yellow shirts for women  # features/Feature_Files/Find_Yellow_Shirts_Women.feature:6
    Given I want to order a shirt                              # features/steps/Find_Purple_Shirts_ClickThrough.py:4 8.223s
    When I search for yellow t shirts in the searchbar         # features/steps/Find_Yellow_Shirts_Women.py:4 0.460s
    And I refine by "women"                                    # features/steps/Find_Yellow_Shirts_Women.py:10 4.204s
    Then I should see some yellow t shirts for women           # features/steps/Find_Yellow_Shirts_Women.py:18 3.088s

Feature: Use the website to save an item for later. # features/Feature_Files/Save_Item_For_Later_ClickThrough.feature:1
  So that I can order a shirt
  As a customer
  I want to be able to save an item for later
  Scenario: Search for t shirts and save for later                    # features/Feature_Files/Save_Item_For_Later_ClickThrough.feature:6
    Given I want to order a shirt from the australlian store          # features/steps/Save_Item_For_Later_Clickthrough.py:4 8.736s
    When I search for purple t shirts AUS                             # features/steps/Save_Item_For_Later_Clickthrough.py:9 5.762s
    And I click on an image of a shirt to take me to the product page # features/steps/Save_Item_For_Later_Clickthrough.py:17 5.023s
    And I click the save symbol                                       # features/steps/Save_Item_For_Later_Clickthrough.py:25 3.379s
    Then I should see saved items in my saved item page               # features/steps/Save_Item_For_Later_Clickthrough.py:34 5.105s




```
## BDD ( Behaviour Driven Development) basics
Tests start with writing "Feature" files that use plain english to describe the steps of your test. Features use keywords to form the actual steps being taken in the test:

* **Given** we put the system in a known state before the user (or external system) starts interacting with the system (in the When steps). Avoid talking about user interaction in givens.

* **When** we take key actions the user (or external system) performs. This is the interaction with your system which should (or perhaps should not) cause some state to change.

* **Then** we observe outcomes.

Within the 'Feature_Files' directory are all of the feature scenarios used for testing. They describe interactions with the website and map directly to functions to perform the actions.

These feature files are name the same as the python files located in the 'Steps' directory.
The python files are where the functions to perform website operations are stored.
 These files call on factory classes with a generic base set of functions are located which aid with wrapping common functions in one place, the factory files are found in Page_Objects.
 There is current a base class -> basePage which then is inherited by two other classes to extend functionality specific to that page:

            '''
            basePage   --> bag (bag operations)
                       --> savedItem (saved item operations)
            '''

## How does this work?

environment.py - defines the codes to be executed before or after the events


## Notes
```
useful link to selenium geckodriver
https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
```
