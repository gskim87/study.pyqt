import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

import time

TIME_LIMIT = 100

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.TIME_LIMIT = 100
        self.flag_break = False
        
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0,0,300,25)
        self.progress.setMaximum(100)
        self.button = QPushButton('Start', self)
        self.button_stop = QPushButton('stop', self)
        self.button.move(0, 30)
        self.button_stop.move(0, 60)
        self.show()

        self.button.clicked.connect(self.onButtonClick)
        self.button_stop.clicked.connect(self.onButtonClick_stop)
        self.setGeometry(800, 400, 500, 300)


    def onButtonClick_stop(self):
        self.flag_break = True


    def onButtonClick(self):
        count = 0
        while count < TIME_LIMIT:
            if self.flag_break:
                break
            count += 1
            time.sleep(0.01)
            self.progress.setValue(count)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()