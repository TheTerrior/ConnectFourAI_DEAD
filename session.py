from base import *
from userinterface import GUI
from concurrent.futures import ThreadPoolExecutor, as_completed
from PySimpleGUI import WIN_CLOSED, TIMEOUT_KEY
import threading
import time
#from models import Player, Generation, Rank, NeuralNetwork, Layer, Perceptron

class Session():
    def __init__(self, use_gui = True):
        Base.metadata.create_all(engine) #ensure all tables are created and database exists
        self.use_gui = use_gui

    def set_use_gui(self, use_gui):
        self.use_gui = use_gui

    def __run_with_gui(self):
        print("Running with GUI")
        print("Initializing GUI")
        self.GUI = GUI()
        tmainloop = threading.Thread(target = self.__main_loop_with_gui)
        #t1 = threading.Thread(target=thread1, args=(10,))

        print("Threading initializing")
        tmainloop.start()
        self.GUI.start()

        tmainloop.join()
        print("Threading has completed")
        return "EXIT"


    def __main_loop_with_gui(self):
        ret = ""
        while True: #main loop
            event, values = self.GUI.read()
            if event == WIN_CLOSED or event == "Exit" or event == None:
                print("Closing event:", event)
                break
            elif event == TIMEOUT_KEY:
                pass
            else:
                print("GUI event:", event)
            time.sleep(0.25) #should be similar to GUI time
            
        print("Main loop was closed")
        return ret


    def __run_without_gui(self):
        print("Running without GUI")

        while True: #main loop
            break

        return "EXIT"


    def run(self):
        if self.use_gui:
            ret = self.__run_with_gui()
        else:
            ret = self.__run_without_gui()
        self.__shutdown() 

    def __shutdown(self):
        pass

