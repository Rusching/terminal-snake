import msvcrt
from board import Board
import os
import time

legalKeys = {'u', 'l', 'd', 'r', 'q'}

KeyMap = {
    105: 'u', # i 
    106: 'l', # j
    107: 'd', # k
    108: 'r', # l
    113: 'q', # q
}

def getKey():
        """Return a key pressed by the user"""
        while True:
            if msvcrt.kbhit():
                a = ord(msvcrt.getch())
                return KeyMap.get(a, 'n')

class Game(object):
    def __init__(self) -> None:
        self.board = Board()
        self.score = 0
        self.__is_windows = True
        self.clear_screen = True

    def clearScreen(self):
        """Clear the console"""
        if self.clear_screen:
            os.system('cls' if self.__is_windows else 'clear')
        else:
            print('\n')

    def mainLoop(self) -> int:
        dirc = 'u'
        while True:
            self.clearScreen()
            print(self.board.__str__())
            # if 
            if msvcrt.kbhit():
                a = ord(msvcrt.getch())
                k = KeyMap.get(a, 'n')
                if k not in legalKeys: continue
                if k == 'q': break
                dirc = k
            self.board.move(dirc)
            time.sleep(0.2)
            

if __name__ == "__main__":
    g = Game()
    g.mainLoop()