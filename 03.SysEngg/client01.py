from http.client import RemoteDisconnected
import socket

# Prepare Socket
soc=socket.socket()
print("Socket Created")

#Connect to Server
remoteDetails=("127.0.0.1",9090)
soc.connect(remoteDetails)

#Receive data from the server
msg=soc.recv(1024)
print("Message from SERVER: ",msg)

soc.close()