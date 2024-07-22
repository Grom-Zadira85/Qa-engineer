import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://victoretc.github.io/webelements_information/?"


def test_auth_positive():
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "username")
    input1.send_keys("Grom")

    input2 = browser.find_element(By.ID, "password")
    input2.send_keys("12345")
    browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
    time.sleep(1)
    browser.find_element(By.ID, "registerButton").click()
    time.sleep(2)
    assert browser.find_element(By.CSS_SELECTOR, "button[disabled]"), 'Url не соответствует ожидаемому'
    browser.quit()
