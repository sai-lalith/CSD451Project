import socket
import pickle

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
serverSocket.bind(("127.0.0.1",9090))

serverSocket.listen()

credit_details = []

while(True):

    (clientConnected, clientAddress) = serverSocket.accept()

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))

   

   # while(True) :

    #    dataFromClient = clientConnected.recv(1024).decode()
     #   x = dataFromClient.split()
      #  print(x)

       # if not dataFromClient :
        #    break

    # Acknowldegement to sever '''
    message = pickle.loads(clientConnected.recv(1024))


    clientConnected.send("received".encode())
    print(message)

