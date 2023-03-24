import selenium
import undetected_chromedriver as uc
from selenium import webdriver
sel_version=selenium.__version__ 
print("Selinium Version : "+ sel_version )


def create_session():
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    options.add_argument("--lang=fr-FR")

    #options.add_argument('proxy-server=106.122.8.54:3128')
    options.add_argument('--no-proxy-server')
    #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    browser = uc.Chrome(options=options, executable_path="/usr/bin/chromedriver-109")
    return browser
