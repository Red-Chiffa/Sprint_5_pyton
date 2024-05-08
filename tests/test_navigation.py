from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarburgersLocators
from config import BASE_URL, LOGIN_URL, PROFILE_URL


class TestNavigation:

    def test_move_to_personal_account(self, driver, login):
        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.EXIT_ACCOUNT_BTN))
        assert driver.current_url == PROFILE_URL

    def test_move_to_constructor_from_personal_account_by_consructor_btn(self, driver, login):
        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.EXIT_ACCOUNT_BTN))
        driver.find_element(*StellarburgersLocators.CONSTRUCTOR_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.ORDER_BTN))
        assert driver.current_url == BASE_URL

    def test_move_to_main_page_from_personal_account_by_logo_btn(self, driver, login):
        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.EXIT_ACCOUNT_BTN))
        driver.find_element(*StellarburgersLocators.LOGO_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.ORDER_BTN))
        assert driver.current_url == BASE_URL

    def test_account_quit(self, driver, login):
        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.EXIT_ACCOUNT_BTN))
        driver.find_element(*StellarburgersLocators.EXIT_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(expected_conditions.
                                       visibility_of_element_located(StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE))
        assert driver.current_url == LOGIN_URL
