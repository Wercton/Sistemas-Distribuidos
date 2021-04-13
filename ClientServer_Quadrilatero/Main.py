from UDPClient import Client
from UDPServer import Server

PORT = 1239


def main():
    while True:
        escolha = menu()
        print()
        if escolha == 1:
            try:
                s = Server(PORT)
                print("Server iniciado.")
                s.rodar_server()
            except Exception as e:
                print("Server já está aberto.")
        elif escolha == 2:
            c = Client(PORT)
            c.rodar_cliente()
        elif escolha == 3:
            try:
                s = Server(PORT)
                s.encerrar_server()
                print("Nenhum server aberto.")
            except Exception as e:
                c = Client(PORT)
                c.encerrar_server()
                print("Server encerrado.")
        elif escolha == 4:
            break
        else:
            print("Comando inválido.")
        print()


def menu():
    return int(input("(1) Abrir Server\n(2) Abrir Client\n(3) Fechar Server\n(4) Sair\n"))

if __name__ == '__main__':
    main()