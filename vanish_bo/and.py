
import socket # socket
import subprocess  # Subprocess
import pyautogui  # PyAutoGui
import time  # Time


def connection_function(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  print(s.recv(1024))

connection_function("192.168.1.7", 2222)


def adb_connection(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  print(s.recv(1024))

  subprocess.call(['ssh -p 2222 -L 5555:localhost:5555 kristi@explorer.htb'], shell=True)
  password = "baba123"
  print(s.recv(1024))
  
adb_connection("192.168.1.7", 2222)
