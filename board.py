import numpy as np

class Board():
    def __init__(self):
        #self.matrix = [ [ "BLANK" for _ in range(6) ] for _ in range(7) ]
        self.matrix = np.zeros((7,6))
        self.win = 0
        self.cols_open = 7

    '''
    Drop a piece onto the board. Accepts a column (integer) and a color (either "RED" or "YELLOW").
    Returns True for a successful drop or False for an unsuccessful drop (but no crash).
    '''
    def drop(self, column, color):
        if color == "RED" or color == "YELLOW":
            if color == "RED":
                color = 1
            else:
                color = 2
            if isinstance(column, int) and column >= 0 and column <= 6:
                return self.__place((column, 5), color)
            else:
                raise ValueError("'drop' given invalid column!")
        else:
            raise ValueError("'drop' given invalid color!")
    
    def __place(self, coords, color):
        #if coords[1] < 0 or self.matrix[coords[0]][coords[1]] != "BLANK" or self.win > 0:
        if coords[1] < 0 or self.matrix[coords[0], coords[1]] != 0 or self.win > 0:
            return False
        if not self.__place((coords[0], coords[1] - 1), color):
            #self.matrix[coords[0]][coords[1]] = color
            self.matrix[coords[0], coords[1]] = color
            if coords[1] == 5:
                self.cols_open -= 1
                if self.cols_open == 0:
                    self.win = 2
            self.__win_detect(coords)
        return True

    def __win_detect(self, coords):
        #color = self.matrix[coords[0]][coords[1]]
        color = self.matrix[coords[0], coords[1]]
        if self.__win_recursive((coords[0] + 1, coords[1]), 0, color) + self.__win_recursive((coords[0] - 1, coords[1]), 4, color) > 2:
            self.win = 1
            return
        if self.__win_recursive((coords[0]+1, coords[1]+1), 1, color) + self.__win_recursive((coords[0]-1, coords[1]-1), 5, color) > 2:
            self.win = 1
            return
        if self.__win_recursive((coords[0], coords[1] + 1), 2, color) + self.__win_recursive((coords[0], coords[1] - 1), 6, color) > 2:
            self.win = 1
            return
        if self.__win_recursive((coords[0]-1, coords[1]+1), 3, color) + self.__win_recursive((coords[0]+1, coords[1]-1), 7, color) > 2:
            self.win = 1
        
    def __win_recursive(self, coords, direction, color):
        if coords[0] < 0 or coords[0] > 6 or coords[1] < 0 or coords[1] > 5:
            return 0
        #if self.matrix[coords[0]][coords[1]] == color:
        if self.matrix[coords[0], coords[1]] == color:
            if direction == 0:
                return 1 + self.__win_recursive((coords[0], coords[1] + 1), direction, color)
            elif direction == 1:
                return 1 + self.__win_recursive((coords[0] + 1, coords[1] + 1), direction, color)
            elif direction == 2:
                return 1 + self.__win_recursive((coords[0], coords[1] + 1), direction, color)
            elif direction == 3:
                return 1 + self.__win_recursive((coords[0] - 1, coords[1] + 1), direction, color)
            elif direction == 4:
                return 1 + self.__win_recursive((coords[0] - 1, coords[1]), direction, color)
            elif direction == 5:
                return 1 + self.__win_recursive((coords[0] - 1, coords[1] - 1), direction, color)
            elif direction == 6:
                return 1 + self.__win_recursive((coords[0], coords[1] - 1), direction, color)
            else:
                return 1 + self.__win_recursive((coords[0] + 1, coords[1] - 1), direction, color)
        return 0
