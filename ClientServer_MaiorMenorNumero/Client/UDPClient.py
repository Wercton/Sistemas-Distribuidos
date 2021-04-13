import socket as sk


class Client:
    
    def __init__(self, port):
        self.c = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.c.connect((sk.gethostname(), port))
        self.enviar_numeros()
    
    def enviar_numeros(self):
        numeros = input("Digite três números: ")
        self.c.sendall(bytes(numeros, "utf-8"))
        msg = self.c.recv(1024)
        msg = msg.decode("utf-8")
        print(msg)

        self.c.close()


if __name__ == '__main__':
    port = 1241
    Client(port)