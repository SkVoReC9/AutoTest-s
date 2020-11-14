import pytest
import allure

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Test_Login:

    @pytest.fixture(scope="class")
    def driver(self):
        print('Initialize driver')
        driver = webdriver.Chrome(executable_path='C:/Users/SkVoReC/Desktop/Работа/Автотесты/chromedriver.exe')
        driver.get('https://battlearena:tobattle!@web-stable.arenum.games/ru/')
        yield driver
        print('Close driver')
        driver.quit()

    def test_google_login(self, driver):
        driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        # Вход на сайт через Google аккаунт
        login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[3]')))
        driver.execute_script("arguments[0].click();", login_wait)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'identifier')))
        driver.find_element_by_name('identifier').send_keys('skvorcov_a@arenum.games')
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
        driver.find_element_by_name('password').send_keys('Bass2000v_8f_8trestat')
        driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
        result = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        assert result == True
        print('Google login OK!')

