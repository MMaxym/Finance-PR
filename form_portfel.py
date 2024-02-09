import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design7 import Ui_MainWindow7

class MainWindow7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow7()
    window.show()
    sys.exit(app.exec_())
