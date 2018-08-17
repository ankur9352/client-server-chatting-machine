import socket
s=socket.socket()
host="192.168.43.239"
print("Server will start at ",host)
port=1234
s.bind((host,port))
print("Server created successfully waiting for connection")
s.listen(1)
con,adr=s.accept()
print(adr,"It is connected to server")
while True:
	message=input(">>\t")
	message=message.encode()
	con.send(message)
	i_msg=con.recv(1024)
	i_msg=i_msg.decode()
	print("Client says:\t",i_msg)
	print("\n")