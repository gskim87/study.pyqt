import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))

from PyQt5.QtWidgets import *
from PyQt5 import uic


file_path = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))
form_class = uic.loadUiType(os.path.abspath(os.path.realpath(os.path.join(file_path, '../ui/main_button.ui'))))[0]
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self, "타이틀", "내용")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()