#Here I have created the radio button through coding only
from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,400)
        self.setWindowTitle("RadioButton")

        self.create_radio_btn()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        #self.label = QLabel("Adithri")
        self.label = QLabel()
        self.label.setFont(QFont("Verdana",12))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def create_radio_btn(self):
        self.groupbox = QGroupBox("What is your Favourite Food?")
        self.groupbox.setFont(QFont("Verdana",10))

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Dosai")
        self.rad1.setChecked(True)
        self.rad1.setIcon(QIcon("C:\\Users\\Asus-2020\\PycharmProjects\\PyQt\\Dosai.png"))
        self.rad1.setIconSize(QSize(80,80))
        self.rad1.setFont(QFont("verdana",14))
        self.rad1.toggled.connect(self.radio_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Poori")
        #self.rad2.setChecked(True)
        self.rad2.setIcon(QIcon("C:\\Users\\Asus-2020\\PycharmProjects\\PyQt\\Poori.png"))
        self.rad2.setIconSize(QSize(80, 80))
        self.rad2.setFont(QFont("verdana", 14))
        self.rad2.toggled.connect(self.radio_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("Egg Briyani")
        # self.rad2.setChecked(True)
        self.rad3.setIcon(QIcon("C:\\Users\\Asus-2020\\PycharmProjects\\PyQt\\Briyani.png"))
        self.rad3.setIconSize(QSize(80, 80))
        self.rad3.setFont(QFont("verdana", 14))
        self.rad3.toggled.connect(self.radio_selected)
        hbox.addWidget(self.rad3)


        self.groupbox.setLayout(hbox)
    def radio_selected(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            self.label.setText("You have Selected : " + radio_button.text())

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec_())