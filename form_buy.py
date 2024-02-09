import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design5 import Ui_MainWindow5

class MainWindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow5()
    window.show()
    sys.exit(app.exec_())
