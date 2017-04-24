import socket

#   setup
serverSocket = socket.socket()
host = socket.gethostname()
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
