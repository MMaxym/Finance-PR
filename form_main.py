import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design3 import Ui_MainWindow3

class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow3()
    window.show()
    sys.exit(app.exec_())
