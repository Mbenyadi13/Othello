from color import Color
from Pawn import Pawn
from cell import Cell
from Board import Board
from fonctions_globales import moveToCoord

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
        """Place a pawn on the board for the player."""
        #1/ coups possibles
        moves=board.validMoveColor(self.color)
        if not moves:
            print(f"{self.name} ({self.color.name}) has no possible move - pass.")
            return False

        #2/ Affichage (liste + possibleMove)
        moves_set = set(moves)
        as_str = ", ".join(f"{chr(ord('A')+j)}{i+1}" for i, j in moves)
        print(f"Possible moves for {self.name} ({self.color.name}) : {as_str}")
        board.drawGrid(possibleMove=moves_set)
        
        #3/ boucle d'entre d'utilisateur: Possible/Not possible
        while True:
            move=input("What is your move?").strip().upper()
            try:
                i, j = moveToCoord(move)   
            except Exception as e:
                print(e)
                continue
            if (i, j) not in moves_set:
                print("Invalid move: not in the list of possible moves. Try again.")
                continue
            if not board.checkValidMove(i, j, self.color):
                print("Invalid move. Try again.")
                continue
            ##4/ Ajout du pion (sans flip pour l'instant)
            try:
                board.playMove(i, j, self.color)
                board.drawGrid()     # feedback visuel
                return               # <-- on SORT de la boucle (clé du problème)
            except ValueError as e:
                # Si jamais le coup est soudainement invalide, on réessaie
                print(e)
                continue
 
    


  
            





        

