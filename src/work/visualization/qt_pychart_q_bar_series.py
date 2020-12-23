import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt BarChart')
        self.setGeometry(400, 400, 680, 500)

        self.create_bar()
        self.show()


    def create_bar(self):
        set0 = QBarSet('son')
        set1 = QBarSet('dele')
        set2 = QBarSet('kane')
        set3 = QBarSet('lucas')
        set4 = QBarSet('winks')

        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Percent BarChart Example')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # chart.legend().setVisible(True)
        # chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
