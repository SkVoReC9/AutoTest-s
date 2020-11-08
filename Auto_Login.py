from selenium import webdriver
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://tournament-stable.arenum.games/login")
login = driver.find_element_by_id('enter-login')
login.send_keys('Boomer_23')
passw = driver.find_element_by_id('enter-password')
passw.send_keys('rein2612')
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-submit"))
    )
except BaseException:
    print('Hello')
finally:
    sub = driver.find_element_by_id('login-submit')
    sub.click()

elem = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "left-bar-tournaments")))

trn = driver.find_element_by_xpath("//a[@id='left-bar-tournaments']")
trn.click()

elem1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div/div[1]/section/header/section/div/div[2]/div[2]")))

Create_Tour = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/section/header/section/div/div[2]/div[2]")
Create_Tour.click()

wait_Tour_create = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'main-create'))
)

Game_Pick = driver.find_element_by_id("game-Call of Duty")
Game_Pick.click()

#Locale_Ru_Pick = driver.find_element_by_id("tournament-description-locale-ru_RU")

Input_Title = driver.find_element_by_id("tournament-title")
Input_Title.send_keys('At:Русский(Саша)')

Input_Descr = driver.find_element_by_id("tournament-description-title")
Input_Descr.send_keys('At:русский(Саша)')

#54554543