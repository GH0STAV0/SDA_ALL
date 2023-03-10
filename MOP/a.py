
import os ,random


file_list_1='NCH_list_1'

pwd = os.path.dirname(os.path.realpath( __file__ ))

vpn_folder=pwd+"/CHEAP_VPN/"

all_vpn_config_file=os.listdir(vpn_folder)


def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines


def write_new_list(new_vpn_arry):
	with open(file_list_1,"w") as fw:
		for i in new_vpn_arry:
			fw.write(i)
	print("OK !!")





def check_list_vpn_lengh():
	num_lines = sum(1 for line in open(file_list_1))
	if num_lines==0:
		creat_list_of_vpn()
	else:
		pass


def creat_list_of_vpn():
	with open(file_list_1,'w') as fw:
		for i in all_vpn_config_file:
			fw.write(i+"\n")



def remove_from_list_running(vpn_name):
	print("REMOVING THE VPN CONFIG [ "+vpn_name+" ]",end=' ',flush=True)
	vpn_name=vpn_name+"\n"
	arry_vpn_list=read_current_list_vpn()
	arry_vpn_list.remove(vpn_name)
	write_new_list(arry_vpn_list)




def get_random_vpn():
	check_list_vpn_lengh()
	arry_vv=read_current_list_vpn()
	random_vpn=random.choice(arry_vv)
	random_vpn=random_vpn.replace('\n','')
	final_vpn=vpn_folder+random_vpn
	# print(random_vpn)
	return final_vpn , random_vpn


def main():
	final_vpn , random_vpn=get_random_vpn()
	remove_from_list_running(random_vpn)

if __name__ == '__main__':

	main()

