# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'financeDesign6.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1273, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"D:\HPK\3_KURS\PRAKTUKA\Python\PracticePR211-prt1-finance-main\form6.png"))
        self.label.setObjectName("label")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(510, 310, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 210, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 600, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: transparent; color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 170, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #DDE4FE;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #DDE4FE;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 540, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #2A34CA; color: white;  border-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 450, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("color: green;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: #DDE4FE;")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 270, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #DDE4FE;")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Продаж акцій"))
        self.pushButton_3.setText(_translate("MainWindow", "Повернутися назад"))
        self.label_4.setText(_translate("MainWindow", "Акція"))
        self.label_2.setText(_translate("MainWindow", "200.00 $"))
        self.pushButton.setText(_translate("MainWindow", "ПРОДАТИ"))
        self.label_6.setText(_translate("MainWindow", "200.00 $"))
        self.label_3.setText(_translate("MainWindow", "Ім\'я користувача"))
        self.label_7.setText(_translate("MainWindow", "Кількість акцій"))
