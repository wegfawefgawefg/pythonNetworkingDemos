import socket

#   setup
serverSocket = socket.socket()
#serverSocket.setblocking(0)
serverSocket.settimeout(0.1)
host = "10.0.0.43"  # socket.gethostname( )
print( host )
port = 1337
serverSocket.bind( (host, port) )

greeting = "Welcome, traveler."

#   be a server
serverSocket.listen(5)
connections = []

while True:
    #   look for a new connection
    connection = None
    try:
        connection, address = serverSocket.accept()
    except socket.timeout:
        pass
    if connection is not None:
        print( "New Traveler: ", address )
        connection.send( greeting.encode() )
        #   add connection to connections list
        connections.append( connection )
        connection = None


    #   check through connection list for new messageFromServer
    for transmitter in connections:
        rawMessage = None
        try:
            rawMessage = transmitter.recv( 1024 )
        except socket.timeout:
            pass
        if rawMessage is not None:
            print( "Traveler ", transmitter.getsockname(), "says: ", rawMessage.decode() )
            #   trasmit that message to all other connections in the list
            for receiver in connections:
                #   do not send the message to the original sender
                if receiver == transmitter:
                    break
                receiver.send( rawMessage )
