#client code for private chatting application
import socket
s=socket.socket()
host=input('enter the name of server--')
port=1234
s.connect((host,port))
print('connected  to server')
while(1):
    i_msg=s.recv(1024)
    i_msg=i_msg.decode()
    print('server says:  ',i_msg)
    msg=input('>> ')
    msg=msg.encode()
    s.send(msg)
    
    