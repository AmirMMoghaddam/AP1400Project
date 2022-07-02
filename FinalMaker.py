import copy
from Backtracker import *
from genartor import *
import random
from random import seed
from random import randint
from time import time


class Earaser:
    def __init__(self, FullPuzzle, Number):
        self.puzzle = FullPuzzle
        self.index = 0
        self.Enumb = Number
        self.counter = 0  # number of unearased members
        self.taken = list(range(1, 82))  # A list for elements that are earased
        self.uniqueness = True

    def indexDecoding(self, numb):
        a = 0
        number = numb
        while number > 9:
            number = number - 9
            a += 1
        return [a, number - 1]

    def GetUntakenIndex(self):
        a = random.choice(self.taken)
        self.index = self.indexDecoding(a)
        self.taken.remove(a)

    def checkIfUnique(self):
        temp = copy.deepcopy(self.puzzle)
        self.uniqueness = sudoku(temp, self.counter)

    def Earase(self):
        temp = self.puzzle
        self.GetUntakenIndex()
        for i in range(self.Enumb+1):
            self.GetUntakenIndex()
            a = temp[self.index[0]][self.index[1]]
            temp[self.index[0]][self.index[1]] = 0
            self.counter += 1
            self.checkIfUnique()
            while True:
                if self.uniqueness:
                    print("entered 1")
                    break

                else:
                    print("entered 2")
                    temp[self.index[0]][self.index[1]] = a
                    self.GetUntakenIndex()
                    a = temp[self.index[0]][self.index[1]]
                    temp[self.index[0]][self.index[1]] = 0
                    self.checkIfUnique()

    def starter(self):
        self.Earase()
        return self.puzzle


def RandomNumber(start, end):
    seed(time())
    return randint(start, end)


def startMaker(puzzle, number):
    myP = Earaser(puzzle, number)
    a = myP.starter()
    return a
