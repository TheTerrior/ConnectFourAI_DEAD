class Player:

    '''
    window = the window object itself from PySimpleGUI
    '''

    def __init__():
        '''
        Initiate a new GUI 
        '''
        pass
    
    #prompt the user to input a location for the new piece, check if input is valid
    def prompt_turn(board):
        pass

class NeuralNetwork:

    #initiate the new neural network given the optional parameters
    def __init__(layers = 1, sizes = [1], mutability = 0.5):
        if isinstance(layers, int):
            if isinstance(sizes, list):
                if len(sizes) == layers:

                    layers = [] #contains all layers of perceptrons, a single layer means a single layer after the input
                    for i in range(0, layers):
                        newlayer = []
                        if i == 0: #if this is the first layer, hence we know the amount of inputs
                            for j in range(0, sizes[i]):
                                newlayer.append(Perceptron(inputs = 42))
                        else: #if this is a recursively made layer
                            for j in range(0, sizes[i]):
                                newlayer.append(Perceptron(inputs = sizes[i-1]))
                        layers.append(tuple(newlayer))
                    self.layers = tuple(layers)

                    if isinstance(mutability, float) or isinstance(mutability, int):
                        self.mutability = mutability
                    else:
                        print("Warning: The provided mutability was not an integer. Defaulting to 0.5.")
                        self.mutability = 0.5

                else:
                    raise ValueError("Received {} sizes of layers for {} layers.".format(len(sizes), layers))
            else:
                raise ValueError("Parameter 'sizes' was not a list!")
        else:
            raise ValueError("Parameter 'layers' was not an integer!")

    #send board info to the neural network and generate an output. If main output is invalid, choose the next valid output
    def prompt_turn(board):
        pass

class Perceptron:

    #initiate a new perceptron given the parameters, used as the basis for a neural network
    def __init__(input_size, weights, bias = 0): #inputs is the number of inputs to this perceptron, weights is a list of weights for each input
        if isinstance(inputs, int):
            if isinstance(weights, list):
                if len(weights) != inputs:

                    self.input_size = input_size
                    self.weights = tuple(weights) #saved as tuple to boost performance and save space

                    if isinstance(bias, int):
                        self.bias = bias
                    else:
                        print("Warning: The provided bias was not an integer. Defaulting to 0.")
                        self.bias = 0

                else:
                    raise ValueError("The number of inputs and the number of weights do not match!")
            else:
                raise ValueError("Parameter 'weights' was not a list!")
        else:
            raise ValueError("Parameter 'inputs' was not an integer!")

    def generate(input):
        if len(input) == self.input_size:
            pass
        else:
            raise ValueError("Perceptron received an input with a size other than its input size!")