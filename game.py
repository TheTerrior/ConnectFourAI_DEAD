from board import *
from userinterface import Player
from models import NeuralNetwork

class Game():

    def __init__(self, player1, player2):
        self.board = Board()
        if isinstance(player1, NeuralNetwork) or isinstance(player1, Player):
            if isinstance(player2, NeuralNetwork) or isinstance(player2, Player):
                self.player1 = player1
                self.player2 = player2
                self.turn = True
            else:
                raise ValueError("Player2 is not a valid opponent type!")
        else:
            raise ValueError("Player1 is not a valid opponent type!")

    def board_info(self):
        return self.board.matrix

    #Will prompt the next player to make a move, then return whether a win has occurred and the last player to make a move
    def next_turn(self):
        if self.turn: #Player1's turn
            move = self.player1.prompt_turn(generate_board_info())
        else: #Player2's turn
            move = self.player2.prompt_turn(generate_board_info())
        self.turn = not self.turn
