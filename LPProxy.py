#Archivo Proxy.txt


import asyncio, os, colorama
from proxybroker import Broker
from colorama import *


async def save(proxies, filename):
    with open(filename, 'w+') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            proto = 'https' if 'HTTPS' in proxy.types else 'http'
            row = '%s:%d\n' % (proxy.host, proxy.port)
            f.write(row)
            print(Fore.WHITE + "[LPProxies] HTTP(s) Proxy Agregada! " + Fore.GREEN + str(proxy))

		
def main():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], limit= 99999),
                           save(proxies, filename='proxy.txt'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


if __name__ == '__main__':
    print("  - HTTP Proxy Gathering -  ")
    print("     CTRL + C To STOP       ")
    print("     File = proxy.txt       ")
    main()
