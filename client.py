import socket

#   setup
socketToServer = socket.socket()
serverIP = "76.30.234.227"
port = 1337

#   be a client
socketToServer.connect( (serverIP, port) )
bytesFromServer = socketToServer.recv( 1024 )
messageFromServer = bytesFromServer.decode()
print( messageFromServer )
socketToServer.close()
