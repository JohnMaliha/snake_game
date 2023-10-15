import pygame
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
    Crashed = 8 


class Direction(Enum):
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT


class Messages(Enum):
    WELCOME = 'Welcome to Snake Game! Press the up or down key twice to start'
    GAME_OVER = 'Game Over!!'
    APP_NAME = 'Snake Game By John'
    EXIT_MSG = 'Thank you for playing! Exiting game'
    GAME_PAUSED = 'Game Paused. Press s to resume'