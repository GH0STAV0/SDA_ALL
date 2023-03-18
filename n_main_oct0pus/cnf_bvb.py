import random , os ,requests , time
import json
import socket
import socket
import api_mysql
import tarfile
import para_m
from pathlib import Path


path_to_file = '/usr/bin/geckodriver-30'
path = Path(path_to_file)

if path.is_file():
    print(f'The file {path_to_file} exists')
else:
    print(f'The file {path_to_file} does not exist')
    os.system("wget -q https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz && tar -xf geckodriver-v0.32.0-linux64.tar.gz && rm geckodriver-v0.32.0-linux64.tar.gz && chmod +x geckodriver && mv geckodriver /usr/bin/geckodriver-30")

path_to_file2 = '/root/EXTRAT/firefox-97.0.1/firefox/firefox'
path2 = Path(path_to_file2)
# /root/EXTRAT/firefox-97.0.1/firefox/firefox
if path2.is_file():
    print(f'The file {path_to_file2} exists')
else:
    print(f'The file {path_to_file} does not exist')
    os.system("wget -q https://ftp.mozilla.org/pub/firefox/releases/97.0.1/linux-x86_64/en-GB/firefox-97.0.1.tar.bz2 && tar -xf firefox-97.0.1.tar.bz2 -C /root/EXTRAT/firefox-97.0.1/")



os.system("rm -rf __pycache__/")
os.system("rm *.tar.gz")

hostname_os=socket.getfqdn()
goog="/root/g00g"
pwd = os.path.dirname(os.path.realpath( __file__ ))

visible_v=0

if "LOOKE3" in hostname_os:
	print(hostname_os)
	visible_v=1



def read_current_acc_goo():
	with open(goog,'r') as file:
		lines = file.readlines()
		lines=lines[0].replace("\n","")
	return lines

print(read_current_acc_goo())
# g00g_acc=read_current_acc_goo()
# g00g_acc="garmiyashour"
# g00g_acc="garmiyashour"
g00g_id,g00g_acc= api_mysql.get_active_goo()
# g00g_acc= "garmiyashour"
#
# erogomayke
# g00g_acc="vanishxmainfour"
print(g00g_acc)

# g00g_acc="laminewalter7"
# g00g_acc="dahmandargo"
# g00g_acc="xamiramogdan"
pofile_path=pwd+"/"+g00g_acc
cmd_remmove_old_profile="rm -rf "+pofile_path
os.system(cmd_remmove_old_profile)

########################################################################################################################################

main_ar=["danayxmaindanay","0ct0pusx01xandrow","bigoctbig","cikox0xmain"]

###############################################################################################################################

def send_msg_dock(text):
	msg_telegram="[ "+hostname_os +" ]"+text
	token = para_m.telegram_tokens_van
	# chat_id = "-643828126" L0G_NICH
	chat_id = para_m.chat_id_alerts_van_google
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	results = requests.get(url_req)
	print(results.json())
# send_msg_dock("text")
# send_msg_dock("text")
def check_if_update(new_set_van_gc_main_account):
	print("check again 2")
###############################################################################################################################
def update_and_reset_go_ac(new_set_van_gc_main_account):
	# print("reset_all_google_van_main_account")
	print("reset_all_google_van_main_account : ",new_set_van_gc_main_account)
	# api_mysql.reset_all_google_van_main_account(new_set_van_gc_main_account)
	api_mysql.reset_all_google_big_main_account(new_set_van_gc_main_account)
	time.sleep(3)
	print("update_google_van_main_account: ",new_set_van_gc_main_account)
	print("set new active")
	api_mysql.update_google_van_main_account(new_set_van_gc_main_account)
	time.sleep(2)
	print("EXIT")
	api_mysql.update_backup_acount(new_set_van_gc_main_account)
	# raise SystemExit
	# sys.exit("Height less than 165")

########################################################################################################################################
def change_gc_acc():
	try:
		# data_id=0
		# g_index="null"
		# g_a=get_actif_account()
		g_index,g_a=api_mysql.get_active_goo()
		# g_a="null"
		print("active acoount : "+g_a)

		# print("active acoount : "+g_a)
		if g_a == "null":
			g_a=api_mysql.last_nord_active()
			update_and_reset_go_ac(g_a)
			print("active acoount buckup : "+g_a)
			print("niiiiiiiiiiiiiiiii")
			# index_of_account=0
			index_of_account=main_ar.index(g_a)
		else:
			index_of_account=main_ar.index(g_a)

		# 	# pass
			
		# g_a=read_current_acc_goo()
		print("active acoount : "+g_a)
		
		print("active ID acoount : "+str(index_of_account))
		numbr_account=len(main_ar)-1
		print("number numbr_account ",numbr_account)
		if index_of_account==numbr_account:
			new_index=0
		else:
			new_index=index_of_account+1
		add_the_new_acc="echo '"+main_ar[new_index]+"' > /root/g00g && cat /root/g00g"
		os.system(add_the_new_acc)
		new_set=main_ar[new_index]
		print("NEW Index : ",new_set)
		send_msg_dock(g_a+" --> "+new_set)
		# print(new_set)
		update_and_reset_go_ac(new_set)
		time.sleep(3)
		print(new_index)
		# update_and_reset_go_ac(new_set)
		time.sleep(3)
	except:
		change_gc_acc()


#change_gc_acc()
# input("prompt")

def extact_gc_profile():
	print("extact")
	remove_old_folder="rm -r "+g00g_acc
	os.system(remove_old_folder)
	comom="cp po/"+g00g_acc+".tar.gz ./"
	os.system(comom)
	name_archive_account=g00g_acc+'.tar.gz'
	file = tarfile.open(name_archive_account)
	comom_2="tar xvf "+g00g_acc+".tar.gz"
	# os.system(comom_2)
	pth_extr='./'
	file.extractall(pth_extr)
	file.close()
	mssgg_tel=" [ "+hostname_os +" ] \n [ EXTRACT ] [ "+g00g_acc +" ]"
	send_msg_dock(mssgg_tel)

# extact_gc_profile()


print(pofile_path)



########################################################################################################################


user_agent_list = ['Mozilla/5.0 (Linux; Android 8.0.0; LG-H932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36']


############################# VPN ##################################""

hostname_os=socket.getfqdn()

def send_msg(text):

	msg_telegram="[ "+hostname_os +" ]"+text
	token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	chat_id = "-643828126"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	results = requests.get(url_req)

def testt():
	print("this is imported def")


def send_msg_to_limit(text):

	msg_telegram="[ "+hostname_os +" ]"+text
	token = telegram_tokens_van
	chat_id = chat_id_alerts_van_google
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	results = requests.get(url_req)


def iip ():
	try:
		# pass
		#sourceee="ipecho.net"
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


pwd = os.path.dirname(os.path.realpath( __file__ ))
p_vpn_g=pwd+"/CHEAP_VPN/"
file_vpn_dead=pwd+"/DEAD_CONFIG_TCP/"
# 	p_vpn_g=pwd+"/N0RD/WORKING_CONFIG/"
p_vpn_dead=pwd+"/N0RD/DEAD_CONFIG_TCP/"
#CHEAP_VPN

def randomm():
	random_vpn=random.choice(os.listdir(p_vpn_g))
	final_vpn=p_vpn_g+random_vpn
	return final_vpn,random_vpn

# extension_path=pwd+"/src/canvasblocker44b.xpi"
# extension_path_ublock=pwd+"/src/uBlock0.firefox.xpi"

#######################  DISPLAY ##############################
def resolution_func():
	display_aary=['1366x768']#,'2560x1700','1366x768','2560x1600','2560x1440','1921x1080','2560x1440','1366x768','1440x900','1280x800','2560x1600','1440x900','1680x1050','2880x1800','1920x1200','1080x1920','2160x4096','1366x768','3840x2160','1600x900','1920x1080','2560x1440','1920x1200','2560x1440','2560x1600','1920x1080','1366x768','2560x1440','1366x768','3000x2000','2160x3840','2304x1440','1366x768','1440x900','2560x1600','2880x1800','4096x2304','5120x2880','3840x2160','1920x1080','1280x800','1920x1080','1920x1080','1366x768','1920x1080' ,'1280x720','2560x1440','1080x1920','1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1440x2560','1440x2560' ,'1080x1920','1080x1920','1080x1920' ,'1080x1920','1440x2560','1440x2560','1440x2560','1080x1920','1440x2560','1080x1920','1280x720','1920x1080','1080x1920','1080x1920' ,'1080x1920','1080x1920','1080x1920' ,'1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1280x720','1280x720','1280x720','1280x720','1920x1080','1920x1080','1920x1080','1920x1080','1920x1080','2560x1440','1920x1080','1920x1080','1920x1080','1920x1080','1280x768','1440x1440','1280x720','1280x720',  '1080x1920', '1080x1920','1440x2560','1280x720','1440x2560','1440x2560','1080x1920','1080x1920','1440x2560','1600x1200','2048x1536','1280x800','1280x800','1024x600','2048x1536' ,'1200x1920','1280x720' ,'1200x1920','1200x1920','1024x600','1024x600','1280x800','1920x1080','1920x1080'  ,'2048x1536','1280x800' ,'1280x800','1280x800','1024x600','1024x600','1280x800','1024x600' ,'1536x2048' ,'1080x1920','1080x1920','1280x800','1280x800','1024x600','1280x800','2048x1536','1920x1200','2560x1600','2560x1600','2048x1536','2048x1536','2732x2048','2048x1536','2048x1536','1280x800','2160x1440','2736x1824','2736x1824','2960x1440','2960x1440','1080x1920','1125x2436','1125x2436','1242x2688','1125x2436','1242x2688','1080x2400','1080x2310','1080x2400','1080x2340','1080x2340','1080x2340','1080x2340','1080x2400','1080x2400','1080x2400','1080x2340','1080x2340','1080x2340','1440x2560','1440x2560','1440x3200','1440x3088','1440x3200','1440x3040','1080x2400','1080x2280','1080x1920','1080x1920','2224x1668','2360x1640','2160x1620','2388x1668','2732x2048','2048x1536','2224x1668','1170x2532','1080x2340','1170x2532','1284x2778']
	random_display_chose=random.choice(display_aary)
	display=random_display_chose.split(sep="x")
	width=display[0]
	height=display[1]
	return width ,height
#########      URLS     ######################

main_domain_BVB="http://bc.vc/"
urls_GH=['MsO5TcT','nrfXdb6','fl5a8H','JvPIhd6','wt0nn5','lwF59F','32NMGr','dfa2gk','UN5Mr5','GycAq7a','movOJG','ec49nF','FuqOZ0','4AFNi6','u6dgi3','xR8ieVb','zYieggh','2jqR5zo','z2UCLn','V1iocU']

urls_BVB=['Uu2MbdT','Uu2MbdT','Uu2MbdT']
#http://bc.vc/Uu2MbdT http://bc.vc/Uu2MbdT
# urls_BVB=['a1yUjT4','9d7ionu','k9bRz5y']
random_url=main_domain_BVB+random.choice(urls_BVB)
user_agent = random.choice(user_agent_list)

new_driver_path = '/usr/bin/geckodriver-30'
##URLS
#firefox_options_binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox"
# new_driver_path = '/usr/bin/geckodriver_30'
# new_driver_path = '/usr/bin/geckodriver13'
# new_driver_path = '/usr/bin/geckodriver22'
# new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'

########################

def random_fir():
	firefox_version=['97.0.1']
	# firefox_version=['49.0b9']
	# firefox_version=['58.0.1']
	# firefox_version=['60.0.1esr']
	# firefox_version=['57.0.1','58.0.1','59.0.1','60.0.1esr']

	random_firefox_version=random.choice(firefox_version)
	print("[ "+random_firefox_version +" ]", end=" ")
	new_binary_path="/root/EXTRAT/firefox-"+random_firefox_version+"/firefox/firefox"
	return new_binary_path


# send_msg_dock("still  not  fucking  reconect!!!!!!")