import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    list1 = QListView()
    list2 = QListView()

    grid = QGridLayout()
    grid.setRowStretch(0, 6)
    grid.setRowStretch(0, 4)
    # grid.setRowStretch(1, 4)
    grid.addWidget(list1)
    grid.setSpacing(10)
    # grid.addWidget(list2)

    win.setLayout(grid)
    win.setGeometry(300, 150, 350, 300)
    win.setWindowTitle("Example")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
   window()