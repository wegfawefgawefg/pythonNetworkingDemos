import socket

#   -----   setup   -----   #
serverSocket = socket.socket()
#   set static ip for server device through router
#   #   ex: T430S dns-disabled ip = 10.0.0.43
hostLocalIP = "10.0.0.43"
print( hostLocalIP )
#   pick a port between 1024 and 49151
#   #   other ports are reserved for stuff
port = 1337
serverSocket.bind( (hostLocalIP, port) )

#   -----   be a server ----- #
serverSocket.listen()
while True:
    connection, address = serverSocket.accept()
    print( address, " connected." )
    message = ">///< aah, dont look s-senpai!"
    connection.send( message.encode() )
    connection.close()
    print( address, " disconnectd." )
