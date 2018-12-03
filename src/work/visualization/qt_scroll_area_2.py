import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

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
        # widget : 그림과 스크롤 붙을 위젯
        window_width = 600
        window_height = 600
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedSize(window_width, window_height)
        # layout_all : 붙을 레이아웃
        self.layout_all = QVBoxLayout()
        self.layout_all.addWidget(self.widget)
        # layout_all_2 : 전체 레이아웃(ex. central layout)
        self.layout_all_2 = QVBoxLayout(self)
        self.layout_all_2.addLayout(self.layout_all)

        # widget 세팅
        self.widget.setLayout(QtWidgets.QVBoxLayout())

        # fig, canvas
        fig = plt.Figure(figsize=(30,30),tight_layout=True)
        # self.fig = fig
        self.canvas = FigureCanvas(fig)
        # fig 그리기()
        self.draw_graph(fig)
        self.canvas.draw()

        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)
        self.widget.layout().addWidget(self.scroll)


    def draw_graph(self, fig):
        print(':: draw_graph ::')
        code = '078930.KS'
        df = web.DataReader(code, "yahoo")
        df['MA20'] = df['Adj Close'].rolling(window=20).mean()
        df['MA60'] = df['Adj Close'].rolling(window=60).mean()

        ax = fig.add_subplot(111)
        ax.plot(df.index, df['Adj Close'], label='Adj Close')
        ax.plot(df.index, df['MA20'], label='MA20')
        ax.plot(df.index, df['MA60'], label='MA60')
        ax.legend(loc='upper right')
        ax.grid()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()