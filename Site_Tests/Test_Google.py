import pytest
import allure

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def pytest_generate_tests(metafunc):
    if 'url' in metafunc.fixturenames:
        metafunc.parametrize(
            'url', list(['https://battlearena:tobattle!@web-stable.arenum.games/ru/',
                         'https://battlearena:tobattle!@web-stable.arenum.gg/ru/']), scope='class')


@allure.epic("Тестирование с помощью Google")
@allure.feature('Вход и выполнение задания')
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
    @allure.feature('Вход и выполнение задания')
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
                (By.CLASS_NAME, 'header-profile')))
            assert True
        except TimeoutException:
            assert False

    @allure.epic("Тестирование с помощью Google")
    @allure.feature('Вход и выполнение задания')
    @allure.story('Выполняем задания')
    def test_quest_google(self, driver):
        with allure.step('Переходим в профиль'):
            WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
                (By.CLASS_NAME, 'header-profile')))
            driver.find_element_by_class_name('header-profile').click()
            WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
        try:
            WebDriverWait(driver, 4).until(ec.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        except TimeoutException:
            driver.find_element_by_class_name('header-profile').click()
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
