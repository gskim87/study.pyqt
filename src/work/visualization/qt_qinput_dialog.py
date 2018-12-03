import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("QInputDialog")

        # push button, label
        self.pushButton = QPushButton("Input number")
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
        #QInputDialog.getInt(부모위젯, 타이틀, 창 내부에 출력될 텍스트)
        # 정수 : getInt, 실수 : getDouble, 텍스트 : getText
        # text, flag = QInputDialog.getInt(self, '매수 수량', '매수 수량을 입력하세요.')
        # if flag:
        #     self.label.setText(str(text))
        items = ("KOSPI", "KOSDAK", "KONEX")
        # QInputDialog.getItem(부모위젯, 타이틀, 창 내부에 출력될 텍스트, 아이템리스트, 초기 아이템 인덱스, 아이템 수정 가능 여부)
        item, flag = QInputDialog.getItem(self, "시장선택", "시장을 선택하세요.", items, 0, False)
        if flag:
            self.label.setText(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()