from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
#Library to set icons for the window
from PyQt5.QtGui import QIcon

#Create a Class
#Here QWidget is a base class and we are going to derive from the base class
class WindowExample(QWidget):
    #Create an init method(reserved method or constructor)
    #This method is called when an object is created from the class and it allows us initialize the attributes for the class.
    def __init__(self):
        #Super function gives access to methods(QWidget)
        super().__init__()
        self.setGeometry(200, 200, 400, 300)

        #Set the title for window
        self.setWindowTitle("PyQt Window")


        #Set icons for the window
        self.setWindowIcon(QIcon('C:\\Users\\Asus-2020\\PycharmProjects\\PyQt\\Arj.png'))

        self.create_buttons()
        self.show()
#Iam going to create a new method for creating a new buttons
    def create_buttons(self):
        btn1 = QPushButton("Click Here",self)

        #Set location of the button
        #btn1.move(250,250)

        #Change the width and height of the button
        btn1.setGeometry(200,200,100,40)

        #Set button icon
        btn1.setIcon((QIcon("C:\\Users\\Asus-2020\\PycharmProjects\\PyQt\\Arj.png")))

        #Stylesheet for button
        btn1.setStyleSheet("color:blue")
        #Background color
        btn1.setStyleSheet("background-color:cyan")



app = QApplication([])
window = WindowExample()
sys.exit(app.exec_())