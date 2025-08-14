from Players import Player
from color import Color
import Board

class Othello:
    def __init__(self):
        name1 = input("Enter the name of Black player ")
        name2 = input("Enter the name of White player")
        self.playerb=Player(Color.BLACK,name1)
        self.playerw=Player(Color.WHITE,name2)
        self.board=Board()

        
    #Player Alternated moves
   
    def playerTurns(self,color):
            if color==Color.BLACK:
                
                print(self.playerb.name + " Your turn to play")
            elif color == Color.WHITE:
                print(self.playerw.name + " Your turn to play")
            else:
                 raise ValueError ('Must be a color')
    
    
            
            
            
    
            
