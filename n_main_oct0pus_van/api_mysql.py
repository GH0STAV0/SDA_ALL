import para_m


import requests
import json ,os
#  ls ~/VPN/N0RD/WORKING_CONFIG | wc -l

api_url=para_m.url
# print(api_url)


#/////////////////////  get_config_with_api ///////////////////////////////////////////

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
	response = requests.get(f'{api_url}/van/count')
	data = response.json() #.get('COUNT(*)')
	d2=str(data[0]).split(":")
	d2=d2[1].replace('}',"")
	d3=d2.replace(' ',"")
	count_left_count = d3
	# print(count_left_count)
	return count_left_count
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

def get_active_goo():
	try:
		response = requests.get(f'{api_url}/google_account_van/active')
		data = response.json()
		data_id = data[0].get('acc_numbre')
		data_name_acc = data[0].get('account_id')
		# d2=str(data[0]).split(":")
		# d2=d2[1].replace('}',"")
		# d3=d2.replace(' ',"")
		# count_left_count = d3
		print(data_id,data_name_acc)
	except:
		get_active_goo()


	return data_id , data_name_acc

# count_left_api()
# get_active_goo()

#////////  count_left_api /////////////////////////////////////////////////////////////

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

#/////////////////////   /////////////////////////////////////////// 
def update_google_van_main_account(van_gc_main_account):
	# van_count_left_api()
	# print(id_config)
	# get_config_with_api_van(id_config)
	d_data = {'id':'1'}
	response = requests.put(f"{api_url}/van/account/act/%s" %van_gc_main_account)
	print(response.content)
	# get_config_with_api_van(id_config)
	# van_count_left_api()
# update_conf_van_api(185)

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