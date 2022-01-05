import PySimpleGUIQt as sg

#will be generated if player asks to play and will be provided the UI window object
class Player():

    '''
    window = the window object itself from PySimpleGUI
    '''

    def __init__(self):
        '''
        Initiate a new GUI 
        '''
        pass
    
    #prompt the user to input a location for the new piece, check if input is valid
    def prompt_turn(self, board):
        pass

class GUI():
    
    def __init__(self, func):
        self.func = func
        layout = [[sg.Button("testing my boi")]]
        window = sg.Window('AudioForge', layout) # , size = (10,50)

    def run(self):
        print("running this inside of GUI now")
        return self.func()