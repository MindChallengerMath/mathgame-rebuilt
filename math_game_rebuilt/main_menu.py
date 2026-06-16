import sys
from PySide6.QtWidgets import (QMainWindow,
                                QBoxLayout,
                                QVBoxLayout,
                                QLineEdit,
                                QLabel,
                                QPushButton,
                                QWidget,
                                QApplication,
                                QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut

class main_window(QMainWindow):
    def __init__(self):
       
        super().__init__()
        self.setWindowTitle("Mental Math Master")
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)
        self.title = QLabel("Mental Math Master")
        self.title.setAlignment(Qt.AlignCenter)
        self.start = QPushButton("Start")
        self.modifiers = QPushButton("Modifiers")
        self.quit = QPushButton("Quit")
        self.quit.clicked.connect(self.are_you_sure)



        layout.addWidget(self.title)
        layout.addWidget(self.start)
        layout.addWidget(self.modifiers)
        layout.addWidget(self.quit)
        ''' Lable(Title) 
            Button(Start)
            Button(Modifiers)
            Button(Exit)
            if modifiers:
                show menu
            if exit:
                prompt user if they actually want to leave'''
    def are_you_sure(self):
        if QMessageBox.question(self, "Exit", "Are you sure?") == QMessageBox.Yes:
            print("exit")
            sys.exit()
        elif QMessageBox.No:
            print("stay")
            

app = QApplication()
window = main_window()
window.resize(1000, 600)
window.show()
app.exec()
