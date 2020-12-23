import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # self.di = {
        #     '조건':[

        #         # ([''],['='],lineEdit)
        #         ]
        #     ,'정렬':[]

        # }
        self.di = {"name":["Bill", "Dan", "Steve"], "age":["45","21","78"]}
        self.sign = ['=','>','<','!=']
        self.initUI()
        self.populateTree()

    def initUI(self):
        self.tree = QTreeWidget()
        self.tree.setColumnCount(3)
        self.setCentralWidget(self.tree)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()

    def populateTree(self):
        # Add widget item to tree
        for key, value in self.di.items():
            print(key)
            item1 = QTreeWidgetItem()
            item1.setText(0, key)
            item1.setExpanded(True)
            self.tree.addTopLevelItem(item1)
            # Add Combo Box to widget item
            item2 = QTreeWidgetItem(item1)
            combo = QComboBox(self.tree)
            combo.addItems(value)
            combo_sign = QComboBox(self.tree)
            combo_sign.addItems(self.sign)
            self.tree.setItemWidget(item2, 0, combo)
            self.tree.setItemWidget(item2, 1, combo_sign)
            self.tree.setItemWidget(item2, 2, QLineEdit())
            # combo.currentIndexChanged.connect(lambda index, combo=combo: self.doSomething(combo.currentText()))

    def doSomething(self, n):
        print (n)            

if __name__ == "__main__":
    app = QApplication([])
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    