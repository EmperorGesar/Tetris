import numpy


class Board:

    def __init__(self):

        self.grid = numpy.zeros((24, 12))

        for i in range(12):
            self.grid[23][i] = 1

        for i in range(24):
            self.grid[i][0] = self.grid[i][11] = 1

        self.hasBlock = False
        self.offset = [2, 4]

    def update(self, currentBlock):

        blockGrid = currentBlock.getGrid()

        if not self.hasBlock:

            if blockGrid.shape[0] == 2:
                for i in range(4):
                    self.grid[self.offset[0]][i + self.offset[1]] = blockGrid[0][i]
                    self.grid[self.offset[0] + 1][i + self.offset[1]] = blockGrid[1][i]
            else:
                for i in range(2):
                    self.grid[i + self.offset[0] - 1][self.offset[1] + 1] = blockGrid[0][i]
                    self.grid[i + self.offset[0] - 1][self.offset[1] + 2] = blockGrid[1][i]

            self.offset[0] += 1
            self.hasBlock = True

        else:

            valid = True

            if blockGrid.shape[0] == 2:

                for i in range(4):
                    if i + self.offset[1] < 11:
                        if self.grid[self.offset[0]][i + self.offset[1]] == 1 and blockGrid[0][i] == -1:
                            valid = False
                        elif self.grid[self.offset[0] + 1][i + self.offset[1]] == 1 and blockGrid[1][i] == -1:
                            valid = False

                if valid:

                    for i in range(23):
                        for j in range(1, 11):
                            if self.grid[i][j] == -1:
                                self.grid[i][j] = 0

                    for i in range(4):
                        if i + self.offset[1] < 11:
                            if blockGrid[0][i] == -1:
                                self.grid[self.offset[0]][i + self.offset[1]] = -1
                            if blockGrid[1][i] == -1:
                                self.grid[self.offset[0] + 1][i + self.offset[1]] = -1

                    self.offset[0] += 1

                else:

                    for i in range(23):
                        for j in range(1, 11):
                            if self.grid[i][j] == -1:
                                self.grid[i][j] = 1

                    self.hasBlock = False
                    self.offset = [2, 4]

            else:

                for i in range(4):
                    if i + self.offset[0] < 25:
                        if self.grid[i + self.offset[0] - 1][self.offset[1] + 1] == 1 and blockGrid[i][0] == -1:
                            valid = False
                        elif self.grid[i + self.offset[0] - 1][self.offset[1] + 2] == 1 and blockGrid[i][1] == -1:
                            valid = False

                if valid:

                    for i in range(23):
                        for j in range(1, 11):
                            if self.grid[i][j] == -1:
                                self.grid[i][j] = 0

                    for i in range(4):
                        if i + self.offset[0] < 25:
                            if blockGrid[i][0] == -1:
                                self.grid[i + self.offset[0] - 1][self.offset[1] + 1] = -1
                            if blockGrid[i][1] == -1:
                                self.grid[i + self.offset[0] - 1][self.offset[1] + 2] = -1

                    self.offset[0] += 1

                else:

                    for i in range(23):
                        for j in range(1, 11):
                            if self.grid[i][j] == -1:
                                self.grid[i][j] = 1

                    self.hasBlock = False
                    self.offset = [2, 4]

    def moveLeft(self, currentBlock):

        blockGrid = currentBlock.getGrid()
        valid = True

        if blockGrid.shape[0] == 2:

            for i in range(4):
                if i + self.offset[1] > 0:
                    if self.grid[self.offset[0] - 1][i + self.offset[1] - 1] == 1 and blockGrid[0][i] == -1:
                        valid = False
                    elif self.grid[self.offset[0]][i + self.offset[1] - 1] == 1 and blockGrid[1][i] == -1:
                        valid = False

            if valid:

                for i in range(23):
                    for j in range(1, 11):
                        if self.grid[i][j] == -1:
                            self.grid[i][j] = 0

                for i in range(4):
                    if i + self.offset[1] > 0:
                        if blockGrid[0][i] == -1:
                            self.grid[self.offset[0] - 1][i + self.offset[1] - 1] = -1
                        if blockGrid[1][i] == -1:
                            self.grid[self.offset[0]][i + self.offset[1] - 1] = -1

                self.offset[1] -= 1

        else:

            for i in range(4):
                if i + self.offset[1] > 0 and i + self.offset[0] < 24:
                    if self.grid[i + self.offset[0]][self.offset[1]] == 1 and blockGrid[i][0] == -1:
                        valid = False
                    elif self.grid[i + self.offset[0]][self.offset[1] + 1] == 1 and blockGrid[i][1] == -1:
                        valid = False

            if valid:

                for i in range(23):
                    for j in range(1, 11):
                        if self.grid[i][j] == -1:
                            self.grid[i][j] = 0

                for i in range(4):
                    if i + self.offset[1] > 0 and i + self.offset[0] < 24:
                        if blockGrid[i][0] == -1:
                            self.grid[i + self.offset[0]][self.offset[1]] = -1
                        if blockGrid[i][1] == -1:
                            self.grid[i + self.offset[0]][self.offset[1] + 1] = -1

                self.offset[1] -= 1

    def moveRight(self, currentBlock):

        blockGrid = currentBlock.getGrid()
        valid = True

        if blockGrid.shape[0] == 2:

            for i in range(4):
                if i + self.offset[1] < 11:
                    if self.grid[self.offset[0] - 1][i + self.offset[1] + 1] == 1 and blockGrid[0][i] == -1:
                        valid = False
                    elif self.grid[self.offset[0]][i + self.offset[1] + 1] == 1 and blockGrid[1][i] == -1:
                        valid = False

            if valid:

                for i in range(23):
                    for j in range(1, 11):
                        if self.grid[i][j] == -1:
                            self.grid[i][j] = 0

                for i in range(4):
                    if i + self.offset[1] < 11:
                        if blockGrid[0][i] == -1:
                            self.grid[self.offset[0] - 1][i + self.offset[1] + 1] = -1
                        if blockGrid[1][i] == -1:
                            self.grid[self.offset[0]][i + self.offset[1] + 1] = -1

                self.offset[1] += 1

        else:

            for i in range(4):
                if i + self.offset[1] < 12 and i + self.offset[0] < 24:
                    if self.grid[i + self.offset[0]][self.offset[1] + 2] == 1 and blockGrid[i][0] == -1:
                        valid = False
                    elif self.grid[i + self.offset[0]][self.offset[1] + 3] == 1 and blockGrid[i][1] == -1:
                        valid = False

            if valid:

                for i in range(23):
                    for j in range(1, 11):
                        if self.grid[i][j] == -1:
                            self.grid[i][j] = 0

                for i in range(4):
                    if i + self.offset[1] < 12 and i + self.offset[0] < 24:
                        if blockGrid[i][0] == -1:
                            self.grid[i + self.offset[0]][self.offset[1] + 2] = -1
                        if blockGrid[i][1] == -1:
                            self.grid[i + self.offset[0]][self.offset[1] + 3] = -1

                self.offset[1] += 1

    def clear(self):
        for i in range(3, 23):
            full = True
            for j in range(1, 11):
                if self.grid[i][j] == 0:
                    full = False
            if full:
                for k in range(i, 2, -1):
                    for j in range(1, 11):
                        self.grid[k][j] = self.grid[k - 1][j]

    def hasCurrentBlock(self):
        return self.hasBlock

    def getGrid(self):
        return self.grid
