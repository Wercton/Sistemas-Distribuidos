import socket as sk
import sys
from _thread import *


class Server:
    
    def __init__(self, port):
        self.s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
        self.s.bind((sk.gethostname(), port))
        self.estado_servidor = True
        self.rodar_server()
        
    def rodar_server(self):
        thread_count = 0
        
        self.s.listen(5)
        self.s.settimeout(1)
        
        while self.estado_servidor:
            try:
                clientsocket, address = self.s.accept()
                start_new_thread(self.client_thread, (clientsocket, address))
                thread_count += 1
                print("ThreadNumber:", thread_count)
            except sk.timeout:
                pass
            
        self.fechar_server()

    def maior_numero(self, numeros):
        
        numeros = list(map(int, numeros.split()))

        if numeros[0] < 0:
            return "O servidor será fechado."
        numeros = sorted(numeros)
        return f"{numeros[2]} é o maior número e {numeros[0]} é o menor número."

    def client_thread(self, clientsocket, address):
        
        print(f"Conexão com {address} foi estabelecida!")

        msg = clientsocket.recv(1024)
        msg = msg.decode("utf-8")
        print("Valores recebidos:", msg)
        
        msg = self.maior_numero(msg)
        clientsocket.send(bytes(msg, "utf-8"))
        
        print(f"Conexão com {address} foi encerrada!")
        clientsocket.close()
        
        if msg == "O servidor será fechado.":
            print("\nServer encerrado.")
            self.estado_servidor = False

    def fechar_server(self):
        print("\nServer encerrado.")
        self.s.close()
        
if __name__ == '__main__':
    port = 1241
    Server(port)