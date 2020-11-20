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


@allure.epic("Тестирование с помощью Google")
@allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
class TestGoogle:
    @pytest.yield_fixture(scope="class", autouse=True)
    def driver(self, url):
        with allure.step('Инициализация драйвера'):
            driver = webdriver.Chrome(executable_path='C:/Users/SkVoReC/Desktop/Работа/Автотесты/chromedriver.exe')
            driver.implicitly_wait(10)
        driver.get(url)
        yield driver
        driver.close()

    @allure.epic("Тестирование с помощью Google")
    @allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
    @allure.story('Заходим в Google аккаунт')
    def test_google_login(self, driver):
        with allure.step('Открываем сайт и нажимаем войти'):
            driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        # Вход на сайт через Google аккаунт
        with allure.step('Выбираем Google'):
            login_wait = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[3]')))
            driver.execute_script("arguments[0].click();", login_wait)
        with allure.step('Вводим данные и заходим'):
            WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.NAME, 'identifier')))
            driver.find_element_by_name('identifier').send_keys('skvorcov_a@arenum.games')
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
            WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.NAME, 'password')))
            driver.find_element_by_name('password').send_keys('Bass2000v_8f_8trestat')
            driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
        try:
            WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture')))
            assert True
        except TimeoutException:
            assert False

    @allure.epic("Тестирование с помощью Google")
    @allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
    @allure.story('Выполняем задания')
    def test_quest_google(self, driver):
        with allure.step('Переходим в профиль'):
            WebDriverWait(driver, 100).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/picture').click()
            time.sleep(2.5)
            WebDriverWait(driver, 5).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
            WebDriverWait(driver, 4).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        with allure.step('Переходим во вкладку задания'):
            # Переходим во вкладку задания
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div').click()
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="profile-rewards"]/div[1]/a[2]')))
        assert True

    @allure.epic("Тестирование с помощью Google")
    @allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
    @allure.story('Меняем аватарку')
    def test_avatar_google(self, driver):
        with allure.step('Переходим во вкладку редактирования'):
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]').click()
            WebDriverWait(driver, 5).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]')))
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[1]/div[1]/input')
        ))
        with allure.step('Загружаем одну из 3 картинок'):
            driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div[1]/div[1]/input').send_keys(
                'C:/Users/SkVoReC/Desktop/Работа/Автотесты/Picturies/Arenum_' + str(random.randint(1, 3)) + '.jpg')
        time.sleep(3)
        with allure.step('Выходим обратно в профиль'):
            driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[1]/div/a').click()
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        assert True

    @allure.epic("Тестирование с помощью Google")
    @allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
    @allure.story('Меняем никнейм')
    def test_nickname_google(self, driver):
        with allure.step('Переходим во вкладку редактирования'):
            WebDriverWait(driver, 5).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]')
            ))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]').click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]')))
        time.sleep(1)
        with allure.step('Нажимаем на никнейм'):
            driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]').click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div/div/div[2]')
        ))
        with allure.step('Очищаем поле и меняем никнейм'):
            driver.execute_script("setTimeout(() => {document.getElementsByClassName('input--big')[0].focus()}, 1000)")
        action = action_chains.ActionChains(driver)
        action.move_by_offset(907, 457).click().perform()
        time.sleep(1)
        driver.find_element_by_class_name('input--big').clear()
        driver.find_element_by_class_name('input--big').send_keys('Google_'+str(random.randint(1, 50)))
        with allure.step('Сохраняем и возвращаемся в профиль'):
            driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[1]/div/div[2]').click()
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div[2]/div/a[2]')))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/a[2]').click()
        WebDriverWait(driver, 100).until(ec.presence_of_element_located(
            (By.CLASS_NAME, 'header-profile')
        ))
        assert True
