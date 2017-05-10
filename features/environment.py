from seleniumWrapper import SeleniumWrapper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def before_all(context):
  driver = webdriver.Firefox()
  driver.implicitly_wait(10)
  context.driver = driver
  context.keys = Keys


def after_all(context):
  # context.driver.quit()
    pass