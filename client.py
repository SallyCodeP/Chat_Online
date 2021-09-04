import socket as ss
from random import randint
from pyautogui import alert

class Clientt:
    def __init__(self):
        self.cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.cliente.bind((ss.gethostname(), randint(50000, 60000)))
        self.cliente.connect((ss.gethostname(), 34345))
        
        self.my_name = input("Coloque seu nome ---> ")
        self.cliente.send(bytes(self.my_name, "utf-8"))
        
        while True:
            querer = input("Conectar a uma sala (1) // Ver clientes ativos (2) // Criar sala (3) // Ver salas ativas (4) // Sair (5)\n---> ")
            if querer == "1":
                pass
            
            elif querer == "2":
                conectados = self.ver_conexoes()
                print("-="*30)
                if len(conectados) == 0:
                    print("Apenas você está online!")
                else:
                    print(conectados)
                print("-=" * 30)
            
            elif querer == "3":
                self.criar_room()

            elif querer == "4":
                pass

            elif querer == "5":
                self.cliente.close()
                break
    
    def receber(self):
        while True:
            try:
                nome = self.cliente.recv(1024)
            except ConnectionResetError:
                break
            except ConnectionAbortedError:
                break
            if nome:
                menssagem = nome.decode("utf-8")
                if menssagem != "$" and "\n%" in menssagem:
                    return menssagem.split("\n%")[1]

    def ver_conexoes(self):
        self.cliente.send(bytes("envie_dicionario", "utf-8"))
        tratamento = self.receber()
        try:
            retorno = tratamento.split("\n")
            retorno.remove(self.my_name)
            return retorno
        except ValueError:
            pass

    def criar_room(self):
        while True:
            erro = False
            nop = ["\n", "_", "%", "$", "\n%", "#"]

            room = [input("Coloque o nome da sala ---> "), input("senha da sala ---> ")]
            for element in nop:
                if element in room[0] or element in room[1]:
                    erro = True

            try:
                num = int(input("Quantas pessoas podem entrar na sala ---> "))
                room.append(str(num))
            except TypeError:
                print("Invalido!")
                continue
            
            if not erro:
                break
        self.cliente.send(bytes(f'criar\nsala\n\n%{"#%".join(room)}', "utf-8"))
        conferir = self.receber()
        if conferir == "Criado!":
            alert(conferir)
            # agora a gente vai fazer as funções de um cliente que está conectado em uma room UwU
            
        
        
            



Clientt()
