import time
import random
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:

    def __init__(self, site_url, driverfile):
        self.driver = Chrome(driverfile)
        self.base_url = site_url
        random.seed()

    def getDriver(self):
        return self.driver

    def openURL(self, url, delay=0):
        self.driver.get(url)
        self.wait(delay)

    def openSubPath(self, subpath, delay=0):
        if not subpath.startswith('/'):
            subpath = '/' + subpath
        self.openURL(self.base_url + subpath, delay)

    def quit(self):
        self.driver.close()

    def goBack(self):
        self.driver.back()

    def goForward(self):
        self.driver.forward()

    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait(1)

    def wait(self, seconds):
        if(seconds > 0):
            time.sleep(seconds)

    def microdelay(self):
        time.sleep(abs(round(random.gauss(0.3, 0.2), 2)))

    defaulttimeout = 8
    def getElementBy(self, method, query_string, timeout):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method, query_string))
            )
        except:
            return None

    def getElementByXPath(self, xpath, timeout=defaulttimeout):
        return self.getElementBy(By.XPATH, xpath, timeout)

    def getElementByTag(self, tag, timeout=defaulttimeout):
        return self.getElementBy(By.TAG_NAME, tag, timeout)

    def getElementsByTag(self, tag):
        return self.driver.find_elements_by_tag_name(tag)

    def getBaseURL(self):
        return self.base_url
