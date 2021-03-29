"""
                    Scuffed Whatsapp Server v.04

                    @author : Rashed Alnuman

"""

try:

    import sys
    import socket
    import random
    import string
    import logging
    import threading
    from pyDes import *
    from datetime import datetime
 

except ImportError as IE:
    print(IE, "\n Missing modules to run whatsapp 2, please install the modules first then run")
    sys.exit(1)

# setting up logging and  using lambda to log


logging.basicConfig(filename='Msg.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
log = lambda msg : logging.info(msg)


clients = list()
users = dict()




def DEScrypt(msg, mod, key):

    """
    Uses Triple DES algorithm to encrypt string or bytes passed to function,
    mod defines whether to encrypt or decrypt and key is the key (obviously)
    to either encrypt or decrypt. if encryption is false meaning no encryption
    is required by the client-user then it will return a byte format of the
    original string
    """
    
    if encryption:  # dont encrypt or decrypt if encryption doesnt exist
        
      
        cipher = des(key, CBC, "\0\0\0\0\0\0\0\0", pad = None, padmode = PAD_PKCS5)

        if mod == 1:
            encrypted_data = cipher.encrypt(msg) 
            return encrypted_data
        

        elif mod == 2:
            decrypted_data = cipher.decrypt(msg)
            return decrypted_data

    else:
        return bytes(str(msg), "utf-8")





def chatSession(connection, address):

    with connection:

        connection.send( DEScrypt( private_key, 1, public_key)) # send private key to client
        connection.send( DEScrypt( "Enter your name: ", 1, private_key)) # request username from the user
        enc_username = connection.recv(1024)
        dec_username = DEScrypt( enc_username, 2, private_key)
        username = dec_username.decode("utf-8")

        try:
            while True:

                enc_msg = connection.recv(1024)
                dec_msg = DEScrypt(enc_msg, 2, private_key)
                msg     = dec_msg.decode("utf-8")
                
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                msg2 = current_time + ' - ' + username + ' : ' + msg
                
                logger(current_time + '  : ' + msg2) # logs what the user sent and the time
        
               
                for member in clients:
                    member.send( DEScrypt(msg2, 1, private_key))
                
        except:
            print("broblem")





def main():
    

    """
    Main function, static host, port and public key. Creates TCP socket object sock
    and binds to host,port tuple. after listening and connecting to a client, creates
    a connection thread and sends the client connection to that thread and gets ready
    to accept a new client. 
    """

    log("Server Started...")
   
    

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80)) 
    host = s.getsockname()[0]   # retrieve the IP of the server
    s.close()                   # close temporary socket
    
    port= 65432        # Listening on this specific port


    global public_key
    public_key = "1a2b3c4d"

    #server will send private key encrypted by the public key
    
    global private_key
    private_key = session_key = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 8))# generating a random 8 character session key


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        sock.bind((host, port))

        while True:
            
            print("Socket bounded succesffuly...")
            print("Awaiting connection...\n")
        
            sock.listen()
        
            connection, address = sock.accept() # when making multi threaded server, we will pass the connection
            msg = connection, " connected succesfully to the server"      # and address to the thread function and then wait for another 
            clients.append(connection)          # add ip of client to the client list
        
       
            socket_thread = threading.Thread(target = chatSession, args=(connection, address,))
            msg = "connected ", connection, " to the chat session"
            socket_thread.start()
            


     
main()
