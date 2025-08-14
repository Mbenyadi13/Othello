from color import Color
from Pawn import Pawn
from cell import Cell
from Board import Board


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

    def placePawn(self,board):
        colsnames=["A","B","C","D","E","F","G","H"]
        rownames=["1","2","3","4","5","6","7","8"]
        inloop=True
        while inloop:
            move=input("What is your move?")
            if move[0] in colsnames and move[1] in rownames:
                j= colsnames.index(move[0])
                i=rownames.index(move[1])        
                if board.makeMove((i,j)) == True:
                    Cell.addpawn(Pawn(self.color))
                    inloop = False
                else:
                    print('This cell is not available, please choose another one')
        else: 
            print('Input Incorrect')


  
            





        

