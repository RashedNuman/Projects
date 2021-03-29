"""
                    Scuffed Whatsapp Client v.04

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


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myIP = s.getsockname()[0]
    s.close()

    port = 65432
    host = "192.168.0."

    #Dynamically looks for the server on the network

    for octet in range(254, 2, -1): #starts from higher IP to lower
                                    #Since most IP have high 4th octets
        host += str(octet)
        print(host)

        try:
        
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock.connect((host, port))
                print("I have connected")
                break
            
        except socket.timeout:
            host = host[:-len(str(octet))]
            if octet == 2:
                print("Finished scanning")
            else:
                print("Not this Ip checking next")
                continue
    print("ELLO")
    
main()
