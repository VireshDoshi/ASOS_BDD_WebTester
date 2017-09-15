# Selenium Testing with Behave in Python


New changes in this forked version contain information on how to run this project in an isolated python virtual environment. 

## Pre-requisites
You will need to have python installed. In my case, I have python 2.7.10 installed.

## Python Virtual environment 
```
$ sudo pip install virtualenvwrapper

$ mkvirtualenv env1
$ workon env1
$ pip install -r requirements.txt
```

The following pip packages are required which are shown here for information.
```
$ pip freeze 
 

ansible==2.3.1.0
asn1crypto==0.22.0
bcrypt==3.1.3
behave==1.2.5
cffi==1.10.0
cryptography==2.0
enum34==1.1.6
idna==2.5
ipaddress==1.0.18
Jinja2==2.9.6
MarkupSafe==1.0
page-objects==1.1.0
paramiko==2.2.1
parse==1.8.2
parse-type==0.3.4
pyasn1==0.2.3
pycparser==2.18
pycrypto==2.6.1
PyNaCl==1.1.2
PyYAML==3.12
selenium==3.4.3
six==1.10.0

```
## Manual setup ( skip if using python virtual env)
To get started, we'll need to ensure that Behave is installed. The easiest means of doing so is with Pip:

```
$ pip install Behave
```

Alternatively you can read [installation documenation](http://pythonhosted.org/behave/install.html) on the Behave website. 


Next, we'll need to install Selenium:

```
$ pip install selenium
```

## Install the geckodriver

Finally, we'll need to install gekodriver from :
https://github.com/mozilla/geckodriver/releases
 (place this in your python directory).
 ```
$ wget 
$ cp ~/geckodriver ~/.virtualenvs/env1/bin/python
```

## Execution

In terminal / cmd
```
cd into ASOS_BDD_WebTester
$ behave
```




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

## Notes
```
useful link to selenium geckodriver
https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
```