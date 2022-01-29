class Solution:
    def __init__(self):
        self.board=None
    def isValidSudoku(self,board):
        self.board=board
        if self.row_safe()==False:
            return False
        if self.col_safe()==False:
            return False
        if self.area_safe()==False:
            return False
        return True
    def row_safe(self):
        for row in range(0,9):
            tmp=self.board[row].copy()
            if self.count(tmp)==False:
                return False
        return True
    def col_safe(self):
        for col in range(0,9):
            tmp=[self.board[i][col] for i in range(0,9)]
            if self.count(tmp)==False:
                return False
        return True
    def area_safe(self):
        center=[]
        for row in [1,4,7]:
            for col in [1,4,7]:
                center.append((row,col))
        for cen in center:
            tmp=[]
            for row in [-1,0,1]:
                for col in [-1,0,1]:
                    x=(cen[0]-row)
                    y=cen[1]-col
                    tmp.append(self.board[x][y])
            if self.count(tmp)==False:
                return False
        return True
    def count(self,li):
        typ=list(set(li))
        if '.' in typ:
            typ.remove('.')
        for i in typ:
            count=0
            while True:
                if count>1:
                    return False
                if i in li:
                    li.remove(i)
                    count+=1
                else:
                    break
        return True
