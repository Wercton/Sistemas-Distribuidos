import socket as sk
import sys
from Mercado import Mercado
from _thread import *

'''estado_servidor = True
thread_count = 0
mercado = Mercado()'''

class Server:
    
    def __init__(self, port):
        self.s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
        self.s.bind((sk.gethostname(), port))
        self.estado_servidor = True
        self.thread_count = 0
        self.mercado = Mercado()
        self.rodar_server()
        
    def rodar_server(self):
        self.s.listen(5)
        self.s.settimeout(1)
        
        while self.estado_servidor:
            try:
                clientsocket, address = self.s.accept()
                start_new_thread(self.client_thread, (clientsocket, address))
                self.thread_count += 1
            except sk.timeout:
                pass
            
        self.encerrar_server()
        

    def client_thread(self, clientsocket, address):
        
        print(f"Conexão com {address} foi estabelecida!")

        while True:
            enviar = True
            msg = clientsocket.recv(1024)
            msg = msg.decode("utf-8").split("|")
            
            if msg[0] == "1":
                msg = self.mercado.inserir_produto(msg[1])
            elif msg[0] == "2":
                msg = self.mercado.atualizar_produto(msg[1], int(msg[2]))
            elif msg[0] == "3":
                msg = self.mercado.listar_produtos()
            elif msg[0] == "terminar":
                self.estado_servidor = False
                clientsocket.close()
                break
            else:
                enviar = False

            if enviar:
                clientsocket.send(bytes(msg, "utf-8"))
    
    def encerrar_server(self):
        print("Server encerrado.")
        self.s.close()

if __name__ == '__main__':
    PORT = 1240
    Server(PORT)
