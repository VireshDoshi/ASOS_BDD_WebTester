from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException





def before_all(context):
    driver = webdriver.Firefox()
    context.driver = driver
    context.driver.implicitly_wait(10)
    context.keys = Keys
    context.WebDriverWait = WebDriverWait
    context.EC = EC
    context.TimeoutException = TimeoutException
    context.ActionChains = ActionChains


def after_all(context):
    context.driver.quit()
