import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import LOGIN_URL
from locators import StellarburgersLocators


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys('aleksandra_menshikova_8@ya.ru')  # имя Александра
    driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys('888888')
    driver.find_element(*StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(StellarburgersLocators.ORDER_BTN))
