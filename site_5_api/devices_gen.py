from selenium import webdriver
from selenium_stealth import stealth
import time ,os
import cnf_bvb
from device_detector import DeviceDetector
import urllib.parse
import json
import random


# ua=cnf_bvb.user_agent

renderers_nv= [
"GeForce 8600M GT/PCIe/SSE2",
"GeForce GT 430/PCIe/SSE2",
"GeForce GT 520/PCIe/SSE2",
"GeForce GTX 650 Ti/PCIe/SSE2",
"GeForce GTX 680/PCIe/SSE2",
"GeForce GTX 770/PCIe/SSE2",
"NVIDIA GeForce 320M OpenGL Engine",
"NVIDIA GeForce 8600M GT OpenGL Engine",
"NVIDIA GeForce 8800 GS OpenGL Engine",
"NVIDIA GeForce 8800 GT OpenGL Engine",
"NVIDIA GeForce 9400 OpenGL Engine",
"NVIDIA GeForce 9400M OpenGL Engine",
"NVIDIA GeForce 9600M GT OpenGL Engine",
"NVIDIA GeForce GT 130 OpenGL Engine",
"NVIDIA GeForce GT 330M OpenGL Engine",
"NVIDIA GeForce GT 640M OpenGL Engine",
"NVIDIA GeForce GT 650M OpenGL Engine",
"NVIDIA GeForce GT 750M OpenGL Engine",
"NVIDIA GeForce GTX 660M OpenGL Engine",
"NVIDIA GeForce GTX 675MX OpenGL Engine",
"NVIDIA GeForce GTX 680MX OpenGL Engine",
"Quadro 2000/PCIe/SSE2",
"Quadro 2000M/PCIe/SSE2",
"Quadro FX 1800/PCIe/SSE2",
"Quadro K600/PCIe/SSE2"]



RENDERER_MOBILE = [
  'Mali-T830',
  'Mali-G71',
  'Adreno (TM) 540',
  'Mali-G72',
  'Mali-T880',
  'Adreno (TM) 630',
  'Apple A7 GPU',
  'Adreno (TM) 530',
  'Mali-T720',
  'Adreno (TM) 506',
  'Mali-T760',
  'Adreno (TM) 308',
  'Adreno (TM) 505',
  'Adreno (TM) 306',
  'PowerVR SGX 543',
  'Mali-400 MP',
  'Adreno (TM) 330',
  'Mali-T860',
  'Adreno (TM) 512',
  'Adreno (TM) 304',
  'Adreno (TM) 405',
  'Adreno (TM) 510',
  'Mali-450 MP',
  'Adreno (TM) 509',
  'Adreno (TM) 430',
  'llvmpipe (LLVM 6.0 256 bits)',
  'Mali-G51',
  'Google SwiftShader',
  'Adreno (TM) 305',
  'Adreno (TM) 418',
  'Adreno (TM) 508',
  'Mali-G76',
  'Apple GPU',
  'PowerVR Rogue GE8100',
  'Vivante GC7000UL',
  'Mali-T624',
  'Mali-G72 MP3',
  'Adreno (TM) 420',
  'Adreno (TM) 320',
  'PowerVR Rogue GE8320',
  'Mali-T628',
  'PowerVR Rogue G6200',
  'Qualcomm Adreno 430',
  'Adreno (TM) 615',
  'Adreno (TM) 616',
  'Qualcomm Adreno 305',
  'Qualcomm Adreno 304',
  'PowerVR Rogue G6430',
  'PowerVR Rogue GX6250',
  'PowerVR SGX 544MP2',
  'Chromium',
  'PowerVR Rogue GT7400 Plus',
  'PowerVR SGX 544MP',
  'Apple A12X GPU',
  'Intel(R) HD Graphics for BayTrail',
  'Intel(R) HD Graphics 6000',
  'Adreno (TM) 225',
  'AMD Radeon Pro 455 OpenGL Engine',
  'Gallium 0.4 on llvmpipe (LLVM 3.8 256 bits)',
  'VideoCore IV HW',
  'Adreno (TM) 203',
  'AMD Radeon Pro 560 OpenGL Engine',
  'AMD Radeon R9 M380 OpenGL Engine',
  'GC1000 core',
  'Intel Iris OpenGL Engine',
  'Intel Iris Pro OpenGL Engine',
  'llvmpipe (LLVM 7.0 256 bits)',
  'PowerVR Rogue GE8200',
  'PowerVR Rogue GE8300'
]

def mokking(ua):

	device=DeviceDetector(ua).parse()
	# ua = 'Mozilla/5.0 (Linux; Android 4.3; C5502 Build/10.4.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36'

	# print(str(ua))
	device_name=device.is_desktop()
	# device_plat=device.
	os_name=device.os_name()
	os_version=device.os_version()
	engine=device.engine()
	device_brand=device.device_brand()
	device_brand_name=device.device_model()
	device_type=device.device_type()
	# print(device_name, os_name,os_version,device_brand+" model "+device_brand_name+ " device_type "+device_type)
	device.is_bot()
	device.device_brand()
	device.engine()
	# print(ua)
	paaaa=urllib.parse.quote(ua)
	# os.system('curl https://api.apicagent.com/?ua="'+paaaa+'"')
	import requests
	datab = {"ua":'"'+ua+'"'}
	r = requests.post("https://api.apicagent.com/", json={'json_payload': datab})


	url = 'https://api.apicagent.com'
	payload = {'some': 'data'}
	headers = {'content-type': 'application/json'}

	response = requests.post(url, data=json.dumps(datab), headers=headers)



	jsonResponse=response.json()
	# print(jsonResponse)
	os_name=jsonResponse["os"]["name"]
	# print(os_name)
	# print(jsonResponse["device"]["type"])
	# print(jsonResponse["device"]["brand"])
	# print(jsonResponse["os"]["platform"])
	vendor = "NVIDIA Corporation"
	randerer= user_agent = random.choice(renderers_nv)
	platfom="x64"
	try:
		if "Windows" in os_name:
			vendor = "NVIDIA Corporation"
			randerer= user_agent = random.choice(renderers_nv)
			platfom="x64"
		if "Android" in os_name:
			vendor = "ARM Corporation"
			randerer= user_agent = random.choice(RENDERER_MOBILE)
			platfom="ARM"
		if "iOS" in os_name:
			vendor = "ARM Corporation"
			randerer= user_agent = random.choice(RENDERER_MOBILE)
			platfom="Appel Inc"
		if "Debian" in os_name:
			vendor = "NVIDIA Corporation"
			randerer= user_agent = random.choice(renderers_nv)
			platfom="x64"
	except:
		vendor = "NVIDIA Corporation"
		randerer= user_agent = random.choice(renderers_nv)
		platfom="x64"

	# Debian

	# print(vendor,randerer,platfom)
	return vendor,randerer,platfom




# mokking(ua)