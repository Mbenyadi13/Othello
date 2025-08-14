import numpy as np
import matplotlib.pyplot as plt
 
from cell import Cell
from Pawn import Pawn
from color import Color, flipColor
from direction import Direction

class Board:

    def __init__(self, size=8):             
        """Initialise le plateau de jeu Othello."""   
        self.size=size ## Taille du plateau Othello
        self.grid = np.empty((self.size,self.size), dtype=Cell)
        
        # Création des cellules avec cell 
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i, j] = Cell(i, j)
        self.placeInitialPawns()
    
        
    def placeInitialPawns(self):
        """Place les pions de départ d'Othello."""
        m = self.size // 2
        self.grid[m-1, m-1]._pawn = Pawn(Color.WHITE)
        self.grid[m-1, m  ]._pawn = Pawn(Color.BLACK)
        self.grid[m  , m-1]._pawn = Pawn(Color.BLACK)
        self.grid[m  , m  ]._pawn = Pawn(Color.WHITE)


    def drawGrid(self, possibleMove=None):
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
                if p is None:
                    if possibleMove and (i,j) in possibleMove: 
                        ligne.append("X") ## marqueur du coup possible
                    else:
                        ligne.append(" ")
                else :
                    ligne.append(p.color.value)
            print(f"{i+1:2d} │ " + " | ".join(ligne) + " │") ## affichage de 1 à 8 à gauche 
            if i != self.size-1:
                print(mid)
        print(bas)


    def listCells(self):
        """Retourne la liste des cellules du plateau (i,j,cell).
        Permet d'eviter les doubles boucles par la suite."""
        for i in range (self.size):
            for j in range (self.size):
                yield i,j, self.grid [i,j]


    def countersCells(self):
        """Retourne le nombre de pions noirs et blancs sur le plateau ainsi
        que le nombre de cases vides."""
        self.empty = 0
        self.black = 0
        self.white = 0
        for _, _, cell in self.listCells():
            if cell.isempty():
                self.empty += 1
            else:
                if cell.pawn.color == Color.BLACK:
                    self.black += 1
                else:
                    self.white += 1
        return self.empty, self.black, self.white               
        
    def Score(self):
        """Retourne le score des joueurs."""
        count= self.countersCells()
        return (f'Black: {count[1]} vs White {count[2]} \n Still {count[0]} moves to play')
        
        
    def dicPawns (self):
        """Retourne un dictionnaire des pions présents sur le plateau."""
        coords = {"black": [], "white": []}
        for i,j,cell in self.listCells():
            if cell.isfull():
                if cell.pawn.color == Color.BLACK:
                    coords["black"].append((i, j))
                else:
                    coords["white"].append((i, j))
        return coords    
  
    
    def inBoard(self, i, j):
        """Vérifie si les coordonnées (i, j) sont dans le plateau."""
        if 0<= i < self.size and 0<= j < self.size :
            return True          
        

    def _dir_captures(self, i, j, direction, color):
        """Vérifie si un coup dans une direction donnée capture des pions."""
        di, dj = direction.value
        ci, cj = i + di, j + dj
        # Le premier voisin doit être un pion adverse et on check sur les cases du plateau
        if not self.inBoard(ci, cj):
            return False
        first = self.grid[ci, cj].pawn
        if first is None or first.color != flipColor(color):
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
    
    def validMoveColor(self, color):
        """Liste [(i,j), ...] des coups jouables pour 'color'."""
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j].pawn is None and len(self.dirCapturing(i, j, color)) > 0:
                    moves.append((i, j))
        return moves

    def checkValidMove(self, i, j, color):
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
    
    def playMove(self, i, j, color):
        """Pose un pion de la couleur donnée et retourne les pions capturés."""
        # Vérifie validité du coup
        if not self.checkValidMove(i, j, color):
            raise ValueError("Coup invalide")

        # Pose le pion
        self.grid[i, j].addpawn(Pawn(color))

        # Pour chaque direction capturante, retourner les pions adverses
        for d in self.dirCapturing(i, j, color):
            di, dj = d.value
            ci, cj = i + di, j + dj
            while self.inBoard(ci, cj) and self.grid[ci, cj].pawn.color != color:
                self.grid[ci, cj].pawn.flip()
                ci += di
                cj += dj

        
        
if __name__ == "__main__":
    test=Board()
    test.drawGrid()
    dico = test.dicPawns()
    print("Noirs :", dico["black"])
    print("Blancs :", dico["white"])
    test.drawGrid()
    print(test.checkValidMove(4, 5, Color.WHITE))
    print(test.countersCells())
    print(test.Score())
    
    moves_black = test.validMoveColor(Color.BLACK)
    moves_white = test.validMoveColor(Color.WHITE)
    test.drawGrid(possibleMove=set(moves_black))
    test.drawGrid(possibleMove=set(moves_white))
    
    test.playMove(4, 5, Color.BLACK)
    print(test.drawGrid())

