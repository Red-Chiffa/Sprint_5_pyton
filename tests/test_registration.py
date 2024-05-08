import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import get_registration_data
from locators import StellarburgersLocators
from config import REGISTRATION_URL, LOGIN_URL


class TestRegistrationPage:
    def test_success_regisration(self, driver):
        driver.get(REGISTRATION_URL)
        name, email, password = get_registration_data()
        driver.find_element(*StellarburgersLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*StellarburgersLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE))
        assert driver.current_url == LOGIN_URL

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_wrong_password(self, driver, password):
        driver.get(REGISTRATION_URL)
        name, email, password_data = get_registration_data()
        driver.find_element(*StellarburgersLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*StellarburgersLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.WRONG_PASSWORD))
        assert driver.find_element(*StellarburgersLocators.WRONG_PASSWORD).is_displayed()
