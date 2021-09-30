from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_frame = QtWidgets.QFrame(self.centralwidget)
        self.name_frame.setGeometry(QtCore.QRect(278, 0, 800, 101))
        self.name_frame.setStyleSheet("#name_frame {\n"
"    background-color: rgb(36, 36, 36);\n"
"}")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.nome_da_sala = QtWidgets.QLabel(self.name_frame)
        self.nome_da_sala.setGeometry(QtCore.QRect(0, 19, 800, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.nome_da_sala.setFont(font)
        self.nome_da_sala.setStyleSheet("#nome_da_sala {\n"
"    color: white;\n"
"}")
        self.nome_da_sala.setScaledContents(True)
        self.nome_da_sala.setAlignment(QtCore.Qt.AlignCenter)
        self.nome_da_sala.setIndent(50)
        self.nome_da_sala.setObjectName("nome_da_sala")
        self.send_frame = QtWidgets.QFrame(self.centralwidget)
        self.send_frame.setGeometry(QtCore.QRect(280, 610, 801, 110))
        self.send_frame.setStyleSheet("#send_frame {\n"
"        background-color: rgb(47, 47, 47);\n"
"}")
        self.send_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.send_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.send_frame.setObjectName("send_frame")
        self.line_msg = QtWidgets.QLineEdit(self.send_frame)
        self.line_msg.setGeometry(QtCore.QRect(40, 40, 630, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_msg.setFont(font)
        self.line_msg.setToolTipDuration(0)
        self.line_msg.setStyleSheet("#line_msg {\n"
"    border-radius: 15px;\n"
"    color: black;\n"
"}")
        self.line_msg.setText("")
        self.line_msg.setCursorPosition(0)
        self.line_msg.setClearButtonEnabled(False)
        self.line_msg.setObjectName("line_msg")
        self.send_button = QtWidgets.QPushButton(self.send_frame)
        self.send_button.setGeometry(QtCore.QRect(680, 30, 100, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.send_button.setFont(font)
        self.send_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_button.setStyleSheet("#send_button {\n"
"    background-color: rgb(0, 0 ,0, 0);\n"
"    color: white;\n"
"}\n"
"\n"
"#send_button::hover {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"}")
        self.send_button.setObjectName("send_button")
        self.menu_list = QtWidgets.QListWidget(self.centralwidget)
        self.menu_list.setGeometry(QtCore.QRect(0, 0, 280, 550))
        self.menu_list.setStyleSheet("#menu_list {\n"
"    background-color: rgb(112, 112, 112);\n"
"    border-radius: 1px;\n"
"}")
        self.menu_list.setObjectName("menu_list")
        self.msg_frame = QtWidgets.QListWidget(self.centralwidget)
        self.msg_frame.setGeometry(QtCore.QRect(279, 100, 800, 510))
        self.msg_frame.setStyleSheet("#msg_frame {\n"
"    background-color: rgb(71, 71, 71);\n"
"    border: none;\n"
"}")
        self.msg_frame.setObjectName("msg_frame")
        self.my_account = QtWidgets.QFrame(self.centralwidget)
        self.my_account.setGeometry(QtCore.QRect(0, 609, 280, 111))
        self.my_account.setStyleSheet("#my_account {\n"
"    background-color: rgb(38, 38, 38);\n"
"}\n"
"")
        self.my_account.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.my_account.setFrameShadow(QtWidgets.QFrame.Raised)
        self.my_account.setObjectName("my_account")
        self.my_name_label = QtWidgets.QLabel(self.my_account)
        self.my_name_label.setGeometry(QtCore.QRect(110, 10, 170, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.my_name_label.setFont(font)
        self.my_name_label.setStyleSheet("#my_name_label {\n"
"    color: white;\n"
"}")
        self.my_name_label.setIndent(15)
        self.my_name_label.setObjectName("my_name_label")
        self.my_photo = QtWidgets.QLabel(self.my_account)
        self.my_photo.setGeometry(QtCore.QRect(20, 15, 80, 80))
        self.my_photo.setText("")
        self.my_photo.setPixmap(QtGui.QPixmap("../../../../image/saphira.png"))
        self.my_photo.setScaledContents(True)
        self.my_photo.setObjectName("my_photo")
        self.my_name_button = QtWidgets.QPushButton(self.my_account)
        self.my_name_button.setGeometry(QtCore.QRect(110, 29, 170, 51))
        self.my_name_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.my_name_button.setStyleSheet("#my_name_button {\n"
"    background-color: rgb(0,0,0,0);\n"
"}")
        self.my_name_button.setText("")
        self.my_name_button.setObjectName("my_name_button")
        self.my_photo_button = QtWidgets.QPushButton(self.my_account)
        self.my_photo_button.setGeometry(QtCore.QRect(20, 15, 80, 80))
        self.my_photo_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.my_photo_button.setStyleSheet("#my_photo_button {\n"
"    background-color: rgb(0,0,0,0);\n"
"}")
        self.my_photo_button.setText("")
        self.my_photo_button.setObjectName("my_photo_button")
        self.new_room = QtWidgets.QPushButton(self.centralwidget)
        self.new_room.setGeometry(QtCore.QRect(0, 549, 280, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.new_room.setFont(font)
        self.new_room.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_room.setStyleSheet("#new_room {\n"
"    background-color: rgb(43, 43, 43);\n"
"    border: 1px solid;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"")
        self.new_room.setObjectName("new_room")
        self.msg_frame.raise_()
        self.menu_list.raise_()
        self.name_frame.raise_()
        self.send_frame.raise_()
        self.my_account.raise_()
        self.new_room.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nome_da_sala.setText(_translate("MainWindow", "Exemplo"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.my_name_label.setText(_translate("MainWindow", "LittleKiwi"))
        self.new_room.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
