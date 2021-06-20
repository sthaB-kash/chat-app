from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont

import sys
import requests


class Home(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PanelGame")
        self.setWindowIcon(QIcon("icon.jpg"))
        # self.setGeometry(0,0,100,400)
        # self.setFixedHeight(500)
        # self.setFixedWidth(1200)
        # self.move(50, 300)
        # data = requests.get('https://api.github.com/events')
        # print(data.json()[0])
        greeting = QLabel("<h1>Bikash</h1>", parent=self)
        greeting.move(20, 20)
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("left button"))
        layout.addWidget(QPushButton("center "))
        layout.addWidget(QPushButton("right"))


        layout1 = QVBoxLayout()
        greetBtn = QPushButton("Greet")
        greetBtn.clicked.connect(self.greeting)
        self.msg = QLabel("msg")
        layout1.addWidget(greetBtn)
        layout1.addWidget(self.msg)
        layout1.addWidget(QPushButton("left button2"))
        layout1.addWidget(QPushButton("center2 "))
        layout1.addWidget(QPushButton("right2"))
        layout.addLayout(layout1)

        self.setLayout(layout)

    def greeting(self):
        if not self.msg.text():
            self.msg.setText("Hello")
        else:
            self.msg.setText("")



app = QApplication(sys.argv)

panelGame = Home()
panelGame.show()
sys.exit(app.exec())

