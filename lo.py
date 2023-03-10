import undetected_chromedriver as uc
import random,time,os,sys
# from selenium.webdriver.common.keys import Keys

GMAIL = '<GMAIL_HERE>'
PASSWORD = '<PASSWORD_HERE>'

chrome_options = uc.ChromeOptions()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-popup-blocking")

chrome_options.add_argument("--profile-directory=Default")

chrome_options.add_argument("--ignore-certificate-errors")

chrome_options.add_argument("--disable-plugins-discovery")

chrome_options.add_argument("--incognito")

chrome_options.add_argument("user_agent=DN")

driver = uc.Chrome(options=chrome_options)

driver.delete_all_cookies()

driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)

time.sleep(10)
# from selenium_stealth import stealth
# from selenium import webdriver
# driver = webdriver.Chrome()
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
# mail_address = ''
# password = ''

# from selenium import webdriver

# UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
# PHANTOMJS_ARG = {'phantomjs.page.settings.userAgent': UA}
# driver = webdriver.Chrome(desired_capabilities=PHANTOMJS_ARG)

# url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp/'
# driver.get(url)
# input("lll")

# driver.find_element_by_id("Email").send_keys(mail_address)
# driver.find_element_by_id("next").click()
# driver.find_element_by_id("Passwd").send_keys(password)
# driver.find_element_by_id("signIn").click()
