import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.item = {'Item12': {'ItemEnabled': True}}
        self.setupUi()

        TreeList = ({
            'Header1': ('Item11', 'Item12',),
            'Header2': ('Item21', 'Item22',),
        })

        for key, value in TreeList.items():
            parent = QTreeWidgetItem(self.treeWidget, [key])
            for val in value:
                child = QTreeWidgetItem([val])
                child.setFlags(child.flags() | QtCore.Qt.ItemIsUserCheckable)
                child.setCheckState(0, QtCore.Qt.Checked if val in self.item else QtCore.Qt.Unchecked)
                parent.addChild(child)

        self.treeWidget.itemChanged.connect(self.treeWidgetItemChanged)


    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.gridLayout.addWidget(self.treeWidget)
        self.setCentralWidget(self.centralwidget)


    def treeWidgetItemChanged(self, widgetItem, column):
        print("Item {} is checked: {}".format(widgetItem, widgetItem.checkState(column) == QtCore.Qt.Checked))
        itemName = str(widgetItem.text(column))
        try:
            self.item[itemName]['ItemEnabled'] = widgetItem.checkState(column) == QtCore.Qt.Checked
        except KeyError:
            self.item[itemName] = {'ItemEnabled': widgetItem.checkState(column) == QtCore.Qt.Checked}
        print(self.item)



if __name__ == "__main__":
    app = QApplication([])
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()