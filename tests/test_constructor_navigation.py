from locators import StellarburgersLocators

class TestConstructorNavigation:
    def test_move_to_buns(self, driver, login):
        driver.find_element(*StellarburgersLocators.SAUCES_BTN).click()
        driver.find_element(*StellarburgersLocators.BUNS_BTN).click()
        real_attribute = driver.find_element(*StellarburgersLocators.BUNS_BTN).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in real_attribute

    def test_move_to_sauces(self, driver, login):
        driver.find_element(*StellarburgersLocators.SAUCES_BTN).click()
        real_attribute = driver.find_element(*StellarburgersLocators.SAUCES_BTN).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in real_attribute

    def test_move_to_fillings(self, driver, login):
        driver.find_element(*StellarburgersLocators.FILLINGS_BTN).click()
        real_attribute = driver.find_element(*StellarburgersLocators.FILLINGS_BTN).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in real_attribute
