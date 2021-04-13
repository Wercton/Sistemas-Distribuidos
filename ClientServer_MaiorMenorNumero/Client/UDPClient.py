import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

try:
    s.connect((sk.gethostname(), 1241))
except sk.error as e:
    print(str(e))
    raise SystemExit


numeros = input("Digite três números: ")
s.sendall(bytes(numeros, "utf-8"))
msg = s.recv(1024)
msg = msg.decode("utf-8")
print(msg)

s.close()
