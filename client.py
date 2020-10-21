import socket # import the socket library 
no_exception = True
host = socket.gethostname()     # get hostname from socket and put it in host variable 
port = 12345                   # using the same port as the one used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# intialize socket
try :
	s.connect((host, port)) # Try connecting to the interface and port of the server 
except Exception as e: # if an error is encountered
    print ("There was an error , No server to connect to !!! , try running 'server.py' first.") # print to user that there is an error 
    no_exception = False 
if no_exception :
	st= input("Enter your name :") # Get the Full name from the user
	byt = st.encode() #encode the full name 
	s.send(byt) # send the full name to the server 
	data = s.recv(1024)# recieve data from the server
	s.close() #close the connection 
	print('Received from server Your Family name is  ', repr(data.decode('utf-8'))) # print data received from the server which is the family name 


