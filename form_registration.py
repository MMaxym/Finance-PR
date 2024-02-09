import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design2 import Ui_mainWindow2 as Ui_MainWindow2

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    sys.exit(app.exec_())
