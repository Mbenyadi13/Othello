class Cell:
    def __init__(self,i,j,pawn=None):
        self._i = i
        self._j = j
        self._pawn = pawn

    @property
    def i(self):
        return self._i

    def j(self):
        return self._j

    def pawn(self):
        return self._pawn

    def isfull(self,pawn):
        if pawn == None:
            return False
        else:
            return True
        
    def isempty(self,pawn):
        if pawn == None:
            return True
        else:
            return False
        
    def __add__(self, i, j, pawn):
        if self.isempty(pawn)== True:
            return self.isempty(pawn) == False
        else:
            return TypeError (f'Cell not empty! Choose another one')



    