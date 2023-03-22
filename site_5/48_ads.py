import cnf_bvb
import mod_vpn2
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
import drive_md_chrom
import extt
# import pickle
dd="nnnn"
dd1="nnnn"
telrgram_text=[]
telrgram_text_log=[]
###########global urls_BVB
telrgram_text_log.append("object")

# print(extt.fuckk)
# print(telrgram_text_log)
# input('')
url_1=cnf_bvb.url_1
url_y="https://www.youtube.com/watch?v=9dgydVy_8xU"
print (url_1)

url_site_2=cnf_bvb.url_site_4
second_2_visit=cnf_bvb.second_2_visit
url_6=cnf_bvb.url_6

user_agent = cnf_bvb.user_agent



sys_use_agent=re.findall('\(.*?\)',user_agent)[0]

# telrgram_text_log.extend((url_1,user_agent,sys_use_agent))
extt.fuckk.extend((url_1,user_agent,sys_use_agent))
# print(telrgram_text_log)


########################################################################################################################################
##############################################################
l05_00='l05_00'
def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")
	# 	# for i in all_vpn_config_file:

##############################################################


def read_current_l0g():
	final_msg=''
	with open(l05_00,'r') as file:
		lines = file.readlines()
		for i in lines:
			final_msg=final_msg + i
	return final_msg
############################################################################




def clean_up():
	os.system("rm -rf /tmp/*")
	os.system("rm geckodriver.log && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf  __pycache__/ ")
	os.system("service openvpn restart")

	init_fire()


def stage_1():
	try:
		#print (url_1)
		init_fire()
		os.system("rm -rf /tmp/* && rm l05_00")
		os.system("clear && sleep 1")
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+url_1+' :check_mark_button: :alien:'))
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("service openvpn restart")
		time.sleep(5)
	except Exception as error:
		print (str(error))
	#starting_tasks()
############################################################################################

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

def lets_play(driver) :
	time.sleep(1)
	try:
		ads_class(driver)
	except Exception as error:
		print(str(error))



###################################################################################################

	
	# cnf_bvb.send_msg(str(lines))
	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')

###################################################################################################

	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass


###################################################################################################

def check_ads(driver,banner_text):
	#"BC.Game FIFA world cup",
	# preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
	#"Win Crypto Answering Avatar: TLA Trivia on YouTube",
	# matches = ["BC.Game FIFA world cup","Free to play, win USD","Primebit - P2P Trading","Swap On ETHPOWETHPOW !","Hurry","BTCMiddleMan.com","Metaplayerone","Telegram","Primebit", "PROJECTS?", "Claim","More Opportunity , More Benefits","FIRST LIQUID CRYPTO TRADING BOT!"]
	# matches = ["Dollarmoon","A new crypto investment game","ARE YOU INTERESTED IN CRYPTO PROJECTS?","Dollarmoon is the safe way to the moon","UnityMeta Token Wishes Happy New Year 2023","BTCMiddleMan.com","BC.Game FIFA world cup","Swap On ETHPOWETHPOW !","Metaplayerone","Win Crypto Answering Avatar: TLA Trivia on YouTube","The Best Rates in DeFi !","Claim your P2,500 risk free first bet","Best Earning App","Primebit - P2P Trading","Token check if it is a probable honeypot or risky.","Free to play, win USD","FIRST LIQUID CRYPTO TRADING BOT!","More Opportunity , More Benefits"]
	# "",DAILY FREE CASE **NO PAYMENT** $500 PRIZE! $3000 New User Rewards
	matches=cnf_bvb.matches

	# matches = ["Get Rich Quick with Gold Recovery","Trend On CMC","BC.Game FIFA world cup","Launch your website with a 1-click install","TapCrypto","Play casino games","$3000 New User Rewards","DAILY FREE CASE **NO PAYMENT** $500 PRIZE!","BUSDchain","GET FREE SPINS","Join IMPT.io","Join IMPT.io before USE Case 1 is Live","Free to play, win USD XD","Mint, lock and launch your tokens for free","GET FREE SPINS","Got crypto? Got bills? Setup bill pay and GET $50!","Dollarmoon","A new crypto investment game","ARE YOU INTERESTED IN CRYPTO PROJECTS?","Dollarmoon is the safe way to the moon","UnityMeta Token Wishes Happy New Year 2023","BTCMiddleMan.com","New vaults up to 80% APY","Swap On ETHPOWETHPOW !","Metaplayerone","Win Crypto Answering Avatar: TLA Trivia on YouTube","The Best Rates in DeFi !","Claim your P2,500 risk free first bet","Best Earning App","Primebit - P2P Trading","Token check if it is a probable honeypot or risky.","Free to play, win USD","FIRST LIQUID CRYPTO TRADING BOT!","More Opportunity , More Benefits"]
	final_text=" CLICKED BANNERS_TEXT : "+banner_text
	print(final_text)
	donn_o="null"
	# preform_tow.click()
	if any(x in banner_text for x in matches):
		preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
		preform_tow.click()
		append_to_l0g("XD "+final_text+" XD")
		donn_o="XD XD"
		
		time.sleep(25)
	extt.fuckk.extend((banner_text,donn_o))

###################################################################################################

#################################"MAIN STARTING"##############################
def ads_class(driver):
	ads_ban_1=""
	ads_ban_2=""
	action = ActionChains(driver)
	banner_text=""

	try:
		###############################################################################################
		print("VISITE WEB-SITE [   "+url_y+"  ].. ",end='',flush=True)

		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)

		driver.get(url_1)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
		action.move_to_element(SUCCESS_MSG_BUTTON)
		action.perform()
		# print("peform 01")
		time.sleep(7)

		try:
			iframes = driver.find_elements_by_xpath("//iframe")
			print("peform donn ")
			driver.switch_to.frame(0)
			time.sleep(2)
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
			print("peform1 : "+SUCCESS_MSG_BUTTON.text)
			do0n="peform1 : "+SUCCESS_MSG_BUTTON.text
			print(do0n)
			# banner_text=SUCCESS_MSG_BUTTON.text
			ads_ban_1=SUCCESS_MSG_BUTTON.text
			time.sleep(7)
		except:
			print("P 1")
		try:
			do0n="peform1 : "
			imges_ifam = driver.find_elements_by_xpath("//img")
			# print(str(imges_ifam))
			for i in imges_ifam :
				# print(i.get_attribute("alt"))
				do0n=do0n+ " | "+i.get_attribute("alt")
				ads_ban_1=i.get_attribute("alt")
			print(" "+do0n)
			time.sleep(7)
			pass
		except:
			print("P 2")
		driver.switch_to.parent_frame()
		time.sleep(2)
		append_to_l0g(do0n)

		time.sleep(15)
	except Exception as e:
		print(str(e))
#####################################################################################
	print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)
	driver.get(url_1)
	action = ActionChains(driver)
	time.sleep(2)
	preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
	action.move_to_element(preform_tow)
	action.perform()
	print("peform")
	time.sleep(9)
	try:
		iframes = driver.find_elements_by_xpath("//iframe")
		driver.switch_to.frame(0)
		time.sleep(2)

		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
		print("peform2 : "+SUCCESS_MSG_BUTTON.text)
		do0n="peform2 : "+SUCCESS_MSG_BUTTON.text
		banner_text=SUCCESS_MSG_BUTTON.text
		ads_ban_2=SUCCESS_MSG_BUTTON.text
		print(do0n)
		time.sleep(7)
	except:
		print("P 1")
	try:
		do0n="peform2 : "
		imges_ifam = driver.find_elements_by_xpath("//img")
		for i in imges_ifam :
			do0n=do0n+ " | "+i.get_attribute("alt")
			banner_text=i.get_attribute("alt")
			ads_ban_2=banner_text
		print(" "+do0n)
		time.sleep(7)
		pass
	except:
		print("P 2")


	driver.switch_to.parent_frame()

	check_ads(driver,banner_text)
	append_to_l0g(do0n)
	time.sleep(12)
	extt.fuckk.extend((ads_ban_1,ads_ban_2))
	# print(extt.fuckk)
	# input('')
	append_to_l0g("VISITE WEB-SITE [ 2 ] : [ +second_2_visit+]  OK")
	driver.delete_all_cookies()
	print("Remove Cookies")
#####################################################################################

def starting_tasks():
	width ,height=cnf_bvb.resolution_func()
	try:
		stage_1()### CLEAR
		# cnf_bvb.p0st_phase()
		visible_v=cnf_bvb.visible_v
		# telrgram_text_log.extend((visible_v))
		extt.fuckk.extend((str(visible_v)))
		# print(extt.fuckk)
		# input('')
		mod_vpn2.fnc_vpn ()
		display = Display(visible=visible_v, size=(width,height)).start()
		# cnf_bvb.alias_send_msg_2()
		# os.environ['DISPLAY']
		# driver=mod_driver2.build_driver(width ,height)
		# sz=width+","+height
		sz=height+","+width
		# extt.fuckk.extend((str(sz)))

		# print(extt.fuckk)
		# input('')
		driver=drive_md_chrom.build_driver(sz)
		driver.maximize_window()
		lets_play(driver)
		#driver.delete_all_cookies()
		display.stop()
	except Exception as error:
		print (str(error))
	



os.system("rm -rf /tmp/*")





def main():
	starting_tasks()
	lines=read_current_l0g()
	cnf_bvb.telegrame_api_send_chanel(str(lines))
	# append_to_l0g("text_add")
	clean_up()
	print(extt.fuckk)
	extt.tel_banner(extt.fuckk)


if __name__ == '__main__':

	main()


# begaining_loop()
