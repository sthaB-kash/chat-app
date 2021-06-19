from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont

import sys
import requests


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PanelGame")
        self.setWindowIcon(QIcon("icon.jpg"))
        # self.setGeometry(0,0,100,400)
        self.setFixedHeight(500)
        self.setFixedWidth(1200)
        data = requests.get('https://api.github.com/events')
        print(data.json()[0])


app = QApplication(sys.argv)

window = Home()
window.show()
sys.exit(app.exec())

