import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon,QPalette
from PyQt5.QtGui import QPainter,QFont,QColor,QPen,QPainterPath,QBrush
from PyQt5.QtCore import Qt, QTimer

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from math import pi,acos,sin,cos,atan2
import random

class spinner(QWidget):
    
    def __init__(self, parent_form):
        super().__init__()
        self.delta=0
        self.setFixedSize(100, 100)
        #self.setGeometry(300, 300, 300, 220)
        #self.setWindowTitle('Icon')
        #self.setWindowIcon(QIcon('web.png'))
        self.parent = parent_form
        print(':: __init__ ::')
        print(type(self.parent))
        # self.parent.addWidget(self)
        # self.parent.setEnabled(False)
        # self.start()
        
    def start(self):
        print(':: start ::')
        self.show()
        self.parent.setEnabled(False)
        self.timer=QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10);
        self.blue_target=255.0
        self.green_target=0.0
        self.red_target=0.0
        
    def stop(self):
        print(':: stop ::')
        self.timer.stop()
        self.parent.setEnabled(True)
        self.hide()
        
    def update(self):
        # print(':: update ::')
        self.delta=self.delta+5
        if self.delta>360:
            self.delta=0

        self.blue_target=0#self.blue_target+20*random.random()-10
        self.green_target=0#self.green_target+20*random.random()-10
        self.red_target=0#self.red_target+20*random.random()-10
        if self.blue_target>255:
            self.blue_target=255

        if self.red_target>255:
            self.red_target=255

        if self.green_target>255:
            self.green_target=255

        if self.blue_target<0:
            self.blue_target=0

        if self.red_target<0:
            self.red_target=0

        if self.green_target<0:
            self.green_target=0
            
        self.repaint()
        
    def paintEvent(self, e):
        print(':: paintEvent ::')
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
        
    def drawWidget(self, qp):
        print(':: drawWidget ::')
        color = self.palette().color(QPalette.Background)
        qp.setBrush(QColor(100,0,0))

        pen=QPen()
        pen.setWidth(self.width()/10)
        
        pen.setColor(QColor(0,0,255))
        pen.setCapStyle(Qt.RoundCap)

        w=self.width()/2
        x_shift=w+w*0.05
        y_shift=w+w*0.05
        r=0.35*w
        r1=w*0.8
        qp.setPen(pen)

        my_max=100
        p=[]
        c=[]
        for phi in range(0,360,30):
            p.append(phi)
            c.append(0)
        f=0
        for i in range(0,len(p)):
            if p[i]>self.delta:
                f=i
                break
        i=f
        m=1.0
        while(i>=0):
            c[i]=m
            m=m*0.7
            i=i-1
            
        i=len(c)-1
        
        while(i>f):
            c[i]=m
            m=m*0.7
            i=i-1

        for i in range(0,len(p)):
            self.pos=p[i]
            x = r *  cos( (2*pi)*self.pos/360 )
            y = r *  sin( (2*pi)*self.pos/360 )
        
            x1 = r1 *  cos( (2*pi)*self.pos/360 )
            y1 = r1 *  sin( (2*pi)*self.pos/360 )
            cb=self.blue_target*c[i]+color.blue()*(1.0-c[i])
            cg=self.green_target*c[i]+color.green()*(1.0-c[i])
            cr=self.red_target*c[i]+color.red()*(1.0-c[i])
            
            pen.setColor(QColor(cr,cg,cb))
            qp.setPen(pen)
            qp.drawLine(x+x_shift,y+y_shift,x1+x_shift,y1+y_shift)

class RequestRunnable(QRunnable):
    def __init__(self, dialog):
        QRunnable.__init__(self)
        self.w = dialog

    def run(self):
        print(':: run ::')
        QThread.msleep(3000)
        # for i in range(0, 10000000000):
        #     pass
        QMetaObject.invokeMethod(self.w, "setData",
                                 Qt.QueuedConnection,
                                 Q_ARG(str, "finish"))


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 400, 300, 300)
        
        
        
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.spinner = spinner(self)

        self.btn = QPushButton("Submit", self.widget)
        self.btn.clicked.connect(self.submit)

        self.setLayout(self.layout)
        self.layout.addWidget(self.widget)
        # self.layout.addWidget(self.btn)
        # self.layout.addWidget(self.widget)
        # self.widget.addWidget(self.btn)
        # self.widget.addWidget(self.spinner)
        
        # self.layout.addWidget(self.spinner)


    def submit(self):
        self.btn.setEnabled(False)
        self.spinner.start()
        runnable = RequestRunnable(self)
        QThreadPool.globalInstance().start(runnable)


    @pyqtSlot(str)
    def setData(self, data):
        print(data)
        self.spinner.stop()
        self.btn.setEnabled(True)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    # spinner = spinner()
    # spinner.show()
    sys.exit(app.exec_())