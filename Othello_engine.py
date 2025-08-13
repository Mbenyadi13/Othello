from Players import Player
from color import Color

class Othello:
    def __init__(self):
        name1 = input("Enter the name of Player 1 ")
        name2 = input("Enter the name of Player 2 ")
        self.player1=Player(Color.BLACK,name1)
        self.player2=Player(Color.WHITE,name2)

        
    #Player Alternated moves
   
    def player_turns(self,color,name1, name2):
            if color==Color.BLACK:
                
                return input( name1 + "Your turn to play")
            elif color == Color.WHITE:
                return input( name2 + "Your turn to play")
            else:
                 raise ValueError (f'Must be a color')
            
            
            
    
            
