from enum import Enum 

class GameStatus(Enum):
    Starting = 0
    Running = 1
    Win = 2
    Lose = 3
    Pause = 4
    Stopping = 5
    Exit = 6
    GameOver = 7