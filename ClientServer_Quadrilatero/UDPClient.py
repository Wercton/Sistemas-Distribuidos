import socket as sk
import pickle
from Quadrilatero import Quadrilatero


class Client(object):
    
    def __init__(self, port):
        self.c = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.c.connect((sk.gethostname(), port))
    
    def rodar_cliente(self):
        
        try:
            q = Quadrilatero()
            
            q.le_dados(*list(map(int, input("Digite os tamanhos de lado1 lado2 lado3 lado4: ").split())))
        
            object_string = pickle.dumps(q)
            self.c.send(object_string)
            
            while True:
                q = self.c.recv(4096)
                q = pickle.loads(q)
                q.mostra_dados()
                if q:
                    break
        except Exception as e:
            print(str(e))
            
        self.fechar_client()
    
    def fechar_client(self):
        self.c.close()
        
    def encerrar_server(self):
        self.c.sendall(bytes("4", "utf-8"))


