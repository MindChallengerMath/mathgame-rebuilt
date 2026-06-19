from operations import Operations
import random
from PySide6.QtWidgets import (QMainWindow,
                               QApplication,
                               QVBoxLayout,
                               QLabel,
                               QLineEdit,
                               QPushButton,
                               QWidget
                               )
from PySide6.QtCore import Qt

class mainWindow(QMainWindow):
    operaters = ("+", "-", "*", "/")
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    sign = random.choice(operaters)

    def __init__(self):
        super().__init__()
        container = QWidget()
        if self.sign == "+":
            self.answer = Operations.plus(self.n1, self.n2)
        elif self.sign == "-":
            self.answer = Operations.minus(self.n1, self.n2)
        elif self.sign == "*":
            self.answer = Operations.multi(self.n1, self.n2)
        else:
            self.answer = Operations.divide(self.n1, self.n2) 
        self.setWindowTitle("Mental Math Master")
        self.setCentralWidget(container)
        self.thelayout = QVBoxLayout(container)
        self.score = QLabel("0")
        self.score.setAlignment(Qt.AlignCenter)
        self.equation = QLabel(f"{self.n1} {self.sign} {self.n2}")
        self.equation.setAlignment(Qt.AlignCenter)
      
        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.enterAnswer)

      
        self.enter = QPushButton("Enter")
        self.enter.clicked.connect(self.enterAnswer)
        layout.addWidget(self.score)
        self.thelayout.addWidget(self.equation)
        self.thelayout.addWidget(self.userInput)
        self.thelayout.addWidget(self.enter)
    def enterAnswer(self):
        try:
            float(self.userInput.text())
            if float(self.userInput.text()) == self.answer:
              self.userInput.setText("")
              self.score += 10
              self.n1 = random.randint(1, 10)
              self.n2 = random.randint(1, 10)
              self.sign = random.choice(operators)
              if self.sign == "+":
                answer = Operations.plus(n1, n2)
              elif self.sign == "-":
                answer = Operations.minus(n1, n2)
              elif self.sign == "*":
                answer = Operations.multi(n1, n2)
              else:
                answer = Operations.divide(n1, n2)
              self.showScore.setText(f"Score: {self.score}")
              self.equation.setText(f"{self.n1} {self.sign} {self.n2}")
            else:
              self.showScore.setText(f"Final Score: {self.score}")
              self.equation.setText("You Lose")
              self.thelayout.removeWidget(self.enter)
              self.thelayout.removeWidget(self.userInput)
              self.enter.deleteLater()
              self.userInput.deleteLater()
              

        except ValueError:
            self.userInput.setText("That in not a number")


app = QApplication()
window = mainWindow()
window.resize(1000, 600)
window.show()
app.exec()
        
