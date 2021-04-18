import numpy
import random


class Block:

    def __init__(self):
        self.grid = numpy.zeros((2, 4))
        self.type = 0

    def regenerate(self):

        self.grid = numpy.zeros((2, 4))
        self.type = random.randint(0, 6)

        if self.type == 0:
            self.grid[0][1] = self.grid[0][2] = self.grid[1][1] = self.grid[1][2] = -1
        elif self.type == 1:
            self.grid[0][2] = self.grid[0][3] = self.grid[1][1] = self.grid[1][2] = -1
        elif self.type == 2:
            self.grid[0][1] = self.grid[0][2] = self.grid[1][2] = self.grid[1][3] = -1
        elif self.type == 3:
            self.grid[0][1] = self.grid[1][1] = self.grid[1][2] = self.grid[1][3] = -1
        elif self.type == 4:
            self.grid[0][3] = self.grid[1][1] = self.grid[1][2] = self.grid[1][3] = -1
        elif self.type == 5:
            self.grid[0][2] = self.grid[1][1] = self.grid[1][2] = self.grid[1][3] = -1
        else:
            self.grid[0][0] = self.grid[0][1] = self.grid[0][2] = self.grid[0][3] = -1

    def transform(self):

        if self.grid.shape[0] == 2:

            target = numpy.zeros((4, 2))

            if self.type == 6:
                for i in range(4):
                    target[i][0] = self.grid[0][i]
            else:
                for i in range(4):
                    for j in range(2):
                        target[i][j] = self.grid[1 - j][i]

            self.grid = target

        else:

            target = numpy.zeros((2, 4))

            if self.type == 6:
                for i in range(4):
                    target[0][i] = self.grid[i][0]
            elif self.type == 0:
                for i in range(4):
                    for j in range(2):
                        target[1 - j][i] = self.grid[i][j]
            else:
                for i in range(1, 4):
                    for j in range(2):
                        target[j][i] = self.grid[4 - i][j]

            self.grid = target

    def getType(self):
        return self.type

    def getGrid(self):
        return self.grid
