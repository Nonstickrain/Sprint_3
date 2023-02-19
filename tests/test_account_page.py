from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_account_page_account_page(account):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click() #локатор кнопки личного кабинета

    driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys(account[0]) #локатор поля ввода почты на экране авторизации
    driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys(account[1]) #локатор поля ввода пароля на экране авторизации

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() #локатор кнопки войти на экране авторизации
    account_button = driver.find_element(By.XPATH, ".//a[@href = '/account']") #локатор кнопки личного кабинета
    driver.execute_script("arguments[0].click();", account_button)

    account_main_element = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']") #локатор страницы аккаунта
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((account_main_element)))

    assert driver.find_element(account_main_element[0], account_main_element[1]).is_displayed()

    driver.quit()

def test_account_page_log_out_from_account(account):
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click() #локатор кнопки личного кабинета

    driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys(account[0]) #локатор поля ввода почты на экране авторизации
    driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys(account[1]) #локатор поля ввода пароля на экране авторизации

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() #локатор кнопки войти на экране авторизации
    account_button = driver.find_element(By.XPATH, ".//a[@href = '/account']") #локатор кнопки личного кабинета
    driver.execute_script("arguments[0].click();", account_button)

    account_main_element = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']") #локатор страницы аккаунта
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((account_main_element)))
    driver.find_element(By.XPATH, ".//button[text() = 'Выход']").click() #локатор кнопки выхода из аккаунта


    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()