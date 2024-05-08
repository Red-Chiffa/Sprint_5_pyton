from selenium.webdriver.common.by import By


class StellarburgersLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")  # поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # поле ввода пароля
    REGISTRATION_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться
    WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")  # подпись "Некорректный пароль" под полем ввода пароля
    LOGIN_BTN_LOGIN_PAGE = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти на странице авторизации
    LOGIN_BTN_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка Войти на главной странице
    ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка Оформить заказ на главной
    PERSONAL_ACCOUNT_BTN = (By.XPATH, "//a[.='Личный Кабинет']")  # кнопка "Личный кабинет"
    LOGIN_BTN_REGISTRATION_FORM = (By.XPATH, "//a[text()='Войти']")  # кнопка Войти на странице регистрации и на странице восстановления пароля
    EXIT_ACCOUNT_BTN = (By.XPATH, "//button[text()='Выход']")  # Кнопка Выход в личном кабинете
    CONSTRUCTOR_BTN = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка конструктор в хэдере
    LOGO_BTN = (By.XPATH, "//header/nav/div")  # Кнопка логотип в хэдере
    BUNS_BTN = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # кнопка Булки в конструкторе
    SAUCES_BTN = (By.XPATH, "//span[text() = 'Соусы']/parent::div")  # кнопка Соусы в конструкторе
    FILLINGS_BTN = (By.XPATH, "//span[text() = 'Начинки']/parent::div") # кнопка Начинки в конструкторе
