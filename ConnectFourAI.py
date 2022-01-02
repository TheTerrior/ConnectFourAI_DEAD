#from base import *
#from models import Player, Generation, Rank, NeuralNetwork, Layer, Perceptron
from session import Session

#temp:
from board import Board



#Base.metadata.create_all(engine)


#x = Perceptron(4, [1, 2, 3, 4])
#session.add(x)
#session.commit()

#x = Query(Perceptron)
#for i in x:
#    print(i.id)


'''
Ideally this page should contain minimal code, allowing the rest of the program to run basically independently

How board info should be transferred:
    Should be represented as a list of lists of Tiles (from board.py), where [0][0] is the bottom left 
    and [6][5] the top right. This will be the case for all locations where board info is required.
'''

def main():
    sesh = Session()
    b = Board()


main()
