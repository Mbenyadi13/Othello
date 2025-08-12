from enum import Enum
class color(Enum):
    BLACK= "black"
    WHITE= "white"

print(color.BLACK)
print(color.WHITE)
print(color.WHITE ==color.BLACK)
print(color.BLACK == color.WHITE)



class Pawn:
    def __init__(self,color):
        self._color = color

    @property 
    def color(self):
        return self._color

    def flippawn(self):
        if self._color == color.BLACK:
            self._color == color.WHITE
        else:
            self._color == color.BLACK
        
