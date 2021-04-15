import socket as sk
import os.path
from os import path
import pathlib


# path_relativo = "ext4/Server/"
path_relativo = ""

try:
    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    s.bind((sk.gethostname(), 8081))
except sk.error as e:
    print(str(e))
    raise SystemExit(0)
s.listen(5)
estado_servidor =  True

def client_thread(clientsocket, addr):
    global estado_servidor, s
    
    print(f"Conexão com {addr} foi estabelecida.")
    
    while True:
        msg = clientsocket.recv(2048)
        msg = msg.decode("utf-8").split("|")
        
        if msg[0] == "1":
            filename = msg[2]
            print("FILENAME:", filename)
            file_data = clientsocket.recv(2048)
            with open(filename, 'wb') as file:
                file.write(file_data)
                print("Salvo com sucesso!")
                
        elif msg[0] == "2":
            filename = path_relativo + msg[1]
            try:
                with open(filename, 'rb') as file:
                    clientsocket.send(bytes("1", "utf-8"))
                    file_data = file.read(1024)
                    clientsocket.send(file_data)
                    print("\nArquivo enviado!")
            except IOError:
                clientsocket.send(bytes("-1", "utf-8"))
                
        elif msg[0] == "3":
            clientsocket.close()
            estado_servidor = False
            print("Servidor encerrando...")
            s.close()
            break


while estado_servidor:
    clientsocket, addr = s.accept()
    client_thread(clientsocket, addr)
