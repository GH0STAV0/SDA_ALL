import os ,random ,subprocess,time 

import cnf_add
import cnf_bvb


########################### VPN  #############################/N0RD/WORKING_CONFIG/

# file_list_1='NORD_list_1'
file_list_1='NCH_list_1'
# 
retry_count=[]

# pwd = os.path.dirname(os.path.realpath( __file__ ))
pwd="/root/VPN"

vpn_folder=pwd+"/CHEAP_VPN/"
# vpn_folder=pwd+"/N0RD/WORKING_CONFIG/"
all_vpn_config_file=os.listdir(vpn_folder)




########################### VPN  #############################/N0RD/WORKING_CONFIG/
# pwd = os.path.dirname(os.path.realpath( __file__ ))


vpn_type=cnf_bvb.vpn_type
if "N" in vpn_type:
	file_list_1='NORD_list_1'
	vpn_folder=pwd+"/N0RD/WORKING_CONFIG/"
	typ0="N"


if "C" in vpn_type:
	file_list_1='NCH_list_1'
	vpn_folder=pwd+"/CHEAP_VPN/"
	typ0="C"
	


def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")
	# 	# for i in all_vpn_config_file:




all_vpn_config_file=os.listdir(vpn_folder)


# file_vpn_dead=cnf_bvb.file_vpn_dead
# p_vpn_dead=cnf_bvb.p_vpn_dead

##############################################################

file_vpn_dead=cnf_add.file_vpn_dead
p_vpn_dead=cnf_add.p_vpn_dead

##############################################################

def check_list_vpn_lengh():
	num_lines = sum(1 for line in open(file_list_1))
	if num_lines==0:
		creat_list_of_vpn()
	else:
		pass

##############################################################

def creat_list_of_vpn():
	with open(file_list_1,'w') as fw:
		for i in all_vpn_config_file:
			fw.write(i+"\n")

##############################################################

def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines

##############################################################

def write_new_list(new_vpn_arry):
	with open(file_list_1,"w") as fw:
		for i in new_vpn_arry:
			fw.write(i)
	print("OK !!")

##############################################################

def remove_from_list_running(vpn_name):
	print("REMOVING THE VPN CONFIG [ "+vpn_name+" ]",end=' ',flush=True)
	vpn_name=vpn_name+"\n"
	arry_vpn_list=read_current_list_vpn()
	arry_vpn_list.remove(vpn_name)
	write_new_list(arry_vpn_list)

##############################################################

def get_random_vpn():
	check_list_vpn_lengh()
	arry_vv=read_current_list_vpn()
	random_vpn=random.choice(arry_vv)
	random_vpn=random_vpn.replace('\n','')
	final_vpn=vpn_folder+random_vpn
	# print(random_vpn)
	return final_vpn , random_vpn

##############################################################

def change_time_zon(t_z):
	# t_z=get_time_zon()
	print("Changing Time Zone ", end="")
	x = subprocess.Popen(['timedatectl', 'set-timezone', t_z])
	print('OK'+t_z)
	time.sleep(3)


def read_pass():
	# def read_current_list_vpn():
	with open('0nord_pass','r') as file:
		lines = file.readlines()
	return lines
#####################
# def fnc_vpn():

# 	final_vpn,random_vpn=get_random_vpn()
# 	print("###################################################")
# 	print("KILLING OPENVPN ....",end=' ')
# 	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
# 	time.sleep(3)
# 	os.system("rm -rf /var/log/openvpn/openvpn.log")
# 	os.system("touch /var/log/openvpn/openvpn.log")
# 	print ("OK !!!!!")
# 	print("STARTING VPN " , end="")
# 	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',final_vpn , '--log' , '/var/log/openvpn/openvpn.log'])
# 	remove_from_list_running(random_vpn)
# 	time.sleep(12)
# 	print("["+random_vpn+"]" , end="")
# 	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
# 		if logfile.read().find('Sequence Completed') !=-1:
# 			print ("OK !!!!!")
# 			ac_ip,tz,loc=cnf_bvb.iip()
# 			os.environ['TZ'] = tz
# 			print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip+"||"+ tz)
# 			return [x ,True]
# 		else :
# 			print("")
# 			print("VPN STATUS = OFF || "+ random_vpn )
# 			fnc_vpn ()
# 			return [x ,False]

# 	time.sleep(5)
# 	os.system("echo '' > /var/log/openvpn/openvpn.log")



	

# ########################################################################################################################################
def read_default_timezone():
	# def read_current_list_vpn():
	try:
		
		with open('/root/test707','r') as file:
			titi_zon = file.readlines()
			titi_zon=titi_zon[0].replace("\n","")
			print(titi_zon)
	except Exception as e:
		# raise e
		titi_zon="Europe/Paris"
# read_default_timezone()
	return titi_zon


# ################################

# #cnf_bvb.testt()
# # fnc_vpn ()
def fnc_vpn():

	os.system("echo '' > /var/log/openvpn/openvpn.log")
	final_vpn,random_vpn=get_random_vpn()
	print("###################################################")
	print("KILLING OPENVPN ....",end=' ')
	os.system("ps aux | grep  openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	# def_tz=read_default_timezone()

	# change_time_zon(def_tz)
	# print(str(len(retry_count)))

	time.sleep(3)
	# os.system("rm -rf /var/log/openvpn/openvpn.log")
	time.sleep(3)
	# os.system("touch /var/log/openvpn/openvpn.log")
	print ("OK !!!!!")
	print("\n")
	print("STARTING VPN " , end="")
	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',final_vpn , '--log' , '/var/log/openvpn/openvpn.log'])
	remove_from_list_running(random_vpn)
	print("["+random_vpn+"]" , end="")
	time.sleep(18)
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:

		if logfile.read().find('Sequence Completed') !=-1:
			print ("OK !!!!!")
			ac_ip,tz,loc=cnf_bvb.iip()
			# change_time_zon(tz)
			os.environ['TZ'] = tz
			bass=read_pass()
			def_titi= read_default_timezone()
			mm=""
			for i in bass:
				mm=mm+i
			meddas=mm+def_titi+" [ CONNECTED VPN] [ "+str(1)+" ] : [ "+ random_vpn  +" ] \n"+"|| [ IP ] : [ "+ ac_ip+" ] || [ TIME_Z ] : ["+ tz+" ]"+"\n"
			# " [ "+url_1+" ]"
			# append_to_l0g(meddas)
			# vpn_sql.update_to_db_as_used(random_vpn,typ0)
			print(meddas)
			# cnf_bvb.ap_2_l0g(meddas)
			# cnf_bvb.alias_send_msg(meddas)
			return [x ,True]
		if logfile.read().find('AUTH_FAILED'):
			print("\nAUTH_FAILED")
			os.system("echo '' > /var/log/openvpn/openvpn.log")
			# random_pass()

			retry_count.append("")
			print(str(len(retry_count)))
			time.sleep(3)
			x.kill()
			fnc_vpn ()
			return [x ,False]


		else :
			print("")
			print("VPN STATUS = OFF || "+ random_vpn )
			os.system("service openvpn restart")
			fnc_vpn ()
			return [x ,False]


	time.sleep(5)
	os.system("echo '' > /var/log/openvpn/openvpn.log")


