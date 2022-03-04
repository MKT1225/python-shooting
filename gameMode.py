from enum import Enum

class GameMode(Enum):
    START    = 0;
    GAME     = 1;
    BOSS     = 2;
    CLEAR    = 3;
    GAMEOVER = 4;