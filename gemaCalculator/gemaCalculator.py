# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QComboBox

import os
import webbrowser

from henderson import Henderson

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 398)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(27, 70, 330, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 160, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(23, 320, 160, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 300, 330, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(27, 120, 331, 170))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 344, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(335, 344, 25, 25))
        self.pushButton_4.setObjectName("pushButton_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 81, 71))
        self.label.setObjectName("label")
        self.pixmap = QPixmap('logo_final.png')
        self.label.setPixmap(self.pixmap)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.fileBanco = []
        self.pastaSalvar = []
        self.pushButton.clicked.connect(self.openDatabase)
        self.pushButton_2.clicked.connect(self.openDirectory)
        self.pushButton_3.clicked.connect(self.calcular)

        self.pushButton_4.clicked.connect(self.help)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora A e A- (Quaas & Henderson)"))
        self.pushButton.setText(_translate("MainWindow", "Carregar Dados"))
        self.pushButton_2.setText(_translate("MainWindow", "Salvar em..."))
        self.pushButton_3.setText(_translate("MainWindow", "Calcular"))
        self.pushButton_4.setText(_translate("MainWindow", "?"))

    def openDatabase(self):
        file = QFileDialog.getOpenFileName(None,'Abrir Banco de Dados', self.lineEdit.text())
        print(file[0])
        self.lineEdit.setText(str(file[0]))
        with open(file[0]) as f:
            self.plainTextEdit.appendPlainText(f.read())
        self.fileBanco = file[0]

    def openDirectory(self):
        cwd = os.getcwd()
        file = QFileDialog.getExistingDirectory(None,'Selecione o local para salvar o resultado', cwd)
        self.lineEdit_2.setText(str(file+'/saida.txt'))

    def calcular(self):
        self.pastaSalvar = self.lineEdit_2.text()
        calc = Henderson(self.fileBanco,self.pastaSalvar)
        calc.calculo()
        QMessageBox.information(None, 'Tudo pronto!', 'As matrizes foram calculadas!')

    def help(self):
        webbrowser.open_new_tab('https://github.com/romuere/gemaCalculator')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
