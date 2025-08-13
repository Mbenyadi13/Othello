from Pawn import Pawn

class Cell:
    def __init__(self,i,j,pawn=None):
        self._i = i
        self._j = j
        self._pawn = pawn

    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    @property
    def pawn(self):
        return self._pawn

    def isfull(self):
        return isinstance(self.pawn, Pawn)
        
    def isempty(self):
        return not self.isfull()
        
    def addpawn(self, pawn):
        if self.isempty():
             self._pawn = pawn
        else:
            raise TypeError (f'Cell not empty! Choose another one')


if __name__ == "__main__":
    test=Cell(3,3)
    test.isfull  
    


    