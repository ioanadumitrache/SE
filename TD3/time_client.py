"""

@author Ioana Dumitrache

"""

import socket 
import threading 
 
 
tLock = threading.Lock() 
closed = False 
 
 
print "Introduissez 'esc' pour fermer le chat" 
 
 
def receving(name, sock): 
    while not closed: 
        try: 
            tLock.acquire() 
            while True: 
                data, addr = sock.recvfrom(1024) 
        except: 
            pass 
        finally: 
            tLock.release() 

 
host = socket.gethostname() 
port = 6666 
 
 
server = (host, port) 

 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.connect((host, port)) 
s.setblocking(0) 

 
recvT = threading.Thread(target=receving, args=("RecvThread",s)) 
recvT.start() 
 
 
s.sendto("Cet usager est entre dans la conversation",server) 
message = raw_input("Ecrivez: ") 
 
 
while message != 'esc': 
    if message != '': 
        s.sendto(message, server) 
    tLock.acquire() 
    message = raw_input("Ecrivez: ") 
    tLock.release() 

 
s.sendto("Cet usager s'est deconnecte",server) 

 
closed = True 
recvT.join() 
s.close() 
