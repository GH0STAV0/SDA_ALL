

import mysql.connector
import time ,os
from datetime import datetime





HOST="zzroiqlkjzv2.eu-west-2.psdb.cloud"
USERNAME="c4cz3k2azim8"
PASSWORD="pscale_pw_SZsOhzZm6AVnde53meT3ygRRh7zSjXdZ4dawwURylQo"
DATABASE="plan"






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



check_connect_mysql()