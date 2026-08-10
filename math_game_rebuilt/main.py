from gameFoundation import (operations, difficultyData)
from sceneChanger import SceneChanger
import sys
from PySide6.QtWidgets import (QApplication)
from screens.difficultyScreen import DifficultyScreen
from screens.mainMenu import MainMenu
from game import Game




def main():
    app = QApplication()
    operators = operations.Operations()
    data = difficultyData.DifficultyData()
    difficulty = data.difficulty
    sceneChanger = SceneChanger()
    mainMenu = MainMenu(sceneChanger)
    difficultyScreen = DifficultyScreen(difficulty, sceneChanger)
    game = Game(sceneChanger, difficultyScreen, operators)
    sceneChanger.stack.addWidget(mainMenu)
    sceneChanger.stack.addWidget(difficultyScreen)
    sceneChanger.stack.addWidget(game)
    sceneChanger.changeScene(0)
    sceneChanger.stack.show()
    print(data.difficulty)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()