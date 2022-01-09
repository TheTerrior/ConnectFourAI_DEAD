from base import *
import numpy as np

class Generation(Base):
    __tablename__ = 'generation'
    id = Column(Integer, primary_key = True)
    number = Column(Integer)

    ais = relationship("Rank", back_populates = "generation")

class Rank(Base):
    __tablename__ = 'rank'
    id = Column(Integer, primary_key = True)
    placement = Column(Integer)

    generation_id = Column(Integer, ForeignKey('generation.id'))
    generation = relationship("Generation", back_populates = "ais")
    neuralnetwork_id = Column(Integer, ForeignKey('neuralnetwork.id'))
    neuralnetwork = relationship("NeuralNetwork", back_populates = "ranks")

    def __init__(self, generation, neuralnetwork, rank = 0):
        if isinstance(generation, Generation):
            if isinstance(neuralnetwork, NeuralNetwork):
                self.generation = generation
                self.neuralnetwork = neuralnetwork
                if rank != 0: #can receive a rank later, doesn't need to right now
                    self.rank = rank
            else:
                raise ValueError("'Rank' received an invalid NeuralNetwork object.")
        else:
            raise ValueError("'Rank' received an invalid Generation object.")

class NeuralNetwork(Base):
    __tablename__ = 'neuralnetwork'
    id = Column(Integer, primary_key = True)
    mutability = Column(Float)
    _shape = Column(String, default = ";")

    layers = relationship("Layer", back_populates = "neuralnetwork")
    ranks = relationship("Rank", back_populates = "neuralnetwork")
    #a given neural network will never be edited once created, apart from the ranks it's associated with

    #initiate the new neural network given the optional parameters
    def __init__(self, shape, mutability = 0.5):
        if isinstance(shape, list):

            '''
            #layers = [] #contains all layers of perceptrons, a single layer means a single layer after the input
            for i in range(0, layers):
                newlayer = []
                if i == 0: #if this is the first layer, hence we know the amount of inputs
                    for j in range(0, sizes[i]):
                        newlayer.append(Perceptron(inputs = 42))
                else: #if this is a recursively made layer
                    for j in range(0, sizes[i]):
                        newlayer.append(Perceptron(inputs = sizes[i-1]))
                self.layers.append(Layer(newlayer))
            #self.layers = layers
            '''

            for i, size in enumerate(shape):
                layers.append(Layer(self, size, i))

            if isinstance(mutability, float) or isinstance(mutability, int):
                self.mutability = mutability

                self.ordered_layers = self.layers.order_by(asc(Layer.order)) #allows for faster accessing for this session

            else:
                print("Warning: The provided mutability was not a number. Defaulting to 0.5.")
                self.mutability = 0.5
        else:
            raise ValueError("Parameter 'shape' was not a list!")

    #send board info to the neural network and generate an output. If main output is invalid, choose the next valid output
    def prompt_turn(self, board):
        return self.process(board.ravel()) #returns a reference to the matrix, so careful not to edit values, faster than .flatten()

    def process(self, input):
        if len(input) == len(self.shape[0]):
            pass
        else:
            raise ValueError("Neural network received an input with a size other than its input size!")

    @property
    def shape(self):
        return stol(self._shape)
    @shape.setter
    def shape(self, value):
        if isinstance(value, list):
            self._shape = ltos(value)
        else:
            raise ValueError("Attribute 'shape' was not a list! Encountered error when setting .shape attribute.")

#holds lists of perceptrons
class Layer(Base):
    __tablename__ = 'layer'
    id = Column(Integer, primary_key = True)
    size = Column(Integer)
    order = Column(Integer)

    neuralnetwork_id = Column(Integer, ForeignKey('neuralnetwork.id'))
    neuralnetwork = relationship("NeuralNetwork", back_populates = "layers")
    perceptrons = relationship("Perceptron", back_populates = "layer")

    def __init__(self, neuralnetwork, size, order):
        if isinstance(neuralnetwork, NeuralNetwork):
            if isinstance(size, int) and isinstance(order, int):
                self.size = size
                self.neuralnetwork = neuralnetwork
                self.order = order
                #perceptrons aren't generated here in case we need specific weights and such
                #as such, perceptron creation is handled by the code that calls this class
                #we do however store the size of this layer for reference
            else:
                raise ValueError("'Rank' received an invalid size or order; not an integer.")
        else:
            raise ValueError("'Rank' received an invalid NeuralNetwork object.")
    
    def process(self, input):
        if len(input) == len(self.perceptrons):
            pass
        else:
            raise ValueError("Layer received an input with a size other than its input size!")

class Perceptron(Base):
    __tablename__ = 'perceptron'
    id = Column(Integer, primary_key = True)
    input_size = Column(Integer)
    bias = Column(Float)
    order = Column(Integer)
    _weights = Column(String, default = ";")

    layer_id = Column(Integer, ForeignKey('layer.id'))
    layer = relationship("Layer", back_populates = "perceptrons") #a given perceptron will be tied to only one layer ever

    #initiate a new perceptron given the parameters, used as the basis for a neural network
    def __init__(self, input_size, weights, bias = 0):
        if isinstance(input_size, int):
            if isinstance(weights, list):
                if len(weights) == input_size:

                    self.input_size = input_size
                    self.weights = weights

                    if isinstance(bias, float) or isinstance(bias, int):
                        self.bias = bias
                    else:
                        print("Warning: The provided bias was not a number. Defaulting to 0")
                        self.bias = 0

                else:
                    raise ValueError("The number of inputs and the number of weights do not match!")
            else:
                raise ValueError("Parameter 'weights' was not a list!")
        else:
            print(type(input_size))
            raise ValueError("Parameter 'input_size' was not an integer!")

    def process(self, input):
        if len(input) == self.input_size:
            print("Perceptron process is yet to be implemented")
        else:
            raise ValueError("Perceptron received an input with a size other than its input size!")

    @property
    def weights(self):
        #return self._weights.split(";")[:-1]
        return stol(self._weights)
    @weights.setter
    def weights(self, value):
        if isinstance(value, list):
            '''
            self._weights = ""
            for x in value:
                self._weights += '%s;' % x
            if len(value) == 0:
                self._weights = ';'
            '''
            if len(list) == self.input_size:
                self._weights = ltos(value)
            else:
                raise ValueError("Size of 'weights' does not equal input size! Encountered error when setting .weights attribute.")
        else:
            raise ValueError("Attribute 'weights' was not a list! Encountered error when setting .weights attribute.")


#a convenient way to convert a list of writable types to a string
def ltos(list):
    if len(list) == 0:
        return ";"
    ret = ""
    for val in list:
        ret += f"{val};"
    return ret

#a way to convert stringified lists back to lists
def stol(string):
    return string.split(";")[:-1]


def generate_new_perceptron(weights):
    p = Perceptron(len(weights), weights)
    return p

def generate_new_weights(size):
    pass

def generate_new_ai(shape):
    nn = NeuralNetwork(shape)
    for i, size in enumerate(shape):
        if size == nn.ordered_layers[i].size:
            #create the perceptrons for this layer
            for p in range(size):
                nn.ordered_layers[p].perceptrons.append(generate_new_perceptron(generate_new_weights(size)))
    return nn

def generate_child_ai(nn_parent, nn_parent1):
    if isinstance(nn_parent, NeuralNetwork) and isinstance(nn_parent1, NeuralNetwork):
        if nn_parent.shape == nn_parent1.shape:
            nn = NeuralNetwork(nn_parent.shape)
            return nn
        else:
            raise ValueError("Cannot generate child from parents with differing shapes.")
    else:
        raise ValueError("Parent parameters are not instances of NeuralNetwork!")