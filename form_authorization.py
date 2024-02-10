import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from API import PolygonAPI 
from design1 import Ui_MainWindow
from design2 import Ui_mainWindow2
from design3 import Ui_MainWindow3
from design4 import Ui_MainWindow4
from design5 import Ui_MainWindow5
from design6 import Ui_MainWindow6
from design7 import Ui_MainWindow7
from form_buy import MainWindow5
from form_sell import MainWindow6


class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
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
        self.ui = Ui_mainWindow2()
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

        self.api_key = "3oOUAK2xJT_TQuaVibS1I5uc4zAWHOQj"  # Ваш API ключ
        self.api = PolygonAPI(self.api_key)

        self.ui.pushButton.clicked.connect(self.show_mainwindow2)
        self.ui.pushButton_2.clicked.connect(self.show_mainwindow4)
        self.ui.pushButton_3.clicked.connect(self.show_mainwindow7)
        self.ui.pushButton_4.clicked.connect(self.show_Mainwindow5)
        self.ui.pushButton_5.clicked.connect(self.show_Mainwindow6)

        self.update_tickers_data()

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

    def show_Mainwindow5(self):  # Визначення методу для кнопки ui.pushButton_4
        self.hide()
        self.window5 = MainWindow5()
        self.window5.show()

    def show_Mainwindow6(self):  # Визначення методу для кнопки ui.pushButton_5
        self.hide()
        self.window6 = MainWindow6()
        self.window6.show()

    def update_tickers_data(self):
        ticker_types = self.api.get_ticker_types()
        tickers = ticker_types.get("results", [])

        # Встановлюємо кількість рядків у таблиці
        self.ui.tableWidget.setRowCount(len(tickers))

        for i, ticker in enumerate(tickers):
            name = ticker.get('name')
            price = ticker.get('price')
            percent_change = ticker.get('percent_change')

            # Створюємо об'єкти QTableWidgetItem та встановлюємо їх для кожного рядка та стовпця
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(percent_change)))


class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_mainwindow3)

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

class MainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self)

        # Підключаємо обробники подій для кнопок
        self.ui.pushButton.clicked.connect(self.open_mainwindow3)
        self.ui.pushButton_3.clicked.connect(self.open_mainwindow3)

    def open_mainwindow3(self):
        # Створюємо нове вікно MainWindow3 та показуємо його
        self.hide()
        self.mainwindow3 = MainWindow3()
        self.mainwindow3.show()

class MainWindow6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)

        # Підключаємо обробники подій для кнопок
        self.ui.pushButton.clicked.connect(self.open_mainwindow3)
        self.ui.pushButton_3.clicked.connect(self.open_mainwindow3)

    def open_mainwindow3(self):
        # Створюємо нове вікно MainWindow3 та показуємо його
        self.hide()
        self.mainwindow3 = MainWindow3()
        self.mainwindow3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)   
    window = MainWindow2()  
    window.show()
    sys.exit(app.exec_())
