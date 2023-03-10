import mysql.connector
import time ,os
from datetime import datetime
# import api_mysql

###############################################################################################
# HOST="zzroiqlkjzv2.eu-west-2.psdb.cloud"
# USERNAME="c4cz3k2azim8"
# PASSWORD="pscale_pw_SZsOhzZm6AVnde53meT3ygRRh7zSjXdZ4dawwURylQo"
# DATABASE="plan"
# HOST="remotemysql.com"
# USERNAME="f6V3kVwxvH"
# PASSWORD="sOVnW1130i"
# DATABASE="f6V3kVwxvH"
HOST="sql.freedb.tech"
USERNAME="freedb_sOVnW1130i"
PASSWORD="wsY*Bgz#WCrwq5@"
DATABASE="freedb_32931bb"



# host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH"


# host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH"


def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
	except  Exception as e :
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)
		time.sleep(18)
		check_connect_mysql()



# check_connect_mysql()
#######################################################################################


def insert_to_db(cnf_name):
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	mycursor = mydb.cursor()
	sql = "INSERT INTO nord_list (cnf_names, used) VALUES (%s, %s)"
	val = (cnf_name, "n")
	mycursor.execute(sql, val)
	time.sleep(2)

	mydb.commit()

##############################################################################################

def loop_conf():
	for i in all_vpn_config_file:
		print(i)
		insert_to_db(i)

###############################################################################################

def get_value_cnf(fresh_config):
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	print(" RANDOM_SQL  OF  : ",end='',flush=True)
	mycursor = mydb.cursor()
	input=(fresh_config)
	print(fresh_config)
	sql = "SELECT * FROM `nord_list2` WHERE `cnf_names`= "+"'"+fresh_config+"'"+""
	mycursor.execute(sql)
	record = mycursor.fetchall()
	for row in record:
		sql_last_bin=str(row[2])
		print(sql_last_bin)
	return 
###############################################################################################

def set_table(typ0):
	# vpn_type=cnf_bvb.vpn_type
	if "N" in typ0:
		# print("NORD VPN")
		tab_list_1='nord_list2'
		# vpn_folder=pwd+"/N0RD/WORKING_CONFIG/"
		# typ0="N"
#       ######################################################          
	elif "C" in typ0:
		# print(" NAME_CHEAP")
		tab_list_1='name_cheap'
		# vpn_folder=pwd+"/CHEAP_VPN/"
		# typ0="C"
	return tab_list_1
	


def get_fresh_config(typ0):
	try:

		# check_connect_mysql()
		mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)

		this_table=set_table(typ0)

		
		# print(" RANDOM_FRESH CONFIG   : ",end='',flush=True)
		mycursor = mydb.cursor()
		sql = "SELECT * FROM `"+this_table+"` WHERE (`used`='n') ORDER BY RAND() LIMIT 1"
		mycursor.execute(sql)
		record = mycursor.fetchall()
		#count=mycursor.rowcount
		int_count=counting_used_config_config(this_table)
		# print(str(int_count))
		for row in record:
			fresh_config=str(row[1])
		return fresh_config ,int_count
	except:
		time.sleep(18)

#################################################################################################


def update_to_db_as_used(cnf_name,typ0):
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	# check_connect_mysql()

	print(" UPDATE_SQL STATUS CONFIG [ "+cnf_name+" ] : ",end='',flush=True)
	mycursor = mydb.cursor()
	input=("y",cnf_name)
	this_table=set_table(typ0)

	sql = "UPDATE `"+this_table+"` SET used= %s  WHERE cnf_names = %s"
	mycursor.execute(sql,input)
	mydb.commit()
	print("[ SUCCED ] ")
	# get_value_cnf(cnf_name)
##########################################################################################

def drop_sql_table():
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	try:

		print(" drop_sql_table  OF  : ",end='',flush=True)
		# mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
		mycursor = mydb.cursor()
		sql = "DROP TABLE IF EXISTS nord_list2"
		print("[ DROP : cant drop_sql_table ] ")
		mycursor.execute(sql)
		print("[ SUCCED ] ")
	except:
		print("[ ERR0R : cant drop_sql_table ] ")
		os.system("mysql -h remotemysql.com -u f6V3kVwxvH -psOVnW1130i f6V3kVwxvH < nord_list2.sql")


def restored_fresh_sql_table():
	try:
		drop_sql_table()
	except:
		print("[ ERR0R : cant drop_sql_table ] ")
		pass
	print(" restored_fresh_sql_table  OF nord_list2 nord_list2.sql : ",end='',flush=True)
	os.system("mysql -h remotemysql.com -u f6V3kVwxvH -psOVnW1130i f6V3kVwxvH < nord_list2.sql")
	print("[ SUCCED ] ")






def counting_left():
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	print(" RANDOM_FRESH CONFIG   : ",end='',flush=True)
	mycursor = mydb.cursor()
	sql = "SELECT * FROM `nord_list2` WHERE (`used`='n') "
	mycursor.execute(sql)
	record = mycursor.fetchall()
	count=mycursor.rowcount
	print(str(count))

	if ( count < 1500 ):
		print (" should reset sql table" )
		restored_fresh_sql_table()
	else:
		print (" VPN LEFT :"+str(count))

	# for row in record:
# counting_left()


###############################################################################################

def counting_used_config_config(typ0):
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	this_table=typ0
	# mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	# print(" counting_used_config_config  : ",end='',flush=True)
	mycursor = mydb.cursor()
	sql = "SELECT * FROM `"+this_table+"`  WHERE `used` LIKE 'y'"
	mycursor.execute(sql)
	record = mycursor.fetchall()
	count=mycursor.rowcount

	print(" VPN : [ "+this_table+" ]    |     Used Counting [ "+str(count)+" ]")
	# for row in record:
	# 	fresh_config=str(row[1])
	return count

#################################################################################################
# get_fresh_config()

# 
# restored_fresh_sql_table()


##########################################################################################
##########################################################################################
# fresh_config=get_fresh_config()
# print(fresh_config)
# get_value_cnf()
# update_to_db_as_used(fresh_config)
# get_value_cnf()

#
# check_connect_mysql()
# loop_conf()
# SELECT * FROM `nord_list2` WHERE (`used`='n') ORDER BY RAND() LIMIT 1




# typ0="N"
# counting_left()
# vpn_folder="/root/VPN/N0RD/WORKING_CONFIG/"


# all_vpn_config_file=os.listdir(vpn_folder)
# # print(str(len(all_vpn_config_file)))

# def creat_list_of_vpn():
# 	with open(file_list_1,'w') as fw:
# 		for i in all_vpn_config_file:
# 			fw.write(i+"\n")


# get_fresh_config("N")