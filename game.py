import msvcrt
from board import Board
import os
import time
import threading

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
        self.dirc = 'u'
        self.lock = threading.Lock()
        self.end = False

    def clearScreen(self):
        """Clear the console"""
        if self.clear_screen:
            os.system('cls' if self.__is_windows else 'clear')
        else:
            print('\n')

    def input_thread(self):
        # listen to user input

        global dirc
        while True:
            if msvcrt.kbhit():
                a = ord(msvcrt.getch())
                k = KeyMap.get(a, 'n')
                if k not in legalKeys:
                    continue
                
                # Prevent reverse direction change (as before)
                # ...

                with self.lock:
                    if k == 'q':
                        self.end = True
                    self.dirc = k

    def mainLoop(self) -> int:
        threading.Thread(target=self.input_thread, daemon=True).start()  # daemon=True ensures the thread exits when main program exits
        cdirc = self.dirc
        while not self.end:
            self.clearScreen()
            print(self.board.__str__())
            
            with self.lock:
                cdirc = self.dirc

            self.board.move(cdirc)
            time.sleep(0.01)
            

if __name__ == "__main__":
    g = Game()
    g.mainLoop()