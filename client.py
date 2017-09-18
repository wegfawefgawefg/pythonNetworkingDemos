import socket

#   -----   setup   -----   #
socketToServer = socket.socket()
#T430SIP = "76.30.234.227"
jacobsLaptopIP = "98.198.242.96"
serverIP = jacobsLaptopIP
port = 1337

#   -----   be a client -----   #
socketToServer.connect( (serverIP, port) )
bytesFromServer = socketToServer.recv( 1024 )
messageFromServer = bytesFromServer.decode()
print( messageFromServer )
socketToServer.close()
