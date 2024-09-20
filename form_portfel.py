import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design7 import Ui_MainWindow7
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt, widgets

class MainWindow7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self)

        self.setWindowTitle("Графік")
        self.setGeometry(100, 100, 800, 600)
        
        self.plot_widget = QWidget()
        self.plot_layout = QVBoxLayout(self.plot_widget)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.canvas)

        self.load_data_and_plot()

        self.setCentralWidget(self.plot_widget)

    def load_data_and_plot(self):
        x = [1, 2, 3, 4, 5]
        y = [5, 7, 2, 8, 4]

        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow7()
    window.show()
    sys.exit(app.exec_())
