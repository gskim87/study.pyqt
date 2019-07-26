import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MySignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(1, 2)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        my_signal = MySignal()
        my_signal.signal1.connect(self.signal1_emitted)
        my_signal.signal2.connect(self.signal2_emitted)
        my_signal.run()


    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")


    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    exit(app.exec_())