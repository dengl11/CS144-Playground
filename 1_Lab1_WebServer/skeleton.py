# Skeleton Python Code for the Web Server


#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 3000))
serverSocket.listen()
#Fill in end
quest = 0
while True:
    #Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr =  serverSocket.accept()
    #Fill in end
    quest += 1
    try:
        print("------------------\n  Serving Quest {} \n------------------\n".format(quest))
        #Fill in start
        message = connectionSocket.recv(1024).decode()
        #Fill in end
        print("message: {}".format(message))
        filename = message.split()[1]
        print("filename: {}".format(filename))
        f = open(filename[1:])
        #Fill in start
        outputdata = f.readlines()
        #Fill in end
        # #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        # #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
         #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
