import socket as sk


class Client:
    
    def __init__(self, port):
        self.c = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.c.connect((sk.gethostname(), port))
        self.enviar = True
        self.rodar_client()
        
    def rodar_client(self):
        
        while True:
            
            msg = []
            self.enviar = True
            comando = input("\n(1) Cadastrar produto no estoque\n(2) Atualizar estoque\n(3) Listar estoque\n(4) Sair\nDigite 'terminar' para encerrar o servidor\n")
            msg.append(comando)
            
            if comando == "1":
                self.entrada_estoque(msg)
            elif comando == "2":
                self.atualizar_estoque(msg)
            elif comando == "3":
                self.listar_estoque(msg)
            elif comando == "4":
                break
            elif comando == "terminar":
                self.terminar(msg)
                break
            else:
                self.comando_invalido()
            
            if self.enviar:
                msg = self.c.recv(1024)
                msg = msg.decode("utf-8")
                print(chr(27) + "[2J")
                print(msg)
                
        self.fechar_client()
    
    def entrada_estoque(self, msg):
        msg.append(input("Digite o nome do produto: "))
        self.c.sendall(bytes("|".join(msg), "utf-8"))
    
    def atualizar_estoque(self, msg):
        msg.append(input("Digite o nome do produto: "))
        msg.append(input("Digite a quantidade a ser inserida ou retirada: "))
        self.c.sendall(bytes("|".join(msg), "utf-8"))
    
    def listar_estoque(self, msg):
        self.c.sendall(bytes("|".join(msg), "utf-8"))
    
    def terminar(self, msg):
        self.c.sendall(bytes("|".join(msg), "utf-8"))
        print("Server será encerrado.")
        
    def comando_invalido(self):
        self.enviar = False
        print(chr(27) + "[2J")
        print("Comando não identificado.")
    
    def fechar_client(self):
        self.c.close()

if __name__ == '__main__':
    PORT = 1240
    Client(PORT)
