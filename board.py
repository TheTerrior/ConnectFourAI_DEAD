class Board():
    def __init__(self):
        pass

    #Drop a piece onto the board. Accepts a column (integer) and a color (either "RED" or "YELLOW")
    def drop(self, column, color):
        if color == "RED" or color == "YELLOW":
            if isinstance(column, int) and column >= 0 and column <= 6:
                pass
            else:
                raise ValueError("'drop' given invalid column!")
        else:
            raise ValueError("'drop' given invalid color!")

class Tile():

    def __init__(self, color = "BLANK"):
        if color in ["BLANK", "RED", "YELLOW"]:
            self.color = color
            self.adjacent = 0
        else:
            print("Warning: The provided color was invalid. Defaulting to \"BLANK\"")

    

