import sys
from PySide2 import QtGui, QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)

def add_image(where, filename, x, y):
    image = QtGui.QImage()
    image.load(filename)
    image = image.scaled(x, y)
    image = QtGui.QPixmap.fromImage(image)
    try:
        where.setPixmap(image)
    except AttributeError:
        where.setFixedSize(x, y)
        where.setIcon(image)
        where.setIconSize(QtCore.QSize(x - 10, y - 10))

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        v = QtWidgets.QVBoxLayout(self)
        back = QtWidgets.QPushButton()
        add_image(back, "images/strzalka.png", 200, 200)

        v.addWidget(back)
        v.addStretch()

        h = QtWidgets.QHBoxLayout(self)
        for im_name in ["rss", "spoti", "yt"]:
            button = QtWidgets.QPushButton()
            add_image(button, "images/{}.png".format(im_name), 200, 200)
            if (im_name == "rss"):
                button.setStyleSheet("background-color:black;");
            h.addStretch()
            h.addWidget(button)
        h.addStretch()

        v.addLayout(h)
        v.addStretch()

window = MainWindow()
window.show()

app.exec_()