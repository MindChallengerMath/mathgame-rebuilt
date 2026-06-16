from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from PySide6.QtCore import Qt

class difficulty_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mental Math Master")
        container = QWidget()
        self.setCentralWidget(container)
        self.label = QLabel("Enter Difficulty")
        self.label.setAlignment(Qt.AlignCenter)

        self.user_input = QLineEdit("Input an interger")
        self.enter = QPushButton("Enter")
        self.enter.clicked.connect(self.enterDifficulty)
        self.user_input.returnPressed.connect(self.enterDifficulty)

        layout = QVBoxLayout(container)
        layout.addWidget(self.label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.enter)

    def enterDifficulty(self):
        try:
            int(self.user_input.text())
            print("User entered difficulty")
        except ValueError:
            self.user_input.setText("This is not an interger")


app = QApplication()
window = difficulty_window()
window.resize(1000, 600)
window.show()
app.exec()
