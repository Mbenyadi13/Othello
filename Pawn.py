from color import Color
class Pawn:
    def __init__(self,color):
        self._color = color

    @property 
    def color(self):
        return self._color

    def flippawn(self):
        if self._color == Color.BLACK:
            self._color == Color.WHITE
        else:
            self._color == Color.BLACK
        
