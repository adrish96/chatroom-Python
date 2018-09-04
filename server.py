#chatroom server 

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accepting_clients():
	while True:
		client,addr=s.accept()
		client.send(bytes("welcome to the chatroom, enter your name and press enter!","utf8"))
		print("< %s > has connected" %addr)
		addresses[client]= addr		#stores IP addresses of clients
		Thread(target=handling_clients, args=(client,)).start()		

def handling_clients(client):
	name=client.recv(150).decode("utf8")	
	clients[client]=name
	welcome_mesg="welcome %s, type {quit} whenever you wish to exit!" %name
	client.send(bytes(welcome_mesg,"utf8"))
	msg="%s has joined the chatroom" %name
	broadcast(msg, "")	
	while True:
		msg=client.recv(100)
		if msg!=bytes("{quit}","utf8"):
			broadcast(msg,name)
		else:
			client.send("{quit}","utf8") 	#triggers action on client side
			client.close()
			del clients[client]
			broadcast(bytes("%s has left chat" %name,"utf8"),"")
			break 	 #end of thread
		
def broadcast(msg, name):
	message=name+": "+msg
	for client in clients:
		client.send(bytes(message,"utf8"))

clients={}
addresses={}
ip="127.0.0.1"
port=9999
address=(ip,port)
s=socket(AF_INET, SOCK_STREAM)
s.bind(address)

if __name__=="__main__":
	s.listen(10)
	print("Server on, waiting for clients!")
	new_thread=Thread(target=accepting_clients)
	new_thread.start()
	new_thread.join()  #stops thread till conn closes
	s.close()


