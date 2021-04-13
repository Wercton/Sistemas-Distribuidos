import socket as sk
import pickle
from _thread import *
from Quadrilatero import Quadrilatero


def main():
    
    s = abrir_server()
    estado_servidor = True
    thread_count = 0
    
    while estado_servidor:
        clientsocket, address = s.accept()
        start_new_thread(client_thread, (clientsocket, address))
        # client_thread(clientsocket, address)
        thread_count += 1
    
    s.close()


def abrir_server():
    
    try:
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.bind((sk.gethostname(), 1235))
    except sk.error as e:
        print(str(e))
        raise SystemExit(0)
    
    s.listen(5)
    return s


def client_thread(clientsocket, address):
    
    print(f"Conexão com {address} foi estabelecida!")

    objeto = clientsocket.recv(4096)
    objeto = pickle.loads(objeto)

    objeto.indica_tipo_quadrilatero()
    
    print("Indicando tipo do quadrilatero...")
    
    objeto = pickle.dumps(objeto)
    clientsocket.send(objeto)
    
    print(f"Retornado o objeto para {address}.\n")
    
    clientsocket.close()


if __name__ == '__main__':
    main()