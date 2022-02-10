import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import uic

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    static_uri = 'http://static-maps.yandex.ru/1.x/'

    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.coords = [37.530887, 55.7031181]
        self.scale = 0.002
        self.map_type = 'map'
        self.getImage()

    def getImage(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
        # response = requests.get(map_request)
        params = {
            'll': ','.join(map(str, self.coords)),
            'spn': f'{self.scale},{self.scale}',
            'l': self.map_type
        }
        response = requests.get(self.static_uri, params=params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.map = response.content
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.map, 'PNG')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
