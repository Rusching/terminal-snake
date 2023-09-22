import random
from random import randint as ri
from collections import deque
from colorama import init, Fore, Style
import pdb

init(autoreset=True)

class Board(object):

    COLORS = {
        3: Fore.BLUE + Style.BRIGHT,
        2: Fore.GREEN,
        1: Fore.RED,
        0: Fore.YELLOW,
    }

    def __init__(self) -> None:
        # on board:
        # 0: empty
        # 1: apple
        # 2: snake body
        # 3: snake head

        self.width = 12
        self.height = 12
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.margins = {'left': 10, 'top': 10, 'bottom': 10}
        
        self.die = False
        self.snake = deque([(3, 3)])
        self.speed = 0.002
        self.direction = 'u'
        self.moveSwitch = False

        self.markSnake()        
        self.board[5][5] = 1


    def markSnake(self) -> None:
        # mark 2 as snake body, 3 as snake head
        hx, hy = self.snake[0]
        self.board[hx][hy] = 3
        if len(self.snake) > 1:
            for i in range(1, len(self.snake)):
                self.board[self.snake[i][0]][self.snake[i][1]] = 2

    def genApple(self) -> None:
        # marked as 1 apple
        x, y = ri(0, self.height - 1), ri(0, self.width - 1)
        while (x, y) in self.snake:
            x, y = ri(0, self.height - 1), ri(0, self.width - 1)
        self.board[x][y] = 1

    def move(self, dirc) -> None:
        headx, heady = self.snake[0]
        if dirc == 'u': nx, ny = headx - 1 if headx != 0 else self.height - 1, heady
        if dirc == 'd': nx, ny = headx + 1 if headx != self.height - 1 else 0, heady
        if dirc == 'l': nx, ny = headx, heady - 1 if heady != 0 else self.width - 1
        if dirc == 'r': nx, ny = headx, heady + 1 if heady != self.width - 1 else 0
        if self.board[nx][ny] == 2:
            self.die = True
            return False
        if self.board[nx][ny] == 1:
            # eat an apple and grow one length
            self.snake.insert(0, (nx, ny))
            self.board[nx][ny] = 2
            self.genApple()
        else:
            # move forward

            # first erase the tail from board
            tx, ty = self.snake[-1]
            self.board[tx][ty] = 0

            # perform move
            self.snake.pop()
            self.snake.insert(0, (nx, ny))
            
            # mark on board
            self.markSnake()

    def getCellStr(self, x, y) -> None:
        curCell = self.board[x][y]
        if curCell == 0: return self.COLORS.get(curCell) + "%2s"%' ' + Style.RESET_ALL
        elif curCell == 1: return self.COLORS.get(curCell) + "%2s"%'a' + Style.RESET_ALL
        elif curCell == 2: return self.COLORS.get(curCell) + "%2s"%'s' + Style.RESET_ALL
        else: return self.COLORS.get(curCell) + "%2s"%'h' + Style.RESET_ALL

    def printBoard(self) -> None:
        for i in range(self.height): print(self.board[i])

    def __str__(self) -> None:
        
        topMargin = '\n' * self.margins.get('top', 0) + ' ' * (self.margins.get('left', 0) + 1) + '-' * self.width * 2 + '\n'
        bottomMargin = ' ' * (self.margins.get('left', 0) + 1) + '-' * self.width * 2 + '\n' + '\n' * self.margins.get('bottom', 0)
        boardStr = ""
        for row in range(self.height):
            boardStr += ' ' * self.margins.get('left', 0) + '|' + "".join([self.getCellStr(row, i) for i in range(self.width)]) + '|\n'
        return topMargin + boardStr + bottomMargin
        