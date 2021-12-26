class Player:

    '''
    window = the window object itself from PySimpleGUI
    '''

    def __init__():
        '''
        Initiate a new GUI 
        '''
        pass
    
    def prompt_turn():
        pass

class AI: #this may just be merged with NeuralNetwork in the future to reduce redundancy
    '''
    nnet = the neural network object which contains all its weights
    '''

    def __init__():
        '''
        '''
        pass

    def prompt_turn():
        pass

class NeuralNetwork:

    layers = [] #contains all the layers of perceptrons, a single layer means a single layer after the input

    def __init__(layers = 1, sizes = [1]):
        if isinstance(layers, int):
            if isinstance(sizes, list):
                if len(sizes) == layers:
                    for i in range(0, layers):
                        newlayer = []
                        if i == 0: #if this is the first layer, hence we know the amount of inputs
                            for j in range(0, sizes[i]):
                                newlayer.append(Perceptron(inputs = 42))
                        else: #if this is a recursively made layer
                            for j in range(0, sizes[i]):
                                newlayer.append(Perceptron(inputs = sizes[i-1]))
                        self.layers.append(newlayer)
                else:
                    raise ValueError("Received {} sizes of layers for {} layers.".format(len(sizes), layers))
            else:
                raise ValueError("Parameter 'sizes' was not a list!")
        else:
            raise ValueError("Parameter 'layers' was not an integer!")

class Perceptron:

    def __init__(inputs, weights, bias): #inputs is the number of inputs to this perceptron, weights is a list of weights for each input
        if isinstance(inputs, int):
            self.inputs = inputs
        else:
            raise ValueError("Parameter 'inputs' was not an integer!")
        '''
        implement the weights and the bias
        '''