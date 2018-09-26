from  selenium import  webdriver
from  Config11.TestUrl import *

class driver11():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.maxChrome = self.driver.maximize_window()
        self.wait = self.driver.implicitly_wait(15)


    def GetTestUrl(self):
        openurl= self.driver.get(TestURL)
        waite = self.wait


