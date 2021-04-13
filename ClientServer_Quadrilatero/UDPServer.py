import socket as sk
import pickle
from _thread import *
from Quadrilatero import Quadrilatero


class Server:
    
    def __init__(self, port):
        self.s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
        self.s.bind((sk.gethostname(), port))
        self.estado_servidor = True
        self.thread_count = 0
        
    def rodar_server(self):
        self.s.listen(5)
        self.s.settimeout(1)
        
        while self.estado_servidor:
            try:
                clientsocket, address = self.s.accept()
                start_new_thread(self.client_thread, (clientsocket, address))
                # self.client_thread(clientsocket, address)
                self.thread_count += 1
            except sk.timeout:
                pass
        
        self.fechar_server()
    
    def client_thread(self, clientsocket, address):
        
        # print(f"Conexão com {address} foi estabelecida!")

        objeto = clientsocket.recv(4096)
        
        try:
            if objeto.decode('utf-8') == '4':
                self.estado_servidor = False
        except Exception as _:
            print(f"Conexão com {address} foi estabelecida!")
            
            objeto = pickle.loads(objeto)

            objeto.indica_tipo_quadrilatero()
            
            print("Indicando tipo do quadrilatero...")
            
            objeto = pickle.dumps(objeto)
            clientsocket.send(objeto)
            
            print(f"Retornado o objeto para {address}.\n")
        
        clientsocket.close()
    
    def fechar_server(self):
        print("Server encerrado.")
        self.s.close()
        
