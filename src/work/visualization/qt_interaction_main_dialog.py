import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class LogInDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.id = None
        self.pw = None


    def setupUi(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("Sign in")
        # self.setWindowIcon(QIcon('icon.png'))

        # label, line edit
        label1 = QLabel("ID : ")
        label2 = QLabel("PW : ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1 = QPushButton("Sign In")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        # layout
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        # 위젯 삽입
        self.setLayout(layout)


    def pushButtonClicked(self):
        self.id = self.lineEdit1.text()
        self.pw = self.lineEdit2.text()
        self.close()



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("QInputDialog")
        # self.setWindowIcon(QIcon('icon.png'))

        # push button, label
        self.pushButton = QPushButton("Sign In")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        # 위젯 삽입
        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(layout)


    def pushButtonClicked(self):
        dlg = LogInDialog()
        dlg.exec_()
        _id = dlg.id
        _pw = dlg.pw
        self.label.setText("id : %s pw : %s" % (_id, _pw))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()