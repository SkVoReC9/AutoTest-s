from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from selenium.common.exceptions import TimeoutException
import unittest
import random


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/SkVoReC/Desktop/Работа/Автотесты/chromedriver.exe')
    def test_log_in_discord(self):
        #Вход на сайт и логин в дискорд
        print('Start Discord Test')
        print('Discord login start')
        driver = self.driver
        driver.get('https://battlearena:tobattle!@web-stable.arenum.games/ru/')
        Login = driver.find_element_by_xpath('//button[contains(text(),Войти)]')
        Login.click()
        Login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[2]')))
        driver.execute_script("arguments[0].click();", Login_wait)

        Login_Social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'email')))
        driver.find_element_by_name('email').send_keys('p_a.a.skvortsov@mpt.ru')
        driver.find_element_by_name('password').send_keys('Bass2000v_8')
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
        Login_Social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]')))
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        print('Discord Login Ok!')
        print('Start Arenum Quests')
        #Переходим в профиль для выполнения задания
        Login_Succes = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        LogOut_Dis = driver.find_element_by_class_name('header-profile').click()

        #Выполение заданий
        Go_To_Quest = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
        Go_To_Quest = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
        try:
            Go_To_Quest = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            Go_To_Quest = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        except TimeoutException:
            LogOut_Dis = driver.find_element_by_class_name('header-profile').click()
            Go_To_Quest = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            Go_To_Quest = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
            Go_To_Quest = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            Go_To_Quest = driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()

        Go_To_Quest = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div').click()
        Go_To_Quest = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="profile-rewards"]/div[1]/a[2]')))
        Go_To_Quest = driver.find_element_by_xpath('//*[@id="profile-rewards"]/div[1]/a[2]').click()
        Quest_Telephone = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//input[@name="telephone"]')))
        Quest_Telephone = driver.find_element_by_xpath('//input[@name="telephone"]').send_keys('+7999999'+str(random.randint(1000, 9999)))
        Quest_Telephone = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[3]/div/button[1]').click()
        Quest_Telephone = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__layout"]/div/div[6]/div[2]/div/div[1]')))
        Quest_Telephone = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[6]/div[2]/div/div[1]').click()
        print('Arenum Quests OK!')

        # Выходим из аккаунта после выполнения заданий
        LogOut_Dis = driver.find_element_by_class_name('header-profile').click()
        LogOut_Dis = WebDriverWait(driver,10).LogOut_Dis = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[2]')))
        LogOut_Dis = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[2]').click()
        LogOut_Dis = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div/div[6]/span')))

        LogOut_Dis = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div/div[6]/span').click()
        LogOut_Dis = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/div[2]/div[2]/a[1]')))
        LogOut_Dis = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[2]/div/div[2]/div[2]/a[1]').click()
        LogOut = driver.find_element_by_xpath('//button[contains(text(),Войти)]')
        self.assertTrue(LogOut, 'Test Failed')
        print('Discord log out ok!')
        print('Discord Test OK!')

    def test_log_in_Google(self):
        print('Google test start')
        print('Google login start')
        driver = self.driver
        driver.get('https://battlearena:tobattle!@web-stable.arenum.games/ru/')
        driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        Login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[3]')))
        driver.execute_script("arguments[0].click();", Login_wait)
        Login_Social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'identifier')))
        Login_Social = driver.find_element_by_name('identifier').send_keys('skvorcov_a@arenum.games')
        Login_Social = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
        Login_Social = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
        Login_Social = driver.find_element_by_name('password').send_keys('Bass2000v_8f_8trestat')
        Login_Social = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
        Login_Social = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        self.assertTrue(Login_Social, "Test Failed")
        print('Google login end')
        print('Google test OK!')
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()