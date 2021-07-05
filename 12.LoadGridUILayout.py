from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        #Add your name of Layout ui file
        uic.loadUi("GridLayoutUI.ui", self)
        self.show()
#Find our Widgets
#'pushbutton' is the name of the button which we implemented.
        #button = self.findChild(QPushButton,'pushButton')
        #Connect
        #button.clicked.connect(self.clicked_btn)

#Create a method
    #def clicked_btn(self):
       # print("Button Clicked")

app = QApplication([])
Ui = UI()
Ui.show()
app.exec_()