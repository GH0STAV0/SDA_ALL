import cnf_bvb
# import mod_vpn2
import mod_driver2
import emoji
import gc_ac__sql
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
import signal

def handler(signum, frame):
	print("############################")
	print("Ctrl-c was pressed. You are Killing the prossec !!! really want to exit!!")
	res='y'
	if res == "y":
		kiliing_scr()
		exit(1)

	# res = "y"
	# 	if res == 'y':
	# 		exit(1)
signal.signal(signal.SIGINT, handler)

telrgram_text=[]







email=cnf_bvb.g00g_acc

paxx="g0ping0*"


url_1="https://console.cloud.google.com/"

user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]



random_ads=cnf_bvb.random_ads
url_click_ads="https://click.a-ads.com/1859747/"+random_ads+"/"
########################################################################################################################################


###################################################################################################
def kiliing_scr():
	init_fire()
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf __pycache__/")
	# os.system("rm -rf tmp/*")



def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf __pycache__/")
	# os.system("rm -rf tmp/*")
	init_fire()
#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i geckodriver_15 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*")
		os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		#
		time.sleep(5)
		print(" OK !!!")
		# os.system("rm -rf tmp/*")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################






	#starting_tasks()
############################################################################################









def lets_play(driver) :
	
	time.sleep(1)
	try:
		ads_class(driver)	
	except Exception as error:
		cnf_bvb.send_msg_dock(str(error))
		print(str(error))

	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')


	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass


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
	print("CHECK TEMINAL DISPONIBILITY ..... ",end='',flush=True)
	try:
		reconnect_button=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloudshell"]/div/horizontal-split/div[2]/devshell/terminal-container/terminal-status-bar/status-message/mat-toolbar/button[2]')))
		reconnect_button.click()
		print("syeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!")
		cnf_bvb.alias_send_msg("NO syeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ")
		starting_tasks()
		
	except Exception as e:
		print("still  not  fucking  reconect!!!!!!")
		open_login_button=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
		# open_login_button.click()
		open_login_button.send_keys("clear && docker ps",Keys.ENTER)
		cnf_bvb.alias_send_msg("still  not  fucking  reconect!!!!!!")
		time.sleep(300)
		# driver.save_screenshot("scr.png")
		print("OK XTERMINAL FOUND !!!!!!")
		check_reconect(driver)

def check_recovery(driver):
	print("CHECK RECOVERY MAIL !!!!!!")
	try:
		click_on_recovery_email=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div')))
		click_on_recovery_email.click()
		time.sleep(5)
		input_on_recovery_email=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
		input_on_recovery_email.send_keys("cha3b0n@protonmail.com",Keys.ENTER)
		print("OK recovery EMAIL ENTRED !!!!!!")
		time.sleep(8)



	except Exception as e:
		print("NO RECOVERY ")



#################################"MAIN STARTING"##############################
def ads_class(driver):
	try:
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		try:
			# pass
			driver.get("https://shell.cloud.google.com/?cloudshell=true&show=terminal")
			time.sleep(10)
			print(" OK")
			check_profile_validity(driver)

			# 

			open_login_button=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
			# input('google loginAAAAAAAAAyAAA')
			print("we are here")
			staage="OK XTEMINAL ACTIVATED [ "+cnf_bvb.g00g_acc+" ]"
			print(staage)
			cnf_bvb.send_msg_dock(staage)
			time.sleep(13)
			# input('google loginAAAAAAAAAyAAA')
			# open_login_button.click()
			time.sleep(3)
			print("0000000 we are here")
			open_login_button.send_keys("sudo su",Keys.ENTER)
			time.sleep(10)
			open_login_button.send_keys("clear && docker ps",Keys.ENTER)
			time.sleep(3)
			open_login_button.send_keys("./start.sh",Keys.ENTER)
			time.sleep(25)
			check_reconect(driver)
		except Exception as e:
			cnf_bvb.send_msg_dock("ERROR "+str(e))
			print(str(e)+" errrrrrrrro1")

	except Exception as e:
		print("ads error"+str(e))
		cnf_bvb.send_msg_dock("ERROR ")
	# driver.delete_all_cookies()
###########################################################################
def check_limit(driver):
	try:
		open_login_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/cloud-shell-root/div/stand-alone/div[1]/div/loading-screen/div/div/div[2]/div[1]/div/div/div/div')))
		print(open_login_button.text)
		cnf_bvb.alias_send_msg("TIME_LIMIT "+open_login_button.text)
		# input("terminaaa")
		# init_fire()
	except:
		cnf_bvb.alias_send_msg("NO TIME_LIMIT ")

#################################"MAIN STARTING"##############################

def check_profile_validity(driver):

	print("check_profile_validity",end='',flush=True)
	cnf_bvb.alias_send_msg("check_profile_validity ")
	get_url = driver.current_url
	
	if "signinchooser" in get_url:
		etat="Deconnected"
		print(" ",etat)
		
		# print(get_url)
		# input("dec")
		deconected_prof(driver)
	get_url = driver.current_url
	if "shell.cloud" in get_url :
		etat="Connected"
		check_limit(driver)
		# input("Connected")
	print(" ",etat)
	msg="etat : "+etat
	cnf_bvb.alias_send_msg(msg)

	try:
		dissmi=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/cloud-shell-root/div/stand-alone/div[1]/div/horizontal-split/div[2]/devshell/terminal-container/terminal-status-bar/status-message/mat-toolbar/button')))
		# input('google loginAAAAAAAAAyAAA')
		dissmi.click()
		time.sleep(3)
		print('ok Dissmissed')
	except :
		print('no Dissmissed')

def deconected_prof(driver):
	# 
	try:
		d3coneted_button=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')))
		print("found D3conecte : ", d3coneted_button.text)
		insert_pass(driver)
		# pass
	except Exception as e:
		print("no deconecte")
	
######################USER AGENT ###################################################


####################################################################################################################################################################################################################################################################################
def insert_pass(driver):
	print("clicking ",end='',flush=True)

	try:
		# pass
		
		d3coneted_button=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')))
		d3coneted_button.click()
		# input("deconected_prof : FINISH")
		time.sleep(5)
		print("ENTER PA55 : ")
		pass_input_button=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
		pass_input_button.click()
		pass_input_button.send_keys(paxx,Keys.ENTER)
		print("deconected_prof : FINISH")
	except Exception as e:
		# input("deconected_prof : error FINISH")
		print("deconected_prof : error FINISH")
		# raise e
####################################################################################################################################################################################################################################################################################



######################USER AGENT ###################################################
		
def starting_tasks():
	cnf_bvb.alias_send_msg("starting_tasks")

	try:
		width ,height=cnf_bvb.resolution_func()
		stage_1()### CLEAR
		# mod_vpn2.fnc_vpn ()
		visible_v=cnf_bvb.visible_v
		# print(str(height))
		display = Display(visible=visible_v, size=(width,height)).start()
		# input('xxx')
		driver=mod_driver2.build_driver(width ,height)
		lets_play(driver)
		display.stop()
		clean_up()

	except Exception as error:
		cnf_bvb.send_msg_dock(str(error))
		print (str(error) +"eeee")



os.system("rm -rf /tmp/*")

# cnf_bvb.alias_send_msg("twiiiiiiiitarr")



def main():
	cnf_bvb.send_msg_dock("main")
	cnf_bvb.extract_pof()
	try:
		starting_tasks()
	except Exception as error:
		print(str(error)+"00000000000000000")
		cnf_bvb.send_msg_dock(str(error))
	kiliing_scr()


if __name__ == '__main__':

	main()
	kiliing_scr()


# begaining_loop()