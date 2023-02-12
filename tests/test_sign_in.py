from selenium import webdriver
from selenium.webdriver.common.by import By

def test_sign_in_open_sign_in_screen_from_main_page(account):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button").click() #локатор кнопки авторизации под блоком корзины ингредиентов

    driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys(account[0]) #локатор поля ввода почты на экране авторизации
    driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys(account[1]) #локатор поля ввода пароля на экране авторизации

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() #локатор кнопки войти на экране авторизации

    assert  driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_sign_in_open_sign_in_screen_from_account_page(account):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click() #локатор кнопки личного кабинета

    driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys(account[0]) #локатор поля ввода почты на экране авторизации
    driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys(account[1]) #локатор поля ввода пароля на экране авторизации

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() #локатор кнопки войти на экране авторизации

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_sign_in_open_sign_in_screen_from_register_page(account):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click() #локатор кнопки личного кабинета
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() #локатор кнопки регистрации на экране авторизации
    driver.find_element(By.XPATH, ".//a[text() = 'Войти']").click() #локатор кнопки входа в аккаунт на экране регистрации

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()

def test_sign_in_open_sign_in_screen_from_password_recovery_page(account):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click() #локатор кнопки личного кабинета
    driver.find_element(By.XPATH, ".//a[text() = 'Восстановить пароль']").click() #локатор кнопки восстановления пароля на экране авторизации
    driver.find_element(By.XPATH, ".//a[text() = 'Войти']").click() #локатор кнопки входа в аккаунт на экране восстановления пароля

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()