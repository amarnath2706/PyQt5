from PyQt5.QtWidgets import QApplication, QWidget
import sys


#Create a Class
#Here QWidget is a base class and we are going to derive from the base class
class WindowExample(QWidget):
    #Create an init method(reserved method or constructor)
    #This method is called when an object is created from the class and it allows us initialize the attributes for the class.
    def __init__(self):
        #Super function gives access to methods(QWidget)
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.show()

app = QApplication([])
window = WindowExample()
sys.exit(app.exec_())

