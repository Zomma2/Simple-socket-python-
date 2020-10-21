import socket # import the socket library 
print('Waiting for client connections') # print address bound to the socket on the other end of the connection
host = ''        # Define host
port = 12345     # Choose an arbitrary port to connect to 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # intialize socket
s.bind((host, port)) #   Bind to our  port on our  interface

print (host , port) # print out interface and port 
s.listen(1) # start to listen to clients
conn, addr = s.accept() # Accept a connection. 
#The socket must be bound to an address and listening for connections. 
#The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection 
# addr is the address bound to the socket on the other end of the connection
print('Connected Suceesfully  by', addr) # print address bound to the socket on the other end of the connection
while True:

    try:
        data = conn.recv(1024) # Recieve data

        if not data: break # break if no data

        print ("Full name that was  sent by client : ",data.decode('utf-8')) # print full name recieved from client 
        st = str(data.decode('utf-8').split()[-1])#get the family/last name from the full name
        byt = st.encode() #encode the family name 
        conn.send(byt) # send the family name to the client 


    except Exception as e: # if an error is encountered
        print ("There was an error.") # print to user that there is an error 
        break #break from the loop 

print ("Connection is  successfully closed.") # print that connection is closed
conn.close() # close connection 