from base import *
from userinterface import GUI
#from models import Player, Generation, Rank, NeuralNetwork, Layer, Perceptron

class Session():
    def __init__(self, gui = True):
        Base.metadata.create_all(engine) #ensure all tables are created and database exists
        self.gui = gui

    def set_gui(self, gui):
        self.gui = gui

    def __run_with_gui(self):
        print("we testing this yall")
        print(self)
        return "EXIT"

    def __run_without_gui(self):
        print("running without gui, not implemented")
        return "EXIT"

    def run(self):
        if self.gui:
            session_gui = GUI(self.__run_with_gui)
            ret = session_gui.run()
        else:
            ret = self.__run_without_gui()
        self.__shutdown() 

    def __shutdown(self):
        pass

