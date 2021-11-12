
import socket
import pickle

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("127.0.0.1",9090))

amount = input("Enter the amount: ")
ccn = input("Enter your credit card number: ")
cvv = input("Please enter your cvv: ")

l = [amount,ccn,cvv]

#for i in range(len(l)):
 #   clientSocket.send(l[i].encode())
datasent = pickle.dumps(l)
clientSocket.send(datasent)  
    
print(l)

dataFromServer = clientSocket.recv(1024)

print(dataFromServer.decode())

 

 