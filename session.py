from base import *
from models import Player, Generation, Rank, NeuralNetwork, Layer, Perceptron

class Session():
    def __init__(self):
        Base.metadata.create_all(engine) #ensure all tables are created and database exists


