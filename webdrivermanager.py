
from lib2to3.pgen2 import driver
from mimetypes import init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.maximize_window()
driver.get_window_size()
driver.get('google.com')


# init()
# demo()
# def initiate(self):
#     self.__init__()