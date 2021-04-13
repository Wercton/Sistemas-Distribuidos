import socket as sk
import sys
from _thread import *

estado_servidor = True
thread_count = 0


try:
    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
    s.bind((sk.gethostname(), 1241))
except sk.error as e:
    print(str(e))
    raise SystemExit(0)
s.listen(5)
s.settimeout(1)

def maior_numero(numeros):
    
    numeros = list(map(int, numeros.split()))

    if numeros[0] < 0:
        return "O servidor será fechado."
    numeros = sorted(numeros)
    return f"{numeros[2]} é o maior número e {numeros[0]} é o menor número."


def client_thread(clientsocket, address):
    global estado_servidor
    global s
    
    print(f"Conexão com {address} foi estabelecida!")

    msg = clientsocket.recv(1024)
    msg = msg.decode("utf-8")
    print("Valores recebidos:", msg)
    
    msg = maior_numero(msg)
    clientsocket.send(bytes(msg, "utf-8"))
    
    print(f"Conexão com {address} foi encerrada!")
    clientsocket.close()
    
    if msg == "O servidor será fechado.":
        print("\nServer encerrado.")
        estado_servidor = False


while estado_servidor:
    try:
        clientsocket, address = s.accept()
        start_new_thread(client_thread, (clientsocket, address))
        thread_count += 1
        print("ThreadNumber:", thread_count)
    except sk.timeout:
        pass
    
s.close()
