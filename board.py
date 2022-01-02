class Board():
    def __init__(self):
        self.matrix = [ [ Tile((x, y)) for y in range(5) ] for x in range(6) ]
        self.win = False

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

    '''
    def __adjacent_generator(self, coords):
        yield 0, matrix[coords[0]][coords[1] + 1], matrix[coords[0]][coords[1] - 1]
        yield 1, matrix[coords[0] + 1][coords[1] + 1], matrix[coords[0] - 1][coords[1] - 1]
        yield 2, matrix[coords[0] + 1][coords[1]], matrix[coords[0] - 1][coords[1]]
        yield 3, matrix[coords[0] - 1][coords[1] + 1], matrix[coords[0] + 1][coords[1] - 1]

    def __update_new_tile(self, coords):
        cur = matrix[coords[0]][coords[1]]
        for direction, checkpos, checkneg, coords in __adjacent_generator(coords):
            cur.adjacent[direction] = ((checkpos.adjacent if checkpos.color == cur.color else 0) +
                (checkneg.adjacent if checkneg.color == cur.color else 0) + 1)
            if checkpos.color == cur.color:
                __update_tiles(checkpos.color)
            if checkneg.color == cur.color:
                __update_tiles(checkneg.color)
        ''
        cur.adjacent = ((checkpos.adjacent if checkpos.color == cur.color else 0) +
            (checkneg.adjacent if checkneg.color == cur.color else 0) + 1)
        ''
    '''

    def __update_new_tile(coords):
        cur = matrix[coords[0]][coords[1]]
        
    def __update_tiles(self, tile, direction, checked):
        pass

class Tile():

    def __init__(self, coords, color = "BLANK"):
        if color in ["BLANK", "RED", "YELLOW"]:
            self.color = color
            self.adjacent = [0, 0, 0, 0]
            self.coords = coords
        else:
            print("Warning: The provided color was invalid. Defaulting to \"BLANK\"")

    

