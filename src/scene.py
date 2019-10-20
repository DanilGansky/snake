from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QPen, QColor, QBrush, QFont
from PyQt5.QtCore import QRectF, QTimer
from src.snake import Snake
from random import randint
import time


class ScoreText(QGraphicsTextItem):
    def __init__(self, score_text, x, y):
        super().__init__()

        self.setHtml(score_text)
        self.setFont(QFont('Noto Sans', 16, 70))
        self.setDefaultTextColor(QColor('cyan'))
        self.setX(x)
        self.setY(y)


class GameScene(QGraphicsScene):
    """Custom QGraphicsScene"""
    def __init__(self, food_count, update_rate, statistic_list):
        super().__init__()

        self.sceneRect = QRectF(0.0, 0.0, 500.0, 500.0)
        self.setSceneRect(self.sceneRect)
        self.width = int(self.width())
        self.height = int(self.height())
        self.snake = None
        self.timer = QTimer()
        self.timer_snake = QTimer()
        self.update_rate = update_rate
        self.food_count = food_count
        self.food_items = []
        self.score = 0
        self.statistic_list = statistic_list
        self.time = 0
        self.game_status = False

        self.startUpdate()

        # Signals
        self.timer.timeout.connect(self.update)
        self.timer_snake.timeout.connect(self.killSnake)

    def startUpdate(self):
        self.timer.start(self.update_rate)
        self.timer_snake.start(self.update_rate)
        self.game_status = True

    def pauseUpdate(self):
        self.timer.stop()
        self.timer_snake.stop()

    def drawGrid(self):
        for row in range(0, self.height + 20, 20):
            for column in range(0, self.width + 20, 20):
                self.addLine(0, row, self.width, row, 
                             QPen(QColor('white'), 1))
                self.addLine(column, 0, column, self.height,
                             QPen(QColor('white'), 1))

    def createSnake(self):
        self.snake = Snake(0.0, 0.0)
        self.createFood()
        self.time = time.time()

        return self.snake

    def update(self):
        self.clear()
        self.drawGrid()
        self.placeFood()
        self.updateScore()
        self.catchFood()
        self.drawSnake()

    def killSnake(self):
        if self.snake.x not in range(0, self.width) or \
           self.snake.y not in range(0, self.height) or\
           self.snake.pos() in self.snake.positions[2:]:
            self.time = round(time.time() - self.time, 3)
            self.statistic_list.addItem('Game finished: {} s. Score: {}'\
                               .format(self.time, self.score))

            self.pauseUpdate()
            self.game_status = False


    def createFood(self):
        for item in range(self.food_count):
            random_x = abs(round(randint(0, self.width) / 20) * 20 - 20)
            random_y = abs(round(randint(0, self.height) / 20) * 20 - 20)
            food_item = QRectF(random_x, random_y, 20, 20)

            while food_item in self.food_items:
                random_x = abs(round(randint(0, self.width) / 20) * 20 - 20)
                random_y = abs(round(randint(0, self.height) / 20) * 20 - 20)
                food_item = QRectF(random_x, random_y, 20, 20)

            self.food_items.append(food_item)

    def placeFood(self):
        for item in self.food_items:
            self.addRect(item, QPen(QColor('white'), 1),
                         QBrush(QColor('red')))

    def updateScore(self):
        self.addItem(ScoreText('Score: {}'.format(self.score), -30, -40))

    def catchFood(self):
        for index, item in enumerate(self.food_items):
            if self.snake.pos() == (item.x(), item.y()):
                self.score += 10
                del self.food_items[index]
                self.snake.eat()

        if not self.food_items:
            self.createFood()

    def drawSnake(self):
        for index, pos in enumerate(self.snake.positions):
            self.addRect(pos[0], pos[1], 20, 20,
                     QPen(QColor('white'), 1),
                     QBrush(QColor('green')))

            if index == 0:
                self.addRect(pos[0] + 8, pos[1] + 8, 4, 4,
                     QPen(QColor('yellow'), 1),
                     QBrush(QColor('yellow')))

    def getStatus(self):
        return self.game_status
