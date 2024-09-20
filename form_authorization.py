import json
#from msilib.schema import ComboBox
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QComboBox
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAbstractItemView
from api import PolygonAPI 
from design1 import Ui_MainWindow
from design2 import Ui_mainWindow2
from design3 import Ui_MainWindow3
from design4 import Ui_MainWindow4
from design5 import Ui_MainWindow5
from design6 import Ui_MainWindow6
from design7 import Ui_MainWindow7
from form_buy import MainWindow5
from form_sell import MainWindow6
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot



class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.show_mainwindow2_cancel)
        self.ui.pushButton.clicked.connect(self.show_mainwindow2_create)

        self.ui.textEdit.installEventFilter(self)
        self.ui.textEdit_2.installEventFilter(self)
        self.ui.textEdit_3.installEventFilter(self)
        self.ui.textEdit_4.installEventFilter(self)

    
    def eventFilter(self, obj, event):
        if obj in [self.ui.textEdit, self.ui.textEdit_2, self.ui.textEdit_3, self.ui.textEdit_4]:
            if event.type() == QEvent.KeyPress:
                current_text = obj.toPlainText()
                key = event.key()
                if len(current_text) >= 20:
                    if key not in [Qt.Key_Backspace, Qt.Key_Home, Qt.Key_End]:
                        return True
                elif key in [Qt.Key_Return, Qt.Key_Enter]:
                    return True
        return super().eventFilter(obj, event)

    def show_mainwindow2_cancel(self):
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()

    def show_mainwindow2_create(self):
        
        text_edit_text1 = self.ui.textEdit.toPlainText().strip()
        text_edit_text2 = self.ui.textEdit_2.toPlainText().strip()
        text_edit_text3 = self.ui.textEdit_3.toPlainText().strip()
        text_edit_text4 = self.ui.textEdit_4.toPlainText().strip()
        
        if not text_edit_text1:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели прізвище")
            self.ui.textEdit.setFocus()
            return
        
        if not text_edit_text2:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели логін")
            self.ui.textEdit_2.setFocus()
            return
        
        if not text_edit_text3:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели ім'я")
            self.ui.textEdit_3.setFocus()
            return
        
        if not text_edit_text4:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели пароль")
            self.ui.textEdit_4.setFocus()
            return
    
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()    

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow2()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.show_mainwindow1)
        self.ui.pushButton.clicked.connect(self.open_mainwindow3)

        self.ui.textEdit.installEventFilter(self)
        self.ui.textEdit_3.installEventFilter(self)


 # ----------ОБМЕЖЕННЯ-----ENTER-----------------------------
        
    def eventFilter(self, obj, event):
        if obj in [self.ui.textEdit, self.ui.textEdit_3]:
            if event.type() == QEvent.KeyPress:
                current_text = obj.toPlainText()
                key = event.key()
                if len(current_text) >= 20:
                    if key not in [Qt.Key_Backspace, Qt.Key_Home, Qt.Key_End]:
                        return True
                elif key in [Qt.Key_Return, Qt.Key_Enter]:
                    return True
        return super().eventFilter(obj, event)
    
    
    def show_mainwindow1(self):
        self.hide()
        self.window1 = MainWindow1()
        self.window1.show()


  # ----------MessageBox-----ПЕРЕВІРКА-----АВТОРИЗАЦІЇ-------------------------
    
    def open_mainwindow3(self):
        text_edit_text = self.ui.textEdit.toPlainText().strip()
        text_edit_3_text = self.ui.textEdit_3.toPlainText().strip()
        
        if not text_edit_text:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели логін")
            self.ui.textEdit.setFocus()
            return
        
        if not text_edit_3_text:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели пароль")
            self.ui.textEdit_3.setFocus()
            return

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
        self.ui.pushButton_3.clicked.connect(self.show_mainwindow7)
        self.ui.pushButton_4.clicked.connect(self.show_Mainwindow5)
        self.ui.pushButton_5.clicked.connect(self.show_Mainwindow6)
        self.ui.pushButton_6.clicked.connect(self.pushButton6Clicked)

        self.update_tickers_data()
        self.top_three_positive()
        self.top_three_negative()

        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.ui.textEdit.installEventFilter(self)


    def pushButton6Clicked(self):
        text_edit_text = self.ui.textEdit.toPlainText().strip()

        if not text_edit_text:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи нічого не ввели")
            self.ui.textEdit.setFocus()
            self.ui.tableWidget.clear()
            self.update_tickers_data()
            return

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        with open('tickers.json', 'r') as f:
            tickers_data = json.load(f)

        found_data = []
        for ticker in tickers_data:
            if ticker.get('symbol').startswith(text_edit_text):
               found_data.append(ticker)

        if found_data:
            self.ui.tableWidget.setRowCount(len(found_data))
            for i, ticker in enumerate(found_data):
               symbol = ticker.get('symbol')
               price = ticker.get('price')
               percent_change = ticker.get('percent_change')

               item_symbol = QTableWidgetItem(symbol)
               self.ui.tableWidget.setItem(i, 0, item_symbol)

               item_price = QTableWidgetItem(str(price))
               self.ui.tableWidget.setItem(i, 1, item_price)

               item_percent_change = QTableWidgetItem(str(percent_change) + "%")
               if percent_change < 0:
                   item_percent_change.setForeground(QColor("red"))
               else:
                   item_percent_change.setForeground(QColor("green"))
               self.ui.tableWidget.setItem(i, 2, item_percent_change)
        else: 
            QMessageBox.warning(self, "Помилка!!!", "Дані не знайдено")
            self.ui.tableWidget.clear()
            self.update_tickers_data()

        self.ui.textEdit.clear()
        self.ui.textEdit.setFocus()

    def eventFilter(self, obj, event):
       if obj is self.ui.textEdit:
          if event.type() == QEvent.KeyPress:
              key = event.key()
              allowed_keys = [Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, 
                              Qt.Key_F, Qt.Key_G, Qt.Key_H, Qt.Key_I, Qt.Key_J,
                              Qt.Key_K, Qt.Key_L, Qt.Key_M, Qt.Key_N, Qt.Key_O,
                              Qt.Key_P, Qt.Key_Q, Qt.Key_R, Qt.Key_S, Qt.Key_T,
                              Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y,
                              Qt.Key_Z, Qt.Key_Backspace, Qt.Key_Home, Qt.Key_End]
            
              if key not in allowed_keys:
                  return True 

              if key == Qt.Key_Backspace:
                  return False 
            
              if not event.text().isalpha():
                  return True 

              current_text = obj.toPlainText()
              if len(current_text) >= 10 and key not in [Qt.Key_Home, Qt.Key_End]:
                  return True

              if key in [Qt.Key_Return, Qt.Key_Enter]:
                  return True
       return super().eventFilter(obj, event)
    
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

    def show_Mainwindow5(self): 
        self.hide()
        self.window5 = MainWindow5()
        self.window5.show()

    def show_Mainwindow6(self):
        self.hide()
        self.window6 = MainWindow6()
        self.window6.show()

    def update_tickers_data(self):
        filename = 'tickers.json'
        with open(filename, 'r') as f:
            tickers_data = json.load(f)

        self.ui.tableWidget.setRowCount(len(tickers_data))
        for i, ticker in enumerate(tickers_data):
            symbol = ticker.get("symbol")
            price = ticker.get("price")
            percent_change = ticker.get("percent_change")
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(symbol))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            item = QTableWidgetItem(str(percent_change) + " %")
            if percent_change < 0:
                item.setForeground(QColor("red"))
            else:
                item.setForeground(QColor("green"))
            self.ui.tableWidget.setItem(i, 2, item)
    
    def top_three_positive(self):
       filename = 'tickers.json'
       with open(filename, 'r') as f:
           tickers_data = json.load(f)

       sorted_tickers = sorted(tickers_data, key=lambda x: x["percent_change"], reverse=True)

       top_positive_tickers = sorted_tickers[:3]

       self.ui.tableWidget_2.clearContents()
       self.ui.tableWidget_2.setRowCount(0)

       for i, ticker in enumerate(top_positive_tickers):
           symbol = ticker.get("symbol")
           price = ticker.get("price")
           percent_change = ticker.get("percent_change")

           self.ui.tableWidget_2.insertRow(i)
           self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(symbol))
           self.ui.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(price)))
           item = QTableWidgetItem(str(percent_change) + " %")
           item.setForeground(QColor("green"))
           self.ui.tableWidget_2.setItem(i, 2, item)

    def top_three_negative(self):
       filename = 'tickers.json'
       with open(filename, 'r') as f:
           tickers_data = json.load(f)

       sorted_tickers = sorted(tickers_data, key=lambda x: x["percent_change"])

       top_negative_tickers = sorted_tickers[:3]

       self.ui.tableWidget_3.clearContents()
       self.ui.tableWidget_3.setRowCount(0)

       for i, ticker in enumerate(top_negative_tickers):
           symbol = ticker.get("symbol")
           price = ticker.get("price")
           percent_change = ticker.get("percent_change")

           self.ui.tableWidget_3.insertRow(i)
           self.ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(symbol))
           self.ui.tableWidget_3.setItem(i, 1, QTableWidgetItem(str(price)))
           item = QTableWidgetItem(str(percent_change) + " %")
           item.setForeground(QColor("red"))
           self.ui.tableWidget_3.setItem(i, 2, item)       

class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_mainwindow3_pay)
        self.ui.pushButton_2.clicked.connect(self.show_mainwindow3_cancel)

        self.ui.textEdit_4.installEventFilter(self)

    def eventFilter(self, obj, event):
      if obj is self.ui.textEdit_4:
          if event.type() == QEvent.KeyPress:
              current_text = obj.toPlainText()
              key = event.key()
              if key >= Qt.Key_0 and key <= Qt.Key_9 or key == Qt.Key_Backspace or key == Qt.Key_Home or key == Qt.Key_End:
                  if len(current_text) >= 20:
                      if key not in [Qt.Key_Backspace, Qt.Key_Home, Qt.Key_End]:
                          return True
              else:
                  return True
              if key in [Qt.Key_Return, Qt.Key_Enter]:
                  return True
      return super().eventFilter(obj, event)
    
    def show_mainwindow3_cancel(self):
        
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()

    def show_mainwindow3_pay(self):
        text_edit_text = self.ui.textEdit_4.toPlainText().strip()
        
        if not text_edit_text:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели суму")
            self.ui.textEdit_4.setFocus()
            return
        
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()    

class MainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self)
        
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(510, 200, 251, 31))
        self.comboBox.setObjectName("comboBox")
        
        with open('tickers.json') as f:
           data = json.load(f)

        symbols = [item['symbol'] for item in data]
        self.comboBox.clear()
        self.comboBox.addItems(symbols)

        self.ui.pushButton.clicked.connect(self.open_mainwindow3_cancel)
        self.ui.pushButton_3.clicked.connect(self.open_mainwindow3_cancel)
        self.ui.pushButton_4.clicked.connect(self.obrahuvatu)

        self.ui.textEdit_3.installEventFilter(self)

        self.ui.pushButton.setDisabled(True)  

    def obrahuvatu(self):
        text_edit_3_text = self.ui.textEdit_3.toPlainText().strip()
        if not text_edit_3_text:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели кількість акцій")
            self.ui.textEdit_3.setFocus()
            return
        
        self.ui.pushButton.setEnabled(True)

    def eventFilter(self, obj, event):
      if obj is self.ui.textEdit_3:
          if event.type() == QEvent.KeyPress:
              current_text = obj.toPlainText()
              key = event.key()
              if key >= Qt.Key_0 and key <= Qt.Key_9 or key == Qt.Key_Backspace or key == Qt.Key_Home or key == Qt.Key_End:
                  if len(current_text) >= 20:
                      if key not in [Qt.Key_Backspace, Qt.Key_Home, Qt.Key_End]:
                          return True
              else:
                  return True
              if key in [Qt.Key_Return, Qt.Key_Enter]:
                  return True
      return super().eventFilter(obj, event)
   

    def open_mainwindow3_cancel(self):
        if self.ui.pushButton_4.isEnabled():  
            self.hide()
            self.mainwindow3 = MainWindow3()
            self.mainwindow3.show()

class MainWindow6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(510, 210, 251, 31))
        self.comboBox.setObjectName("comboBox")
        
        with open('tickers.json') as f:
           data = json.load(f)

        symbols = [item['symbol'] for item in data]
        self.comboBox.clear()
        self.comboBox.addItems(symbols)

        self.ui.pushButton.clicked.connect(self.open_mainwindow3_cancel)
        self.ui.pushButton_3.clicked.connect(self.open_mainwindow3_cancel)
        self.ui.pushButton_4.clicked.connect(self.obrahuvatu)

        self.ui.pushButton.setDisabled(True)

        self.ui.textEdit_3.installEventFilter(self)

    def obrahuvatu(self):
        text_edit_3_text = self.ui.textEdit_3.toPlainText().strip()
        if not text_edit_3_text:
            QMessageBox.warning(self, "Помилка!!!", "Упс . . .\nВи не ввели кількість акцій")
            self.ui.textEdit_3.setFocus()
            return
        
        self.ui.pushButton.setEnabled(True)

    def eventFilter(self, obj, event):
      if obj is self.ui.textEdit_3:
          if event.type() == QEvent.KeyPress:
              current_text = obj.toPlainText()
              key = event.key()
              if key >= Qt.Key_0 and key <= Qt.Key_9 or key == Qt.Key_Backspace or key == Qt.Key_Home or key == Qt.Key_End:
                  if len(current_text) >= 20:
                      if key not in [Qt.Key_Backspace, Qt.Key_Home, Qt.Key_End]:
                          return True
              else:
                  return True
              if key in [Qt.Key_Return, Qt.Key_Enter]:
                  return True
      return super().eventFilter(obj, event)
 

    def open_mainwindow3_cancel(self):
        if self.ui.pushButton_4.isEnabled():  
            self.hide()
            self.mainwindow3 = MainWindow3()
            self.mainwindow3.show()

class MainWindow7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.show_mainwindow3)
        self.ui.pushButton.clicked.connect(self.show_mainwindow2)
        self.ui.pushButton_2.clicked.connect(self.show_mainwindow4)

        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    

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
    window.setWindowIcon(QIcon('icon1.png'))
    app.setWindowIcon(QIcon('icon1.png'))
    window.show()
    sys.exit(app.exec_())
