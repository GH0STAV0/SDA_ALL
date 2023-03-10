import cnf_bvb
# import mod_vpn2
import mod_driver2
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
import zet
import pickle


telrgram_text=[]
email=zet.email
paxx=zet.paxx
url_1=zet.url_1
user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]

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

def check_recovery(driver):
	print("CHECK RECOVERY MAIL !!!!!!")
	try:
		#/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]
		#//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div
		click_on_recovery_email=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]')))
		click_on_recovery_email.click()
		time.sleep(5)
		# //*[@id="knowledge-preregistered-email-response"]
		input_on_recovery_email=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
		input_on_recovery_email.send_keys("cha3b0n@protonmail.com",Keys.ENTER)
		print("OK recovery EMAIL ENTRED !!!!!!")
		time.sleep(8)
	except:
		print("llllol")
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
		driver.get(url_1)
		print(" [ "+url_1+" ]")
		profiletmp = driver.firefox_profile.path
		# but... the current profile is a copy of the original profile :/
		print("running profile " + profiletmp)
		gmail_id_input=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
		gmail_id_input.send_keys(email,Keys.ENTER)
		#ramitamer613
		time.sleep(5)
		gmail_id_input=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		print(paxx)
		gmail_id_input.send_keys(paxx,Keys.ENTER)

		time.sleep(8)
		print(driver.title,driver.current_url)
		# input("p")
		time.sleep(3)
		driver.get(url_1)
		check_recovery(driver)

		
		time.sleep(25)
		compress_prof(driver)		
		driver.get("https://www.youtube.com/")
		time.sleep(5)
	except Exception as e:
		print(e)
	# driver.delete_all_cookies()
	
def compress_prof(driver):
	print("compress_prof",email)
	# input('ok 1')
	os.system("pkill firefox ")
	time.sleep(5)
	copy_cmd="cp -RT /tmp/rust_mozprofile* "+email
	os.system(copy_cmd)
	compress_p_cmd="tar -czvf "+email+".tar.gz "+email
	os.system(compress_p_cmd)
	os.system("rm -rf "+email+" && mv "+email+".tar.gz t_mp/")

	# os.system("ls /tmp/ru*")
	# driver.quit()
	input('ok 1')


def starting_tasks():
	width ,height=cnf_bvb.resolution_func()


######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# mod_vpn2.fnc_vpn ()
		# display = Display(visible=1, size=(width,height)).start()
		driver=mod_driver2.build_driver(width ,height)
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