import socket

#   setup
socketToServer = socket.socket()
host = "76.30.234.227" # socket.gethostname()
port = 1337

#   be a client
socketToServer.connect( (host, port) )
bytesFromServer = socketToServer.recv( 1024 )
messageFromServer = bytesFromServer.decode()
print( messageFromServer )
socketToServer.close()
