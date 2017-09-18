import socket
import collections

#   ====================    FUNCTIONS    ====================    #
#   check for new messages from clients
def checkForNewMessages( speakers, listeners, disconnectedSpeakers, disconnectedListeners ):
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
            #dealWithNewMessageFromSpeaker( messageFromSpeaker )
            sendMessageToAllListeners( messageFromSpeaker, listeners, disconnectedListeners )

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
    elif clientType == "LSTN":
        listeners.append( newClientConnection )
        newClientConnection.send( listenerGreeting.encode() )
    else:
    #   shun the client, and do not save
        newClientConnection.send( goodbye.encode() );
        newClientConnection.shutdown();
        newClientConnection.close();

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

#   send a message to every connected client
def sendMessageToAllListeners( message, listeners ):
    print( "broadcasting" )
    for listener in listeners:
        try:
            listener.send( message.encode() )
        except socket.error:
            #addClientConnectionToADisconnectList( listener, disconnectedListeners )
            pass

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
speakers = []
listeners = []

#   list of clients to be removed
disconnectedSpeakers = []
disconnectedListeners = []

#   newMesssages container
newMessages = collections.deque()

######!!!!! need to come up with a way to test for timeouts from all the connected clients periodically

#   -----   be a server -----   #
serverSocket.listen(5)

while True:
    checkForNewMessages( speakers, listeners )
    checkForNewClientConnection( speakers, listeners )
