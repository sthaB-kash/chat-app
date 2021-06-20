import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout, QFormLayout
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QGroupBox
from datetime import date, datetime
from PyQt5.QtCore import QTimer, QTime, Qt



# Create a subclass of QMainWindow to setup the calculator's GUI
class Layout(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        self.setWindowTitle('PanelGame')
        self.setFont(QFont("Times new roman", 20))
        self.login_widget = QWidget(self)
        self.dash_board_widget = QWidget(self)
        # self.login_window()
        self.dashboard()


    """------------------------dashboard-section-start --------------------"""
    def dashboard(self):
        self.dash_board_widget.show()
        self.setCentralWidget(self.dash_board_widget)
        self.showNormal()
        self.showFullScreen()
        # self.setFixedSize(700, 500)
        self.setWindowTitle("PanelGame -> Quiz Master - Bikash")
        print("dash board")
        self.startBtn = QPushButton("Start")
        self.startBtn.setFixedSize(100, 40)
        self.startBtn.clicked.connect(self.start)
        self.start_title = QLabel("PanelGame")
        self.start_title.setFont(QFont("Times New Roman", 85))

        self.start_layout = QVBoxLayout()
        self.h = QHBoxLayout()
        self.startup = QGridLayout()
        btn = QHBoxLayout()
        btn.addWidget(self.startBtn)
        self.startup.addWidget(self.start_title, 0, 0)
        self.startup.addLayout(btn, 1, 0)
        self.startup.addWidget(QLabel(), 2, 0)
        self.h.addLayout(self.startup)
        self.start_layout.addLayout(self.h)






        self.main_layout = QGridLayout()

        self.collection_box = QGroupBox("Quiz Collections")
        self.box_layout = QVBoxLayout()
        self.collection_box.setLayout(self.box_layout)
        # self.top_layout.addStretch()

        self.components = QGridLayout()

        today = date.today()
        self.date = QLabel(today.strftime("%A, %d %B %Y"))
        now = datetime.now()
        self.time = QLabel(now.strftime("%I:%M:%S %p"))
        self.components.addWidget(self.date, 0, 0)
        self.components.addWidget(self.time, 0, 2, 1, 1)
        self.date.setFont(QFont("Times new roman", 16))
        # timestyle = (
        #     , 'font-weight: 900', 'text-align: right'
        # )
        self.time.setFont(QFont("Times new roman", 16))

        self.time.setStyleSheet('text-align: right')
        self.date.setFixedHeight(100)

        # buttom layout
        self.bottom_layout = QHBoxLayout()
        self.exitBtn = QPushButton("Exit")
        self.exitBtn.clicked.connect(self.close_panel_game)
        self.exitBtn.setFixedSize(100, 40)
        toggleBtn = QPushButton("Settings")
        self.bottom_layout.addWidget(toggleBtn)
        toggleBtn.clicked.connect(self.toggle)
        self.bottom_layout.addWidget(self.exitBtn)

        # layouts

        self.main_layout.addLayout(self.start_layout, 1, 0)


        self.dash_board_widget.setLayout(self.main_layout)

    def start(self):
        self.main_layout.removeItem(self.start_layout)
        self.start_layout.removeWidget(self.startBtn)
        self.startBtn.hide()
        self.start_title.hide()
        self.project_title = QLabel("<h1><center> Kantipur City College</center</h1>")
        self.insert_new_btn = QPushButton("Insert New")
        self.main_layout.addWidget(self.collection_box, 1, 0, 2, 2)
        self.main_layout.addWidget(self.project_title, 0, 0, 1, 2)
        self.main_layout.addLayout(self.components, 0, 2)
        self.main_layout.addLayout(self.bottom_layout, 2, 2)
        self.main_layout.addWidget(self.insert_new_btn, 2, 0, 1, 2)

        self.participants_layout = QVBoxLayout()
        sn = 1
        self.addParticipant(sn, "Bikash")
        sn += 1
        self.addParticipant(sn, "Bikash")
        sn += 1
        self.addParticipant(sn, "Bikash")
        self.box = QGroupBox("Participants")
        self.box.setLayout(self.participants_layout)
        self.participants_layout.addStretch()
        self.main_layout.addWidget(self.box, 1, 2)

    def addParticipant(self, sn, username):
        p = QHBoxLayout()
        name = QLabel(f'{sn}. {username}')
        name.setFont(QFont("times", 12))
        p.addWidget(name)

        self.participants_layout.addLayout(p)

    def close_panel_game(self):
        self.close()

    def toggle(self):
        if self.exitBtn.isHidden():
            self.exitBtn.show()
        else:
            self.exitBtn.hide()


    def logout(self):
        self.dash_board_widget.hide()
        # self.login_widget.show()
        # self.login_window()

    # ----------------------- login section start  -------------------------
    def login_window(self):

        self.showNormal()
        self.setFixedSize(300, 500)
        print("login")

        self.setWindowTitle("PanelGame -> Login")
        self.setCentralWidget(self.login_widget)
        layout = QVBoxLayout()
        self.login_widget.setLayout(layout)
        print("login shown")

        login_layout = QFormLayout()
        username = QLineEdit()
        password = QLineEdit()
        login_layout.addRow("Username:", username)
        login_layout.addRow("Password: ", password)
        layout.addLayout(login_layout)

        actions = QHBoxLayout()
        layout.addLayout(actions)
        cancel_btn = QPushButton("Cancel")
        login_btn = QPushButton("Loin")
        actions.addWidget(cancel_btn)
        actions.addWidget(login_btn)

        login_btn.clicked.connect(self.login)
        cancel_btn.clicked.connect(self.close_panel_game)

    def login(self):
        self.login_widget.hide()
        self.dashboard()


    '''------------------------login section end -----------------------------------'''



def main():
    """Main function."""
    # Create an instance of QApplication
    screen = QApplication(sys.argv)
    # Show the calculator's GUI
    view = Layout()
    view.show()
    # Execute the calculator's main loop
    sys.exit(screen.exec())

if __name__ == '__main__':
    main()