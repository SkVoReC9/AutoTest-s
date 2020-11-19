import random
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/SkVoReC/Desktop/Работа/Автотесты/chromedriver.exe')

    @unittest.skip('Discord test skipped for Google Test')
    def test_log_in_discord(self):
        #Вход на сайт и логин в дискорд
        print('Start Discord Test')
        print('Discord login start')
        driver = self.driver
        driver.get('web.arenum.games/ru/')
        login = driver.find_element_by_xpath('//button[contains(text(),Войти)]')
        login.click()
        login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[2]')))
        driver.execute_script("arguments[0].click();", login_wait)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'email')))
        driver.find_element_by_name('email').send_keys('p_a.a.skvortsov@mpt.ru')
        driver.find_element_by_name('password').send_keys('Bass2000v_8')
        driver.find_element_by_xpath(
            '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]')))
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        print('Discord Login Ok!')
        print('Start Arenum Quests')
        #Переходим в профиль для выполнения задания
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'header-profile')))
        driver.find_element_by_class_name('header-profile').click()

        #Выполение заданий
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        except TimeoutException:
            driver.find_element_by_class_name('header-profile').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        #Переходим во вкладку задания
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="profile-rewards"]/div[1]/a[2]')))
        #Переходим на задания по заполнению мобильного телефона
        driver.find_element_by_xpath('//*[@id="profile-rewards"]/div[1]/a[2]').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//input[@name="telephone"]')))
        a = '+790000'+str(random.randint(10000, 99999))
        print(a)
        driver.find_element_by_xpath('//input[@name="telephone"]').send_keys(a)
        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[3]/div/button[1]').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[6]/div[2]/div/div[1]')))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[6]/div[2]/div/div[1]').click()

        print('Arenum Quests OK!')

        # Выходим из аккаунта после выполнения заданий
        driver.find_element_by_class_name('header-profile').click()
        WebDriverWait(driver, 10).LogOut_Dis = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[2]')))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[2]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div[1]/div[2]/div/div[6]/span')))

        driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div[1]/div[2]/div/div[6]/span').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/div[2]/div[2]/a[1]')))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[2]/div/div[2]/div[2]/a[1]').click()
        log_out = driver.find_element_by_xpath('//button[contains(text(),Войти)]')
        self.assertTrue(log_out, 'Test Failed')
        print('Discord log out ok!')
        print('Discord Test OK!')

    def test_log_in_Google(self):
        print('Google test start')
        print('Google login start')
        driver = self.driver
        driver.get('web.arenum.games/ru/')
        driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        #Вход на сайт через Google аккаунт
        login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[3]')))
        driver.execute_script("arguments[0].click();", login_wait)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'identifier')))
        driver.find_element_by_name('identifier').send_keys('skvorcov_a@arenum.games')
        driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
        driver.find_element_by_name('password').send_keys('Bass2000v_8f_8trestat')
        driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
        print('Google login OK!')
        #Переходим в профиль
        print('Start Arenum quests')
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        driver.find_element_by_class_name('header-profile').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        except TimeoutException:
            driver.find_element_by_class_name('header-profile').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/a[1]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]')))
            driver.find_element_by_xpath(
                '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        #Переходим во вкладку задания
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/main/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div').click()
        go_to_quest = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="profile-rewards"]/div[1]/a[2]')))

        self.assertTrue(go_to_quest, "Test Failed")
        print('Google Arenum Quest OK!')
        print('Google test OK!')

    def test_log_in_Facebook(self):
        print('Facebook test start')
        print('Facebook login start')
        driver = self.driver
        driver.get('web.arenum.games/ru/')
        driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        # Вход на сайт через Google аккаунт
        Login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[4]')))
        driver.execute_script("arguments[0].click();", Login_wait)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.NAME, 'email')))
        driver.find_element_by_name('email').send_keys('sashaskvorcov19@gmail.com')
        driver.find_element_by_name('pass').send_keys('Bass2000v_8f_8trestat')
        driver.find_element_by_name('login').click()
        login_social = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        self.assertTrue(login_social, 'Test Failed')
        print('Facebook login OK!')
        print('Facebook test OK!')
    @unittest.skip('Do not work with 2 step auth')
    def test_log_in_AppleId(self):
        print('AppleId test start')
        print('AppleId login start')
        driver = self.driver
        driver.get('https://battlearena:tobattle!@web-stable.arenum.games/ru/')
        driver.find_element_by_xpath('//button[contains(text(),Войти)]').click()
        # Вход на сайт через AppleID
        login_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[2]/div/div[2]/div[2]/button[5]')))
        driver.execute_script("arguments[0].click();", login_wait)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'account_name_text_field')))
        driver.find_element_by_id('account_name_text_field').send_keys('skvorcov_a@arenum.games')
        driver.find_element_by_id('account_name_text_field').send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'password_text_field')
        ))
        driver.find_element_by_id('password_text_field').send_keys('pass')
        driver.find_element_by_id('password_text_field').send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="1605251974871-0"]/div/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="1605251974871-0"]/div/div/button[1]').click()
        #Выбор региона
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/div/div[2]/button[2]')))
        driver.find_element_by_xpath('//*[@id="__layout"]/div/div[3]/div[2]/div/div/div[2]/button[2]').click()
        #Повторный логин
        driver.find_element_by_id('account_name_text_field').send_keys('skvorcov_a@arenum.games')
        driver.find_element_by_id('account_name_text_field').send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'password_text_field')
        ))
        driver.find_element_by_id('password_text_field').send_keys('pass')
        driver.find_element_by_id('password_text_field').send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="1605251974871-0"]/div/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="1605251974871-0"]/div/div/button[1]').click()
        #Профиль
        login_Social = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'header-profile')))
        self.assertTrue(login_Social, 'Test Failed')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()