import os , requests
fuckk=[]

telegram_tokens_van="5842682178:AAHhcZ41vh4XpIXvVhZ0-RuN0KkCClVgg4g"
chat_id_alerts_van_google = "-1001633899177"


# log_01=["1111111111111"]





def repport_telegram_send(text):

	msg_telegram="👽 [  ]\n"+text
	# msg_telegram="👽 [ "+hostname_os +" ]\n"+text
	token = telegram_tokens_van
	chat_id = chat_id_alerts_van_google
	url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
	results = requests.get(url_req)


# log_01=['LOOKE3', 'SITE_5 V 6.0 io/IMG = xm0uray-site_5 | chrome api ++v977',
#  'https://mohmal.eu.org/', 'https://mohmal.eu.org/', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36', 
#  '(Windows NT 6.1)', '1',
#   'https://apiv7-koy01apiv7.koyeb.app', 'us8263.nordvpn.com.tcp.ovpn', 77, '2707', 'Africa/Algiers',
#    '45.143.82.88', 'America/Los_Angeles', '47.4485,-122.2922',
#     ['DHmwrGCdvYLjYjwnDBNKVZsi\n', 'j9WiqUvujJBKH67QWxPqG1BD'], 'Africa/Algiers', '1920,1200',
#      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36',
#       'x64', 'NVIDIA Corporation', 'GeForce GTX 770/PCIe/SSE2', 'BC.Game FIFA world cup', 'XD XD', 'BTCMiddleMan.com', 'BC.Game FIFA world cup']


def tel_banner(log_01):
	# print(log_01)
	'''+log_01[8]+log_01[9]+log_01[9]+'''
	s = str(log_01[7])
	s2=s.replace("https://","")
	vis_and_size=log_01[17]+' | '+str(log_01[6])
	vpn_info=log_01[8]+' | '+str(log_01[9])+' | '+str(log_01[10])
	vpn_info_geo=log_01[12]+' | '+str(log_01[13])#+' | '+str(log_01[14])
	devv=log_01[19]+' | '+str(log_01[20])+' | '+str(log_01[21])
	adsss1=log_01[24]
	adsss2=log_01[22]
	text000000000='''💫[ '''+log_01[0]+''' ] 💫
	🎩 [  IMAGE   ] : '''+log_01[0]+''' 🎩
	🎩 [   URL    ] : '''+log_01[2]+''' 🎩
	🎩 [    UA    ] : '''+log_01[5]+''' 🎩
	🎩 [   SIZE   ] : '''+vis_and_size+''' 🎩
	🎩 [   API    ] : ['''+s2+'''] 🎩
	🎩 [   VPN    ] : [ '''+vpn_info+''' ] 🎩
	🎩 [   GEO    ] : [ '''+vpn_info_geo+''' ] 🎩
	🎩 [   DEV    ] : [ '''+devv+''' ] 🎩
	🎩 [  ADS 01  ] : [ '''+adsss1+''' ] 🎩
	🎩 [  ADS 02  ] : [ '''+adsss2+''' ] 🎩
	🎩 [  CLIKED  ] : [ '''+log_01[23]+''' ] 🎩'''
	repport_telegram_send(text000000000)


# tel_banner(log_01)
# s = str(log_01[7])
# s2=s.replace("https://","")
# print(s2)