from seleniumWrapper import SeleniumWrapper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def before_all(context):
  context.driver = webdriver.Firefox()
  context.keys = Keys


def after_all(context):
  # context.driver.quit()
    pass