import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP stream orinted connection

server_socket.bind(('127.0.0.1',5080))

server_socket.listen(10)

print("Listening for connections on 127.0.0.1:5080 ")

while True:

	conn, addr = server_socket.accept()
	print("Got a connection from  {}".format(addr))

	while True:

		data = conn.recv(1024) # Specified the limit of  bites to be receive

		if(data.decode() == 'end'): # TO end the communication...
			break
		print(" Client sent",data.decode())
		server_data = input("Enter Data to send--> ")
		conn.send(server_data.encode())

		conn.send(b' This is server')

	conn.close()
	print("!!! Client Disconnecte !!!")	

