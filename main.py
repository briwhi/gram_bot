from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import *

chrome_driver_path = "C:/Users/brian/Documents/chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass

    
insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()

