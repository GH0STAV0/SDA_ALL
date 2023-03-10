import cnf_bvb
import emoji
# from pyvirtualdisplay import Display
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
# from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
#from selenium.webdriver import ActionChains
os.system("rm -rf /tmp/*")
def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		#os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")

def build_driver(width,height):
	#init_fire()
	print("BUILDING PROFILE DRIVER  ...... ",end='')
	user_agent = cnf_bvb.user_agent
	sys_use_agent=re.findall('\(.*?\)',user_agent)[0]
	#random_display_chose=cnf_bvb.random_display_chose
	# width=cnf_bvb.width
	# height=cnf_bvb.height
	#width , height =cnf_bvb.resolution_func()
	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)
	try:
		new_driver_path = cnf_bvb.new_driver_path
		new_binary_path = cnf_bvb.random_fir()
		#print(new_binary_path)
		serv = Service(new_driver_path)
		# fp = webdriver.FirefoxProfile()
		fp = webdriver.FirefoxProfile(cnf_bvb.pofile_path)
		ops = Firefox_Options()
		#user_agent = cnf_bvb.user_agent
		#firefox_options = Firefox_Options()		
		ops.add_argument(moz_wid)
		ops.add_argument(moz_hig)
		# my_proxy="127.0.01:9050"
		# ipp,pport=my_proxy.split(':')
		######################################
		# fp.set_preference('browser.sessionhistory.max_total_viewers', 0)
		# #fp.set_preference('browser.cache.memory.enable', False)
		# #fp.set_preference('browser.cache.offline.enable', False)
		# #fp.set_preference('browser.cache.disk.enable', False)
		# fp.set_preference('browser.safebrowsing.enabled', False)
		# fp.set_preference('browser.shell.checkDefaultBrowser', False)
		# fp.set_preference('browser.startup.page', 0)
		# fp.set_preference('dom.ipc.plugins.enabled.timeoutSecs', 15)
		# fp.set_preference('dom.max_script_run_time', 10)
		# fp.set_preference('extensions.checkCompatibility', False)
		# fp.set_preference('extensions.checkUpdateSecurity', False)
		# fp.set_preference('extensions.update.autoUpdateEnabled', False)
		# fp.set_preference('extensions.update.enabled', False)
		# fp.set_preference('network.http.max-connections-per-server', 30)
		# fp.set_preference('network.prefetch-next', False)
		# fp.set_preference('plugin.default_plugin_disabled', False)
		# fp.set_preference('print.postscript.enabled', False)
		# fp.set_preference('toolkit.storage.synchronous', 0)
		# fp.set_preference('image.animation_mode', 'none')
		# fp.set_preference('images.dither', False)
		# fp.set_preference('content.notify.interval', 1000000)
		# fp.set_preference('content.switch.treshold', 100000)
		# fp.set_preference('nglayout.initialpaint.delay', 1000000)
		# fp.set_preference('network.dnscacheentries', 200)
		# fp.set_preference('network.dnscacheexpiration', 600)
		# #######################################
		# # fp.set_preference('network.proxy.type', 1)
		# # fp.set_preference('network.proxy.socks', ipp)
		# # fp.set_preference('network.proxy.socks_port', int(pport))
		# # fp.set_preference('network.proxy.socks', '127.0.0.1')
		# # fp.set_preference('network.proxy.socks_port', 9150)
		# fp.set_preference("dom.webdriver.enabled", False)
		# fp.set_preference('useAutomationExtension', False)
		# # #fp.set_preference("http.response.timeout",95)
		# # # fp.set_preference("dom.popup_maximum", 2)
		# # fp.set_preference("general.useragent.override",user_agent)
		# fp.set_preference('webdriver.load.strategy','unstable')
		# fp.set_preference("modifyheaders.headers.count", 2)
		# fp.set_preference("dom.webdriver.enabled", False)
		# fp.set_preference("modifyheaders.headers.action0", "Add")
		# fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		# fp.set_preference("dom.push.enabled", False)
		# fp.set_preference("intl.accept_languages", "en-GB");
		fp.set_preference("security.sandbox.content.level", 0)
		fp.update_preferences()
		ops.binary_location = new_binary_path
		ops.profile=fp

		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		# driver.set_page_load_timeout(79)
		# driver.set_page_load_timeout(79)
		driver.maximize_window()
		print(emoji.emojize("Ok DRIVER "' :check_mark_button: :alien:'))

		#driver = webdriver.Firefox(service=serv, options=ops)
		#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		#driver.set_page_load_timeout(79)

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		#print(new_binary_path)
	except Exception as error:
		print("    Error !!!!! ----->"+str(error))
	return driver