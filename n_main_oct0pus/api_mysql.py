import para_m
# import requests
import json ,os

import logging
import requests
from requests.adapters import HTTPAdapter, Retry
# logging.basicConfig(level=logging.DEBUG)

#  ls ~/VPN/N0RD/WORKING_CONFIG | wc -l

api_url=para_m.url
# print(api_url)

def last_nord_active():
	try:

		session = requests.Session()
		retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
		session.mount('http://', HTTPAdapter(max_retries=retries))

		response = session.get('https://apiv10.onrender.com/nor/account/last_active/0')
		data = response.json()
		data_id = data.get('compt_nord')
		# print(data_id)
		return data_id
	except:
		last_nord_active()

data_id_backup=last_nord_active()
print(data_id_backup)


#/////////////////////  get_config_with_api VVVV ///////////////////////////////////////////

def get_config_with_api_van(i_d):
	response = requests.get(f"{api_url}/van/%d" %i_d )
	data = response.json()
	data_id = data.get('id')
	data_cnf_names = data.get('cnf_names')
	data_used = data.get('used')
	print(data_id,data_cnf_names,data_used)
	return data_id,data_cnf_names,data_used


#////////////////////////////////////////////////////////////////
#//////// * VANISH * - count_left_api ////////////////////////////////////////////////////////
def van_count_left_api():
	try:
		response = requests.get(f'{api_url}/van/count', timeout=5)
		data = response.json() #.get('COUNT(*)')
		d2=str(data[0]).split(":")
		d2=d2[1].replace('}',"")
		d3=d2.replace(' ',"")
		count_left_count = d3
		# print(count_left_count)
		return count_left_count
	except:
		van_count_left_api()

#////////////////////////////////////////////////////////////////
# van_count_left_api()

# van_count_left_api()

#////////// * VANISH * get_random_api ///////////////////////////////////////////////////////////////

def get_random_api_van():
	response = requests.get(f'{api_url}/van/ran')
	data = response.json()
	data_id = data[0].get('id')
	data_cnf_names = data[0].get('cnf_names')
	data_used = data[0].get('used')
	van_config_left=van_count_left_api()
	print(data_id,data_cnf_names,data_used,van_config_left)
	return data_id,data_cnf_names,data_used,van_config_left
#////////////////////////////////////////////////////////////////
# get_random_api_van()

#/////////////////  update_conf_nord_api ///////////////////////////////////////////////
def update_conf_van_api(id_config):
	van_count_left_api()
	# print(id_config)
	get_config_with_api_van(id_config)
	d_data = {'id':'1'}
	response = requests.put(f"{api_url}/van/update/%d" % id_config)
	# print(response.content)
	get_config_with_api_van(id_config)
	van_count_left_api()
# update_conf_van_api(185)

#/////////////////////   ///////////////////////////////////////////  get_config_with_api

#/////////////////   /////////////////////////////////////////////// reset_van_api

def reset_van_api():
	response = requests.put(f'{api_url}/van/reset_all')
	data = response.json()
	data_message = data.get('message')
	# print(response.content)
	print(data_message)

#//////////////////////////////////////////////////////////////////////////////////////////////
#////////  Account Active ////////////////////////////////////////////////////////
def check_online():
	try:
		print("tgtg")
		response = requests.get(f'{api_url}/all' , timeout=5)
		data = response.json()
		# print(data)
	except:
		print("error active")
		check_online()

def get_active_goo():
	 # , timeout=5
	data_id = "null" 
	data_name_acc="null"
	check_online()
	try:
		response = requests.get(f'{api_url}/nor/account/active' , timeout=5)
		data = response.json()
		data_id = data[0].get('acc_numbre')
		data_name_acc = data[0].get('account_id')
		# d2=str(data[0]).split(":")
		# d2=d2[1].replace('}',"")
		# d3=d2.replace(' ',"")
		# count_left_count = d3
		print(data_id,data_name_acc)
	except:
		print("error")
		#get_active_goo()
	print(data_id,data_name_acc)
	return data_id , data_name_acc


# get_active_goo()

# count_left_api()
# get_active_goo()

#////////  count_left_api ////////////////////////////////////////////////////////

def count_left_api():
	response = requests.get(f'{api_url}/nor/count')
	data = response.json() #.get('COUNT(*)')
	d2=str(data[0]).split(":")
	d2=d2[1].replace('}',"")
	d3=d2.replace(' ',"")
	count_left_count = d3
	# print(count_left_count)


	return count_left_count

# count_left_api()

#//////////  get_random_api //////////////////////////////////////////////////////

def get_random_api():
	response = requests.get(f'{api_url}/nor/ran')

	data = response.json()
	data_id = data[0].get('id')
	data_cnf_names = data[0].get('cnf_names')
	data_used = data[0].get('used')

	return data_id,data_cnf_names,data_used


#/////////////////  reset_nord_api ///////////////////////////////////////////////
#////////////////
def reset_nord_api():

	response = requests.put(f'{api_url}/nor/reset_all')
	data = response.json()
	data_message = data.get('message')
	# print(response.content)
	print(data_message)

#/////////////////  update_conf_nord_api ///////////////////////////////////////////////
def update_conf_nord_api(id_config):
	count_left_api()
	# print(id_config)
	get_config_with_api(id_config)
	d_data = {'id':'1'}
	response = requests.put(f"{api_url}/nor/update/%d" % id_config)
	# print(response.content)
	get_config_with_api(id_config)
	count_left_api()


#/////////////////////  get_config_with_api ///////////////////////////////////////////

def get_config_with_api(i_d):
	response = requests.get(f"{api_url}/nor/%d" %i_d )

	data = response.json()
	data_id = data.get('id')
	data_cnf_names = data.get('cnf_names')
	data_used = data.get('used')
	print(data_id,data_cnf_names,data_used)
	return data_id,data_cnf_names,data_used


#////////////////////////////////////////////////////////////////
def update_and_reset_go_ac(new_set):
	print("OOOOOOOOOOO")


def update_backup_acount(nord_gc_main_account):
	# van_count_left_api()
	# print(id_config)
	# get_config_with_api_van(id_config)
	d_data = {'id':'0'}
	response = requests.put(f"{api_url}/nor/update/last/%s" % nord_gc_main_account)
	# print(response.content)
	# get_config_with_api_van(id_config)
	# van_count_left_api()
# update_conf_van_api(185)
#/////////////////  update_conf_nord_api ///////////////////////////////////////////////

#/////////////////  update_conf_nord_api ///////////////////////////////////////////////
def reset_all_google_van_main_account(van_gc_main_account):
	# van_count_left_api()
	# print(id_config)
	# get_config_with_api_van(id_config)
	d_data = {'id':'1'}
	response = requests.put(f"{api_url}/google_account/update_van/%s" % van_gc_main_account)
	# print(response.content)
	# get_config_with_api_van(id_config)
	# van_count_left_api()
# update_conf_van_api(185)
#/////////////////  update_conf_nord_api ///////////////////////////////////////////////
def reset_all_google_big_main_account(big_gc_main_account):
	print("\n RESET : "+big_gc_main_account)
	try:
		d_data = {'id':'1'}
		response = requests.put(f"{api_url}/nor/account/update/%s" % big_gc_main_account, timeout=5)
		#print(response.content)
		print(response.text)
	except:
		reset_all_google_big_main_account(big_gc_main_account)
# reset_all_google_big_main_account("cikox0xmain")
	# get_config_with_api_van(id_config)
	# van_count_left_api()
	# print(id_config)
	# print(response.content)
	# get_config_with_api_van(id_config)
	# van_count_left_api()
# update_conf_van_api(185)

#/////////////////////   ///////////////////////////////////////////
def update_google_van_main_account(nord_gc_main_account):
	print("nord_gc_main_account")
	try:
		# van_count_left_api()
		# print(id_config)
		# get_config_with_api_van(id_config)
		d_data = {'id':'1'}
		response = requests.put(f"{api_url}/nor/account/act/%s" %nord_gc_main_account , timeout=5)
		print(response.content)
	except:
		update_google_van_main_account(nord_gc_main_account)
	g_index,g_a=get_active_goo()
	print("ok : "+g_a)
	if g_a == nord_gc_main_account :
		print("yes it the same")
	else:
		 update_google_van_main_account(nord_gc_main_account)



	# get_config_with_api_van(id_config)
	# van_count_left_api()
# update_conf_van_api(185)
# update_google_van_main_account("danayxmaindanay")
#/////////////////////   ///////////////////////////////////////////
# reset_all_google_van_main_account("id_config")
# update_google_van_main_account("vanishmainxxone")
#/////////////////////  get_config_with_api ///////////////////////////////////////////

# change_gc_acc()



# reset_nord_api()


# idd=4017

# update_conf_nord_api(idd)

print("Loading module : para OK ! [ "+count_left_api() + " ]")
# data_id,data_cnf_names,data_used=get_random_api()
# print(data_id,data_cnf_names,data_used)
