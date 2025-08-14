### Fonctions globales et variables globales partagées par tous les modules


def moveToCoord(move):
    colsnames=["A","B","C","D","E","F","G","H"]
    rownames=["1","2","3","4","5","6","7","8"]
    if move[0] in colsnames and move[1] in rownames:
        j= colsnames.index(move[0])
        i=rownames.index(move[1])
        return (i,j)
    else:
        raise ValueError("Invalid move format. Use column letter followed by row number (e.g., 'A1').")