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
        SYMBOLES = {None: " ", Color.BLACK: "●", Color.WHITE: "○"}
        colonnes = " a  " .join(chr(ord('A') + k) for k in range(self.size))
        haut  = "   ┌" + "───┬"*(self.size-1) + "───┐"
        mid   = "   ├" + "───┼"*(self.size-1) + "───┤"
        bas   = "   └" + "───┴"*(self.size-1) + "───┘"
        print("     " + colonnes)
        print(haut)
        for i in range(self.size):
            ligne = []
            for j in range(self.size):
                p = self.grid[i, j].pawn
                ligne.append(SYMBOLES[None if p is None else p.color])
            print(f"{i+1:2d} │ " + " | ".join(ligne) + " │") ## affichage de 1 à 8 à gauche 
            if i != self.size-1:
                print(mid)
        print(bas)
                  

    def makeMove(self):
        pass

    def display (self) :
        pass





test=Board()
test.drawGrid()



#Non interactif 
        #  # Création de la figure
        # fig, ax = plt.subplots(figsize=(6, 6))
        # ax.set_axis_off()  # Pas d'axes

        # # Création d'une table matplotlib
        # tableau = ax.table(cellText=[["" for _ in range(8)] for _ in range(8)],
        #     cellLoc='center',
        #     loc='center')

        #     # Ajuster la taille des cellules
        # for i in range(8):
        #     for j in range(8):
        #         tableau[i, j].set_height(1/8)
        #         tableau[i, j].set_width(1/8)
        #         tableau[i, j].set_facecolor("#228B22")  # vert plateau Othello
        #         tableau[i, j].set_edgecolor("black")    # bordure noire
                

# # plt.show()