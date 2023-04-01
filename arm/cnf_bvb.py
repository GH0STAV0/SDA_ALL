import random , os ,requests
import json
import socket


vversion="arm-v5  0ct0pus_child N0RD V2"

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
# g00g_acc="xxtawelchildxtow"
# email="xxtawelchildxtow"
# 
g00g_acc=read_current_acc_goo()
pofile_path=pwd+"/tmp/"+g00g_acc

print(pofile_path)


########################################################################################################################################
def alias_send_msg(text):

	# count_used=str(counting_used_config_config())
	# global lommmmp
	# lommmmp="jhj"
	# pol=emoji.emojize(""':man_genie:')
	# print(lommmmp)
	hoost=read_current_acc_goo()
	# lommmmp=count_used
	# print(lommmmp)
	###################################################

	# mp=emoji.emojize(dt_string+" \n"'  :dizzy:'+"[ "+hostname_os +" ] "':dizzy:'+" \n"''+"  [ "+vversion+" ] "'')
	# msg_telegram=mp+" \n"+text+" ] \n "+pol+" [ "+""+" ] \n "+pol+"[ "+vversion+" ] "
	msg_telegram="    [ "+hoost+" ]                [   ] \n[  ]   [  ] "+"[ "+text+" ] "+"[ "+vversion+" ] "
	# token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	#-609247805
	# token=get_tokens()
	# token="5086890807:AAEEM2OhQaR9mB7KUZvwkE60mHvoSY4BhOQ"
	# token="5035848854:AAG9a-7bHDYTOXiNEdjXRsnM-gbkdw9TCfE"
	token="5351653833:AAEUeIwPT187sCG5vb33t_2JGHBlcLT-kNU"
	chat_id = "-723950994"
	# chat_id = "-1001616252735"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	# url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram

	results = requests.get(url_req)
	# check_tolerance(count_used)
########################################################################################################################

def send_msg_dock(text):

	msg_telegram="[ "+hostname_os +" ]"+text
	# 5609508648:AAHp0XxaFsL66wNE6AxEJX2qI8Xr6AZ4Q2g
	# 5609508648
	token = "5609508648:AAHp0XxaFsL66wNE6AxEJX2qI8Xr6AZ4Q2g"
	# chat_id = "-643828126"
	chat_id = "-895535637"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	results = requests.get(url_req)
	# print(results.json())
###############################################################################################################################
send_msg_dock("text")

def extract_pof():
	os.system('rm -rf tmp/'+g00g_acc)
	print("extact")
	os.system('mkdir -p tmp/')
	send_msg_dock("EXTACTING :"+g00g_acc)
	comom="cp po/"+g00g_acc+".tar.gz tmp/"
	os.system(comom)
	comom_2="cd tmp && tar xvf "+g00g_acc+".tar.gz"
	os.system(comom_2)
	os.system('cd ..')

##############################################
# extract_pof()

user_agent_list = [
'AppleCoreMedia/1.0.0.12B466 (Apple TV; U; CPU OS 8_1_3 like Mac OS X; en_us)','Mozilla/5.0 (Android 7.0; Mobile; LG-M150; rv:68.0) Gecko/68.0 Firefox/68.0']

#p_vpn_g="/root/install_add/moya/yserverListTCP/"
#
############################# VPN ##################################""



ads=['148554','148477','148709','143423','146817','147629','147257','148786','146991','148787','148066','148643','148283','144375','148279','144442','148555','148264','148804','148556','147277','147415','146209','148523','148680','144002','148540','147710','144323','144498','148758','144525','148263','146622','142824','146831','147535','148510','148600','145992','148482','139001','148628','148784','148685','147791','148059','144604','147966','146160','139480','148498','148760','148657','148721','148577','146708','148761','148762','139705','146145','143247','148717','148677','148539','148749','145585','148476','148522','147370','139134','148471','148759','148061','147081','145096','148242']

random_ads=random.choice(ads)

hostname_os=socket.getfqdn()

def send_msg(text):

	msg_telegram="[ "+hostname_os +" ]"+text
	token = "2137513961:AAGENlwIUQnfvbKZX64-fZ72R_oStto8oFo"
	chat_id = "-643828126"
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram
	results = requests.get(url_req)
	# print(results.json())



def testt():
	print("this is imported def")


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


#final_vpn,random_vpn=randomm()


extension_path=pwd+"/src/canvasblocker44b.xpi"
# extension_path_ublock=pwd+"/src/uBlock0_1.36.2.firefox.xpi"
#uBlock0.firefox
extension_path_ublock=pwd+"/src/uBlock0.firefox.xpi"

#######################  DISPLAY ##############################
def resolution_func():

	display_aary=['1366x768']
	random_display_chose=random.choice(display_aary)
	display=random_display_chose.split(sep="x")
	width=display[0]
	height=display[1]
	return width ,height


#########      URLS     ######################

# main_domain_BVB="http://bc.vc/"
# urls_GH=['MsO5TcT','nrfXdb6','fl5a8H','JvPIhd6','wt0nn5','lwF59F','32NMGr','dfa2gk','UN5Mr5','GycAq7a','movOJG','ec49nF','FuqOZ0','4AFNi6','u6dgi3','xR8ieVb','zYieggh','2jqR5zo','z2UCLn','V1iocU']

# urls_BVB=['Uu2MbdT','Uu2MbdT','Uu2MbdT']
#http://bc.vc/Uu2MbdT http://bc.vc/Uu2MbdT
# urls_BVB=['a1yUjT4','9d7ionu','k9bRz5y']
# random_url=main_domain_BVB+random.choice(urls_BVB)
user_agent = random.choice(user_agent_list)


##URLS 
#firefox_options_binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox"
# new_driver_path = '/usr/bin/geckodriver_15'
# new_driver_path = '/usr/bin/geckodriver13'
# new_driver_path = '/usr/bin/geckodriver22'
new_driver_path = '/usr/bin/geckodriver-30'
# new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'

########################


def random_fir():
	firefox_version=['97.0.1']
	# firefox_version=['59.0.1','60.0.1esr']
	random_firefox_version=random.choice(firefox_version)
	print("[ "+random_firefox_version +" ]", end=" ")
	new_binary_path="/root/EXTRAT/firefox-"+random_firefox_version+"/firefox/firefox"
	return new_binary_path




# send_msg_dock("ERROR : ")





