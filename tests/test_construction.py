from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_constuct_choose_sause_section():
    driver = webdriver.Firefox()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click() #локатор кнопки раздела соусов

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Соусы']")))

    assert driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Соусы']") #локатор изменённого контейнера раздела соусов в конструкторе

    driver.quit()

def test_constuct_choose_bun_section():
    driver = webdriver.Firefox()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//span[text() = 'Соусы']")))

    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click() #локатор кнопки раздела соусов
    driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click() #локатор кнопки раздела булок

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Булки']")))

    assert driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Булки']") #локатор изменённого контейнера раздела булок в конструкторе

    driver.quit()

def test_constuct_choose_filling_section():
    driver = webdriver.Firefox()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//span[text() = 'Начинки']")))

    driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click() #локатор кнопки раздела начинок

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Начинки']")))

    assert driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Начинки']") #локатор изменённого контейнера раздела начинок в конструкторе

    driver.quit()