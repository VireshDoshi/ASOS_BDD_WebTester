from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException

import time

def before_scenario(context, scenario):
    driver = webdriver.Firefox()
    context.driver = driver
    context.driver.implicitly_wait(10)
    context.keys = Keys
    context.WebDriverWait = WebDriverWait
    context.EC = EC
    context.TimeoutException = TimeoutException
    context.ActionChains = ActionChains
    context.Select = Select
    context.time = time


def after_scenario(context, scenario):
    #Quit the driver after each test has been ran.
    context.driver.quit()
