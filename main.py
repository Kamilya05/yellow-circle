import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint

Ui_Form, QMainWindowWindow = uic.loadUiType("UI.ui")


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
        self.coords = []
        self.pushButton.clicked.connect(self.click)

    def click(self):
        x, y = randint(0, 600), randint(0, 500)
        d = randint(5, 150)
        self.coords.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QColor('yellow'))
        for x, y, d in self.coords:
            qp.drawEllipse(x, y, d, d)
        qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
