from PySide6.QtWidgets import (QWidget,
                               QPushButton,
                               QLabel,
                               QVBoxLayout,
                               QHBoxLayout,
                               QSlider)
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
import sys


class MainMenu(QWidget):
    def __init__(self, sceneChanger):
        super().__init__()
        
        self.sceneChanger = sceneChanger
        self.label = QLabel("Mental Math Master")
        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.start)

        self.settingsButton = QPushButton("Settings")
        self.settingsButton.clicked.connect(self.settings)
        self.soundLabel = QLabel("Sound: 100%", self)
        self.soundSlider = QSlider(Qt.Horizontal)
        self.soundSlider.setRange(0, 100)
        self.soundSlider.setValue(100)
        self.soundSlider.valueChanged.connect(self.soundValue)


        self.exitButton = QPushButton("Exit")
        self.exitButton.clicked.connect(self.exit)
        self.yesButton = QPushButton("Yes")
        self.yesButton.clicked.connect(self.yes)
        self.noButton = QPushButton("No")
        self.noButton.clicked.connect(self.no)
        self.hbox = QHBoxLayout()



        self.initUI()
        self.initAudio()
    def initUI(self):
        self.setWindowTitle("Mental Math Master -- Main Menu")
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.startButton)
        self.vbox.addWidget(self.settingsButton)
        self.vbox.addWidget(self.exitButton)

        self.vbox.addLayout(self.hbox)
        self.hbox.addWidget(self.soundLabel)
        self.hbox.addWidget(self.soundSlider)
        #Find a way to make the slider horizontal
        #And find a way to make a new line
        self.hbox.addWidget(self.yesButton)
        self.hbox.addWidget(self.noButton)
        self.soundLabel.hide()
        self.soundSlider.hide()
        self.yesButton.hide()
        self.noButton.hide()
        self.setStyleSheet("""
""")

    def initAudio(self):
        self.mediaPlayer = QMediaPlayer()
        self.sound = QAudioOutput

    def start(self):
        self.sceneChanger.changeScene(1)

    def exit(self):
        self.startButton.hide()
        self.settingsButton.hide()
        self.exitButton.hide()
        self.label.setText("Are you sure?")
        self.yesButton.show()
        self.noButton.show()

    def yes(self):
        sys.exit()

    def no(self):
        self.label.setText("Mental Math Master")
        self.startButton.show()
        self.settingsButton.show()
        self.exitButton.show()
        self.yesButton.hide()
        self.noButton.hide()
    def settings(self):
        self.label.setText("Settings")
        self.startButton.hide()
        self.settingsButton.hide()
        self.exitButton.hide()
        self.soundLabel.show()
        self.soundSlider.show()
        #Change value of soundLabel
    def soundValue(self, value):
        self.soundLabel.setText(f"Sound: {value}%")
       



    
    
        