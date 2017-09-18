import socket
from sys import stdin

#   setup
socketToServer = socket.socket()
#socketToServer.setblocking(0)
socketToServer.settimeout(0.1)
host = "76.30.234.227" # socket.gethostname()
port = 1337

#   connect to server
socketToServer.connect( (host, port) )
bytesFromServer = socketToServer.recv( 1024 )
messageFromServer = bytesFromServer.decode()
print( messageFromServer )

#   be a client
userMessage = None
byesFromServer = None
while True:
    #   check for message from the user
    print( "i am here" )
    userMessage = stdin.readline()
    print( "im here now" )
    if userMessage is not None:
        socketToServer.send( userMessage.encode() )
        userMessage = None
    #   check for message from the server
    print( "receiving" )
    try:
        bytesFromServer = socketToServer.recv(1024)
    except socket.timeout:
        pass
    print( "received" )
    if bytesFromServer is not None:
        print( bytesFromServer.decode() )
        bytesFromServer = None
