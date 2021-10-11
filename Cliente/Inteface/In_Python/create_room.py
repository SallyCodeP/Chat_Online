from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 375)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nome_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nome_input.setGeometry(QtCore.QRect(20, 110, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nome_input.setFont(font)
        self.nome_input.setStyleSheet("#nome_input {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    background-color: rgb(124, 124, 124, 0.7);\n"
"}\n"
"")
        self.nome_input.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_input.setObjectName("nome_input")
        self.senha_input = QtWidgets.QLineEdit(self.centralwidget)
        self.senha_input.setGeometry(QtCore.QRect(20, 170, 230, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.senha_input.setFont(font)
        self.senha_input.setStyleSheet("#senha_input {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    background-color: rgb(124, 124, 124, 0.7);\n"
"}\n"
"")
        self.senha_input.setAlignment(QtCore.Qt.AlignCenter)
        self.senha_input.setObjectName("senha_input")
        self.quantidade_input = QtWidgets.QLineEdit(self.centralwidget)
        self.quantidade_input.setGeometry(QtCore.QRect(20, 235, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.quantidade_input.setFont(font)
        self.quantidade_input.setStyleSheet("#quantidade_input {\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    background-color: rgb(124, 124, 124, 0.7);\n"
"}\n"
"")
        self.quantidade_input.setText("")
        self.quantidade_input.setAlignment(QtCore.Qt.AlignCenter)
        self.quantidade_input.setObjectName("quantidade_input")
        self.button_criar = QtWidgets.QPushButton(self.centralwidget)
        self.button_criar.setGeometry(QtCore.QRect(20, 280, 230, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_criar.setFont(font)
        self.button_criar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_criar.setStyleSheet("#button_criar {\n"
"    background-color:white;\n"
"    color: black;\n"
"    border: 1px solid;\n"
"    border-color: black;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"#button_criar::hover {\n"
"    background-color: rgb(34, 34, 34);\n"
"    color: white;\n"
"    border: 2px solid;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.button_criar.setObjectName("button_criar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 201, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(109, 140, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setObjectName("label_6")
        self.Avisos = QtWidgets.QLabel(self.centralwidget)
        self.Avisos.setGeometry(QtCore.QRect(14, 335, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Avisos.setFont(font)
        self.Avisos.setStyleSheet("color: white;")
        self.Avisos.setText("")
        self.Avisos.setObjectName("Avisos")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_criar.setText(_translate("MainWindow", "Criar"))
        self.label.setText(_translate("MainWindow", "Crie uma sala"))
        self.label_4.setText(_translate("MainWindow", "Quantidade"))
        self.label_5.setText(_translate("MainWindow", "Senha"))
        self.label_6.setText(_translate("MainWindow", "Nome da sala"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
