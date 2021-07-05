#Add or import the QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
#Library to set icons for the window
from PyQt5.QtGui import QIcon


class WindowExample(QWidget):

    def __init__(self):

        super().__init__()
        self.setGeometry(200, 200, 400, 300)


        self.setWindowTitle("PyQt Window")


        self.setWindowIcon(QIcon('C:\\Users\\Asus-2020\\PycharmProjects\\PyQt\\Arj.png'))


        self.setStyleSheet('background-color:cyan')

        vbox = QVBoxLayout()

        bt1 = QPushButton('Click one', self)
        bt2 = QPushButton('Click Two', self)
        bt3 = QPushButton('Click Three', self)
        bt4 = QPushButton('Click Four', self)

        vbox.addWidget(bt1)
        vbox.addWidget(bt2)
        vbox.addWidget(bt3)
        vbox.addWidget(bt4)
        self.setLayout(vbox)
        self.show()

app = QApplication([])
window = WindowExample()
sys.exit(app.exec_())