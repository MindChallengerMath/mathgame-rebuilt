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
        layout = QVBoxLayout(container)
        self.score = QLabel("0")
        self.score.setAlignment(Qt.AlignCenter)
        self.equation = QLabel(f"{self.n1} {self.sign} {self.n2}")
        self.equation.setAlignment(Qt.AlignCenter)
      
        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.enterAnswer)

      
        self.enter = QPushButton("Enter")
        self.enter.clicked.connect(self.enterAnswer)
        layout.addWidget(self.score)
        layout.addWidget(self.equation)
        layout.addWidget(self.userInput)
        layout.addWidget(self.enter)
    def enterAnswer(self):
        try:
            float(self.userInput.text())
        except ValueError:
            self.userInput.setText("That in not a number")


app = QApplication()
window = mainWindow()
window.resize(1000, 600)
window.show()
app.exec()
        
