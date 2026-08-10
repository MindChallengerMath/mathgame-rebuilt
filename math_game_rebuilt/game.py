from PySide6.QtWidgets import (QWidget,
                               QLabel,
                               QLineEdit,
                               QPushButton,
                               QGridLayout,
                               QVBoxLayout,
                               QHBoxLayout)
from PySide6.QtCore import Qt
import sys
import random

class Game(QWidget):
    def __init__(self, sceneChanger, difficultyData, operations):
        super().__init__()
        self.sceneChanger = sceneChanger
        self.difficultyData = difficultyData
        self.operations = operations
        self.maxNum = 10
        self.answer = None
        self.score = 0
        self.label = QLabel()
        self.scoreLabel = QLabel(f"Score: {self.score}")
        self.errorLabel = QLabel()
        self.userInput = QLineEdit()
        self.button = QPushButton("Enter")
        self.restartButton = QPushButton("Restart")


        self.mainMenuButton = QPushButton("Main Menu")
        self.hbox = QHBoxLayout()

        self.button.clicked.connect(self.enterAnswer)
        self.restartButton.clicked.connect(self.restart)

        self.vbox = QVBoxLayout()
        self.initUI()
        self.equation()

    def initUI(self):
        self.setLayout(self.vbox)
        self.setStyleSheet("""
                            """)

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.scoreLabel)
        self.vbox.addWidget(self.errorLabel)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)
        self.vbox.addLayout(self.hbox)
        self.hbox.addWidget(self.restartButton)
        self.hbox.addWidget(self.mainMenuButton)
        self.restartButton.hide()
        self.mainMenuButton.hide()

    def enterAnswer(self):
        try:
            if float(self.userInput.text()) == self.answer:
                self.errorLabel.clear()
                self.score += 10
                self.scoreLabel.setText(f"Score: {self.score}")
                self.maxNum += self.difficultyData.difficulty
                print(self.difficultyData)
                print(self.maxNum)
                self.equation()
            else:
                self.errorLabel.clear()
                self.lose()


        except ValueError:
            self.errorLabel.setText("This is not an number.")
    def lose(self):
        self.label.setText("You Lose")
        self.scoreLabel.setText(f"Final Score: {self.score}")
        self.userInput.hide()
        self.button.hide()
        self.restartButton.show()
        self.mainMenuButton.show()
    def restart(self):
        self.score = 0
        self.maxNum = 10
        self.scoreLabel.setText(f"Score: {self.score}")
        self.userInput.show()
        self.button.show()
        self.restartButton.hide()
        self.mainMenuButton.hide()
        self.equation()
        





    def equation(self):
        sign = random.choice(self.operations.operators)
        n1 = random.randint(1, self.maxNum)
        n2 = random.randint(1, self.maxNum)
        match sign:
            case "+":
                self.answer = self.operations.plus(n1, n2)
            case "-":
                self.answer = self.operations.minus(n1, n2)
            case "*":
                self.answer = self.operations.multiply(n1, n2)
            case _ :
                self.answer = self.operations.divide(n1, n2)
        self.label.setText(f"{n1} {sign} {n2}")

        
        