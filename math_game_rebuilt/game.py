from operations import Operations
import random
from PySide6.QtWidgets import (QMainWindow,
                                QBoxLayout,
                                QVBoxLayout,
                                QLineEdit,
                                QLabel,
                                QPushButton,
                                QWidget,
                                QApplication)
from PySide6.QtCore import Qt
difficulty = None

score = 0
operators = ("+", "-", "*", "/")

class Game:
    def equation():
        while True:
            score = 0
            max_number = 10
            running = True
            difficulty = int(input("Enter difficulty(#): "))
            while running:
                n1 = random.randint(1, max_number)
                n2 = random.randint(1, max_number)
                if random.choice(operators) == "+":
                    answer = round(Operations.plus(n1, n2), 2)
                    sign = "+"
                elif random.choice(operators) == "-":
                    answer = round(Operations.minus(n1, n2), 2)
                    sign = "-"
                elif random.choice(operators) == "*":
                    answer = round(Operations.multi(n1, n2), 2)
                    sign = "*"
                else:
                    answer = round(Operations.divide(n1, n2), 2)
                    sign = "/"
                print(f"{n1} {sign} {n2}")
                
                print(answer)
                running = False
            break

#Game.equation()
class main_window(QMainWindow):
    def __init__(self):
       
        super().__init__()
        self.setWindowTitle("Calculate The Question")
        container = QWidget()
        self.setCentralWidget(container)
        self.n1 = None
        self.n2 = None
        self.sign = None
        self.difficulty = None
        self.answer = None
        self.score = None
        self.max_number = 10
        self.answer = None
        self.running = True
        self.n1 = random.randint(1, self.max_number)
        self.n2 = random.randint(1, self.max_number)
        if random.choice(operators) == "+":
            self.answer = round(Operations.plus(self.n1, self.n2), 2)
            self.sign = "+"
        elif random.choice(operators) == "-":
            self.answer = round(Operations.minus(self.n1, self.n2), 2)
            self.sign = "-"
        elif random.choice(operators) == "*":
            self.answer = round(Operations.multi(self.n1, self.n2), 2)
            self.sign = "*"
        else:
            self.answer = round(Operations.divide(self.n1, self.n2), 2)
            self.sign = "/"
            print(f"{self.n1} {self.sign} {self.n2}")
            print(self.answer)
            
        layout = QVBoxLayout(container)

        label = QLabel(f"{self.n1} {self.sign} {self.n2}")
        label.setAlignment(Qt.AlignCenter)
        user_input = QLineEdit()
        button = QPushButton("Enter Answer")
        button.clicked.connect(lambda: "Enter")
        layout.addWidget(label)
        layout.addWidget(user_input)
        layout.addWidget(button)
        
    def check_if_input_isValid(user_input):
        while True:
            try:
                val = int(user_input)
                return val
            except ValueError:
                print("This is not a valid answer")
    def check_answer(valid_user_input,answer):
        add_score = 0
        if valid_user_input == answer:
            add_score += 10
            return add_score
        else:
            running = False
            return running
  
        




app = QApplication()
window = main_window()
window.show()
app.exec()