import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Board:

    def __init__(self):             
        
        self.matrix = np.zeros((8,8), dtype=int)
        
        self.initial_pawns_black= np.array([[3, 4], [4, 4]])
        self.initial_pawns_white = np.array([[3, 3], [4, 3]])

    def drawGrid(self):
        
        n = self.matrix.shape[0]
        haut  = "   ┌" + "───┬"*(n-1) + "───┐"
        mid   = "   ├" + "───┼"*(n-1) + "───┤"
        bas   = "   └" + "───┴"*(n-1) + "───┘"
        print("     " + "  ".join(str(i) for i in range(n)))
        print(haut)
        for i in range(n):
            ligne = " | ".join(" " if v==0 else ("1" if v==1 else "2") for v in self.matrix[i])
            print(f" {i} │ {ligne} │")
            if i != n-1:
                print(mid)
        print(bas)
                  

    def makeMove():
        pass

    def display () :
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