import PySimpleGUIQt as sg

#will be generated if player asks to play and will be provided the UI window object
class Player():

    '''
    window = the window object itself from PySimpleGUI
    '''

    def __init__(self, window):
        self.window = window
    
    #prompt the user to input a location for the new piece, check if input is valid
    def prompt_turn(self, board):
        pass

class GUI():
    
    def __init__(self):
        layout = [[sg.Button("testing my boi")]]
        self.window = sg.Window('ConnectFourAI', layout) # , size = (10,50)
        self.page = 0 #0 = front page, 1 = game board, 2 = ai selector, 3 = evolution

    def read(self):
        event, values = self.window.read(timeout = 0)
        if event == sg.WIN_CLOSED or event == "Exit" or event == None:
            self.window.close()
            return "EXIT"
        elif event == sg.TIMEOUT_KEY:
            pass
        else:
            return event

    def update(self):
        pass