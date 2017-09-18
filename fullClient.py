import socket
import collections
from sys import stdin

#   ====================    FUNCTIONS    ====================    #
#   display everything
def displayEverything( messages ):
    #   display the messages
    for message in messages:
        print( message )

    #   display the prompt
    print( "========================================" )
    print( "$: ", end = '' )

#   add a new message from the server to the list of user messages
def addNewMessageToMessage( messageFromServer ):
    messages.popLeft()
    messages.append( messageFromServer )

#   deal with newly received message from server
def dealWithNewMessageFromServer( messageFromServer, socketToServer ):
    #   check if new message is a connection check
    if messageFromServer == "CONNECTION TEST":
        respondToConnectionTest( socketToServer )

    #   check if new message is a user message
    else:
        addNewMessageToMessages( messageFromServer )

#   check for a message from the server
def checkForNewMessageFromServer( socketToServer ):
    socketToServer.settimeout( 0.01 )
    bytesFromServer = None
    try:
        bytesFromServer = socketToServer.recv( 1024 )
    except socket.timeout:
        pass
    if bytesFromServer is not None:
        messageFromServer = bytesFromServer.decode()
        dealWithNewMessageFromServer( messageFromServer, socketToServer )

#   respond to connection test from serverSocket
def respondToConnectionTest( socketToServer ):
    response = "STILL CONNECTED"
    socketToServer.send( response.encode() )

#   check for a new message from the user
def checkForMessageFromUser( socketToServer ):
    userMessage = None
    userMessage = stdin.readline()
    if userMessage is not None:
        socketToServer.send( userMessage.encode() )


#   ====================    MAIN    ====================    #
#   -----   setup   -----   #
socketToServer = socket.socket()
#socketToServer.setblocking(0)
host = "76.30.234.227"
port = 1337

#   -----   connect to server   -----   #
socketToServer.settimeout(5)
socketToServer.connect( (host, port) )
bytesFromServer = socketToServer.recv( 1024 )
serverGreeting = bytesFromServer.decode()
print( serverGreeting )
bytesFromServer = None

#   -----   setup messages  ----- #
messages = collections.deque()
maxMessagesStored = 20
for i in range( 0, maxMessagesStored ):
    blankMessage = ""
    messages.append( blankMessage );

#   -----   be a client -----   #
userMessage = None
bytesFromServer = None
while True:
    checkForNewMessageFromServer( serverSocket )
    checkForMessageFromUser( serverSocket )
