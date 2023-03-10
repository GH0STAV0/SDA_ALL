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
import u_a


telrgram_text=[]



url_1=cnf_bvb.url_1

url_site_2=cnf_bvb.url_site_4
second_2_visit=cnf_bvb.second_2_visit
url_6=cnf_bvb.url_6

user_agent = u_a.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]

random_ads=""

url_click_ads="https://click.a-ads.com/1859747/"+random_ads+"/"
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
	os.system("rm geckodriver.log > /dev/null 2>&1 && rm ipifo.json > /dev/null 2>&1")
	os.system("rm -rf  __pycache__/ ")
	os.system("service openvpn restart")
	os.system("rm -rf /tmp/* && rm  l05_00 ipifo.json > /dev/null 2>&1")
	init_fire()


def stage_1():
	try:
		init_fire()
		os.system("rm -rf /tmp/* && rm  l05_00 ipifo.json > /dev/null 2>&1") 
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("service openvpn restart")
		time.sleep(5)
	except Exception as error:
		print (str(error))


def init_fire():
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
	except:
		print(" NO  some_Error init_fire")

def lets_play(driver) :
	time.sleep(1)
	try:
		ads_class(driver)
	except Exception as error:
		print(str(error))
###################################################################################################
	lines=read_current_l0g()
	cnf_bvb.telegrame_api_send_chanel(str(lines))
	# cnf_bvb.send_msg(str(lines))
###################################################################################################

	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass


###################################################################################################
def ytb(driver):
	try:
		print("daz")
	except:
		print('error youtu')


#################################"MAIN STARTING"##############################
def ads_class(driver):
	action = ActionChains(driver)

	try:
		###############################################################################################/html/body/header/div/iframe
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)


		driver.get(url_1)
		# input("pref1")
		# /html/body/section/iframe
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
		# SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/iframe')))
		action.move_to_element(SUCCESS_MSG_BUTTON)
		action.perform()
		print("peform")
		time.sleep(7)
		# input("pref2222")

		try:

			iframes = driver.find_elements_by_xpath("//iframe")

			driver.switch_to.frame(0)
			time.sleep(2)
			# input("pref1"):

			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
			print("peform1 : "+SUCCESS_MSG_BUTTON.text)
			do0n="peform1 : "+SUCCESS_MSG_BUTTON.text
			print(do0n)
			# cnf_bvb.alias_send_msg(SUCCESS_MSG_BUTTON.text)
			time.sleep(7)
		except:
			do0n="peform1 : "
			imges_ifam = driver.find_elements_by_xpath("//img")
			# print(str(imges_ifam))
			for i in imges_ifam :
				# print(i.get_attribute("alt"))
				do0n=do0n+ " | "+i.get_attribute("alt")
			print(" "+do0n)
			time.sleep(7)
			pass
		driver.switch_to.parent_frame()
		time.sleep(2)
		append_to_l0g(do0n)

		time.sleep(15)
	except Exception as e:
		print(e)
	print("CLICK  AND VISITE WEB-SITE [ 2 ]...... ",end='',flush=True)
	# driver.switch_to.parent_frame()
	driver.get(url_1)
	action = ActionChains(driver)
	time.sleep(2)
	# preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/iframe')))
	preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
	action.move_to_element(preform_tow)
	action.perform()
	print("peform")
	ads_text=""
	time.sleep(9)
	try:


			iframes = driver.find_elements_by_xpath("//iframe")
			# print(str(imges_ifam))
			driver.switch_to.frame(0)
			time.sleep(2)
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
			print("peform2 : "+SUCCESS_MSG_BUTTON.text)
			do0n="peform2 : "+SUCCESS_MSG_BUTTON.text
			print(do0n)
			ads_text=SUCCESS_MSG_BUTTON.text
			# if "Earning App" in ads_text:
			# 	print("ccccccccccccccccccc")
			# 	SUCCESS_MSG_BUTTON.click()
			# if "Primebit - P2P Trading" in ads_text:
			# 	print("ccccccccccccccccccc")
			# 	SUCCESS_MSG_BUTTON.click()

			# cnf_bvb.alias_send_msg(SUCCESS_MSG_BUTTON.text)
			time.sleep(7)
	except:
		do0n="peform2 : "
		imges_ifam = driver.find_elements_by_xpath("//img")
		# print(str(imges_ifam))
		for i in imges_ifam :
			# print(i.get_attribute("alt"))
			do0n=do0n+ " | "+i.get_attribute("alt")

			ads_text=i.get_attribute("alt")
			# i.click()

		print(" "+do0n)
		
		# matches = ["Primebit", "PROJECTS?", "Claim"]
		# preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))

		# preform_tow.click()
		time.sleep(7)
		pass
	driver.switch_to.parent_frame()
	print("oooooooo"+ads_text)
	# "Primebit - P2P Trading",
	# matches = ["Primebit - P2P Trading","Swap On ETHPOWETHPOW !","Hurry","BTCMiddleMan.com","Metaplayerone","Telegram","Primebit", "PROJECTS?", "Claim","More Opportunity , More Benefits","FIRST LIQUID CRYPTO TRADING BOT!"]
	# matches = ["BTCMiddleMan.com","BC.Game FIFA world cup","Swap On ETHPOWETHPOW !","Win Crypto Answering Avatar: TLA Trivia on YouTube","The Best Rates in DeFi !","Claim your P2,500 risk free first bet","Best Earning App","Primebit - P2P Trading","Token check if it is a probable honeypot or risky.","Free to play, win USD"]
	# matches = [" MET500 Unrivaled Crypto Staking","MET500 Unrivaled Crypto Staking","Free to play, win USD XD","Mint, lock and launch your tokens for free","GET FREE SPINS","Got crypto? Got bills? Setup bill pay and GET $50!","Dollarmoon","A new crypto investment game","ARE YOU INTERESTED IN CRYPTO PROJECTS?","Dollarmoon is the safe way to the moon","UnityMeta Token Wishes Happy New Year 2023","BTCMiddleMan.com","New vaults up to 80% APY","Swap On ETHPOWETHPOW !","Metaplayerone","Win Crypto Answering Avatar: TLA Trivia on YouTube","The Best Rates in DeFi !","Claim your P2,500 risk free first bet","Best Earning App","Primebit - P2P Trading","Token check if it is a probable honeypot or risky.","Free to play, win USD","FIRST LIQUID CRYPTO TRADING BOT!","More Opportunity , More Benefits"]
	matches = cnf_bvb.matches

	preform_tow=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/iframe')))
	if any(x in ads_text for x in matches):
		preform_tow.click()
		print(" 22222222222222222xxxx")
		do0n=do0n+" XD"
	append_to_l0g(do0n)
	driver.get("https://bytes-x-space.blogspot.com/2022/01/parsing-json-with-unix-tools.html")
		# SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-box-normal"]/div[3]/button')))
		# SUCCESS_MSG_BUTTON.click()
		# time.sleep(7)
	time.sleep(12)
	# driver.get("https://youtu.be/3bMYY5mF83Y")
	# input("tr")
	# time.sleep(12)

	append_to_l0g("VISITE WEB-SITE [ 2 ] : [ +second_2_visit+]  OK")

		# time.sleep(2)
		# driver.execute_script("window.open('');")
		# driver.switch_to.window(driver.window_handles[2])
		# driver.get("http://dark-market.ueuo.com/index.html")
		# time.sleep(8)
		# time.sleep(3)


	driver.delete_all_cookies()
	print("Remove Cookies")



def blogger(driver):
	try:

		ain_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.top-banner')))
		ain_button.click()
		print('ok click')
		time.sleep(25)
	# driver.get(url_6)
	except Exception as e:
		print("error scrol 1")
		#####################################################################################
	driver.get(url_6)
	time.sleep(5)
	# input("")
	try:
		accept_coockies=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'cookieChoiceDismiss')))
		accept_coockies.click()
		time.sleep(5)
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	except Exception as e:
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	time.sleep(3)
	try:
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML4'))))
		time.sleep(5)
		# driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'PopularPosts1'))))
		# time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML2'))))
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(10)
	except Exception as e:
		print("error scrol 1")
	try:
		post1_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[1]/div[1]/div[2]/a')))
		post1_coockies.click()
		print("1111111111111111111111111")
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML4'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'PopularPosts1'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML2'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(10)

		# time.sleep(5)
		post2_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[2]/div[1]/div[2]/a')))
		post2_coockies.click()
		print("22222222222222222222222222222222")
		time.sleep(5)

		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(5)
		#time.sleep(4)

		post3_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[3]/div[1]/div[2]/a')))
		post3_coockies.click()
		print("X3333333333333333333")
		# input('')
		time.sleep(3)
		time.sleep(5)
	except Exception as e:
		print("error scrol 1")
	# time.sleep(1)
	# driver.execute_script("window.open('');")
	# time.sleep(3)
	# driver.switch_to.window(driver.window_handles[1])
	# time.sleep(3)
# p0st_phase()
def starting_tasks():
	width ,height=cnf_bvb.resolution_func()


######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# cnf_bvb.p0st_phase()
		visible_v=cnf_bvb.visible_v
		mod_vpn2.fnc_vpn ()
		display = Display(visible=visible_v, size=(width,height)).start()
		# cnf_bvb.alias_send_msg_2()
		# os.environ['DISPLAY']
		# driver=mod_driver2.build_driver(width ,height)
		# sz=width+","+height
		sz=height+","+width
		driver,log_driver_chrom = drive_md_chrom.build_driver(sz)
		# print(log_driver_chrom)
		driver.maximize_window()
		lets_play(driver)
		#driver.delete_all_cookies()
		display.stop()


	except Exception as error:
		print (str(error))
	clean_up()

def main():
	starting_tasks()
	clean_up()
	os.system("rm -rf /tmp/*")
	# append_to_l0g("text_add")


if __name__ == '__main__':

	main()


# begaining_loop()
