import pytest
import random
import time
import allure


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import action_chains

@pytest.mark.skip()
@allure.epic("Тестирование с помощью Discord")
@allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
@allure.story('Заходим в Discord аккаунт')
def test_discord_login(driver):
    with allure.step('Открываем сайт  и нажимаем войти'):
        driver.find_element_by_class_name('header-mobile-avatar').click()
    with allure.step('Выбираем Discord'):
        login_wait = WebDriverWait(driver, 100).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[2]')))
        driver.execute_script("arguments[0].click();", login_wait)
    with allure.step('Вводим данные и заходим'):
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.NAME, 'email')))
        driver.find_element_by_name('email').send_keys('p_a.a.skvortsov@mpt.ru')
        driver.find_element_by_name('password').send_keys('Bass2000v_8')
        driver.find_element_by_xpath(
            '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
    with allure.step('Нажимаем авторизовать после входа в аккаунт'):
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]')))
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    try:
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[contains(text(),"Напомнить позже")]')))
        driver.find_element_by_xpath('//*[contains(text(),"Напомнить позже")]').click()
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            (By.CLASS_NAME, 'tab-bar-profile')))
        assert True
    except TimeoutException:
        assert False

@pytest.mark.skip()
@allure.epic("Тестирование с помощью Discord")
@allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
@allure.story('Меняем аватарку')
def test_avatar_discord(driver):
    with allure.step('Переходим во вкладку редактирования'):
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div/div[1]')
        ))
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/picture')))
    driver.find_element_by_xpath(
        '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/picture').click()
    WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[3]')))
    driver.find_element_by_xpath(
        '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[3]').click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[2]/div[2]/div[2]')))
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div[1]/div[1]/input')))
    with allure.step('Загружаем одну из 3 картинок'):
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div[1]/div[1]/input').send_keys(
            'C:/Users/Александр/Desktop/Работа/AutoTest-s/Picturies/Arenum_' + str(random.randint(1, 3)) + '.jpg')
    time.sleep(3)
    with allure.step('Выходим обратно в профиль'):
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[1]/div/a').click()
    WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
        (By.CLASS_NAME, 'header-profile')))
    assert True

@pytest.mark.skip()
@pytest.mark.skip("Так надо")
@allure.epic("Тестирование с помощью Discord")
@allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
@allure.story('Меняем никнейм')
def test_nickname_discord(driver):
    with allure.step('Переходим во вкладку редактирования'):
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/picture')))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/picture').click()
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[3]')
            ))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[3]').click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div/main/div[1]/div[2]/div[2]/div[2]/div[2]/span')))
        time.sleep(1)
    with allure.step('Нажимаем на никнейм'):
        driver.find_element_by_xpath('/html/body/div/div/div/main/div[1]/div[2]/div[2]/div[2]/div[2]/span').click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div/div/div[2]')
    ))
    with allure.step('Очищаем поле и меняем никнейм'):
        driver.execute_script("setTimeout(() => {document.getElementsByClassName('input--big')[0].focus()}, 1000)")
    action = action_chains.ActionChains(driver)
    action.move_by_offset(907, 457).click().perform()
    time.sleep(1)
    driver.find_element_by_class_name('input--big').clear()
    driver.find_element_by_class_name('input--big').send_keys('Discord_'+str(random.randint(1, 50)))
    with allure.step('Сохраняем и возвращаемся в профиль'):
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[1]/div/div[2]').click()
    WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
        (By.XPATH, '//*[@id="__layout"]/div/main/div[2]/div/a[3]')))
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[2]/div/a[3]').click()
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.CLASS_NAME, 'header-profile')
    ))
    assert True

@pytest.mark.skip()
@allure.epic("Тестирование с помощью Discord")
@allure.feature('Вход, выполнение задания, смена аватарки, никнейма')
@allure.story('Выполняем задания')
def test_quest_discord(driver):
    with allure.step('Переходим во вкладку задания'):
        # Переходим во вкладку задания
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[1]/div[3]/a')
        ))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[1]/div[3]/a').click()
    with allure.step('Проверяем наличие заданий'):
        WebDriverWait(driver, 100).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/main/div/div/div/div[3]')))
    assert True
