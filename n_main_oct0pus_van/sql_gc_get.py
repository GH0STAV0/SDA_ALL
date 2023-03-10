import mysql.connector
import time ,os
from datetime import datetime
import cnf_bvb
HOST="sql.freedb.tech"
USERNAME="freedb_sOVnW1130i"
PASSWORD="wsY*Bgz#WCrwq5@"
DATABASE="freedb_32931bb"

# HOST="remotemysql.com"
# USERNAME="f6V3kVwxvH"
# PASSWORD="sOVnW1130i"
# DATABASE="f6V3kVwxvH"

main_ar=["garmiyashour","erogomayke","dahmandargo","laminewalter7"]


this_table="gc_acc"








def get_actif_account():
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	mycursor = mydb.cursor()
	sql = "SELECT * FROM `"+this_table+"` WHERE (`acc_status`='A') ORDER BY RAND() LIMIT 1"
	mycursor.execute(sql)
	record = mycursor.fetchall()
	for row in record:
		fresh_gc_acc=str(row[1])
		print(fresh_gc_acc)
	mycursor.close()
	mydb.close()
	return fresh_gc_acc


def restored_fresh_sql_table():
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	# 

	print(" Reset All G_C table  OF  : ",end='',flush=True)
	mycursor = mydb.cursor()
	sql = "UPDATE `"+this_table+"` SET    `acc_status` = 'NA'"
	mycursor.execute(sql)
	mydb.commit()
	mycursor.close()
	mydb.close()
	print("[ SUCCED ] ")



def update_to_db_as_used(cnf_name):
	mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	# mydb = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
	# # check_connect_mysql()
	restored_fresh_sql_table()

	print(" UPDATE_SQL STATUS CONFIG [ "+cnf_name+" ] : ",end='',flush=True)
	mycursor = mydb.cursor()
	input=("A",cnf_name)
	# this_table=set_table(typ0)

	sql = "UPDATE `"+this_table+"` SET acc_status= %s  WHERE account_id = %s"
	mycursor.execute(sql,input)
	mydb.commit()
	mycursor.close()
	mydb.close()
	print("[ SUCCED ] ")
	# get_value_cnf(cnf_name)
##

def change_gc_acc():
	g_a=get_actif_account()
	# g_a=read_current_acc_goo()
	index_of_account=main_ar.index(g_a)
	print(index_of_account)
	numbr_account=len(main_ar)-1
	print(numbr_account)
	if index_of_account==numbr_account:
		new_index=0
	else:
		new_index=index_of_account+1
	add_the_new_acc="echo '"+main_ar[new_index]+"' > /root/g00g && cat /root/g00g"
	os.system(add_the_new_acc)
	new_set=main_ar[new_index]
	cnf_bvb.send_msg_dock(g_a+" --> "+new_set)
	# print(new_set)
	update_to_db_as_used(new_set)
	print(new_index)




# change_gc_acc()
# activ_acc=get_actif_account()
# print(activ_acc)
#"garmiyashour")
# update_to_db_as_used("erogomayke")
# update_to_db_as_used("garmiyashour")