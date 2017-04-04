"""

@author Ioana Dumitrache

"""

import socket 
import time 

 
host = socket.gethostname() 
port = 6666 

 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
serversocket.bind((host,port)) 
serversocket.setblocking(0) 

 
print "Le serveur est allume" 

 
while True: 
    try: 
        data, addr = serversocket.recvfrom(1024)  # primeste maxim 1024 bytes 
             
        print time.ctime(time.time()) + str(addr) + ": " + str(data) 
    except: 
        pass 
    serversocket.close() 
