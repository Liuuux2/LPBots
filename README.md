# LPBots
LPBotting Service (Fork of Gravy)

## ¿De qué va este proyecto?
Este proyecto fue principalmente originado para poder hacer testeos de seguridad en LatinPlay
Al utilizar esta herramienta, aceptas las condiciones:

1. Útilizar esta herramienta UNICAMENTE en donde te sea permitido, no nos hacemos responsables de tus actos.
2. No comercializar esta herramienta, ya que es gratuita.

Herramienta por GhostyCeh *(Got code from Gravy > https://github.com/Armax/Gravy) // (BETA, Será actualizada con el tiempo)

## ¿Cómo instalar?

Es tan facil como únicamente hacer **git clone** al repositorio y ejecutarla.

* `git clone https://github.com/GhostyCeh/LPBots`
* `cd LPTool`
* `sudo python install.py`

## ¿Cómo utilizar?

Es tan facil como únicamente **ejecutar** LPTool.py.

* `sudo python LPTool.py`

## Documentacion - 

En el archivo 'botlib.py' puedes observar diferentes "metodos" o exploits, puedes quitar el comentario a cada linea para activar
cada una de sus funciones, ESTOS EXPLOITS YA FUERON PARCHEADOS POR FLAMECORD, Sin embargo, se intentara replicar cada exploit que aparezca de servicios como mcspam.tech

La potencia de la herramienta varia en las proxies vivas que poseas, y los threads que utilizes, Ya que esta herramienta es gratuita, por favor utilizar con responsabilidad, no apoyamos de ninguna forma la extorsion ni usos maliciosos.

La herramienta posee un mini proxy gather utilizando el modulo ProxyBroker, utilizalo ejecutando 
> python3 LPProxies/LPProxy.py

## Hay metodos como 
* `Destroyer Method (MCStorm) - Pinguea ilimitadamente el servidor`
* `Invalid Trash - Manda paquetes invalidos`
* `Invalid EncryptionResponseEvent - Altera el packetID durante el proceso de encriptacion de paquetes`
* `Are mods in use? - Paquetes con ID invalida cual causa mayor uso de CPU en el decoder`
* `Creative Drop - Tira items del creativo`
* `Chat Flood - Spamea mensajes`
* `Reconnect Flood - Inicia conexion y la termina y repite` 
* `Packet Flood - Manda paquetes en loop`
* `NBT Exploit - Utiliza exploits como Jessica`
* `TimeOut triggering - Inicia conexion pero no la termina (TCP-Starvation or Slowloris)`
* `Comunes - Llena el servidor de bots`

## Tambien contiene -
* `Port pinguer - Pinguea puerto TCP`
* `Scanner - Utiliza comandos de NMAP`
* `HTTP Flood - Para el exploit de bungeecord o saturar paginas`
* `SMS Bomber - Para el pais US`

Fin de la documentacion
