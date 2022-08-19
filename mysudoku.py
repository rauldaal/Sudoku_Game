from pickletools import float8
from turtle import pos, position
import numpy as np
from random import random, shuffle, seed as random_seed, randrange
import sys
from typing import Iterable, List, Optional, Tuple, Union, cast


class Sudoku:
    _zero = 0

    def __init__(self, width = 3, board=None, difficulty = 0.5, seed = randrange(sys.maxsize)) -> None:
        self.__width = width
        #We don't consider height as it will be the same as width
        self.__size = width*width
        self.__difficulty = difficulty

        assert self.__size == 9
        assert self.__width == 3
        assert 0 < difficulty < 1
        

        if board:
            empty = 0
            assert board is np.array
            self.__board = board
            for row in self.__board:
                for i in range(len(row)):
                    if not row[i] in range(1, self.__size+1):
                        row[i] = Sudoku._zero
                        empty += 1
            if difficulty == None:
                if self.validate():
                    self.__difficulty = empty / (self.__size ** 2)
                else:
                    self.__difficulty = -2
        else:
            positions = list(range(self.__size))
            num = list(range(self.__size))
            random_seed(seed)
            shuffle(positions)
            shuffle(num)
            self.__board = np.zeros((9,9), int)
            for i in range(self.__size):
                for j in range(self.__size):
                    if i == positions[j]: 
                        self.__board[i][j] = num[i]+1

    def difficulty(self, difficulty):
       assert 0< difficulty< 1
       index =  list(range(self.__size * self.__size))
       shuffle(index)
       solved_board = self.solve()
       for index in index[:self.__size*self.__size*self.__difficulty]

s = Sudoku()
print(s)