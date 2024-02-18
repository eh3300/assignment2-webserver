# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Listen for incoming connections
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Are you accepting connections?

        try:
            message = connectionSocket.recv(1024).decode()  # A client is sending you a message
            filename = message.split()[1]

            # Opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python.
            # How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], "rb")  # fill in start: open(filename[1:], "rb")

            # This variable can store the headers you want to send for any valid or invalid request.
            # What header should be sent for a response that is ok?
            # Content-Type is an example on how to send a header as bytes.
            # There are more!
            outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"

            # Note that a complete header must end with a blank line,
            # creating the four-byte sequence "\r\n\r\n"

            for i in f:  # for line in file
                # Append your html file contents
                outputdata += i

            # Send the content of the requested file to the client (don't forget the headers you created)!
            # Send everything as one send command, do not send one line/item at a time!

            # Send command start
            connectionSocket.send(outputdata)
            # Send command end

            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            # Remember the format you used in the try: block!
            # HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n
            # Start fill
            outputdata = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
            # End fill

            connectionSocket.send(outputdata)

            # Close client socket
            # Start fill
            connectionSocket.close()
            # End fill

  # Commenting out the below (some use it for local testing). It is not
  # required for Gradescope, and some students have moved it erroneously in
  # the While loop.
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE
  # GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
