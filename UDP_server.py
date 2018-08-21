#server.py

import socket

ip="10.42.0.109"
port=9999
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip,port))

while True:
	print (s.recvfrom(1000))
	data=raw_input("enter reply: ")
	data.encode()	
	s.sendto(data,("192.168.102.114",8889))
