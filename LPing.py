import socket
import click
import time
import sys


from six.moves import zip_longest
from timeit import default_timer as timer
from collections import namedtuple
from six import print_
from functools import partial
from six import print_
from prettytable import PrettyTable




def ping ():
    O0O0000O0000OOO00 = namedtuple('Estadisticas',['IP','Puerto','Transmitidos','Perdidos','Uptime','Minimo','Maximo','Promedio'])
    O00O00O0O00O0OOOO = partial(print_ ,flush =True )
    def OOOOOO0O00O000O0O (x ):
        return sum (x )/float (len (x ))
    class O00000O000000000O (object ):
        def __init__ (self ,family ,type_ ,timeout ):
            OOO00000OOO0OO0O0 =socket .socket (family ,type_ )
            OOO00000OOO0OO0O0 .settimeout (timeout )
            self ._s =OOO00000OOO0OO0O0
        def connect (self ,host ,OO0OOOOOO000OO000 =25565 ):
            self ._s .connect ((host ,int (OO0OOOOOO000OO000 )))
        def shutdown (self ):
            self ._s .shutdown (socket .SHUT_RD )
        def close (self ):
            self ._s .close ()
    class O00O0OO0OO00O0OO0 (object ):
        def __init__ (self ):
            self .table_field_names =[]
            self .rows =[]
        @property
        def raw (self ):
            OO0000O000OOOO0OO =[]
            for OOO0OOO0OO00OOOOO in self .rows :
                OOO00O0O0O000OOO0 =OOO0OOO0OO00OOOOO .successed +OOO0OOO0OO00OOOOO .failed
                OO000OOOO00O00OOO ='\n--- {}[:{}] Estadisticas ---'.format (OOO0OOO0OO00OOOOO .host ,OOO0OOO0OO00OOOOO .port )
                O00O0O0000OO0OOO0 ='\n{} conexiones, {} transmitidos, {} perdidos, {} uptime'.format (OOO00O0O0O000OOO0 ,OOO0OOO0OO00OOOOO .successed ,OOO0OOO0OO00OOOOO .failed ,OOO0OOO0OO00OOOOO .success_rate )
                OOO000O00O000000O ='\nminimo = {}, maximo = {}, promedio = {}'.format (OOO0OOO0OO00OOOOO .minimum ,OOO0OOO0OO00OOOOO .maximum ,OOO0OOO0OO00OOOOO .average )
                O00OOOOO0O0OO000O =OO000OOOO00O00OOO +O00O0O0000OO0OOO0 +OOO000O00O000000O
                OO0000O000OOOO0OO .append (O00OOOOO0O0OO000O )
            return ''.join (OO0000O000OOOO0OO )
        @property
        def table (self ):
            O0OOOOO0000000O00 =PrettyTable ()
            O0OOOOO0000000O00 .field_names =self .table_field_names
            for OOOOO0OOO0O0O00O0 in self .rows :
                O0OOOOO0000000O00 .add_row (OOOOO0OOO0O0O00O0 )
            return '\n'+O0OOOOO0000000O00 .get_string ()
        def set_table_field_names (self ,field_names ):
            self .table_field_names =field_names
        def add_statistics (self ,row ):
            self .rows .append (row )
    class O0000O0OOO00000OO (object ):
        def __init__ (self ):
            self ._start =0
            self ._stop =0
        def start (self ):
            self ._start =timer ()
        def stop (self ):
            self ._stop =timer ()
        def cost (self ,funcs ,args ):
            self .start ()
            for OOO0OOO000OO0OO00 ,OOO0OO00OOO00OO00 in zip_longest (funcs ,args ):
                if OOO0OO00OOO00OO00 :
                    OOO0OOO000OO0OO00 (*OOO0OO00OOO00OO00 )
                else :
                    OOO0OOO000OO0OO00 ()
            self .stop ()
            return self ._stop -self ._start
    class O00O00OOO00OOOOO0 (object ):
        def __init__ (self ,host ,O0OOOO0000OOO00OO =25565 ,O000O0OOOO00OOO00 =1 ):
            self .print_ =O00O0OO0OO00O0OO0 ()
            self .timer =O0000O0OOO00000OO ()
            self ._successed =0
            self ._failed =0
            self ._conn_times =[]
            self ._host =host
            self ._port =O0OOOO0000OOO00OO
            self ._timeout =O000O0OOOO00OOO00
            self .print_ .set_table_field_names (['IP','Puerto','Transmitidos','Paquetes Perdidos','Uptime','Minimo','Maximo','Promedio'])
        def _create_socket (self ,family ,type_ ):
            return O00000O000000000O (family ,type_ ,self ._timeout )
        def _success_rate (self ):
            OOOO0000OOOOO0000 =self ._successed +self ._failed
            try :
                OOO00O00O0O0OOOOO =(float (self ._successed )/OOOO0000OOOOO0000 )*100
                OOO00O00O0O0OOOOO ='{0:.2f}'.format (OOO00O00O0O0OOOOO )
            except ZeroDivisionError :
                OOO00O00O0O0OOOOO ='0.00'
            return OOO00O00O0O0OOOOO
        def statistics (self ,n ):
            OOOO0OO00OO000O0O =self ._conn_times if self ._conn_times !=[]else [0 ]
            O0OO0000O0O000O00 ='{0:.2f}ms'.format (min (OOOO0OO00OO000O0O ))
            OOOOO0OOO000OO0O0 ='{0:.2f}ms'.format (max (OOOO0OO00OO000O0O ))
            O0OO0000000O00O00 ='{0:.2f}ms'.format (OOOOOO0O00O000O0O (OOOO0OO00OO000O0O ))
            OOOOOOO000OOO00OO =self ._success_rate ()+'%'
            self .print_ .add_statistics (O0O0000O0000OOO00 (self ._host ,self ._port ,self ._successed ,self ._failed ,OOOOOOO000OOO00OO ,O0OO0000O0O000O00 ,OOOOO0OOO000OO0O0 ,O0OO0000000O00O00 ))
        @property
        def result (self ):
            return self .print_
        @property
        def status (self ):
            return self ._successed ==0
        def ping (self ,OO0000000OO0OO00O =10 ):
            for OO0O0OO0O00OO0OO0 in range (1 ,OO0000000OO0OO00O +1 ):
                OO0O00O000O00O00O =self ._create_socket (socket .AF_INET ,socket .SOCK_STREAM )
                try :
                    time .sleep (1 )
                    O0OOO000O0O0OOOO0 =self .timer .cost ((OO0O00O000O00O00O .connect ,OO0O00O000O00O00O .shutdown ),((self ._host ,self ._port ),None ))
                    OO00000O000O0O0OO =1000 *(O0OOO000O0O0OOOO0 )
                    O00O00O0O00O0OOOO ("[LPing] %s[:%s]: seq=%d tiempo=%.2f ms"%(self ._host ,self ._port ,OO0O0OO0O00OO0OO0 ,OO00000O000O0O0OO ))
                    self ._conn_times .append (OO00000O000O0O0OO )
                except socket .timeout :
                    O00O00O0O00O0OOOO ("[LPing] %s[:%s]: seq=%d Paquete Perdido!"%(self ._host ,self ._port ,OO0O0OO0O00OO0OO0 ))
                    self ._failed +=1
                except KeyboardInterrupt :
                    self .statistics (OO0O0OO0O00OO0OO0 -1 )
                    raise KeyboardInterrupt ()
                else :
                    self ._successed +=1
                finally :
                    OO0O00O000O00O00O .close ()
            self .statistics (OO0O0OO0O00OO0OO0 )
    @click .command ()
    @click .option ('--port','-p',default =25565 ,type =click .INT ,help ='Puerto')
    @click .option ('--count','-c',default =10 ,type =click .INT ,help ='Numero de conexiones')
    @click .option ('--timeout','-t',default =1 ,type =click .FLOAT ,help ='Tiempo de espera')
    @click .option ('--report/--no-report',default =True ,help ='Genera tabla con los datos')
    @click .argument ('host')
    def OO0O000O0O000OOOO (host ,port ,count ,timeout ,report ):
        O00OOO0O0O0OO0OOO =O00O00OOO00OOOOO0 (host ,port ,timeout )
        try :
            O00OOO0O0O0OO0OOO .ping (count )
        except KeyboardInterrupt :
            pass
        if report :
            O00O00O0O00O0OOOO (O00OOO0O0O0OO0OOO .result .table )
        else :
            O00O00O0O00O0OOOO (O00OOO0O0O0OO0OOO .result .raw )
        sys .exit (O00OOO0O0O0OO0OOO .status )
    if __name__ =='__main__':
        OO0O000O0O000OOOO ()
        
ping()
