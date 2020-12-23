import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("QLineEdit Widget")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        lb = QLabel()
        le = QLineEdit()

        model = QStringListModel()
        model.setStringList(["Hello", "Hi", "Bye", "Good", "Seoul", "Very Good"])
        # model.setStringList(["Hello", "Hi", "Bye", "Good", "Seoul"])

        completer = QCompleter()
        completer.setModel(model)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        le.setCompleter(completer)

        le.textChanged.connect(lb.setText)

        form_lbx.addWidget(lb)
        form_lbx.addWidget(le)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())