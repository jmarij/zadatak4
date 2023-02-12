from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By

@given('Launch chrome browser')
def launchChrome(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('Open webpage phptravels')
def openHome(context):
    context.driver.get("https://www.phptravels.net/")

@then('Verify Logo present')
def verifyLogo(context):
    status=context.driver.find_element(By.XPATH, "//div[@class='logo']//img[@alt='logo']").is_displayed()
    assert status is True

@then('Close browser')
def closeChrome(context):
    context.driver.close()