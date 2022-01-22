import sys
from random import randrange

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow

from Ui import Ui_MainWindow


class Board(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 800, 600)
        self.setWindowTitle('Желтые окружности')
        self.pushButton.clicked.connect(self.draw_yellow_circle)
        self.not_draw = True

    def draw_yellow_circle(self):
        self.not_draw = False
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        if not self.not_draw:
            x = randrange(0, 400)
            y = randrange(0, 400)
            radius = randrange(5, 200)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Board()
    ex.show()
    sys.exit(app.exec_())

