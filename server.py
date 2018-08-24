#server.py
#using TCP

import socket
import sys

ip="127.0.0.1"
port=9999
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind( (ip,port) )
s.listen(100)
conn,addr= s.accept()
str="connection with server estabilished"
conn.send(str)
while True:
	msg=conn.recv(100)
	print ("<"+addr[0]+"> "+msg.decode() )
	print("enter reply: ")
	data=raw_input()
	conn.send(data.encode())
	
