import random , os ,requests
import json
import socket
import urllib.parse
import emoji
import u_a
import extt

# "$4000 Welcome","join our presale now","medicoinswiss saves life","AMV","BC.Game Free Spin to Get 1 BTC"
matches = ["Get Whitelist for $KVN IDO Now!", "Stakify.io","Play on Khiladi and Win Money 1300%* Welcome Bonus","$4000 Welcome","join our presale now","medicoinswiss saves life","AMV","Coinscasino.io","BC.Game","Trading on Gate.io and MEXC","Richlama - Better Than Sports Betting","Get ready to blast off to the moon!","BC.Game Free Spin to Get 1 BTC","Online Casino","Get COINS every day!","R3T - BRICK BY BRICK WE BUILD AN EMPIRE","Fomo3D_Arbitrum","Solid community ready for take off!","easy 50x after list on cmc","With our ready-made Premium PHP Casino Scripts","Instant payment 650% per hour","BC.Game - spin now!" ,"Receive SMS messages securely and anonymously!","NeRF -- ERC" ,"MEVs Army App","Litecoin Giveaway","ZeroQT Venture Capital","Get FREE NFT","Get Rich Quick with Gold Recovery","Trend On CMC","BC.Game FIFA world cup","Launch your website with a 1-click install","TapCrypto","Play casino games","$3000 New User Rewards","DAILY FREE CASE **NO PAYMENT** $500 PRIZE!","BUSDchain","GET FREE SPINS","Join IMPT.io","Join IMPT.io before USE Case 1 is Live","Free to play, win USD XD","Mint, lock and launch your tokens for free","GET FREE SPINS","Got crypto? Got bills? Setup bill pay and GET $50!","Dollarmoon","A new crypto investment game","ARE YOU INTERESTED IN CRYPTO PROJECTS?","Dollarmoon is the safe way to the moon","UnityMeta Token Wishes Happy New Year 2023","BTCMiddleMan.com","New vaults up to 80% APY","Swap On ETHPOWETHPOW !","Metaplayerone","Win Crypto Answering Avatar: TLA Trivia on YouTube","The Best Rates in DeFi !","Claim your P2,500 risk free first bet","Best Earning App","Primebit - P2P Trading","Token check if it is a probable honeypot or risky.","Free to play, win USD","FIRST LIQUID CRYPTO TRADING BOT!","More Opportunity , More Benefits","Lock your tokens and liquidity for free!","Make your own crypto tokens for free on DxSale!","Launch your crypto tokens for free on DxSale","Start Gambling for Great Rewards!","Win $15 in Crypto for Avatar:TLA Trivia on YouTube","DAILY FREE CASE **NO PAYMENT** $500 PRIZE!","Earn bitcoins or advertise your project with A-ADS","Anuncios que respeten tu privacidad","Lock your tokens and liquidity for free!"]
print(str(len(matches)))
hostname_os=socket.getfqdn()
visible_v=0
os.system("cp /root/0nord_pass /root/SDA_ALL/site_5/0nord_pass")
# curl https://raw.githubusercontent.com/cata0nana/start/main/p/2 > /root/0nord_pass
if "LOOKE3" in hostname_os:
	print(hostname_os)
	visible_v=1


l05_00='l05_00'
def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")



vpn_type="N"
total_l0g=[]
vversion="101_SITE_5 V 6.0 io/IMG = xm0uray-site_5 | chrome api ++v977"
telegram_tokens_bot=["0","5036803152:AAGs0ES1OmEdy86MNJDp7mp19BB5IQhcVHU","5099462819:AAEndTxvXaSqBQ6E_EpiCN02a81ROGPMgr0","5001651751:AAGzzbUfJXWHZz-FKJyLSUxzg-JiRMO5v-Q","5041058138:AAFRher-cMwnRI476iW24tT6Kt8lvC0bmLc","5051743922:AAEOHJTRzv2WIxZ8bR-VrVYNA6io6qB1Ltw"]


def ap_2_l0g(gms):
	total_l0g.append(gms)


urls=["https://mohmal.eu.org/"]

# "NeRF -- ERC" "" ""
url_6=urls #"https://www.bit-plazza.nl.eu.org/?m=0"


def set_url():
	random_url=random.choice(urls)
	return random_url

url_1=set_url()
#"https://dark0s-market.eu.org/index.html"

# url_1="http://free-coin.nichesite.org/index.html"

# url_1="https://dark-market.eu.org/index.html"

# url_1="dark-market.likesyou.org"
# url_1="https://dark-market-crypto.tk/"

# url_1="http://dark-market.likesyou.org/index.html"
# url_1="https://www.iblogger.nl.eu.org/2021/12/getting-hostname-in-bash-in-linux.html"
# url_1="http://dark-market.ueuo.com/index.html"
# url_1="https://darkos-market.eu.org/index.html"
url_site_2="https://www.iblogger.nl.eu.org/index.html"
# url_2=url_1.replace("https://","")
url_2=url_1.replace("https://","")
# url_2=url_2.replace("2021/12/getting-hostname-in-bash-in-linux.html","")
url_2=url_2.replace("/index.html","")
# url_site_2
url_site_4=url_site_2.replace("https://","")
url_site_4=url_site_4.replace("/2021/12/bash-you-can-get-hostname-of-node-in-at.html","")
# N= norrd

# second_2_visit='https://www.iblogger.nl.eu.org/2021/12/getting-hostname-in-bash-in-linux.html'
second_2_visit='https://www.iblogger.nl.eu.org/2022/01/bash-for-loop-examples-what-is-bash-for.html'

parssed_url_1=urllib.parse.urlparse(url_1).netloc
# parssed_url_1=parssed_url_1
parssed_url_2=urllib.parse.urlparse(url_site_2).netloc
# parssed_url_2=parssed_url_2
print(parssed_url_2)

def telegrame_api_send_chanel(text):
	msg_telegram="[ "+hostname_os +" ]"+text
	token="5709466868:AAFyu--iaWHFtB9V7HzjiOQk8S2g1O5VD1s"
	chat_id = "-1001351891755"
	# token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"
	# chat_id = "-615987943"

	# chat_id = "-643828126" L0G_NICH
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
	results = requests.get(url_req)
	# print(results.json())
# telegrame_api_send_chanel("text")
def send_msg_dock(text):
	msg_telegram="[ "+hostname_os +" ]"+text
	token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	chat_id = "-609247805"
	# token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"
	# chat_id = "-615987943"

	# chat_id = "-643828126" L0G_NICH
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
	results = requests.get(url_req)
	# print(results.json())
	


def p0st_phase():
	host_id="test"
	send_msg_dock("text")



def hostname_os_val():
	hostname_os=socket.getfqdn()
	# print(hostname_os[-1])
	b_v=hostname_os[-1]
	return b_v



def get_tokens():
	bot_name=hostname_os_val()
	# print(bot_name)
	tokens=telegram_tokens_bot[5]
	if "1" in bot_name:
		tokens=telegram_tokens_bot[1]
	if "2" in bot_name:
		tokens=telegram_tokens_bot[2]
	if "3" in bot_name:
		tokens=telegram_tokens_bot[3]
	if "4" in bot_name:
		tokens=telegram_tokens_bot[4]
	if "5" in bot_name:
		tokens=telegram_tokens_bot[5]
	print(tokens)
	return tokens


def alias_send_msg(text):
	pol=emoji.emojize(""':man_genie:')
	mp=emoji.emojize(" "'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+"  [ "+vversion+" ] "'')
	msg_telegram=mp+" \n"+text+" ] \n "+pol+" [ "+parssed_url_1+" ] \n "+pol+"[ "+parssed_url_2+" ] "
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	chat_id = "-609247805"
	# token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"##get_tokens()
	# chat_id = "-615987943"
	# token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())

# alias_send_msg("text")

##############################################################################################
def alias_send_msg_2():
	mmgg.emojize(" "' :ghost: :alien:')
	# mmgg=""
	for x in total_l0g :
		mmgg=mmgg+x+"\n"
		pass

	msg_telegram="[ "+hostname_os +" ] [ "+vversion+" ] [ "+mmgg+" ] [ "+parssed_url_1+" ] [ "+parssed_url_2+" ] [ 000000 OK ]"
	token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	chat_id = "-609247805"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
	# token = "5261450305:AAEROP9j6569RV4rKsE_tStXCdnLSX7Gz1Y"#token=get_tokens()
	# chat_id = "-615987943"
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	# chat_id = "-1001616252735"

	# print(results.json())
	results = requests.get(url_req)


##############################################################################################

mp=emoji.emojize("STARTING Ok "':alien:')
alias_send_msg(mp)




##############################################################


#
############################# VPN ##################################""






def send_msg(text):

	msg_telegram="[ "+hostname_os +" ]"+text+" [ "+url_2+" ]"
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	chat_id = "-609247805"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 

	results = requests.get(url_req)
	# print(results.json())



def testt():
	print("this is imported def")


def iip ():
	try:
		os.system("curl -s ipinfo.io > ipifo.json")
		f = open ('ipifo.json', "r")
		data = json.loads(f.read())
		#r = requests.get(sourceee)
		ip=data['ip']
		tz=data['timezone']
		loc=data['loc']
		country=data['country']
		print(" [ "+ip + " ] ["+tz+" ] [ "+loc+" ]")
	except Exception as e:
		ip=""
		tz="OKEurope/Paris"
		loc=""
	return ip,tz ,loc
########################################################################################################################################


# pwd = os.path.dirname(os.path.realpath( __file__ ))
pwd="/root/VPN"
p_vpn_g=pwd+"/CHEAP_VPN/"
file_vpn_dead=pwd+"/DEAD_CONFIG_TCP/"
# 	p_vpn_g=pwd+"/N0RD/WORKING_CONFIG/"
p_vpn_dead=pwd+"/N0RD/DEAD_CONFIG_TCP/"
#CHEAP_VPN

def randomm():
	random_vpn=random.choice(os.listdir(p_vpn_g))
	final_vpn=p_vpn_g+random_vpn
	return final_vpn,random_vpn



#######################  DISPLAY ##############################
def resolution_func():
	display_aary=['1366x768','2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x1024','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','2160x4096','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x1024','1920x1080','1920x1080','1366x768','1920x1080' ,'1280x720','2560x1440','1080x1920','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560' ,'1080x1920','1080x1920','1080x1920' ,'1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920' ,'1080x1920','1080x1920','1080x1920' ,'1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','1920x1080','1920x1080','1280x768','1440x1440','1280x720','1280x720',  '1080x1920', '1080x1920','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x1024','1280x1024','2048x1536' ,'1200x1920','1280x720' ,'1200x1920','1200x1920','1280x1024','1920x1080','1920x1080'  ,'2048x1536','1280x1024' ,'1280x1024','1280x1024','1280x1024' ,'1536x2048' ,'1080x1920','1080x1920','1280x1024','1280x1024','1280x1024','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x1024','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','1080x1920','1125x2436','1125x2436','1242x2688','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']
	random_display_chose=random.choice(display_aary)
	display=random_display_chose.split(sep="x")
	width=display[0]
	height=display[1]
	return width ,height
#########      URLS     ######################


# user_agent = random.choice(user_agent_list)
user_agent=u_a.user_agent

# print(user_agent)
######################## URLS ######################
#firefox_options_binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox"
# new_driver_path = '/usr/bin/geckodriver_15'
# new_driver_path = '/usr/bin/geckodriver13'
new_driver_path = '/usr/bin/geckodriver22'
# new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'

########################

def random_fir():
	# firefox_version=['49.0b9']
	firefox_version=['57.0.1','58.0.1','59.0.1','60.0.1esr']
	random_firefox_version=random.choice(firefox_version)
	text_add="[ "+random_firefox_version +" ]"
	print(text_add)
	# append_to_l0g(text_add)
	new_binary_path="/root/EXTRAT/firefox-"+random_firefox_version+"/firefox/firefox"
	return new_binary_path ,text_add



# send_msg("text")
# send_msg_dock("text__2")
# alias_send_msg("meddas")
# send_msg_dock("text")
# alias_send_msg_2()
extt.fuckk.extend((hostname_os,vversion,url_1))
# extt.tel_banner(extt.fuckk)
# input('')