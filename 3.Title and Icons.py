from PyQt5.QtWidgets import QApplication, QWidget
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

        #Set fixed height and width of the window(you are not able to reshize the window by drag the window)
        #self.setFixedHeight(400)
        #self.setFixedWidth(300)

        #Set window Opacity
        #self.setWindowOpacity(0.8)

        #Style sheet
        self.setStyleSheet('background-color:cyan')
        self.show()

app = QApplication([])
window = WindowExample()
sys.exit(app.exec_())