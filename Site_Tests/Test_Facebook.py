import pytest
import allure

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.epic("Тестирование с помощью Facebook")
@allure.feature('Вход и выполнение задания')
@pytest.mark.skip('Not ready for test')
@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = webdriver.Chrome(executable_path='C:/Users/Александр/Desktop/Работа/AutoTest-s/chromedriver.exe')
    driver.get('https://battlearena:tobattle!@web-stable.arenum.games/ru/')
    yield driver
    driver.quit()