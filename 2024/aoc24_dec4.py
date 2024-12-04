# Advent of Code 2024, December 4

import re
import numpy as np

def silver():
    data = []
    with open("aoc24_dec4_data.txt") as file:
        for line in file:
            data.append(line.strip()+len(line)*"0")
    xmas_tot = 0

    # Create array from data
    data = np.array(data)

    # Original character array, before modifications
    xmas_tot += count_xmas(data)
    
    # Transposed original array
    data_T = transpose_array(data)
    xmas_tot += count_xmas(data_T)
    
    # Set up new arrays to hold original array shifted left & right to account for diagonals
    shift_left  = np.zeros_like(data)
    shift_right = np.zeros_like(data)

    for i in range(len(data)):
        shift_left[i] =  "".join(np.roll(list(data[i]),-i))
        shift_right[i] = "".join(np.roll(list(data[i]), i))

    # Transposed and shifted arrays
    shift_right_T = transpose_array(shift_right)
    shift_left_T  = transpose_array(shift_left)
    xmas_tot += count_xmas(shift_right_T)
    xmas_tot += count_xmas(shift_left_T)

    print(xmas_tot)

def count_xmas(array):
    xmas = 0
    for line in array:
        xmas += len(re.findall(r"XMAS", line))
        xmas += len(re.findall(r"SAMX", line))
    return xmas

def transpose_array(array):
    array_T = ["".join(row) for row in zip(*array)]
    return array_T

def gold():
    data = []
    crosses = 0
    with open("aoc24_dec4_data.txt") as file:
        for line in file:
            data.append(line.strip())


    for i in range(len(data)-2):
        for ii in range(len(data[i])-2):
            if data[i][ii] == "M":
                if data[i][ii+2] == "S":
                    if data[i+1][ii+1] == "A":
                        if data[i+2][ii] == "M":
                            if data[i+2][ii+2] == "S":
                                crosses += 1
                elif data[i][ii+2] == "M":
                    if data[i+1][ii+1] == "A":
                        if data[i+2][ii] == "S":
                            if data[i+2][ii+2] == "S":
                                crosses += 1
            elif data[i][ii] == "S":
                if data[i][ii+2] == "S":
                    if data[i+1][ii+1] == "A":
                        if data[i+2][ii] == "M":
                            if data[i+2][ii+2] == "M":
                                crosses += 1
                elif data[i][ii+2] == "M":
                    if data[i+1][ii+1] == "A":
                        if data[i+2][ii] == "S":
                            if data[i+2][ii+2] == "M":
                                crosses += 1
    
    print(crosses)  
    
if __name__ == "__main__":
    gold()