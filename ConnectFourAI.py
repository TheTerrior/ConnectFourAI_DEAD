#from base import *
#from models import Player, Generation, Rank, NeuralNetwork, Layer, Perceptron
from session import Session




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
    Should be represented as a list of lists of Tiles (from board.py), where [0][0] is 
    the bottom left and [6][5] the top right.
'''

def main():
    sesh = Session()


main()
