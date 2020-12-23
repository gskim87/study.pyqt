# -*- coding: utf-8 -*
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()

        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)

        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        self.setGeometry(300,350,500,300)

        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.myListWidget1)
        self.hboxlayout.addWidget(self.myListWidget2)

        path_dir = os.path.dirname(os.path.realpath('__file__'))
        kakao = os.path.abspath(os.path.realpath(os.path.join(path_dir, '../../static/icon/kakao.jpg')))
        facebook = os.path.abspath(os.path.realpath(os.path.join(path_dir, '../../static/icon/facebook.jpg')))
        band = os.path.abspath(os.path.realpath(os.path.join(path_dir, '../../static/icon/band.jpg')))
        youtube = os.path.abspath(os.path.realpath(os.path.join(path_dir, '../../static/icon/youtube.jpg')))
        twitter = os.path.abspath(os.path.realpath(os.path.join(path_dir, '../../static/icon/twitter.jpg')))
        
        l1 = QListWidgetItem(QIcon(kakao), 'kakao')
        l2 = QListWidgetItem(QIcon(band), 'band')

        self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)

        QListWidgetItem(QIcon(facebook), 'facebook', self.myListWidget2)
        QListWidgetItem(QIcon(youtube), 'youtube', self.myListWidget2)
        QListWidgetItem(QIcon(twitter), 'twitter', self.myListWidget2)

        self.setWindowTitle('PyQt5 Drag and Drop Application')
        self.setLayout(self.hboxlayout)

        self.show()



if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec())
