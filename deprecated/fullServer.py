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
def checkForNewMessagesFromClients( connectedClients, disconnectedClients ):
    for connectedClient in connectedClients:
        connectedClient.settimeout( 0.01 )
        bytesFromClient = None
        try:
            bytesFromClient = connectedClient.recv( 1024 )
        except socket.timeout:
            pass
        except socket.error:
            addClientConnectionToDisconnectList( connectedClient, disconnectedClients )
        if bytesFromClient is not None:
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
def sendAnyPendingNewMessages( newMessages, connectedClients, disconnectedClients ):
    while( len( newMessages ) > 0 ):
        newMessage = newMessages.popleft()
        sendMessageToAllClientConnections( newMessage, connectedClients, disconnectedClients )

#   send a message to every connected client
def sendMessageToAllClientConnections( message, connectedClients, disconnectedClients ):
    for connectedClient in connectedClients:
        try:
            connectedClient.send( message.encode() )
        except socket.error:
            addClientConnectionToDisconnectList( connectedClient, disconnectedClients )

#   remove disconnected clients from list fo clients
def removeDisconnectedClients( disconnectedClients, connectedClients ):
    for disconnectedClient in disconnectedClients:
        connectedClients.remove( disconnectedClient )
        print( "Traveler has left." )

    #   empty the disconectedClients list
    disconnectedClients.clear()

#   add an errord client connection to the remove list
def addClientConnectionToDisconnectList( connectedClient, disconnectedClients ):
    if connectedClient not in disconnectedClients:
        disconnectedClients.append( connectedClient )

#   ====================    MAIN    ====================    #
#   -----   setup   -----   #
serverSocket = socket.socket()
serverSocket.settimeout( 0.01 )
#serverSocket.setblocking(0)
hostLocalIP = "10.0.0.43"
print( hostLocalIP )
port = 1337
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind( (hostLocalIP, port) )

greeting = "Welcome, traveler."

#   -----   setup state    -----   #
#   list of all connected clients
connectedClients = []

#   list of clients to be removed
disconnectedClients = []

#   newMesssages container
newMessages = collections.deque()

######!!!!! need to come up with a way to test for timeouts from all the connected clients periodically

#   -----   be a server -----   #
serverSocket.listen(5)

while True:
    checkForNewMessagesFromClients( connectedClients, disconnectedClients )
    sendAnyPendingNewMessages( newMessages, connectedClients, disconnectedClients )
    removeDisconnectedClients( disconnectedClients, connectedClients )
    checkForNewClientConnection( connectedClients )
