import socket as sk
import pickle
from Quadrilatero import Quadrilatero


def main():
    
    s = abrir_cliente()
    q = Quadrilatero()
    
    q.le_dados(*list(map(int, input("Digite os tamanhos de lado1 lado2 lado3: ").split())))
    
    
    object_string = pickle.dumps(q)
    s.send(object_string)
    
    while True:
        q = s.recv(4096)
        q = pickle.loads(q)
        q.mostra_dados()
        if q:
            break

    s.close()


def abrir_cliente():
    
    s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    try:
        s.connect((sk.gethostname(), 1235))
    except sk.error as e:
        print(str(e))
        raise SystemExit
    
    return s



if __name__ == '__main__':
    main()
