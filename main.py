import requests
import sys
from PIL import Image
from io import BytesIO
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

api_server = "http://static-maps.yandex.ru/1.x/"

lon = "37.530887"
lat = "55.703118"
delta = "0.012"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
    "l": "map",
    "size": "650,450"
}
response = requests.get(api_server, params=params)
print(response.status_code)
image = Image.open(BytesIO(response.content))
image.save('temp/temp.png')

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)  # Загружаем дизайн
        self.intUI()

    def intUI(self):
        self.Scroll_Area.setWidget(self.Image)
        pixmap = QPixmap('temp/temp.png')
        self.Image.setPixmap(pixmap)


    def run(self):
        self.label.setText("OK")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())