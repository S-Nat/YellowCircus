import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:

            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))  # заливка
            x1 = randint(0, 780)
            y1 = randint(0, 500)
            self.x, self.y = x1, y1
            self.drawEll(qp)
            qp.end()

    def drawEll(self, qp):
        r1 = randint(20, 200)
        r2 = randint(20, 200)
        qp.drawEllipse(self.x, self.y, r1, r2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())