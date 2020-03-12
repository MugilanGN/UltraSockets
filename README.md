# UltraSockets
Quasi-Application layer protocol to provide fast and light communication between devices on (W)LAN. It's built to facilitate "casual" data transfer between devices such as laptops and microcontrollers. It is easier and faster to develop compared to TCP, while not having as high of an overhead and baggage as HTTP.

## Features:

####   1. Full-duplex communication with fully-automated threading to enable it

####   2. Supports efficient multiple client-client communication

####   3. Adds Asynchronous Transmission to preserve data integrity

####   4. Has a user-friendly handshake layer which can be modified to provide encryption and compression

# Documentation

This is a very brief documentation of UltraSockets. The package was meant to be easy to use and understand from the very beginning, so this hopefully shouldn't be too confusing. Most of the technical details of TCP should be taken care of, so that even for beginners the package can be usable

## The Client
This is the individual unit of the UltraSockets system. It is a computer which is connected to the communications network.

### client = Client(hostname,name)
Hostname will be the IP of the host/server and the port. "192.168.x.xxx:8000" for example, where 8000 is the port.

Name is the name given to the client. This is just a string like "PC2" which is used to refer to the client when messages are sent.

### client.get(num)
Num can be the number of messages that you want to retrieve from the Queue which contains all the messages recieved so far. If no messages are present, it returns None. It operates as First In, Last Out. It will return a list like so:

[ [ name_of_sender , message , message_serial_number ] , [...] , ... ]

Num can also be "all" which will return a list of all the messages that have been recieved

### client.send(name, message)
The name is the name of the recipient who the messsage is going to be sent to,

Message is the message itself which is going to be transmitted. It can be any data type

### client.close()
It will temporarily close the thread which is used for recieving messages. This means the client can no longer recieve messages. One use case is when an intensive task is being performed, so the client wants to only have the main thread running to maximize efficiency

### client.open()
It will reopen the message collecting thread that has been closed. Now the client can recieve messages again.

### client.terminate()
This will permanently close the message recieving thread. It lets the client cleanly exit out of the network after they are done.

## The Server
The Server object is the host computer. However, it is not really a "host" anymore due to the message routing that takes place under UltraSockets. While it is a server at a technical level, the user will not be able to tell the difference between it, and any other client.

### server = Server(hostname,connections,name)
This will create the server object.

Hostname will be the IP of the host and the port. In this case the server is the host, so your own IP address will be entered as a string."192.168.x.xxx:8000" for example, where 8000 is the port.

Port is the port on which communications will take place. It will be a number like 8000.

Connections is the number of connections supported by the server. It is the number of clients that can connect to the server. This must be exactly equal to the number of clients that will join - no more or no less.

Name is the name given to the server computer. This is just a string like "PC1" which is used to refer to the server

### server.send(name, message)
The name is the name of the recipient who the messsage is going to be sent to,

Message is the message itself which is going to be transmitted. It can be any data type

### server.get(num)
Num can be the number of messages that you want to retrieve from the Queue which contains all the messages recieved so far. If no messages are present, it returns None. It operates as First In, Last Out. It will return a list like so:

[ [ name_of_sender , message , message_serial_number ] , [...] , ... ]

Num can also be "all" which will return a list of all the messages that have been recieved
