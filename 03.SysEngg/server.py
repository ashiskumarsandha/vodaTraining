from http.client import RemoteDisconnected
import socket

# Prepare Socket
soc=socket.socket()
print("Socket Created")

#Bind the Socket
remoteDetails=("",9090)
soc.bind(remoteDetails)

print("Socket Binded to Port 9090")

# Listing Mode
soc.listen(5)
print("Socket Server Listening")

while True:
    c,addr=soc.accept()
    print("Got Connected From ", addr)

    greetMsg="Welcome to My Server..."
    c.send(greetMsg.encode())

    c.close()
    print("Client Connection Closed")