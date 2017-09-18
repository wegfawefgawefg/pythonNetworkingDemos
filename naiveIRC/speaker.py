import socket
import collections
import os
from sys import stdin

#   ====================    FUNCTIONS    ====================    #
#   check for a new message from the user
def checkForMessageFromUser( socketToServer ):
    userMessage = None
    userMessage = stdin.readline()
    if userMessage is not None:
        try:
            socketToServer.send( userMessage.encode() )
        except socket.timeout:
            pass
        else:
            print( "\n!!! CONNECTION LOST !!!" )
            global serverOpen
            serverOpen = False


#   ====================    MAIN    ====================    #
#   -----   setup   -----   #
socketToServer = socket.socket( )
#socketToServer.setblocking(0)
host = "76.30.234.227"
port = 1337

#   -----   connect to server   -----   #
socketToServer.settimeout(5)
socketToServer.connect( (host, port) )
clientType = "SPKR"
socketToServer.send( clientType.encode() )
bytesFromServer = socketToServer.recv( 1024 )
serverGreeting = bytesFromServer.decode()
print( serverGreeting )

#   -----   be a client -----   #
userMessage = None
bytesFromServer = None
socketToServer.settimeout( 0.001 )
serverOpen = True
while serverOpen:
    checkForMessageFromUser( socketToServer )
