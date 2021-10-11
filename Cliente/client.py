import socket as ss
from random import randint
from pyautogui import alert
from threading import Thread
from Inteface.In_Python import chat_interface as chat
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from time import sleep

class Clientt(chat.Citrus_interface):

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
    def __init__(self):
        super().__init__()
        # Start Interface 
        self.show()

        # Client Var
        self.nop = ["\n", "_", "%", "$", "\n%", "#"]
        self.cliente = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.cliente.bind((ss.gethostname(), randint(50000, 60000)))
        self.cliente.connect((ss.gethostname(), 52577))

        self.my_name = input("Coloque seu nome ---> ")
        self.cliente.send(bytes(self.my_name, "utf-8"))
        
        self.rooms = dict()

        # Ver salas ativas
        Thread(target=self.ative_rooms).start()

        while True:
            querer = input("Conectar a uma sala (1) // Ver clientes ativos (2) // Criar sala (3) // Ver salas ativas (4) // Sair (5)\n---> ")
            if querer == "1":
                self.pedir_para_entrar()
            
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

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def ative_rooms(self):
        while True:
            sleep(3)
            self.cliente.send(bytes("all_rooms", "utf-8"))
            try:
                resposta = self.receber().split("\n")
                exist = [a for a in self.rooms.keys()]
                if resposta != exist:
                    self.atualizar_rooms_interface(resposta)
            except AttributeError:
                continue
            
    def atualizar_rooms_interface(self, nome):
        self.menu_list.clear()
        for element in nome:
            self.rooms[element] = QtWidgets.QListWidgetItem(element)
            self.rooms[element].setTextAlignment(QtCore.Qt.AlignHCenter)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.rooms[element].setFont(font)
            self.menu_list.addItem(self.rooms[element])
        print(self.rooms.keys())

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

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def ver_conexoes(self):
        self.cliente.send(bytes("envie_dicionario", "utf-8"))
        tratamento = self.receber()
        try:
            retorno = tratamento.split("\n")
            retorno.remove(self.my_name)
            return retorno
        except ValueError:
            pass

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def criar_room(self):
        while True:
            erro = False
            nop = ["\n", "_", "%", "$", "\n%", "#", "@"]

            room = [input("Coloque o nome da sala ---> "), input("senha da sala ---> ")]
            for element in nop:
                if element in room[0] or element in room[1]:
                    erro = True

            try:
                num = int(input("Quantas pessoas podem entrar na sala ---> "))
                room.append(str(num))
            except TypeError:
                print("Invalido!")
                erro = True
            
            if not erro:
                break
        self.cliente.send(bytes(f'criar\nsala\n\n%{"#%".join(room)}', "utf-8"))
        conferir = self.receber()
        if conferir == "Criado!":
            alert(conferir)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def pedir_para_entrar(self):
        nome_da_sala = input("Qual sala você quer entrar? ---> ")
        senha = input("Senha da sala ---> ")
        self.cliente.send(bytes(f"{nome_da_sala}\n#\n{senha}\n#\n", "utf-8"))
        resposta = self.receber()
        alert(resposta)
        if resposta == "entrou":
            self.chat = True
            Thread(target=self.send_menssages).start()
            self.receber_menssagens_room()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def send_menssages(self):
        print('Para sair da sala escreva "SAIR"!')
        while self.chat:
            menssagem = input("---> ")
            if menssagem == "SAIR":
                self.cliente.send(bytes("SAIR#", "utf-8"))
                self.chat = False
                break
            for element in self.nop:
                if element in menssagem:
                    print("Caracter invalido!")
                    continue
            if menssagem != "":
                self.cliente.send(bytes(f"{self.my_name}__{menssagem}__","utf-8"))

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def receber_menssagens_room(self):
        while self.chat:
            try:
                nome = self.cliente.recv(1024)
            except ConnectionResetError:
                break
            except ConnectionAbortedError:
                break
            if nome:
                menssagem = nome.decode("utf-8")
                if menssagem != "$" and not "\n%" in menssagem and "__" in menssagem:
                    receber = menssagem.split("__")
                    print(f"{receber[0]}: {receber[1]}")

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #


if __name__ == "__main__":
    while True:
        import sys
        try:
            app = QApplication(sys.argv)
            abc = Clientt()
            sys.exit(app.exec_())
        except AttributeError:
            continue