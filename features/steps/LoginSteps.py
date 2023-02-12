from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Verify account visible')
def verifyAccountButton(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ACCOUNT']")))
    status = context.driver.find_element(By.XPATH, "//button[@id='ACCOUNT']").is_displayed()
    assert status is True

@then('Click account')
def clickAccount(context):
    element = context.driver.find_element(By.XPATH, "//button[@id='ACCOUNT']")
    element.click()
    element2 = context.driver.find_element(By.XPATH, "//a[normalize-space()='Customer Login']")
    element2.click()

@when('Enter username "{username}" and password "{pwd}"')
def enterUser(context, username, pwd):
    user = context.driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    password = context.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    user.clear()
    user.send_keys(username)
    password.clear()
    password.send_keys(pwd)
    element3 = context.driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
    element3.click()

@then('Profile picture visible')
def verifyPicture(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='user']")))
    status = context.driver.find_element(By.XPATH, "//img[@alt='user']").is_displayed()
    assert status is True
