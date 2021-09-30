from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 201)
        MainWindow.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.New_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.New_name_line.setGeometry(QtCore.QRect(20, 90, 260, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.New_name_line.setFont(font)
        self.New_name_line.setStyleSheet("background-color: white;\n"
"border-radius: 15px;")
        self.New_name_line.setAlignment(QtCore.Qt.AlignCenter)
        self.New_name_line.setObjectName("New_name_line")
        self.new_name_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_name_button.setGeometry(QtCore.QRect(30, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.new_name_button.setFont(font)
        self.new_name_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_name_button.setStyleSheet("#go {\n"
"    background-color: rgb(29, 29, 29);\n"
"    border: 1px solid;\n"
"    border-color: white;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.new_name_button.setObjectName("new_name_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(34, 29, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"border-radius: 15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_name_button.setText(_translate("MainWindow", "Change"))
        self.label.setText(_translate("MainWindow", "New Name!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
