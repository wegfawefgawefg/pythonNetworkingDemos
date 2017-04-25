import socket

#   setup
serverSocket = socket.socket()
host = "10.0.0.43"  # socket.gethostname( )
print( host )
port = 1337
serverSocket.bind( (host, port) )

#   be a server
serverSocket.listen(5)
while True:
    connection, address = serverSocket.accept()
    print( address, " connected." )
    message = ">///< aah, dont look s-senpai!"
    connection.send( message.encode() )
    connection.close()
