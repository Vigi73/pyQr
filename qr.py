import qrcode
from PyQt5 import QtWidgets
from mainForm import Ui_Form
from PyQt5.QtGui import QPixmap
import os

import sys

#
class my_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pbCREATE.clicked.connect(self.btnClicked)

    def btnClicked(self):
        data = f"👤 {self.ui.leFIO.text().title()}\n" \
               f"📧 {self.ui.leEMAIL.text()}\n" \
               f"☎ {self.ui.lePHONE.text()}"

        qrcode.make(data).save('out.png')

        image_path = 'out.png'
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path).scaled(190, 190)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.ui.gvIMAGE.setScene(scene)


app = QtWidgets.QApplication([])
application = my_window()
application.show()

sys.exit(app.exec())
