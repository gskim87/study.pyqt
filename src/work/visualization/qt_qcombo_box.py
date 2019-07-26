import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setWindowTitle('QComboBox Widget')
        form_lbx = QVBoxLayout(self)
        self.setLayout(form_lbx)

        lb = QLabel()

        qb = QComboBox()
        qb.addItem("Banana")
        qb.addItems(["Apple", "Tomato", "Carrot"])
        qb.insertSeparator(1) # 구분선
        qb.currentTextChanged.connect(lb.setText)

        form_lbx.addWidget(qb)
        form_lbx.addWidget(lb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()