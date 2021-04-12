from urllib.request import Request, urlopen
from _thread import *


texto_final = ""
numero_thread = 0


with open("palavras.txt", "r") as file:
    palavras = []
    lines = file.readlines()
    for line in lines:
        palavras.append(line.strip())


def main():
    global numero_thread
    
    numero_url = int(input("Digite o número máximo de urls a serem pesquisadas: "))
    numero_thread_max = int(input("Digite o número máximo de Threads a serem criadas de uma vez: "))

    with open("urls.txt", "r") as file:
        lines = file.readlines()
        if len(lines) < numero_url:
            numero_url = len(lines)
            
        for i in range(numero_url):
            line = lines[i]
            start_new_thread(abrindo_thread, (line.split(),))
            numero_thread += 1
            while True:
                if numero_thread < numero_thread_max:
                    break
        
        while True:
            if not numero_thread:
                break
            
    with open("resultado.txt", "w") as file:
        file.write(texto_final)


def abrindo_thread(url):
    
    global texto_final, numero_thread
    
    print("\nPesquisando", url[0])
    
    req = Request(url[0], headers={'User-Agent': 'Mozilla/5.0'})
    texto = url[0] + "\n"
    
    for palavra in palavras:
        qtd = 0
        content = urlopen(req).read()
        content = str(content)
        while True:
            posicao = int(content.find(palavra))
            if posicao == -1:
                break
            else:
                qtd += 1
                content = content[posicao+1:]
        texto += f"{palavra}: {qtd}\n"
    texto += "\n"
    
    texto_final += texto
    numero_thread -= 1
    
    print("\nFinalizada pesquisa em", url[0])
 
    
if __name__ == '__main__':
    main()
