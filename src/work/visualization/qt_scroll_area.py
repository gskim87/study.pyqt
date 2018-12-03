import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas_datareader.data as web
import pandas as pd
from pandas import Series, DataFrame

from PyQt5 import QtWidgets

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lst = [u"D", u"E", u"EF", u"F", u"FG", u"G", u"H", u"JS", u"J", u"K", u"M", u"P", u"R", u"S", u"T", u"U", u"V", u"X", u"Y", u"Z"]
        self.setupUi()


    def setupUi(self):
        # 화면 크기
        window_width = 600
        window_height = 600
        self.setFixedSize(window_width, window_height)

        # scroll
        self.scroll_area = QScrollArea()
        self.scroll_area.setFixedWidth(250)
        self.scroll_area.setWidgetResizable(True)
        # self.scroll_area.setWidgetResizable(False)

        # fig, canvas
        # self.fig = plt.Figure()
        self.fig = plt.Figure(figsize=(1000,1000))
        # self.fig = plt.Figure(figsize=(30,30),tight_layout=True)
        self.canvas = FigureCanvas(self.fig)

        # 
        widget = QWidget()
        self.scroll_area.setWidget(widget)
        self.layout_seperate_area = QVBoxLayout(widget)

        self.create_layout_container()
        # self.draw_graph()

        self.layout_all = QVBoxLayout(self)
        self.layout_all.addWidget(self.scroll_area)


    # def draw_graph(self):
    #     print(':: draw_graph ::')
    #     code = '078930.KS'
    #     df = web.DataReader(code, "yahoo")
    #     df['MA20'] = df['Adj Close'].rolling(window=20).mean()
    #     df['MA60'] = df['Adj Close'].rolling(window=60).mean()

    #     ax = self.fig.add_subplot(111)
    #     ax.plot(df.index, df['Adj Close'], label='Adj Close')
    #     ax.plot(df.index, df['MA20'], label='MA20')
    #     ax.plot(df.index, df['MA60'], label='MA60')
    #     ax.legend(loc='upper right')
    #     ax.grid()

    #     self.layout_seperate_area.addWidget(self.canvas)
    #     self.layout_seperate_area.addStretch(1)
    #     # self.scroll_area.setWidget(self.canvas)
    #     # self.canvas.draw()


    def create_layout_container(self):
        for i in range(5):
            self.layout_seperate_area.addWidget(self.create_layout_group(i))
        self.layout_seperate_area.addStretch(1)


    def create_layout_group(self, number):
        seperate_group_box = QGroupBox("GroupBox".format(number), self)
        layout_groupbox = QVBoxLayout(seperate_group_box)
        for i in range(len(self.lst)):
            item = QCheckBox(self.lst[i], seperate_group_box)
            layout_groupbox.addWidget(item)
        layout_groupbox.addStretch(1)
        return seperate_group_box



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()