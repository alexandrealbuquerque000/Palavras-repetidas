
import time
import sys
import os
from termcolor import*
import colorama

#Função para ler apenas letras:
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif
        

def initshow():
    print()
    print("-"*18)
    print("  Busca Palavras")
    print("-"*18)


def options():
    o=str("Deseja importar um arquivo (.txt) da sua área de trabalho ou prefere escrever um texto? ")
    o=leiastr(o)
    if "im" in o or "arq" in o:
        while True:
            print()
            k=str(input("Insira o nome do arquivo desejado: "))
            k=k.lower()
            try:
                a=open( k+".txt", "rt")
            except (FileNotFoundError):
                print()
                print("Esse arquivo não existe.\n\nTente novamente.")
                continue
            else:
                break
        try:
            a=a.read()
        except (UnicodeDecodeError):
            print()
            print("Esse arquivo possui codificações não suportadas.")
            print()
            print("O programa será reiniciado.")
            time.sleep(3)
            os.system("cls")
            return 1
        else:
            pass         
    else:
        print()
        a=str(input("Insira o texto aqui:"))
        pass 

    return a


def search():
    a=options()
    if a==1:
        return 1
    z=str("Deseja ignorar letras maiúsculas e minúsculas? ")
    z=leiastr(z)
    e='s'
    while "s" in e:
        print()
        b=input("Insira a palavra que deseja achar:")
        if "s" in z:
            a=a.lower()
            b=b.lower()
        else:
            pass
        c=a.find(str(b))
        d=a.count (str(b))
        if d >1:
            print()
            print("Existem",int(d), "palavras (",b,") nesse texto.")
            print()
            print("Essas são as suas posições:")
        elif  d ==1:
            print()
            print("Existe",int(d), "palavra (",b,") nesse texto.")
            print()
            print("Essa é a sua posição:")
        else:
            print()
            print("Esta palavra não está presente nesse texto")
        while c!=-1:
            print(' '+str(c))
            c=a.find( str(b), c+1)
        e=str("Deseja procurar por outra palavra? ")
        e=leiastr(e)
        bq=colored(str(b), 'red')
        a=(a.replace( str(b) , str(bq)))
        continue
    else:
        j=str("Deseja mostrar o seu texto? ")
        j=leiastr(j)
        if "s" in j:
            bq=colored(str(b), 'red')
            print()
            print("Aqui está:")
            print()
            print(a.replace( str(b) , str(bq)) )
        else:
            print()
            print("Tudo bem!")


def finish():
    f=str("Deseja reiniciar o programa? ")
    f=leiastr(f)
    if 's' in f:
        os.system("cls")
    return f


def run():
    os.system('color')
    f='s'
    while "s" in f:
        initshow()
        if search()==1:
            continue
        f=finish()
    input("\nObrigado(a) por usar o nosso programa! ;)")


run()
    
