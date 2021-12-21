import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randint


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 500)
        self.pushButton = QPushButton('Больше окружностей!!!', self)
        self.pushButton.setGeometry(225, 225, 150, 50)


class MyWidget(Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Git и случайные окружности')
        self.coords = []
        self.pushButton.clicked.connect(self.click)

    def click(self):
        x, y = randint(0, 600), randint(0, 500)
        d = randint(5, 150)
        c = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.coords.append((x, y, d, c))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        for x, y, d, c in self.coords:
            qp.setBrush(c)
            qp.drawEllipse(x, y, d, d)
        qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
