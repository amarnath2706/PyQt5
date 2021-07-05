import sys
from PyQt5.QtWidgets import QApplication, QWidget




#app = QApplication(sys.argv)
#Create an object for QApplication
app = QApplication([])

#Create an object for window
window = QWidget()
#Display the window
window.show()

#Execute the app
app.exec_()