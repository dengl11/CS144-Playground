# Skeleton Python Code for the Web Server


#import socket module
from socket import *
import sys # In order to terminate the program

# SOCK_STREAM: TCP Socket 
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 3004))

# must listen before accept 
serverSocket.listen()
#Fill in end

quest = 0

while True:
    #Establish the connection
    #Fill in start
    connectionSocket, addr =  serverSocket.accept()
    #Fill in end
    quest += 1
    try:
        print("------------------\n  Serving Quest {} \n------------------\n".format(quest))
        #Fill in start
        message = connectionSocket.recv(1024).decode()
        #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #Fill in start
        outputdata = f.readlines()
        #Fill in end

        # Send one HTTP header line into socket
        #Fill in start
        response_header = "\n".join([
            "HTTP/1.1  ", 
            "Content-Type: text/html",
            "\r\n",
            ]) 

        # encode: string -> bytes 
        connectionSocket.send(response_header.encode())
        #Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError as e:
        #Send response message for file not found
        #Fill in start
        response_msg = "\n".join([
            "HTTP/1.1 404 Not Found", 
            "Content-Type: text/html",
            "\r\n",
            "Your file is not found >_<"
            ]) 

        connectionSocket.send(response_msg.encode())
        connectionSocket.send("\r\n".encode())
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
         #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
