import pytest
import allure

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def pytest_generate_tests(metafunc):
    if 'url' in metafunc.fixturenames:
        metafunc.parametrize(
            'url', list(['https://battlearena:tobattle!@web-stable.arenum.games/ru/',
                         'https://battlearena:tobattle!@web-stable.arenum.gg/ru/']), scope='class')


@allure.epic("Тестирование с помощью Discord")
@allure.feature('Вход и выполнение задания')
class TestDiscord:

    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        with allure.step('Инициализация драйвера'):
            driver = webdriver.Chrome(executable_path='C:/Users/SkVoReC/Desktop/Работа/Автотесты/chromedriver.exe')
            driver.implicitly_wait(10)  # seconds
        yield driver
        driver.quit()

    @allure.epic("Тестирование с помощью Discord")
    @allure.feature('Вход и выполнение задания')
    def test_discord_login(self, driver, url):
        with allure.step('Открываем сайт {0} и нажимаем войти'.format(url)):
            driver.get(url)
            driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        with allure.step('Выбираем Discord'):
            login_wait = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[2]')))
            driver.execute_script("arguments[0].click();", login_wait)
        with allure.step('Вводим данные и заходим'):
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, 'email')))
            driver.find_element_by_name('email').send_keys('p_a.a.skvortsov@mpt.ru')
            driver.find_element_by_name('password').send_keys('Bass2000v_8')
            driver.find_element_by_xpath(
                '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
        with allure.step('Нажимаем авторизовать после входа в аккаунт'):
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]')))
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        try:
            WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
                (By.CLASS_NAME, 'header-profile')))
            assert True
        except TimeoutException:
            assert False
