from color import Color

class Pawn:
    def __init__(self,color):
        self._color = color

    @property 
    def color(self):
        return self._color

    def flip(self):
        if self._color == Color.BLACK:
            self._color = Color.WHITE
        else:
            self._color = Color.BLACK
            
    def __repr__(self):
        if self._color == Color.BLACK:
            return "●"
        else:
            return "○"        
        

if __name__ == "__main__":      
    p = Pawn(Color.BLACK)
    print(p, p.color)  # ● Color.BLACK
    p.flip()
    print(p, p.color)  # ○ Color.WHITE
    p.flip()
    print(p, p.color)  # ● Color.BLACK       
