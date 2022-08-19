from operator import concat
import numpy as np
import sys
import numpy_swaps as ns

sys.setrecursionlimit(10000)

class Table:
    def __init__(self):
        self.table = np.zeros((9,9), int)
    
    def complete(self):
        self.fill_sudoku(0,0, [], False)
    
    def get_number(self, i, j, tablero):
        row = tablero[i]
        column = [x[j] for x in tablero]
        square = []
        
        if i<3:
            square = tablero[0:3]
        elif i >=3 and i<6:
            square = tablero[3:6]
        elif i>=6:
            square = tablero[6:]
        
        if j<3:
            square = square[:, 0:3]
        elif j>=3 and j<6:
            square = square[:, 3:6]
        elif j>=6:
            square = square[:, 6:]
        
        find = False
        num = tablero[i][j]
        while find == False and num<9:
            num += 1
            if num not in row and num not in column and num not in square:
                find = True
                tablero[i][j]=num
            if num >9:
                num = 1
            
        if find == False:
            return False
    
    def fill_sudoku(self, i, j, positions, bck):
        if i == 9:
            return
        if bck == True or self.table[i][j]==0:
            a = self.get_number(i, j, self.table)
            if a == False:
                pos = positions.pop()
                self.table[i][j] = 0
                #print(self.table)
                self.fill_sudoku(pos[0], pos[1], positions, True)
            positions.append((i,j))

        if j == 8:
            j=-1
            i+=1
        
        self.fill_sudoku(i, j+1, positions, False)
        return
    
    def create_sudokus(self):
        # COMBINACIONES PRIMER CUADRANTE EN VERTICAL
        l = [self.table]

        last = self.table

        while len(l)<6:
            if len(l) > 1:
                new_array = ns.swap_columns(last, 0, 1)
                last = new_array
                l.append(new_array)

            new_array = ns.swap_columns(last, 1, 2)    
            l.append(new_array)
            last = new_array

        li = []

        for array in l:
            last = array
            l1 = []
            while len(l1) < 5:
                if len(l1)>1:
                    new_array = ns.swap_columns(last, 3, 4)
                    last = new_array
                    l1.append(new_array)
                new_array = ns.swap_columns(last, 4, 5)    
                l1.append(new_array)
                last = new_array


            #li.remove(array)
            li = concat(li, l1)

        l = []

        for array in li:
            last = array
            l1 = []
            while len(l1) < 5:
                if len(l1)>1:
                    new_array = ns.swap_columns(last, 6, 7)
                    last = new_array
                    l1.append(new_array)
                new_array = ns.swap_columns(last, 7, 8)    
                l1.append(new_array)
                last = new_array


            #li.remove(array)
            l = concat(l, l1)

        # COMBINACIONES EN HORIZONTAL
        li = []
        for array in l:
            last = array
            l1 = []
            while len(l1) < 5:
                if len(l1)>1:
                    new_array = ns.swap_rows(last, 0, 1)
                    last = new_array
                    l1.append(new_array)
                new_array = ns.swap_rows(last, 1, 2)    
                l1.append(new_array)
                last = new_array

            li = concat(li, l1)

        l = []

        for array in li:
            last = array
            l1 = []
            while len(l1) < 5:
                if len(l1)>1:
                    new_array = ns.swap_rows(last, 3, 4)
                    last = new_array
                    l1.append(new_array)
                new_array = ns.swap_rows(last, 4, 5)    
                l1.append(new_array)
                last = new_array

            l = concat(li, l1)

        li = []

        for array in l:
            last = array
            l1 = []
            while len(l1) < 5:
                if len(l1)>1:
                    new_array = ns.swap_rows(last, 6, 7)
                    last = new_array
                    l1.append(new_array)
                new_array = ns.swap_rows(last, 7, 8)    
                l1.append(new_array)
                last = new_array

            li = concat(li, l1)

        return li


# PARA OCULTAR EL  123 HACER SWAPS DE SIMETRIA, HORIZONTAL Y VERTICAL,  DE TRANSPUESTA
    
t = Table()
t.complete()
sudokus = t.create_sudokus()
print(len(sudokus))