import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QBoxLayout, QWidget, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt
from game import Game
import game
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculate The Question")
        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label = QLabel(f"{Game.n1} {Game.sign} {Game.n2}")
        label.setAlignment(Qt.AlignCenter)
        user_input = QLineEdit()
        button = QPushButton("Enter Answer")
        button.clicked.connect(lambda: print("Button clicked"))

        layout.addWidget(label)
        layout.addWidget(user_input)
        layout.addWidget(button)
class start_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        container = QWidget()





        

app = QApplication()

window = main_window()
window.show()

app.exec()