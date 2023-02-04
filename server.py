#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))
print("Listening ....	")
s.listen(1)
client,addr = s.accept()
print("Connected")
while True:
	cmd = input("$ ")
	client.send(cmd.encode())
	if cmd == "exit" or cmd == "q":
		break
	out = (client.recv(1024)).decode()
	print(out)

client.close()
s.close()


