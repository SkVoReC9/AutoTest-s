from selenium import webdriver
import threading
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#Логин в админку
driver.get("https://tournament-stable.arenum.games/login")
login = driver.find_element_by_id('enter-login')
login.send_keys('Boomer_23')
passw = driver.find_element_by_id('enter-password')
passw.send_keys('rein2612')
#Попытка войти в админку
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-submit"))
    )
except BaseException:
    print('Hello')
finally:
    sub = driver.find_element_by_id('login-submit')
    sub.click()
#Переходим в раздел турниры и создаем турнир
elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "left-bar-tournaments")))

trn = driver.find_element_by_xpath("//a[@id='left-bar-tournaments']")
trn.click()

elem1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div/div[1]/section/header/section/div/div[2]/div[2]")))

Create_Tour = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/section/header/section/div/div[2]/div[2]")
Create_Tour.click()

#Ждем пока прогрузится форма
wait_Tour_create = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'main-create'))
)

Game_Pick = driver.find_element_by_id("game-Call of Duty")
Game_Pick.click()

#Заполнение русской локали
Input_Title = driver.find_element_by_id("tournament-title")
Input_Title.send_keys('At:Русский(Саша)')

Input_Descr = driver.find_element_by_id("tournament-description-title")
Input_Descr.send_keys('At:русский(Саша)')

Input_Unreg_Info = driver.find_element_by_id("tournament-unauthorized-description")
Input_Unreg_Info.send_keys('AT')

Input_Reg_Info = driver.find_element_by_id('tournament-authorized-description')
Input_Reg_Info.send_keys('AT')

Input_Final_Info = driver.find_element_by_id('tournament-final-description')
Input_Final_Info.send_keys('AT')

#Заполнение английской локали
Locale_En_Pick = driver.find_element_by_id("tournament-description-locale-en_US")
Locale_En_Pick.click()

Input_Title = driver.find_element_by_id("tournament-title")
Input_Title.send_keys('At:eng(Саша)')

Input_Descr = driver.find_element_by_id("tournament-description-title")
Input_Descr.send_keys('At:Eng(Саша)')
Locale_En_Pick.click()

Input_Unreg_Info = driver.find_element_by_id("tournament-unauthorized-description")
Input_Unreg_Info.send_keys('AT')

Input_Reg_Info = driver.find_element_by_id('tournament-authorized-description')
Input_Reg_Info.send_keys('AT')

Input_Final_Info = driver.find_element_by_id('tournament-final-description')
Input_Final_Info.send_keys('AT')

#Заполнение режима и карты
Trnt_mode = driver.find_element_by_id('tournament-game-mode')
Trnt_mode.send_keys('AT:Regular')

Trnt_map = driver.find_element_by_id('tournament-game-map')
Trnt_map.send_keys('Map')

#Выбор типа турнира

#TODO выбор типа турнира(платный или бесплатный) из выпдаюзего списка(input). Необходимо доработать метод нажатия


