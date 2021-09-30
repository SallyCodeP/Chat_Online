import socket as ss
from threading import Thread
from pyautogui import alert
from time import sleep


class Servidor:

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def __init__(self):

        # Informação clientes (Objeto socket, IP)
        self.conect = dict()

        # Informação chat rooms
        self.rooms = dict()

        # Configuração inicial server
        self.server = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        self.server.bind((ss.gethostname(), 52577))
        self.server.listen(5)
        
        # Iniciando teste de conexão com clientes
        Thread(target=self.testando).start()
        
        # Conectando e configurando clientes
        self.conex()

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #    

    def conex(self) -> None:
        '''
        -Inicia conexão e configura clientes conectados\n
        -Inicializa em Thread função de comunicação server/cliente em requests\n
        '''
        while True:
            obj_client, dress = self.server.accept()
            nome_do_cliente = self.receber(obj_client)
            self.conect[nome_do_cliente] = [obj_client, dress[0]]
            Thread(target=self.menu_do_server, args=[obj_client, ]).start()
            print(self.conect)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    @staticmethod
    def receber(qm) -> str:
        '''
        qm -> Objeto socket\n
        Recebe, descriptografa (utf-8) e retorna pacote de informações do cliente para o servidor
        '''
        while True:
            try:
                nome = qm.recv(10000)
            except ConnectionResetError:
                break
            except ConnectionAbortedError:
                break
            if nome:
                return nome.decode("utf-8")

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def testando(self) -> None:
        '''
        Para cada cliente registrado como conectado no server é enviado bytes para testar a conexão do cliente\n
        Caso o cliente não receba o pacote de Bytes enviado, ele é desconectado do servidor
        '''
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

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def menu_do_server(self, cliente) -> None:
        while True:
            ordem = self.receber(cliente)

            if ordem == "envie_dicionario":
                clientes = "\n".join([a for a in self.conect.keys()])
                cliente.send(bytes(f"\n%{clientes}", "utf-8"))
            
            elif "criar\nsala\n\n%" in ordem:
                code = ordem.split("criar\nsala\n\n%")[1]
                code = code.split("#%")
                self.rooms[code[0]] = [code[1], int(code[2]), []]
                print(self.rooms)
                cliente.send(bytes("\n%Criado!","utf-8"))

            elif "\n#\n" in ordem:
                info = ordem.split("\n#\n")
                try:
                    if len(self.rooms[info[0]][2]) < self.rooms[info[0]][1]:
                        if info[1] == self.rooms[info[0]][0]:
                            self.rooms[info[0]][2].append(cliente)
                            cliente.send(bytes("\n%entrou","utf-8"))
                            self.receber_enviar(info[0], cliente)

                        else:
                            cliente.send(bytes("\n%Senha errada!","utf-8"))
                            continue
                    else:
                        cliente.send(bytes("\n%sala lotada","utf-8"))
                        continue
                
                except KeyError:
                    cliente.send(bytes("\n%Esta sala não existe","utf-8"))
                    continue

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

    def receber_enviar(self, sala, cliente) -> None:
        while True:
            menssagem = self.receber(cliente)
            for conectados in self.rooms[sala][2]:
                if conectados != cliente:
                    try:
                        conectados.send(bytes(menssagem, "utf-8"))
                    except TypeError:
                        pass

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #                

Servidor()
