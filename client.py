#client using tcp

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect( ("127.0.0.1",9999) )
while True:
	msg=s.recv(100)
	print(msg.decode() )
	print("enter reply:")
	data=raw_input()
	s.send(data.encode() )
