import socket as ss
from threading import Thread
from pyautogui import alert
from time import sleep


class Servidor:
    def __init__(self):
        self.conect = dict()
        self.server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.server.bind((ss.gethostname(), 34345))
        self.server.listen(5)
        self.rooms = dict()

        Thread(target=self.testando).start()

        while True:
            obj_client, dress = self.server.accept()
            nome_do_cliente = self.receber(obj_client)
            self.conect[nome_do_cliente] = [obj_client, dress[0]]
            Thread(target=self.menu_do_server, args=[obj_client, ]).start()

    @staticmethod
    def receber(qm):
        while True:
            try:
                nome = qm.recv(10000)
            except ConnectionResetError:
                break
            except ConnectionAbortedError:
                break
            if nome:
                return nome.decode("utf-8")

    def testando(self):
        while True:
            if len(self.conect) != 0:
                try:
                    for key_conectados, conectados in self.conect.items():
                        try:
                            conectados[0].send(bytes("$", "utf-8"))
                            sleep(1.5)
                            print(f"{len(self.conect)} clientes estão conectadas em mim!")
                        except Exception:
                            del self.conect[key_conectados]
                            alert(f"O cliente {key_conectados} foi desconectado!")
                except RuntimeError:
                    continue
            else:
                print("Não há clientes conectados!")
                sleep(1.5)

    def menu_do_server(self, cliente):
        while True:
            ordem = self.receber(cliente)

            if ordem == "envie_dicionario":
                clientes = "\n".join([a for a in self.conect.keys()])
                cliente.send(bytes(f"\n%{clientes}", "utf-8"))
            
            elif "criar\nsala\n\n%" in ordem:
                code = ordem.split("criar\nsala\n\n%")[1]
                code = code.split("#%")
                print(code)
                self.rooms[code[0]] = [code[1], int(code[2]), [cliente]]
                cliente.send(bytes("\n%Criado!","utf-8"))




            if ordem == "chatzinho":
                pass

Servidor()
