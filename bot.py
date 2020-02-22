from selenium import webdriver
from time import sleep

class TwitchBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.twitch.tv/nikolsyk")
        sleep(20)

TwitchBot()