from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration_opens_sign_in_screen(valid_registration):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() #локатор кнопки регистрации на экране авторизации

    driver.find_element(By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default']/input").send_keys(valid_registration[0]) #локатор поля ввода имени
    driver.find_element(By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default']/input").send_keys(valid_registration[1]) #локатор поля ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(valid_registration[2]) #локатор поля ввода пароля

    driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click() #локатор поля ввода кнопки регистрации на экране регистрации

    assert '/login' in driver.current_url

    driver.quit()

def test_registration_error_due_to_invalid_password(invalid_registration_due_to_password):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() #локатор кнопки регистрации на экране авторизации
    driver.find_element(By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default']/input").send_keys(invalid_registration_due_to_password[0]) #локатор поля ввода имени
    driver.find_element(By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default']/input").send_keys(invalid_registration_due_to_password[1]) #локатор поля ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(invalid_registration_due_to_password[2]) #локатор поля ввода пароля

    driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click() #локатор поля ввода кнопки регистрации на экране регистрации

    error_alert = driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']") #локатор алерта ошибки ввода пароля

    assert error_alert.is_displayed() and driver.find_element(By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_password input_size_default input_status_error']") #локатор изменненого контейнера с ошибкой ввода пароля

    driver.quit()
