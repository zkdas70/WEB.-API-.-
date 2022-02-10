import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    static_uri = 'http://static-maps.yandex.ru/1.x/'
    def __init__(self):
        super().__init__()
        self.coords = [37.530887, 55.7031181]
        self.scale = 0.002
        self.map_type = 'map'
        self.getImage()
        self.initUI()



    def getImage(self):
        map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
        #response = requests.get(map_request)
        params = {
            'll': ','.join(map(str, self.coords)),
            'spn': f'{self.scale},{self.scale}',
            'l': self.map_type
        }
        response = requests.get(self.static_uri, params = params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.map = response.content

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.map, 'PNG')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())