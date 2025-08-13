import numpy as np
import matplotlib.pyplot as plt
 
from cell import Cell
from Pawn import Pawn
from color import Color
from direction import Direction

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
  
    
    def inBoard(self, i, j):
        """Vérifie si les coordonnées (i, j) sont dans le plateau."""
        if 0<= i < self.size and 0<= j < self.size :
            return True          


    def opponent(self, color):
        """check la couleur opposée au pion joué"""
        if color == Color.WHITE:
            return Color.BLACK 
        else:
            Color.WHITE


    def _dir_captures(self, i, j, direction, color):
        """Vérifie si un coup dans une direction donnée capture des pions."""
        di, dj = direction.value
        ci, cj = i + di, j + dj
        # Le premier voisin doit être un pion adverse et on check sur les cases du plateau
        if not self.inBoard(ci, cj):
            return False
        first = self.grid[ci, cj].pawn
        if first is None or first.color != self.opponent(color):
            return False
        # Continuer tant qu'on voit des pions adverses
        ci += di
        cj += dj
        while self.inBoard(ci, cj):
            p = self.grid[ci, cj].pawn
            if p is None:
                return False
            if p.color == color:
                return True  # fermé par notre couleur
            ci += di
            cj += dj
        return False  # atteint le bord 
    
    def dirCapturing(self, i, j, color):
        """Retourne la liste des directions qui capturent autour de (i,j)."""
        if not self.inBoard(i, j) or self.grid[i, j].pawn is not None:
            return []
        dirs = []
        for d in Direction:
            if self._dir_captures(i, j, d, color):
                dirs.append(d)
        return dirs
    
    
    def makeMove(self, i, j, color):
        """vérifie si le coup est valide (au moins une direction capturante)
    et si la case est vide & dans le plateau. Ne retourne pas encore les pions.
    """
        ### est-ce que la case est vide ?
        if self.grid[i, j].pawn is not None:
            return False
        ### est ce que la cese est dans le plateau ?
        if self.inBoard(i, j) == False:
            return False
        
        ### est-ce qu'il y a au moins une direction capturante ?
        dirs = self.dirCapturing(i, j, color)
        return len(dirs) > 0

        
            

    def display (self) :
        pass



if __name__ == "__main__":
    test=Board()
    test.drawGrid()
    dico = test.dicPawns()
    print("Noirs :", dico["black"])
    print("Blancs :", dico["white"])
    test.grid[5, 3].addpawn(Pawn(Color.BLACK))
    test.drawGrid()
    test.grid[1, 6].addpawn(Pawn(Color.WHITE))
    test.drawGrid()
    print(test.makeMove(4, 5, Color.BLACK))
    test.grid[0, 1].addpawn(Pawn(Color.WHITE))
    test.drawGrid()
    print(test.makeMove(3, 5, Color.WHITE))

