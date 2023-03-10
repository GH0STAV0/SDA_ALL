import mysql.connector
import time ,os
from datetime import datetime

goog="/root/g00g"
# └─# mysql -h sql.freedb.tech -P 3306 -u freedb_sOVnW1130i -pwsY*Bgz#WCrwq5@ freedb_32931bb < f6V3kVwxvH.sql 


mydb = mysql.connector.connect(host="sql.freedb.tech",user="freedb_sOVnW1130i",passwd="wsY*Bgz#WCrwq5@",database="freedb_32931bb")

# mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")

main_ar=["garmiyashour","erogomayke","dahmandargo","laminewalter7"]

def check_connect_mysql():
	#mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		mycursor = mydb.cursor()
		mycursor.close()
		mydb.close()

		print("MYSQL CONNECTED OK ")
	except  Exception as e :
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)


#check_connect_mysql()

def get_all_sql_record():


	try:
	    # connection = mysql.connector.connect(host='localhost',
	    #                                      database='electronics',
	    #                                      user='pynative',
	    #                                      password='pynative@#29')

	    sql_select_Query = "select * from gc_acc"
	    cursor = mydb.cursor()
	    cursor.execute(sql_select_Query)
	    # get all records
	    records = cursor.fetchall()
	    print("Total number of rows in table: ", cursor.rowcount)
	    now = datetime.now()
	    id = 1
	    formatted_date = now.strftime('%Y-%m-%d %H:%M')
	    print("\nPrinting each row  "+str(formatted_date),now)
	    for row in records:
	        print("Id = ", row[0], )
	        print("Name = ", row[1])
	        print("Type Acc  = ", row[2])
	        print("START Date  = ", row[3])
	        print("END   Date  = ", row[4], "\n")
	    get_one=str(row[0])+"#"+row[1]+"#"+str(row[2])+"#"+str(row[3])+"#"+str(row[4])
	    print(get_one)

	except mysql.connector.Error as e:
	    print("Error reading data from MySQL table", e)
	finally:
	    if mydb.is_connected():
	        mydb.close()
	        cursor.close()
	        print("MySQL connection is closed")

def update_sql():
	now = datetime.now()
	formatted_date = now.strftime('%Y-%m-%d %H:%M')
	time_stamp=str(formatted_date)

	#mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
	check_connect_mysql()
		#now = datetime.now()
	    #id = 1
	    #formatted_date = now.strftime('%Y-%m-%d %H:%M')

	print(" UPDATE_SQL STATUS CONFIG [ "+time_stamp+" ] : ",end='',flush=True)
	mycursor = mydb.cursor()
	input=("y",time_stamp)
	this_table="gc_acc"

	sql = "UPDATE `"+this_table+"` SET used= %s  WHERE time_stamps = %s"
	mycursor.execute(sql,input)
	mydb.commit()
	print("[ SUCCED ] ")
	# get_value_cnf(cnf_name)
################################
def read_current_acc_goo():
	
	with open(goog,'r') as file:
		lines = file.readlines()
		lines=lines[0].replace("\n","")
	return lines
# get_all_sql_record()



def change_gc_acc():
	g_a=read_current_acc_goo()
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
	print(new_index)



change_gc_acc()