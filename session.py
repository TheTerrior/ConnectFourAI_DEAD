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
        print("running with gui, not implemented")
        ret = "Initializing GUI"
        sesh_gui = GUI()

        while True: #main loop
            ret = sesh_gui.read()
            if ret == "EXIT":
                print("GUI was closed")
                break
            elif ret == None:
                pass
            else:
                print(ret)

        return ret

    def __run_without_gui(self):
        print("running without gui, not implemented")

        while True: #main loop
            break

        return "EXIT"

    def run(self):
        if self.gui:
            ret = self.__run_with_gui()
        else:
            ret = self.__run_without_gui()
        self.__shutdown() 

    def __shutdown(self):
        pass

