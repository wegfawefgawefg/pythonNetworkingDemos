import socket
import collections

#   ====================    FUNCTIONS    ====================    #
#   deal with new message from a connected clients
def dealWithNewMessageFromClient( messageFromClient ):
    #   this is where we would check if the message is a ping
    #!!!!!not implemented yet though!!!!!#
    #   if message is not a response to a client request
    #   #   then add it to the deque of new messages
    newMessages.append( messageFromClient )

#   check for new messages from clients
def checkForNewMessagesFromClients( connectedClients ):
    for connectedClient in connectedClients:
        connectedClient.settimeout( 0.01 )
        bytesFromClient = None
        try:
            bytesFromClient = connectedClient.recv( 1024 )
        except socket.timeout:
            pass
        if rawMessageFromClient is not None:
            messageFromClient = bytesFromClient.decode()
            dealWithNewMessageFromClient( messageFromClient )

#   deal with new client connection
def dealWithNewClientConnection( newClientConnection, newClientIPAddress, connectedClients ):
    print( "New Traveler: ", newClientIPAddress )
    newClientConnection.send( greeting.encode() )

    #   add connection to connections list
    connectedClients.append( newClientConnection )

#   check for new client connection
def checkForNewClientConnection( connectedClients ):
        newClientConnection = None
        newClientIPAddress = None
        try:
            newClientConnection, newClientIPAddress = serverSocket.accept()
        except socket.timeout:
            pass
        if newClientConnection is not None:
            dealWithNewClientConnection( newClientConnection, newClientIPAddress, connectedClients )

#   send all the new messages waiting to be sent
def sendAnyPendingNewMessages( newMessages, connectedClients ):
    while( len( newMessages ) > 0 ):
        newMessage = newMessages.popLeft()
        sendMessageToAllClientConnections( newMessage )

#   send a message to every connected client
def sendMessageToAllClientConnections( message, connectedClients ):
    for connectedClient in connectedClients:
        connectedClient.send( message )

#   ====================    MAIN    ====================    #
#   -----   setup   -----   #
serverSocket = socket.socket()
#serverSocket.setblocking(0)
hostLocalIP = "10.0.0.43"
print( hostLocalIP )
port = 1337
serverSocket.bind( (hostLocalIP, port) )

greeting = "Welcome, traveler."

#   -----   setup state    -----   #
#   list of all connected clients
connectedClients = []

#   newMesssages container
newMessages = collections.deque()

######!!!!! need to come up with a way to test for timeouts from all the connected clients periodically

#   -----   be a server -----   #
serverSocket.listen(5)

while True:
    checkForNewMessagesFromClients( connectedClients )
    sendAnyPendingNewMessages( newMessages, connectedClients )
    checkForNewClientConnection( connectedClients )
