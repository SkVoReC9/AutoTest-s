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
        for i in config:
            if config[i][0]['browser'] == SUPPORTED_BROWSER:
                driver = webdriver.Chrome(executable_path='C:/Users/Александр/Desktop/Работа/AutoTest-s/chromedriver.exe')
                num_of_conf = i
            else:
                continue
        mobile_emulation = {"deviceName": config[num_of_conf][0]['deviceName']}
        browser_locale = config[num_of_conf][0]['locale']
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--lang={}".format(browser_locale))
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver.set_window_size(100, 950)
        driver.implicitly_wait(config[num_of_conf][0]['wait_browser'])
    driver.get(config[num_of_conf][0]['url'])
    yield driver
    driver.close()
