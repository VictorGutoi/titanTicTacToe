# from colorama import Fore


class Grid:
    def __init__(self):
        self.grid = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '
        ]

        self.won = False
        self.wonBy = 'X'

        self.ended = False
        self.toMove = False

    def move(self, playing):
        if not self.won and not self.ended:
            x = input('What is your move: ')
            if x in '123456789' and x != '':
                if 0 < int(x) < 10:
                    x = int(x) - 1
                    if self.grid[x] == " ":
                        self.grid[x] = playing

                        if x == 0:
                            return -1, -1
                        elif x == 1:
                            return -1, 0
                        elif x == 2:
                            return -1, 1
                        elif x == 3:
                            return 0, -1
                        elif x == 4:
                            return 0, 0
                        elif x == 5:
                            return 0, 1
                        elif x == 6:
                            return 1, -1
                        elif x == 7:
                            return 1, 0
                        elif x == 8:
                            return 1, 1
                    else:
                        return self.move(playing)
                else:
                    return self.move(playing)
            else:
                return self.move(playing)
        else:
            return 2, 2

    def gridDraw(self):
        # TODO draw colored

        if not self.won:
            return ('_____________',
                    '| ' + self.grid[0] + ' | ' + self.grid[1] + ' | ' + self.grid[2] + ' |',
                    '| ' + self.grid[3] + ' | ' + self.grid[4] + ' | ' + self.grid[5] + ' |',
                    '| ' + self.grid[6] + ' | ' + self.grid[7] + ' | ' + self.grid[8] + ' |')
        else:
            if self.wonBy == 'X':
                return ('_____________',
                        '|   \   /   |',
                        '|     X     |',
                        '|   /   \   |')

            else:
                return ('_____________',
                        '|  /-----\  |',
                        '|  |     |  |',
                        '|  \-----/  |')


class MediumGrid:
    def __init__(self):
        self.won = False
        self.wonBy = 'X'

        self.ended = False

        self.grid = [
            Grid(), Grid(), Grid(),
            Grid(), Grid(), Grid(),
            Grid(), Grid(), Grid()
        ]


class GiantGrid:
    def __init__(self):
        self.grid = [
            MediumGrid(), MediumGrid(), MediumGrid(),
            MediumGrid(), MediumGrid(), MediumGrid(),
            MediumGrid(), MediumGrid(), MediumGrid()
        ]


class Game:
    def __init__(self):
        self.table = GiantGrid()

        self.gridToPlayX = 4
        self.gridToPlayY = 4
        self.movingNow = 'X'

    def move(self):
        x, y = self.table \
            .grid[self.gridToPlayX - self.gridToPlayX % 3 + round((self.gridToPlayY - self.gridToPlayY % 3) / 3)] \
            .grid[self.gridToPlayY % 3 + (self.gridToPlayX % 3) * 3] \
            .move(self.movingNow)

        if x != 2 and y != 2:
            self.gridToPlayX += x
            self.gridToPlayY += y

            if self.gridToPlayX > 8:
                self.gridToPlayX = 0
            elif self.gridToPlayX < 0:
                self.gridToPlayX = 8

            if self.gridToPlayY > 8:
                self.gridToPlayY = 0
            elif self.gridToPlayY < 0:
                self.gridToPlayY = 8

            if self.movingNow == 'X':
                self.movingNow = 'O'
            else:
                self.movingNow = 'X'

        else:
            xy, x2, y2 = self.chooseGrid()

            x1, y1 = xy

            x1 += x2
            y1 += y2

            self.gridToPlayX = x1
            self.gridToPlayY = y1

            if self.gridToPlayY > 8:
                self.gridToPlayY = 0
            elif self.gridToPlayY < 0:
                self.gridToPlayY = 8

            if self.movingNow == 'X':
                self.movingNow = 'O'
            else:
                self.movingNow = 'X'

        self.testIfWonSmallGrid()

    def chooseGrid(self):
        giant = input("What giant grid you choose: ")
        medium = input("Wht medium grid you choose: ")

        if giant in "123456789" and not '':
            if medium in "123456789" and not '' and 0 < int(giant) < 10:
                if 0 < int(medium) < 10:
                    giant = int(giant) - 1
                    medium = int(medium) - 1

                    if not self.table.grid[giant].grid[medium].ended:
                        return self.table.grid[giant].grid[medium].move(self.movingNow), giant, medium
                else:
                    self.chooseGrid()
            else:
                self.chooseGrid()
        else:
            self.chooseGrid()

    def testIfWonSmallGrid(self):
        for x in self.table.grid:
            for y in x.grid:
                # Horizontal
                for a in range(2):
                    if y.grid[a * 3] == y.grid[a * 3 + 1] == y.grid[a * 3 + 2] != ' ':
                        y.ended = True
                        y.won = True

                        y.wonBy = y.grid[a * 3]

                # Vertical
                for a in range(2):
                    if y.grid[0 + a] == y.grid[3 + a] == y.grid[6 + a] != ' ':
                        y.ended = True
                        y.won = True

                        y.wonBy = y.grid[0 + a]

                # Diagonal
                if y.grid[0] == y.grid[4] == y.grid[8] != ' ':
                    y.ended = True
                    y.won = True

                    y.wonBy = y.grid[0]

                if y.grid[2] == y.grid[4] == y.grid[6] != ' ':
                    y.ended = True
                    y.won = True

                    y.wonBy = y.grid[2]

    def testIfWonMediumGrid(self):
        for y in self.table.grid:
            # Horizontal
            for a in range(2):
                if y.grid[a * 3].wonBy == y.grid[a * 3 + 1].wonBy == y.grid[a * 3 + 2].wonBy != ' ':
                    y.ended = True
                    y.won = True

                    y.wonBy = y.grid[a * 3].wonBy

            # Vertical
            for a in range(2):
                if y.grid[0 + a].wonBy == y.grid[3 + a].wonBy == y.grid[6 + a].wonBy != ' ':
                    y.ended = True
                    y.won = True

                    y.wonBy = y.grid[0 + a].wonBy

            # Diagonal
            if y.grid[0].wonBy == y.grid[4].wonBy == y.grid[8].wonBy != ' ':
                y.ended = True
                y.won = True

                y.wonBy = y.grid[0].wonBy

            if y.grid[2].wonBy == y.grid[4].wonBy == y.grid[6].wonBy != ' ':
                y.ended = True
                y.won = True

                y.wonBy = y.grid[2].wonBy



    # TODO test if won medium and large grid

    def draw(self):
        a = [
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 0, 1, 1, 1, 2, 2, 2],

            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],
            [3, 3, 3, 4, 4, 4, 5, 5, 5],

            [6, 6, 6, 7, 7, 7, 8, 8, 8],
            [6, 6, 6, 7, 7, 7, 8, 8, 8],
            [6, 6, 6, 7, 7, 7, 8, 8, 8]
        ]
        b = [
            [0, 1, 2, 0, 1, 2, 0, 1, 2],
            [3, 4, 5, 3, 4, 5, 3, 4, 5],
            [6, 7, 8, 6, 7, 8, 6, 7, 8],

            [0, 1, 2, 0, 1, 2, 0, 1, 2],
            [3, 4, 5, 3, 4, 5, 3, 4, 5],
            [6, 7, 8, 6, 7, 8, 6, 7, 8],

            [0, 1, 2, 0, 1, 2, 0, 1, 2],
            [3, 4, 5, 3, 4, 5, 3, 4, 5],
            [6, 7, 8, 6, 7, 8, 6, 7, 8]
        ]
        for x in range(0, 9):
            row1 = ''
            row2 = ''
            row3 = ''
            row4 = ''

            for y in range(0, 9):
                _1, _2, _3, _4 = self.table.grid[a[x][y]].grid[b[x][y]].gridDraw()

                row1 += _1
                row2 += _2
                row3 += _3
                row4 += _4

            print(row1)
            print(row2)
            print(row3)
            print(row4)
