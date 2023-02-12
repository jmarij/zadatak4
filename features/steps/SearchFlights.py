from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Navigate to Flights')
def step_impl(context):
    context.driver.get("https://www.phptravels.net/flights")

@when('Enter Flight "{search}" to "{search2}"')
def step_impl(context, search, search2):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='autocomplete']")))
    city1 = context.driver.find_element(By.XPATH, "//input[@id='autocomplete']")
    city1.send_keys(search)
    city2 = context.driver.find_element(By.XPATH, "//input[@id='autocomplete2']")
    city2.send_keys(search2)

@when('Search Flights')
def step_impl(context):
    search = context.driver.find_element(By.XPATH, "//button[@id='flights-search']")
    search.click()

@then('List of Flights is visible')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Book Now')]")))
    flights = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Book Now')]").is_displayed()
    assert flights is True
