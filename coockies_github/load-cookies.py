import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def chrome_session():

    options = uc.ChromeOptions()
    options.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox","--disable-web-security"])
    browser = uc.Chrome(options)
    return browser


if __name__ == '__main__':
    browser=chrome_session()
    browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        cookie['domain'] = ".google.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            # print(str(e))
            pass

    browser.get('https://mail.google.com/mail/u/0/#inbox')

    # time.sleep(120)
    input("gfg")
    browser.get('https://amiunique.org/')
    time.sleep(120)