import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chrome():
    def chrome_launch(self):
        baseURL = "https://google.com"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        #driver.implicitly_wait(5)
        driver.get(baseURL)
        time.sleep(5)



test_obj = Chrome()
test_obj.chrome_launch()