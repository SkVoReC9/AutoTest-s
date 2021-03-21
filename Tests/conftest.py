import pytest
import allure
import json

from selenium import webdriver


CONFIG_PATH = "C:/Users/Александр/Desktop/Работа/AutoTest-s/Tests/config.json"
DEFAULT_WAIT = 10
SUPPORTED_BROWSER = 'chrome'


@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="session")
def driver(config):
    with allure.step('Инициализация драйвера'):
        if config['browser'] == SUPPORTED_BROWSER:
            driver = webdriver.Chrome(executable_path='C:/Users/Александр/Desktop/Работа/AutoTest-s/chromedriver.exe')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--lang={}".format(config["locale"]))
            mobile_emulation = {"deviceName": config['deviceName']}
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver.set_window_size(200, 950)
            driver.implicitly_wait(config["wait_time"])
        elif config['browser'] == "firefox":
            mobile_emulation = {"deviceName": config['deviceName']}
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--lang={}".format(config["locale"]))
            firefox_options.set_preference("mobileEmulation", mobile_emulation)
            driver = webdriver.Firefox(executable_path="C:/Users/Александр/Desktop/Работа/AutoTest-s/geckodriver.exe")
            driver.set_window_size(500, 950)
            driver.implicitly_wait(config["wait_time"])
        else:
            raise Exception(f'"{config["browser"]}" is not supported')
    driver.get(config['url'])
    yield driver
    driver.close()
