class Board():
    def __init__(self):
        self.matrix = [ [ Tile() for _ in range(5) ] for _ in range(6) ]

    '''
    Drop a piece onto the board. Accepts a column (integer) and a color (either "RED" or "YELLOW").
    Returns True for a successful drop or False for an unsuccessful drop (but no crash).
    '''
    def drop(self, column, color):
        if color == "RED" or color == "YELLOW":
            if isinstance(column, int) and column >= 0 and column <= 6:
                return __place((column, 5))
            else:
                raise ValueError("'drop' given invalid column!")
        else:
            raise ValueError("'drop' given invalid color!")
    
    def __place(self, coords, color):
        if coords[1] < 0 or matrix[coords[0]][coords[1]].color != "BLANK":
            return False
        if not __place((coords[0], coords[1] - 1), color):
            matrix[coords[0]][coords[1]].color = color
            __update_new_tile(coords)
        return True

    def __update_new_tile(self, coords):
        pass

    def __update_tiles(self, coords, direction):
        pass

class Tile():

    def __init__(self, color = "BLANK"):
        if color in ["BLANK", "RED", "YELLOW"]:
            self.color = color
            self.adjacent = 0
        else:
            print("Warning: The provided color was invalid. Defaulting to \"BLANK\"")

    

