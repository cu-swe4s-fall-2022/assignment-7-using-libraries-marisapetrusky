import random
import numpy as np
import sys
import pdb

# Return num_rows x num_columns matrix of entries between 0 and 1
def get_random_matrix(num_rows, num_columns):
    if not isinstance(num_rows, int) or not isinstance(num_columns, int):
        return None
    else:
        arr = np.empty([num_rows, num_columns])
        for row in range(num_rows):
            for col in range(num_columns):
                arr[row][col] = random.random()
        return arr

def get_file_dimensions(file_name):
	return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
