
from anx import zet , kookie ,session_chrom

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time ,os
from pyvirtualdisplay import Display

from selenium.webdriver.common.keys import Keys
# "vanishmainxxone","vanishxmainxthree","vanishxmainfour"
all_s=["ta3nich","l00k0xmainxvoda","cikox0xmain","danayxmaindanay","cikochildxone","bigoctbig","vanishxmainxtow" \
,"vanishxmainxtow","vanishxmainxthree","vanishxmainfour","cikochildxfour","cikochildxthree","cikochildxtow","cikochildxone"\
,"bigochildxfour","bigochildxthree","bigochildxtow","bigochildxone","vanishmainxxone", \
 "danayxchildx01danay","danayxchildx02danay","danayxchildx03danay"]
email = all_s[0]
# password = "g0ping0*"
password = "baba123A*"
# password = "agoon007A*"
profil_pickle=email+".pkl"
url_y="https://github.com/login"
# url_y="https://shell.cloud.google.com/?cloudshell=true&show=terminal"

# comp=["olamadobano","laminewalter7","kawadurki","vovanvonvowe","gorgegofin","abouichrine"]






def check_now(browser):
    # url_y="https://shell.cloud.google.com/?cloudshell=true&show=terminal"
    try:
        uu=browser.current_url
        print(uu)
        if "cloud.google" in uu :
            print("ok logging")
            browser.get(url_y)

            kookie.dump_coockies(browser,profil_pickle)
    except Exception as a:
        print("Recovery no "+str(a))


def check_confirm(browser):
    try:
        confirmation_preform_tow=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div')))
        print("click confirmation")
        confirmation_preform_tow.click()
        time.sleep(4)
        input_recovey_mail=WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
        input_recovey_mail.send_keys("cha3b0n@protonmail.com",Keys.ENTER)
        print("Recovery Done ..!!!!")
    except Exception as e:
        print("Recovery no ")
    # input('tyu')
    browser.get(url_y)

    # check_now(browser)

def log_in_okt(browser):
    # input("login")
    url_2="https://cloud.okteto.com/#/login"
    browser.get(url_2)
    # //*[@id="app"]/div/div[2]/div/div[2]/button
    input_recovey_mail=WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/button')))
    input_recovey_mail.click()

    input("eeeee")

def log_in(browser):
    # input("login")
    url_1="https://console.cloud.google.com/"
    browser.get(url_y)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'login_field'))).send_keys(email)
    # WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#identifierNext > div > button > span'))).click()
    # password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys(password)
    # input("uuuuuuyyuuuhttps://github.com/login")
    time.sleep(5)
    # WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]'))).click()
    time.sleep(5)
    input("uuuuuuyyuuuhttps://github.com/login")
    # check_confirm(browser)

def check_reconect(browser):
    print("CHECK TEMINAL DISPONIBILITY ..... ",end='',flush=True)
    try:
        print("check")
        reconnect_button=WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloudshell"]/div/horizontal-split/div[2]/devshell/terminal-container/terminal-status-bar/status-message/mat-toolbar/button[2]')))
        reconnect_button.click()
        print("syeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!")
        starting_tasks()
    except Exception as e:
        print("no")
    try:
        print("still  not  fucking  reconect!!!!!!")
        open_login_button=WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
        open_login_button.send_keys("clear && docker ps",Keys.ENTER)
        # cnf_bvb.send_msg_dock("still  not  fucking  reconect!!!!!!")
        time.sleep(3)
        print("OK XTERMINAL FOUND !!!!!!")
        check_reconect(browser)
    except Exception as e:
        print("no2")

def go_go(browser):
    print("go go")
    try:
        open_login_button=WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
        open_login_button.send_keys("sudo su",Keys.ENTER)
        # open_login_button.send_keys("sudo su",Keys.ENTER)
        time.sleep(2)
        open_login_button.send_keys("clear && docker ps",Keys.ENTER)
        time.sleep(3)
        open_login_button.send_keys("./start.sh",Keys.ENTER)
        time.sleep(25)
        check_reconect(browser)

    except Exception as a :
        print(str(a)) 

def check_limit(browser):
    print("Check limite ",flush=True ,end='')
    try:
        open_login_button=WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/cloud-shell-root/div/stand-alone/div[1]/div/loading-screen/div/div/div[2]/div[1]/div/div/div/div')))
        print(" Limites Limite ")
        print(open_login_button.text)

        # cnf_bvb.send_msg_dock("TIME_LIMIT "+open_login_button.text)
    except:
        # cnf_bvb.send_msg_dock("NO TIME_LIMIT ")
        print("No Limites")


def check_shell(browser):
    try:
        browser.get('https://shell.cloud.google.com/?cloudshell=true&show=terminal')
        confirmation_preform_tow=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/dialog-overlay/div[5]/modal-action[2]/button/span[1]')))
        confirmation_preform_tow.click()
        print("close")
        # //*[@id="mat-dialog-0"]/dialog-overlay/div[5]/modal-action[1]/button
    except Exception as e :
        print(str(e))
    check_limit(browser)
    try:
        open_login_button=WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
        print("we are here")
        go_go(browser)
    except Exception as a :
        print(str(a))
def cleann(browser):
    browser.close()
    browser.quit()
    # os.system('rm -rf /tmp/.*  > /dev/null 2>&1 && rm -rf /tmp/tmp* > /dev/null 2>&1')

def dump_cookie(browser):
    log_in(browser)
    # log_in_okt(browser)
    input('ok submit')
    kookie.dump_coockies(browser,profil_pickle)


def load_cookie(browser):

    kookie.load_cookies(browser,profil_pickle)
    # check_shell(browser)
    log_in_okt(browser)
    input('ok submit')
    # kookie.dump_coockies(browser,profil_pickle)


if __name__ == '__main__':
    display = Display(visible=1).start()
    # display = Display(visible=1, size=(width,height)).start()

    browser=session_chrom.create_session()
    # dump_cookie(browser)
    load_cookie(browser)

    # input('ok submit')
    #browser=session_chrom.create_session()
    cleann(browser)
    display.stop()




# preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '')))
# 