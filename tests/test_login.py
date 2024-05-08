from locators import StellarburgersLocators
from config import BASE_URL, REGISTRATION_URL, FOFGOT_PASSWORD_URL, LOGIN_URL
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginPage:

    #  данные для логина получены из предварительной ручной регистраии
    def test_login(self, driver):
        driver.get(LOGIN_URL)
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys('am1234@ya.ru')  # имя Александра
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys('am1234')
        driver.find_element(*StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.ORDER_BTN))
        assert driver.find_element(*StellarburgersLocators.ORDER_BTN).is_displayed()

    def test_main_page_click_login_btn(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*StellarburgersLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE))
        assert driver.find_element(*StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE).is_displayed()

    def test_main_page_click_personal_account_btn(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE))
        assert driver.find_element(*StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE).is_displayed()

    def test_registration_form_click_login_btn(self, driver):
        driver.get(REGISTRATION_URL)
        driver.find_element(*StellarburgersLocators.LOGIN_BTN_REGISTRATION_FORM).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE))
        assert driver.find_element(*StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE).is_displayed()

    def test_forgot_password_page_click_login_btn(self, driver):
        driver.get(FOFGOT_PASSWORD_URL)
        driver.find_element(*StellarburgersLocators.LOGIN_BTN_REGISTRATION_FORM).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE))
        assert driver.find_element(*StellarburgersLocators.LOGIN_BTN_LOGIN_PAGE).is_displayed()
