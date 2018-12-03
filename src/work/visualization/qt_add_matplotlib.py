import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas_datareader.data as web
import pandas as pd
from pandas import Series, DataFrame

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("그래프추가")
        # self.setWindowIcon(QIcon('icon.png'))

        # line edit, push button
        self.lineEdit = QLineEdit()
        code = '078930.KS'
        self.lineEdit.setText(code)
        self.pushButton = QPushButton("차트 그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        # fig, canvas
        self.fig = plt.Figure(figsize=(30,30),tight_layout=True)
        self.canvas = FigureCanvas(self.fig)

        # layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)


    def pushButtonClicked(self):
        print('출력')
        self.fig.clf() #  clear current figure
        code = self.lineEdit.text()
        df = web.DataReader(code, "yahoo")
        df['MA20'] = df['Adj Close'].rolling(window=20).mean()
        df['MA60'] = df['Adj Close'].rolling(window=60).mean()

        ax = self.fig.add_subplot(111)
        ax.plot(df.index, df['Adj Close'], label='Adj Close')
        ax.plot(df.index, df['MA20'], label='MA20')
        ax.plot(df.index, df['MA60'], label='MA60')
        ax.legend(loc='upper right')
        ax.grid()

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()