import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import Qt

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()


    def init_widget(self):
        self.setWindowTitle("QLineEdit Widget")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)
        lb = QLabel()
        le = QLineEdit()
        c = CustomQCompleter()
        le.setCompleter(c)
        le.textChanged.connect(lb.setText)
        form_lbx.addWidget(lb)
        form_lbx.addWidget(le)



class CustomQCompleter(QCompleter):
    def __init__(self, parent=None):
        super(CustomQCompleter, self).__init__(parent)
        self.list_model = ['Hi', 'Positive', 'Hello', 'Good', 'Very good']
        self.source_model = QStringListModel(self.list_model)
        self.setCaseSensitivity(Qt.CaseInsensitive)


    def splitPath(self, path):
        list_temp = []
        for item in self.list_model:
            if path.lower() in item.lower():
                list_temp.append(item)
        print(list_temp)
        self.setModel(QStringListModel(list_temp))
        return []



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
