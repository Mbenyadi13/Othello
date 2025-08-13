from color import Color
class Player:
    def __init__(self, color,name):
        self._color = color
        self._name = name
        
    @property
    def color(self):
        return self._color
    

    @property
    def name(self):
        return self._name

    
        

