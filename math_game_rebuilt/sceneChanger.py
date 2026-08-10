from PySide6.QtWidgets import (QStackedWidget)

class SceneChanger:
    def __init__(self):
        self.stack = QStackedWidget()
    
    def changeScene(self, scene):
        self.stack.setCurrentIndex(scene)