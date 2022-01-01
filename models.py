from base import *

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

class NeuralNetwork(Base):
    __tablename__ = 'neuralnetwork'
    id = Column(Integer, primary_key = True)
    mutability = Column(Float)

    layers = relationship("Layer", back_populates = "neuralnetwork")
    ranks = relationship("Rank", back_populates = "neuralnetwork")

    #initiate the new neural network given the optional parameters
    def __init__(self, layers = 1, sizes = [1], mutability = 0.5):
        if isinstance(layers, int):
            if isinstance(sizes, list):
                if len(sizes) == layers:

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

                    if isinstance(mutability, float) or isinstance(mutability, int):
                        self.mutability = mutability
                    else:
                        print("Warning: The provided mutability was not a number. Defaulting to 0.5.")
                        self.mutability = 0.5

                else:
                    raise ValueError("Received {} sizes of layers for {} layers.".format(len(sizes), layers))
            else:
                raise ValueError("Parameter 'sizes' was not a list!")
        else:
            raise ValueError("Parameter 'layers' was not an integer!")

    #send board info to the neural network and generate an output. If main output is invalid, choose the next valid output
    def prompt_turn(self, board):
        pass

    def process(self, input):
        if len(input) == len(self.layers):
            pass
        else:
            raise ValueError("Neural network received an input with a size other than its input size!")

class Layer(Base):
    __tablename__ = 'layer'
    id = Column(Integer, primary_key = True)
    number = Column(Integer)

    neuralnetwork_id = Column(Integer, ForeignKey('neuralnetwork.id'))
    neuralnetwork = relationship("NeuralNetwork", back_populates = "layers")
    perceptrons = relationship("Perceptron", back_populates = "layer")
    
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
    _weights = Column(String, default = ";")

    layer_id = Column(Integer, ForeignKey('layer.id'))
    layer = relationship("Layer", back_populates = "perceptrons")

    #initiate a new perceptron given the parameters, used as the basis for a neural network
    def __init__(self, input_size, weights, bias = 0):
        if isinstance(input_size, int):
            if isinstance(weights, list):
                if len(weights) == input_size:

                    self.input_size = input_size
                    self.weights = weights #saved as tuple to boost performance and save space

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

    @property
    def weights(self):
        return self._weights.split(";")[:-1]
    @weights.setter
    def weights(self, value):
        if isinstance(value, list):
            self._weights = ""
            for x in value:
                self._weights += '%s;' % x
            if len(value) == 0:
                self._weights = ';'
        else:
            raise ValueError("Attribute 'weights' was not a list! Encountered error when setting .weights attribute.")

    def process(self, input):
        if len(input) == self.input_size:
            print("Perceptron process is yet to be implemented")
        else:
            raise ValueError("Perceptron received an input with a size other than its input size!")
