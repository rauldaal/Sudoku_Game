#       LAST NOTE
#       Hay que hacer backtracking si o si
#       Intentar que sea optimo 
import numpy as np
import time as t
import random as r




class Table:
    def __init__(self, dif) -> None:
        self.table = np.zeros((9,9), int)
        self.__dificulty = dif # 0 = Easy, 1= Med, 2 = Dif
        self.__freq = np.zeros(9, int)
        self.__num = 0
        
    def __get_number(self, x, y):
        POS = [1,2,3,4,5,6,7,8,9]
        if self.table[x,y] != 0:
            return None
        
        for i in range (9):
            if self.table[x, i] != 0:
                try:
                    POS.remove(self.table[x,i])
                except:
                    pass
            if self.table[i, y] != 0:
                try:
                    POS.remove(self.table[i,y])
                except:
                    pass
        start_x = 0
        start_y = 0
        if x > 2: start_x = 3
        if x > 5: start_x = 6
        if y > 2: start_y = 3
        if y > 5: start_y = 6
        
        for i in range(start_x, start_x+3):
            for j in range(start_y, start_y+3):
                if self.table[i, j] != 0:
                    try:
                      POS.remove(self.table[i,j])
                    except:
                        pass
        
        if len(POS) == 0:
            return None
        
        pos_num = r.randint(0, len(POS)-1)
        return POS[pos_num]

    def __get_row(self):
        val = [0]
        rows = [0,1,2,3,4,5,6,7,8]
        for i, row in enumerate(self.table):
            res = np.in1d(val, row)[0]
            if res==False:
                rows.remove(i)
        sel = r.randint(0, len(rows)-1)
        return rows[sel]     
        
    def __get_column(self, row):
        cols = [0,1,2,3,4,5,6,7,8]
        for i in range(9):
            if row[i] != 0:
                cols.remove(i)
        sel = r.randint(0, len(cols)-1)
        return cols[sel]
        

    def __bck_2_create(self):
        x = self.__get_row()
        y = self.__get_column(self.table[x]) 
        l = self.__get_number(x, y)
        if l == None:
            return
        self.table[x, y] = l
        self.__num += 1
        return
    

    def create(self):
        while self.__num < 81:
            self.__bck_2_create()

        
t = Table(1)
t.create()
print(t.table)