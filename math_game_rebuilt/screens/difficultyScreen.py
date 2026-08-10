from PySide6.QtWidgets import (QWidget,
                               QLabel,
                               QLineEdit,
                               QPushButton,
                               QVBoxLayout,
                               QGridLayout,
                               QApplication)
import sys
from PySide6.QtCore import Qt

class DifficultyScreen(QWidget):
    def __init__(self, difficulty, sceneChanger):
        super().__init__()
        self.difficulty = difficulty
        self.sceneChanger = sceneChanger
        self.label = QLabel("Enter Difficulty(Interger)")
        self.userInput = QLineEdit()
        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.enterAnswer)
        self.userInput.returnPressed.connect(self.enterAnswer)


        self.initUI()
    def enterAnswer(self):
        try:
            if int(self.userInput.text()) > 0:
                self.difficulty = int(self.userInput.text())
                print(self.difficulty)
                self.sceneChanger.changeScene(2)
        except ValueError:
            self.label.setText("Please Enter an Interger")
    def initUI(self):
        self.setWindowTitle("Mental Math Master -- Difficulty")
        self.label.setAlignment(Qt.AlignCenter)
        self.userInput.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""

                            """)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)
        



