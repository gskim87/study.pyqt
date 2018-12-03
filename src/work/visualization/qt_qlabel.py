import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setGeometry(800, 400, 400, 150)

        textLabel = QLabel("Message : ", self)
        textLabel.move(20, 20)

        self.label = QLabel("", self)
        self.label.move(80, 20)
        self.label.resize(150, 30)

        btn1 = QPushButton("클릭", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)
        

        btn2 = QPushButton("클리어", self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

        btn3 = QPushButton("종료", self)
        btn3.move(260, 60)
        btn3.clicked.connect(QCoreApplication.instance().quit)


    def btn1_clicked(self):
        self.label.setText("버튼이 클릭되었습니다.")


    def btn2_clicked(self):
        self.label.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()