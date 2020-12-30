from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import *
import time

chrome_driver_path = "C:/Users/brian/Documents/chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://instagram.com")
        time.sleep(1)
        username = self.driver.find_element_by_name("username")
        username.send_keys(I_USER)
        password = self.driver.find_element_by_name("password")
        password.send_keys(I_PASS)
        button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        button.click()
        time.sleep(3)

        save_info_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        save_info_button.click()
        time.sleep(3)

        notification_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_button.click()
        time.sleep(3)
        
    def find_followers(self):
        self.driver.get(FOLLOW_ACCOUNT)
        time.sleep(1)
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(1)
        follower_links = self.driver.find_elements_by_css_selector("button.sqdOP")
        for link in follower_links:
            link.click()

    def follow(self):
        pass


insta = InstaFollower()
insta.login()
insta.find_followers()
# insta.follow()

