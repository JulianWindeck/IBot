import time
from selenium import webdriver
import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def main(u, p):
    b = Browser.Browser('https://gmx.net', './res/chromedriver')
    b.openURL(b.base_url)

    input = b.getElementByXPath('//input[@name="username"]')
    input.send_keys("blabal")
    b.wait(5)
    b.quit()


if __name__ == '__main__':
    main('sonja.windeck@gmx.de', '')