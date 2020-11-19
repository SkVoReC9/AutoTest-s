import pytest
import allure
import random
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import action_chains


def pytest_generate_tests(metafunc):
    if 'url' in metafunc.fixturenames:
        metafunc.parametrize(
            'url', list(['https://battlearena:tobattle!@web-stable.arenum.games/ru/',
                         'https://battlearena:tobattle!@web-stable.arenum.gg/ru/']), scope='class')


@allure.epic("Тестирование с помощью Discord")
@allure.feature('Вход и выполнение задания')
class TestDiscord:
    @pytest.fixture(scope="class", autouse=True)
    def driver(self, url):
        with allure.step('Инициализация драйвера'):
            driver = webdriver.Chrome(executable_path='C:/Users/SkVoReC/Desktop/Работа/Автотесты/chromedriver.exe')
            driver.implicitly_wait(10)
        driver.get(url)
        yield driver
        driver.close()

    @allure.epic("Тестирование с помощью Discord")
    @allure.feature('Вход и выполнение задания')
    @allure.story('Заходим в Discord аккаунт')
    def test_discord_login(self, driver):
        with allure.step('Открываем сайт  и нажимаем войти'):
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
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture')))
            assert True
        except TimeoutException:
            assert False

    @allure.epic("Тестирование с помощью Discord")
    @allure.feature('Вход и выполнение задания')
    @allure.story('Выполняем задания')
    def test_quest_discord(self, driver):
        with allure.step('Переходим в профиль'):
            WebDriverWait(driver, 100).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture').click()
            time.sleep(1)
            WebDriverWait(driver, 5).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
        try:
            WebDriverWait(driver, 4).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        except TimeoutException:
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture').click()
            WebDriverWait(driver, 4).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        with allure.step('Переходим во вкладку задания'):
            # Переходим во вкладку задания
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div').click()
        go_to_quest = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="profile-rewards"]/div[1]/a[2]')))
        assert True
    def test_avatar_discord(self, driver):
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]').click()
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]')))
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[1]/div[1]/input')
        ))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div[1]/div[1]/input').send_keys(
            'C:/Users/SkVoReC/Desktop/Работа/Автотесты/Picturies/Arenum_' + str(random.randint(1, 3)) + '.jpg')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[1]/div/a').click()
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        assert True

    def test_nickname_discord(self, driver):
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]')
        ))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]').click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]')))
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]').click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div/div/div[2]')
        ))
        driver.execute_script("setTimeout(() => {document.getElementsByClassName('input--big')[0].focus()}, 1000)")
        action = action_chains.ActionChains(driver)
        action.move_by_offset(907, 457).click().perform()
        time.sleep(1)
        driver.find_element_by_class_name('input--big').clear()
        driver.find_element_by_class_name('input--big').send_keys('Discord_'+str(random.randint(1, 50)))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[1]/div/div[2]').click()
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[2]/div/a[2]')))
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/a[2]').click()
        WebDriverWait(driver, 100).until(ec.presence_of_element_located(
            (By.CLASS_NAME, 'header-profile')
        ))
        assert True

