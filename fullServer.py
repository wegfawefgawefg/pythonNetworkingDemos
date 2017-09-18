import socket
import collections

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
    checkForNewClientConnection( connectedClients )
    #send all new messages if there are any @@@@THIS NEEEDS TO BE ADDED@@@@@#

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

#   deal with new message from a connected clients
def dealWithNewMessageFromClient( messageFromClient ):
    #   this is where we would check if the message is a ping
    #!!!!!not implemented yet though!!!!!#
    #   if message is not a response to a client request
    #   #   then add it to the deque of new messages
    newMessages.append( messageFromClient )

#   check for new client connection
def checkFoNewClientConnection( connectedClients ):
        newClientConnection = None
        try:
            newClientConnection, address = serverSocket.accept()
        except socket.timeout:
            pass
        if newClientConnection is not None:
            dealWithNewClientConnection( newClientConnection, newClientIPAddress )

#   deal with new client connection
def dealWithNewClientConnection( newClientConnection, newClientIPAddress ):
    print( "New Traveler: ", newClientIPAddress )
    connection.send( greeting.encode() )

    #   add connection to connections list
    connections.append( connection )
