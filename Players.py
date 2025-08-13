from color import Color
class Player:
    def __init__(self, color):
        self._color = color
        
    @property
    def color(self):
        return self._color
    

    def placepawn(self):
        

