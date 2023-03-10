import cnf_bvb_p
# import mod_vpn2
import mod_driver3
import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
from selenium.webdriver import ActionChains
import json
import pickle
# xamiramogdan 
telrgram_text=[]
# email="xamiramogdan"
# email="almidaopo"
# email="azfounmondilla"
# email="abedrahman0x"
# email="don0mar0l0k0"
# email="xamiramogdan"
# email="islamouissam"
# email="xamiramogdan"
# email="xamiramogdan"
# email="abouichrine"
email="youcefshalhoub"
paxx="g0ping0**"

###########global urls_BVB
# urls_BVB=cnf_bvb.random_url
#####################################
# urls_BVB="https://wild-beauty.weebly.com/about.html"
#url_1="https://bitcoin-chat-news-and-games.netlify.app/index.html"
# url_1="https://cryptocurency-space.netlify.app/index.html"
url_1="https://console.cloud.google.com/"

# url_3="https://elated-nobel-943d26.netlify.app/index.html"
# random_display_chose=cnf_bvb.random_display_chose
# width=cnf_bvb.width
# height=cnf_bvb.height
# main_url="https://nordcheckout.com/"
user_agent = cnf_bvb_p.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]



random_ads=cnf_bvb_p.random_ads
url_click_ads="https://click.a-ads.com/1859747/"+random_ads+"/"
########################################################################################################################################




def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf rm -rf __pycache__/")
	init_fire()







	#starting_tasks()
############################################################################################









def lets_play(driver) :
	
	time.sleep(1)
	try:
		ads_class(driver)	
	except Exception as error:
		print(str(error))

	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')


	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass

#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver_15 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*")
		os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		#
		time.sleep(5)
		print(" OK !!!")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (url_1)
		init_fire()
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+url_1+' :check_mark_button: :alien:'))
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")
	except Exception as error:
		print (str(error))

###########################################################################
def check_reconect(driver):
	print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)

	try:
		reconnect_button=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloudshell"]/div/horizontal-split/div[2]/devshell/terminal-container/terminal-status-bar/status-message/mat-toolbar/button[2]')))
		reconnect_button.click()
		print("syeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!")
		starting_tasks()
		
	except Exception as e:
		print("still  not  fucking  reconect!!!!!!")
		open_login_button=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
		open_login_button.click()
		open_login_button.send_keys("clear && docker ps",Keys.ENTER)
		time.sleep(300)
		check_reconect(driver)



#################################"MAIN STARTING"##############################
def ads_class(driver):
	try:
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		# print(driver.execute_script("return navigator.userAgent;"))
		# driver.get("https://sqa.stackexchange.com/questions/2811/how-to-specify-a-firefox-profile-name-when-using-webdriver-python")
		# driver.get(url_1)
		# print(" [ "+url_1+" ]")
		# cookies = pickle.load(open("cookies.pkl", "rb"))
		# # for cookie in cookies:
		# # 	driver.add_cookie(cookie)
		# input("ok cookie")
		# driver.get(url_1)
		# print(driver.get_cookies())
		# cookie1 = driver.get_cookies()
		# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
		# print(cookie1)
		# gmail_id_input=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
		# # gmail_id_input.send_keys("xamiramogdan",Keys.ENTER)
		# # gmail_id_input.send_keys("quarinamouslou",Keys.ENTER)
		# gmail_id_input.send_keys(email,Keys.ENTER)
		# #ramitamer613
		# time.sleep(20)
		# gmail_id_input=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		# # gmail_id_input.send_keys("testpassw0rdDZ*",Keys.ENTER)
		# # gmail_id_input.send_keys("agoon007",Keys.ENTER)
		# gmail_id_input.send_keys(paxx,Keys.ENTER)

		# time.sleep(3)
		# print(driver.get_cookies())
		# # input('')

		
		driver.get("https://shell.cloud.google.com/?cloudshell=true&show=terminal")
		profiletmp = driver.firefox_profile.path
		# but... the current profile is a copy of the original profile :/
		print("running profile " + profiletmp)
		time.sleep(25)

		# input("")
		# input('google loginAAAAAAAAAAAA')
		open_login_button=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
		open_login_button.click()
		open_login_button.send_keys("sudo su",Keys.ENTER)
		time.sleep(10)
		open_login_button.send_keys("clear && docker ps",Keys.ENTER)
		open_login_button.send_keys("./start.sh",Keys.ENTER)
		# input('google loginBBBBBBBBBBBBB')

		# gmail_id_input=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloudshell"]/div/horizontal-split/div[2]/devshell/terminal-container/div/xterm-terminal-tab/div/xterm-terminal/div')))
		# active-terminal-frame ng-star-inserted
		# gmail_id_input.send_keys(Keys.TAB*7,"lol",Keys.ENTER)
		# open_login_button.send_keys("docker ps",Keys.ENTER)
		# input('google login')
		# driver.refresh()
		# time.sleep(5)
		# print("CLICK  AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		# getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'rightbox')))
		# time.sleep(5)
		# print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		# action = ActionChains(driver)
		# action.move_to_element(getLink_button)# .perform()
		# time.sleep(25)
		
		# getLink_button.click()



		# print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)

		# driver.get(url_click_ads)

		time.sleep(25)
		check_reconect(driver)

	except Exception as e:
		print(e)
	# driver.delete_all_cookies()
	
		
def starting_tasks():
	width ,height=cnf_bvb_p.resolution_func()


######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# mod_vpn2.fnc_vpn ()
		# display = Display(visible=1, size=(width,height)).start()
		driver=mod_driver3.build_driver(width ,height)
		lets_play(driver)
		# display.stop()
		clean_up()

	except Exception as error:
		print (str(error))



os.system("rm -rf /tmp/*")





def main():
	starting_tasks()


if __name__ == '__main__':

	main()



# begaining_loop()