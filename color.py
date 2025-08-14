from enum import Enum
class Color(Enum):
    BLACK= "○"
    WHITE= "●"
    
def flipColor(color):
    if not isinstance(color, Color):
        raise TypeError("Invalid color")
    
    if color == Color.BLACK:
        return Color.WHITE
    else:
        return Color.BLACK  