import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setGeometry(800, 400, 300, 300)

        # label
        label = QLabel("매도수량 : ", self)
        label.move(10, 20)

        # spin box
        self.spinBox = QSpinBox(self)
        self.spinBox.move(70, 25)
        self.spinBox.resize(80, 22)

        self.spinBox.setValue(10)
        self.spinBox.setSingleStep(10)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.valueChanged.connect(self.spinBoxChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)


    def spinBoxChanged(self):
        val = self.spinBox.value()
        msg = "%d 주를 매도합니다." % (val)
        self.statusBar.showMessage(msg)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()