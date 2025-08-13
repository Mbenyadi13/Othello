import numpy as np
import matplotlib.pyplot as plt
 
from cell import Cell
from Pawn import Pawn
from color import Color


class Board:

    def __init__(self, size=8):             
        
        self.size=size ## Taille du plateau Othello
        self.grid = np.empty((self.size,self.size), dtype=object)
        
        # Création des cellules avec cell 
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i, j] = Cell(i, j)
        self.initial_pawns()
        
    def initial_pawns(self):
        """Place les pions de départ d'Othello."""
        m = self.size // 2
        self.grid[m-1, m-1]._pawn = Pawn(Color.WHITE)
        self.grid[m-1, m  ]._pawn = Pawn(Color.BLACK)
        self.grid[m  , m-1]._pawn = Pawn(Color.BLACK)
        self.grid[m  , m  ]._pawn = Pawn(Color.WHITE)


    def drawGrid(self):
        """Affiche le plateau de jeu."""
        # SYMBOLES = {None: " ", Color.BLACK: "●", Color.WHITE: "○"}
        colonnes = "   " .join(chr(ord('A') + k) for k in range(self.size))
        haut  = "   ┌" + "───┬"*(self.size-1) + "───┐"
        mid   = "   ├" + "───┼"*(self.size-1) + "───┤"
        bas   = "   └" + "───┴"*(self.size-1) + "───┘"
        print("     " + colonnes)
        print(haut)
        for i in range(self.size):
            ligne = []
            for j in range(self.size):
                p = self.grid[i, j].pawn
                # ligne.append(SYMBOLES[None if p is None else p.color])
                ligne.append(" " if p is None else p.color.value)
            print(f"{i+1:2d} │ " + " | ".join(ligne) + " │") ## affichage de 1 à 8 à gauche 
            if i != self.size-1:
                print(mid)
        print(bas)
        
    def dicPawns (self):
        """Retourne un dictionnaire des pions présents sur le plateau."""
        coords = {"black": [], "white": []}
        for i in range(self.size):
            for j in range(self.size):
                p = self.grid[i, j].pawn
                if p is None:
                    continue
                if p.color == Color.BLACK:
                    coords["black"].append((i, j))
                else:
                    coords["white"].append((i, j))
        return coords    
                  

    def makeMove(self):
        pass

    def display (self) :
        pass



if __name__ == "__main__":
    test=Board()
    test.drawGrid()
    dico = test.dicPawns()
    print("Noirs :", dico["black"])
    print("Blancs :", dico["white"])



