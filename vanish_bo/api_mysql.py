import para_m


import requests
import json
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
	response = requests.get(f'{api_url}/google_account_van/active')
	data = response.json()
	data_id = data[0].get('acc_numbre')
	data_name_acc = data[0].get('account_id')
	print(data_id,data_name_acc)
	return data_id , data_name_acc
#////////////////////////////////////////////////////////////////
get_active_goo()

# count_left_api()
get_active_goo()


#//////// * N0RD * - count_left_api ////////////////////////////////////////////////////////

def count_left_api():
	response = requests.get(f'{api_url}/nor/count')
	data = response.json() #.get('COUNT(*)')
	d2=str(data[0]).split(":")
	d2=d2[1].replace('}',"")
	d3=d2.replace(' ',"")
	count_left_count = d3
	# print(count_left_count)
	return count_left_count
#////////////////////////////////////////////////////////////////


#//////////  get_random_api ///////////////////////////////////////////////////////////////

def get_random_api():
	response = requests.get(f'{api_url}/nor/ran')

	data = response.json()
	data_id = data[0].get('id')
	data_cnf_names = data[0].get('cnf_names')
	data_used = data[0].get('used')

	return data_id,data_cnf_names,data_used
#////////////////////////////////////////////////////////////////


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

def van_check_tolerance():

	
	# count_used=str(counting_used_config_config())
	# print(" [  VPN USED  ]",type(count_used))
	count_used=van_count_left_api()
	int_count=int(count_used)
	# print(" [  VPN USED  ]",type(int_count))
	
	if int_count >= 501 :
		print(int_count)
		print("NO Reset Count : "+str(int_count))
		# restored_fresh_sql_table()
	else :
		print(int_count)
		print(" Reset "+str(int_count))
		reset_van_api()

van_check_tolerance()
# reset_nord_api()


# idd=4017

# update_conf_nord_api(idd)

print("Loading module van : para OK ! [ "+van_count_left_api() + " ]")
# data_id,data_cnf_names,data_used=get_random_api()
# print(data_id,data_cnf_names,data_used)