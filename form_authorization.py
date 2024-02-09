import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design1 import Ui_MainWindow as Ui_MainWindow1
from design2 import Ui_mainWindow2 as Ui_MainWindow2
from design3 import Ui_MainWindow3 as Ui_MainWindow3
from design4 import Ui_MainWindow4 as Ui_MainWindow4
from design7 import Ui_MainWindow7 as Ui_MainWindow7

class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.show_mainwindow2)
        self.ui.pushButton.clicked.connect(self.open_mainwindow3)

    def show_mainwindow2(self):
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()

    def open_mainwindow3(self):
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.show_mainwindow1)
        self.ui.pushButton.clicked.connect(self.open_mainwindow3)

    def show_mainwindow1(self):
        self.hide()
        self.window1 = MainWindow1()
        self.window1.show()

    def open_mainwindow3(self):
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()

class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_mainwindow2)
        self.ui.pushButton_2.clicked.connect(self.show_mainwindow4)
        self.ui.pushButton_3.clicked.connect(self.show_mainwindow7)  # Додано обробник натискання на кнопку pushButton_3

    def show_mainwindow2(self):
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()

    def show_mainwindow4(self):
        self.hide()
        self.window4 = MainWindow4()
        self.window4.show()

    def show_mainwindow7(self):
        self.hide()
        self.window7 = MainWindow7()
        self.window7.show()

class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_mainwindow3)
        self.ui.pushButton_2.clicked.connect(self.show_mainwindow3)  # Додано обробник натискання на кнопку pushButton_2

    def show_mainwindow3(self):
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()

class MainWindow7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.show_mainwindow3)
        self.ui.pushButton.clicked.connect(self.show_mainwindow2)
        self.ui.pushButton_2.clicked.connect(self.show_mainwindow4)

    def show_mainwindow3(self):
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()

    def show_mainwindow2(self):
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()

    def show_mainwindow4(self):
        self.hide()
        self.window4 = MainWindow4()
        self.window4.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    sys.exit(app.exec_())
