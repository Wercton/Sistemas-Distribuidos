import ftplib
import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
# wercton-Aspire-A515-51
# host = input("Digite o endereço do host: ")
host = "wercton-Aspire-A515-51"

try:
    s.connect((host, 8081))
except sk.error as e:
    print(str(e))
    raise SystemExit(0)


def receber_arquivo(msg):
    
    msg.append(input("\nDigite o nome do diretório/arquivo que deseja receber.\nEx.: dir1/test.txt\n"))
    s.sendall(bytes("|".join(msg), "utf-8"))
    
    msg = s.recv(16).decode("utf-8")
    
    if msg != "-1":
        msg = s.recv(2048)
        filename = (input("\nDigite o nome com o qual deseja salvar esse arquivo: "))
        with open(filename, 'wb') as file:
            file.write(msg)
            print("Salvo com sucesso!")
    else:
        print("\nArquivo não encontrado.")


def enviar_arquivo(msg):
    msg.append(input("\nDigite o nome do diretório/arquivo que deseja enviar.\nEx.: dir1/test.txt\n"))
    try:
        with open(msg[1], 'rb') as file:
            msg.append(input("\nDigite o nome de como deseja salvar o arquivo: "))
            s.sendall(bytes("|".join(msg), "utf-8"))
            file_data = file.read(1024)
            s.send(file_data)
            print("Enviado com sucesso!")
    except IOError:
        print("\nArquivo não encontrado.")


while True:
    aguardar = True
    msg = []
    msg.append(input("\nDigite (1) para enviar um arquivo para o server.\nDigite (2) para receber um arquivo do server.\nDigite (3) para encerrar a aplicação.\n"))
    if msg[0] == "1":
        enviar_arquivo(msg)
    elif msg[0] == "2":
        receber_arquivo(msg)
    elif msg[0] == "3":
        s.sendall(bytes("|".join(msg), "utf-8"))
        s.close()
        break
    else:
        print("Comando inválido.")

