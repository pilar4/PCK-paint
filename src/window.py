from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import QRectF, QLineF
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

import sys

width = 1920
height = 1080

BLACK_PEN = QPen(QColor(0, 0, 0), 3)



# Parent class, sets up painter for every other drawing class
class PaintBase(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # anti aliasing
        painter.fillRect(self.rect(), QColor(255, 255, 255))  # white background



class Background(PaintBase):
    def paint(self, painter):       # warning that some functions like this saying "paint may be static"
        painter.setPen(BLACK_PEN)   # should be ignored because it doesn't take PyQt6 into consideration
        parameters_f = QLineF(width / 2, 0, width / 2, height)
        painter.drawLine(parameters_f)



class Euclidean(PaintBase):
    def paint(self, painter):
        painter.setPen(BLACK_PEN)

        radius = (width / 2) - (width / 10)

        x = (width / 4) - (radius / 2)

        y = (height / 2) - (radius / 2)

        # -------Text-------
        text_size = width // 55         # for scaling more or less
        painter.setFont(QFont("Consolas", text_size))
        parameters_text_f = QRectF(x, y - (height/12), radius, text_size * 2)
        painter.drawText(parameters_text_f, Qt.AlignmentFlag.AlignCenter, "Euclidean plane")


        # -------Circle-------
        parameters_circle_f = QRectF(x, y, radius, radius)
        painter.drawEllipse(parameters_circle_f)

        # -------Square-------
        parameters_rect_f = QRectF(x, y, radius, radius)
        painter.drawRect(parameters_rect_f)



class PDM(PaintBase):

    def paint(self, painter):
        painter.setPen(BLACK_PEN)

        radius = (width / 2) - (width / 10)

        x = ((width / 4) * 3) - (radius / 2)

        y = (height / 2) - (radius / 2)

        # -------Text-------
        text_size = width // 55
        painter.setFont(QFont("Consolas", text_size))
        parameters_text_f = QRectF(x, y - (height/12), radius, text_size * 2)
        painter.drawText(parameters_text_f, Qt.AlignmentFlag.AlignCenter, "Poincaré disk plane")

        # -------Circle-------
        parameters_circle_f = QRectF(x, y, radius, radius)
        painter.drawEllipse(parameters_circle_f)




class Scene(PaintBase):
    """Main widget that manages and draws all components."""

    # constructor
    def __init__(self):
        super().__init__()
        # create drawable components
        self.background = Background()
        self.euclidean = Euclidean()
        self.pdm = PDM()
        self.scene = QGraphicsScene()


    def paintEvent(self, event):
        super().paintEvent(event)  # draw background first

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # draw each component
        self.background.paint(painter)
        self.euclidean.paint(painter)
        self.pdm.paint(painter)


def draw():
    app = QApplication(sys.argv)
    window = QMainWindow()

    scene = Scene()
    window.setCentralWidget(scene)


    window.resize(width, height)
    window.show()
    app.exec()
