#sudo slover
class Solution:
    def __init__(self):
        self.board=None
        # self.loc_list=self.get_all_empty()
        # self.area_list=self.make_area()
    def make_area(self):
        tmp_array=[]
        for x in [1,4,7]:
            for y in [1,4,7]:
                tmp=[]
                for a_x in [-1,0,1]:
                    for a_y in [-1,0,1]:
                        tmp.append((x+a_x,y+a_y))
                tmp_array.append(tmp)
        return tmp_array
    def row_safe(self,val,row):
        val=str(val)
        if val in self.board[row]:
            return False
        return True
    def col_safe(self,val,column):
        val=str(val)
        for row in range(0,9):
            if val == self.board[row][column]:
                return False
        return True
    def area_safe(self,val,x,y):
        val=str(val)
        for area in self.area_list:
            if (x,y) in area:
                for loc_x,loc_y in area:
                    if self.board[loc_x][loc_y]==val:
                        return False
        return True
        
        #using sudo validate and adjust it
    def all_rules_safe(self,val,x,y):
        #有任一個False則return False
        if self.row_safe(val,x)==False:
            return False
        if self.col_safe(val,y)==False:
            return False
        if self.area_safe(val,x,y)==False:
            return False
        return True
    def get_all_empty(self):
        '''get all empty location'''
        tmp_list=[]
        for row in range(0,9):
            for col in range(0,9):
                if self.board[row][col]=='.':
                    tmp_list.append((row,col))
        return tmp_list
    def recursive(self,sudo,location):
        item_list=[]
        for i in sudo:
            item_list+=i
        if '.' not in item_list:
            return True
        else:
            #step1 choose one empty loc(using get_all_empty)
            x,y=self.loc_list[location]
            #print(location)
            #step2 determine the val is safe or not.
            for val in range(1,10):
                val=str(val)
                #if want adjust val in board,we need to using str type and val+1
                tmp_location=location+1
                tmp_board=sudo
                if self.all_rules_safe(val,x,y)==True:
                    tmp_board[x][y]=val
                    if self.recursive(tmp_board,tmp_location)==True:
                        return True
                    else:
                        tmp_board[x][y]='.'
         

                
    def solveSudoku(self,board):
        self.board=board
        self.loc_list=self.get_all_empty()
        self.area_list=self.make_area()
        self.recursive(self.board,0)
        return self.board
