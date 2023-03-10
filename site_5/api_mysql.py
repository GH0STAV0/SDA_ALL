import para_m


import requests
import json
#  ls ~/VPN/N0RD/WORKING_CONFIG | wc -l

api_url=para_m.url
# print(api_url)

#////////  count_left_api ////////////////////////////////////////////////////////

def count_left_api():
	print(api_url)
	response = requests.get(f'{api_url}/nor/count')
	data = response.json() #.get('COUNT(*)')
	d2=str(data[0]).split(":")
	d2=d2[1].replace('}',"")
	d3=d2.replace(' ',"")
	count_left_count = d3
	# print(count_left_count)


	return count_left_count


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


def check_tolerance():

	
	# count_used=str(counting_used_config_config())
	# print(" [  VPN USED  ]",type(count_used))
	count_used=count_left_api()
	int_count=int(count_used)
	# print(" [  VPN USED  ]",type(int_count))
	
	if int_count >= 2078 :
		print(int_count)
		print("NO Reset ")
		
		# restored_fresh_sql_table()
	else :
		print(int_count)
		print(" Reset ")
		reset_nord_api()


check_tolerance()

# reset_nord_api()


# idd=4017

# update_conf_nord_api(idd)

print("Loading module : para OK ! [ "+count_left_api() + " ]")
# vvv=count_left_api()
# print("ff "+vvv)

# data_id,data_cnf_names,data_used=get_random_api()
# print(data_id,data_cnf_names,data_used)