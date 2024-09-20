import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design6 import Ui_MainWindow6

class MainWindow6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow6()
    window.show()
    sys.exit(app.exec_())
