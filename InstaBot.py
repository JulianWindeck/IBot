import time
import random
from selenium.webdriver.common.keys import Keys
import Utils
import Browser

class InstaBot:

    #about 200 likes an hour
    #follow / unfollow 15-20 per hour and max of 100-200 a day (when new account)

    loginPath = '/accounts/login/'

    def __init__(self, username, password):
        self.driver = Browser.Browser('https://www.instagram.com', './res/chromedriver')

        self.username = username
        self.passw = password

    def login(self):
        driver = self.driver
        print(type(driver.base_url))
        driver.openSubPath(self.loginPath)


        i_name = driver.getElementByXPath("//input[@name='username']")
        i_pass = driver.getElementByXPath("//input[@name='password']")

        #enter login information and submit by pressing enter
        driver.microdelay()
        i_name.send_keys(self.username)
        driver.microdelay()
        i_pass.send_keys(self.passw)
        driver.microdelay()
        i_pass.send_keys(Keys.ENTER)

    def likePic(self, hashtag):
        driver = self.driver
        driver.openSubPath('/explore/tags/%s/' % hashtag)
        driver.wait(4)

        for i in range(1, 6):
            driver.scrollDown()

        links = driver.getElementsByTag('a')
        pic_links = [link.get_attribute('href') for link in links if '.com/p/' in link.get_attribute('href')]
        print('[+] Found %d photos for %s' % (len(pic_links), hashtag))
        driver.wait(3)

        picsLeft = len(pic_links)
        for pic in pic_links:
            try:
                driver.openURL(pic, 3) #wait 3 seconds before liking pic

                likeBtn = driver.getElementByXPath('//span[@aria-label="Gefällt mir"]')
                likeBtn.click()

                #insta only allows ~200 likes / h
                for second in reversed(range(random.randint(18, 23))):
                    Utils.print_same_line("#" + hashtag + ': unique photos left: ' + str(picsLeft)
                                    + " - sleeping " + str(second))
                    time.sleep(1)
            except Exception as e: #e.g. when site doesn't load
                time.sleep(1)
            picsLeft -= 1

    def terminate(self):
        self.driver.quit()


if __name__ == '__main__':

    #enter your information
    username = 'USERNAME'
    password = 'PASSWORD'
    hashtags = [
        'fitness'
    ]

    random.seed()
    try:
        ibot = InstaBot(username, password)
        ibot.login()
        time.sleep(5)
        tag = random.choice(hashtags)
        ibot.likePic(tag)
    except Exception as e:
        print('[-] Error occured: ', e)
    finally:
        ibot.terminate()