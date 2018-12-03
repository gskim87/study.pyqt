import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setGeometry(800, 400, 400, 150)

        # Label
        label = QLabel("코드", self)
        label.move(20, 20)

        # LineEdit
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 20)
        self.lineEdit.returnPressed.connect(self.lineEditChanged) #엔터키 눌렀을 때
        # self.lineEdit.textChanged.connect(self.lineEditChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)


    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()