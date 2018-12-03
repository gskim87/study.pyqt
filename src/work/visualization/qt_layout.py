import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setGeometry(800, 400, 500, 300)

        # group box, check box
        groupBox = QGroupBox("검색옵션")
        checkBox1 = QCheckBox("상한가")
        checkBox2 = QCheckBox("하한가")
        checkBox3 = QCheckBox("시가총액 상위")
        checkBox4 = QCheckBox("시가총액 하위")
        checkBox5 = QCheckBox("회전율 상위")
        checkBox6 = QCheckBox("대량거래상위")
        checkBox7 = QCheckBox("환산주가상위")
        checkBox8 = QCheckBox("외국인한도소진상위")
        checkBox9 = QCheckBox("투자자별순위")

        # table widget
        tableWidget = QTableWidget(10, 5)
        tableWidget.setHorizontalHeaderLabels(["종목코드","종목명","현재가","등락률","거래량"])
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()        

        # inner layout
        leftInnerLayout = QVBoxLayout()
        leftInnerLayout.addWidget(checkBox1)
        leftInnerLayout.addWidget(checkBox2)
        leftInnerLayout.addWidget(checkBox3)
        leftInnerLayout.addWidget(checkBox4)
        leftInnerLayout.addWidget(checkBox5)
        leftInnerLayout.addWidget(checkBox6)
        leftInnerLayout.addWidget(checkBox7)
        leftInnerLayout.addWidget(checkBox8)
        leftInnerLayout.addWidget(checkBox9)
        groupBox.setLayout(leftInnerLayout)

        
        # layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(groupBox)
        
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(tableWidget)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        # 위젯 삽입
        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()