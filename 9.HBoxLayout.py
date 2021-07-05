#Add or import the QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys
#Library to set icons for the window
from PyQt5.QtGui import QIcon

class WindowExample(QWidget):

    def __init__(self):

        super().__init__()
        self.setGeometry(200, 200, 400, 300)

        self.setWindowTitle("PyQt Window")
        hbox = QHBoxLayout()
        bt1 = QPushButton('Click One')
        bt2 = QPushButton('Click Two')
        bt3 = QPushButton('Click Three')
        bt4 = QPushButton('Click Four')

        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)
        hbox.addWidget(bt4)

        self.setLayout(hbox)

app = QApplication([])
window = WindowExample()
window.show()
sys.exit(app.exec_())