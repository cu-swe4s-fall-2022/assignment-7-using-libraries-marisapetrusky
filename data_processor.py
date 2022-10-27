import random
import numpy as np
import sys
import pdb
import os
import csv
import re


# Return num_rows x num_columns matrix of entries between 0 and 1
def get_random_matrix(num_rows, num_columns):
    if not isinstance(num_rows, int) or not isinstance(num_columns, int):
        raise TypeError('get_random_matrix inputs not integers')
    else:
        arr = np.empty([num_rows, num_columns])
        for row in range(num_rows):
            for col in range(num_columns):
                arr[row][col] = random.random()
        return arr


# Return tuple of (no. rows, no columns)
def get_file_dimensions(file_name, delim=','):
    try:
        f = open(file_name, 'r')
        if (os.path.getsize(file_name) > 0):
            lines = f.readlines()
            num_rows = len(lines)
            cols = lines[0].rstrip().split(delim)
            num_cols = len(cols)
            f.close()
            return (num_rows, num_cols)
        else:
            f.close()
            raise TypeError('File is empty.')
    except FileNotFoundError:
        raise FileNotFoundError('File not found in get_file_dimensions')


# Write random matrix to csv file
def write_matrix_to_file(num_rows, num_columns, file_name):
    arr = get_random_matrix(num_rows, num_columns)
    checkFname = isinstance(file_name, str)
    if checkFname:
        if re.search('.csv', file_name) is not None:
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                for i in range(num_rows):
                    writer.writerow(arr[i][:])
            print('Matrix successfully written.')
            return None
        else:
            raise TypeError('File name does not contain .csv')
    else:
        raise TypeError('File name not a string')
