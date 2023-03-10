import requests
# url="https://api-nod.onrender.com"
# url="https://nd-my-01.onrender.com"
# https://apiv5.onrender.com/
# url="https://apiv5.onrender.com"
# url="https://apiv6.onrender.com"
url="https://apiv7-koy01apiv7.koyeb.app"


telegram_tokens_van="5842682178:AAHhcZ41vh4XpIXvVhZ0-RuN0KkCClVgg4g"
chat_id_alerts_van_google = "-1001633899177"
hostname_os=""

def send_msg(text):

	msg_telegram="👽 [ "+hostname_os +" ]\n"+text
	token = telegram_tokens_van
	chat_id = chat_id_alerts_van_google
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + msg_telegram 
	results = requests.get(url_req)


log_01=['tuesdays','never']
# wash_clothes = 
# clean_dishes = 
text000000000='''💫[ bigochildxtow-gc-emma-3 ] 💫 
🎩 '''+log_01[0]+''' 🎩
'''

send_msg(text000000000)