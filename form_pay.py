import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design4 import Ui_MainWindow4

class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow4()
    window.show()
    sys.exit(app.exec_())
