from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_move_to_construct_from_account_page_by_section_button(account):
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

    driver.find_element(By.XPATH,".//p[text() = 'Конструктор']/..").click() #локатор кнопки секции конструктора в хидере

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']")))

    assert driver.find_element(By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']").is_displayed() #локатор конструктора

    driver.quit()

def test_move_to_construct_from_account_page_by_click_on_logo(account):
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

    driver.find_element(By.XPATH,".//div[@class = 'AppHeader_header__logo__2D0X2']/a").click() #локатор кнопки лого в хидере

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']")))

    assert driver.find_element(By.XPATH, ".//section[@class = 'BurgerIngredients_ingredients__1N8v2']").is_displayed() #локатор конструктора

    driver.quit()

