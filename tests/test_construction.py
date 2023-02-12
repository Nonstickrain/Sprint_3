from selenium import webdriver
from selenium.webdriver.common.by import By

def test_constuct_choose_sause_section():
    driver = webdriver.Firefox()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click() #локатор кнопки раздела соусов


    assert driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Соусы']") #локатор изменённого контейнера раздела соусов в конструкторе

    driver.quit()

def test_constuct_choose_bun_section():
    driver = webdriver.Firefox()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click() #локатор кнопки раздела соусов
    driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click() #локатор кнопки раздела булок


    assert driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Булки']") #локатор изменённого контейнера раздела булок в конструкторе

    driver.quit()

def test_constuct_choose_filling_section():
    driver = webdriver.Firefox()

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()

    driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click() #локатор кнопки раздела начинок


    assert driver.find_element(By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Начинки']") #локатор изменённого контейнера раздела начинок в конструкторе

    driver.quit()