# Jorge Angel Valdez Tristan 1957496 
#Parte1
import sys
import threading
from socket import *

#Parte2
def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result = 0:
        print("Opened Port:", port)
#Parte3 se genera la funcion main junto con sus variables 

if __name__='__main__':
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
    #Parte4

    start_port = int(portstrs[0])
    end_port = int(portstrs[1])
    #Parte5 se obtiene la direcion ip y se almacena en la variable 
    target_ip = gethostbyname(host)

    #Parte 6  bucle for 
    hilos = []
    for port in range(start_port, end_port):
        hilo = threading.Tread(target=tcp_testm args=(port,))
        hilos.append(hilo)
        hilo.start()