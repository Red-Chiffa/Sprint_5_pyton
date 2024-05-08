созданы файлы:
1. conftest.py с фикстурами:
- driver - подключение драйвера
- login - авторизация на сайте
2. config.py с описанием констант (в данном случае URL)
3. data.py с функцией генерации данных для регистрации
4. locators.py с описанием используемых локаторов
5. test_registration.py с тестами:
- test_success_regisration - позитивный тест на регистрацию
- test_registration_wrong_password - параметризированный тест на проверку некорректного пароля (по длиине)
6. test_login.py с тестами:
- test_login - позитивный тест на авторизацию
- test_main_page_click_login_btn - тест на переход на страницу авторизации с главной страницы по кнопке "Войти в аккунт"
- test_main_page_click_personal_account_btn - тест на переход на страницу авторизации с главной страницы по кнопке "Личный кабинет"
- test_registration_form_click_login_btn - тест на переход на страницу авторизации со страницы регистрации по кнопке "Войти"
- test_forgot_password_page_click_login_btn - тест на переход на страницу авторизации со страницы восстановления пароля
7. test_navigation.py с тестами:
- test_move_to_personal_account - тест перехода по кнопке "Личный кабинет" с главной страницы
- test_move_to_constructor_from_personal_account_by_consructor_btn - тест перехода на главную страницу из личного кабинета по кнопке "Конструктор"
- test_move_to_main_page_from_personal_account_by_logo_btn - тест перехода на главную страницу из личного кабинета по клику на лого Stellar Burgers
- test_account_quit - тест выхода из аккаунта
8. test_constructor_navigation.py с тестами:
- test_move_to_buns - тест перехода к разделу "Булки"
- test_move_to_sauces - тест перехода к разделу "Соусы"
- test_move_to_fillings - тест перехода к разделу "Начинки"