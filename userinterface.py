import PySimpleGUIQt as sg
import time

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
        self.page = 0 #0 = front page, 1 = game board, 2 = ai selector, 3 = evolution
        self.event = "init"
        self.values = ["init"]

        #temp
        diam = 30
        border = 30


        col_game = [[sg.Graph(canvas_size = (800, 600), graph_bottom_left = (0, 0), graph_top_right = (800, 600), 
            background_color = '#80B7DF', enable_events = True, change_submits = True, drag_submits = True, key = "_GAMEBOARD_")]]
        layout = [[sg.Col(col_game)]]
        self.window = sg.Window('ConnectFourAI', layout, return_keyboard_events = True, finalize = True)
        graph = self.window['_GAMEBOARD_']         # type: sg.Graph
        circle = graph.DrawCircle((75, 75), 25, fill_color='black', line_color='white')
        rectangle = graph.DrawRectangle((25, 300), (100, 280), line_color='purple')
        line = graph.DrawLine((0, 0), (100, 100))

    def start(self):
        while True:
            self.event, self.values = self.window.read(timeout = 250) #change this to change GUI responsiveness
            if self.event == sg.WIN_CLOSED or self.event == "Exit" or self.event == None:
                break
        self.window.close()
        print("GUI was closed")


    def read(self):
        return self.event, self.values
        '''
        event, values = self.window.read(timeout = 1000)
        if event == sg.WIN_CLOSED or event == "Exit" or event == None:
            self.window.close()
            return "EXIT"
        elif event == sg.TIMEOUT_KEY:
            pass
        #elif event == "a":
        #    self.window.Size = (200, 200)
        else:
            return event
        '''

    def update(self):
        pass