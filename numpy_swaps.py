import numpy as np

def swap_columns(array, i1, i2):
    col1 = array[:, i1]
    col2 = array[:, i2]
    new_array = array.copy()
    new_array[:, i1] = col2
    new_array[:, i2] = col1
    return new_array

def swap_rows(array, i1, i2):
    row1 = array[i1, :]
    row2 = array[i2, :]
    new_array = array.copy()
    new_array[i1, :] = row2
    new_array[i2, :] = row1
    return new_array

