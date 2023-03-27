import codecs
import pickle
import socket
from time import sleep

from Crypto.Cipher import AES
from scapy.all import *

ClientSocket = socket.socket()
BS = 16
key = ''
iv = ''
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

def do_encrypt(data):
    message = codecs.encode(pickle.dumps(data), "base64").decode()
    obj = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
    padmsg = pad(message)
    ciphertext = obj.encrypt(padmsg.encode('utf-8'))
    return ciphertext

async def connect(host, port):
    print('Ожидание подключения...')
    try:
        ClientSocket.connect((host, port))
        Response = ClientSocket.recv(4096)
        print(Response.decode())
        return "0"
    except socket.error as e:
        return e
    
def chunks(lst, n):
    for i in range(0, len(lst), n): 
        yield lst[i:i+n]
    
def sendcheck(message, bytes):
    for chuck in chunks(message, bytes):
           ClientSocket.send(chuck)
           ClientSocket.recv(4096)
    ClientSocket.send(b'end')
    ClientSocket.recv(4096)
    
def Send(charters, disk, filename):
    try:
        filenameencrypt = do_encrypt(filename)
        sendcheck(filenameencrypt,10)
        sleep(1)

        chartersencrypt = do_encrypt(charters)
        sendcheck(chartersencrypt,10)
        sleep(1)
        
        diskencrypt = do_encrypt(disk)
        sendcheck(diskencrypt, 10)
        sleep(1)
        
        endencrypt = do_encrypt("END INFO")
        sendcheck(endencrypt, 10)
        sleep(1)
        print('Отправка данных произошла успешно!')
        ClientSocket.close()
        return True
    except Exception:
        print('Отправка данных завершилась с ошибкой')
        return False
        