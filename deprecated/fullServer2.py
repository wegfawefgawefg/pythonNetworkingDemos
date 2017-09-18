import socket
import collections

#   ====================    FUNCTIONS    ====================    #
#   add an errord client connection to the remove list
def addClientConnectionToADisconnectList( connectedClient, disconnectedClients ):
    if connectedClient not in disconnectedClients:
        disconnectedClients.append( connectedClient )

#   deal with new message from a connected clients
def dealWithNewMessageFromSpeaker( newMessage ):
    #   this is where we would check if the message is a ping
    #!!!!!not implemented yet though!!!!!#
    #   if message is not a response to a client request
    #   #   then add it to the deque of new messages
    newMessages.append( newMessage )

#   check for new messages from clients
def checkForNewMessages( speakers, disconnectedSpeakers ):
    for speaker in speakers:
        speaker.settimeout( 0.1 )
        bytesFromSpeaker = None
        try:
            bytesFromSpeaker = speaker.recv( 1024 )
        except socket.timeout:
            pass
        except socket.error:
            #addClientConnectionToADisconnectList( speaker, disconnectedSpeakers )
            pass
        if bytesFromSpeaker is not None:
            messageFromSpeaker = bytesFromSpeaker.decode()
            dealWithNewMessageFromSpeaker( messageFromSpeaker )

#   deal with new client connection
def dealWithNewClientConnection( newClientConnection, newClientIPAddress, speakers, listeners ):
    print( "New Traveler: ", newClientIPAddress )

    #   get client type
    newClientConnection.settimeout( 1.0 )
    bytesFromClient = newClientConnection.recv( 4 )
    clientType = bytesFromClient.decode()
    if clientType == "SPKR":
        speakers.append( newClientConnection )
        newClientConnection.send( speakerGreeting.encode() )
    else if clientType = "LSTN":
        listeners.append( newClientConnection )
        newClientConnection.send( listenerGreeting.encode() )

    #   greet the client
    newClientConnection.send( goodbye.encode() );

#   check for new client connection
def checkForNewClientConnection( speakers, listeners ):
        newClientConnection = None
        newClientIPAddress = None
        try:
            newClientConnection, newClientIPAddress = serverSocket.accept()
        except socket.timeout:
            pass
        if newClientConnection is not None:
            dealWithNewClientConnection( newClientConnection, newClientIPAddress, speakers, listeners )

#   send all the new messages waiting to be sent
def sendAnyPendingNewMessages( newMessages, listeners, disconnectedListeners ):
    while( len( newMessages ) > 0 ):
        newMessage = newMessages.popleft()
        sendMessageToAllListeners( newMessage, listeners, disconnectedListeners )

#   send a message to every connected client
def sendMessageToAllListeners( message, listeners, disconnectedListeners ):
    for listener in listeners:
        try:
            listener.send( message.encode() )
        except socket.error:
            #addClientConnectionToADisconnectList( listener, disconnectedListeners )
            pass

#           REWRITE THIS SHIT   #
#   remove disconnected clients from list fo clients
def removeDisconnectedClients( disconnectedClients, connectedClients ):
    removedClients = []
    for disconnectedClient in disconnectedClients:
        connectedClients.remove( disconnectedClient )
        removedClients.append( disconnectedClient )
        print( "Traveler has left." )

    #   empty the disconectedClients list
    for removed in removedClients:
        disconnectedClients.remove( removed )
    removedClients.clear()


#   ====================    MAIN    ====================    #
#   -----   setup   -----   #
serverSocket = socket.socket()
#serverSocket.setblocking(0)
hostLocalIP = "10.0.0.43"
print( hostLocalIP )
port = 1337
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind( (hostLocalIP, port) )

speakerGreeting = "Welcome, traveler. Flap your braggart gums."
listenerGreeting = "Welcome, traveler. Rest your weary tongue."
goodbye = "We dont take well to your kind here."

#   -----   setup state    -----   #
#   list of all connected clients
speaker = []
listener = []

#   list of clients to be removed
disconnectedSpeakers = []
disconnectedListeners = []

#   newMesssages container
newMessages = collections.deque()

######!!!!! need to come up with a way to test for timeouts from all the connected clients periodically

#   -----   be a server -----   #
serverSocket.listen(5)

while True:
    checkForNewMessages( speakers, disconnectedSpeakers )
    sendAnyPendingNewMessages( newMessages, listeners, disconnectedListeners )
    #removeDisconnectedClients( speakers, disconnectedSpeakers )
    #removeDisconnectedClients( listeners, disconnectedListeners )
    checkForNewClientConnection( speakers, listeners )
