from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, Qt
from src.widget import Ui_Form
from src.scene import GameScene
import sys


class SnakeGame(Ui_Form, QWidget):
    """Simple snake game"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer()
        self.game_status = False
        self.scene = None
        
        # Signals
        self.pushButton.clicked.connect(self.startGame)
        self.pushButton_2.clicked.connect(self.pauseGame)

    def startGame(self):
        if not self.scene or not self.scene.getStatus():
            self.food_count = self.spinBox.value()
            self.update_rate = self.spinBox_2.value()
            self.scene = GameScene(self.food_count,
                                   self.update_rate,
                                   self.listWidget)
            
            self.snake = self.scene.createSnake()
            self.graphicsView.setScene(self.scene)
            self.timer.timeout.connect(self.snake.moveByDirection)

        self.timer.start(self.update_rate)
        self.game_status = True
        self.scene.startUpdate()

    def pauseGame(self):
        if self.scene:
            self.scene.pauseUpdate()

        self.timer.stop()
        self.game_status = False

    def keyPressEvent(self, event):
        if self.game_status:
            if event.key() == Qt.Key_W:
                self.snake.direction = self.snake.moveUp
            elif event.key() == Qt.Key_S:
                self.snake.direction = self.snake.moveDown
            elif event.key() == Qt.Key_A:
                self.snake.direction = self.snake.moveLeft
            elif event.key() == Qt.Key_D:
                self.snake.direction = self.snake.moveRight


def main():
    app = QApplication(sys.argv)
    snake_game = SnakeGame()
    snake_game.show()
    app.exec_()
    app.deleteLater()
    sys.exit()


if __name__ == '__main__':
    main()
