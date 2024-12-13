# Advent of Code 2024, December 13

import re
import numpy as np
from scipy import linalg

def main(name):
    
    with open(name) as file:
        data = file.read().split("\n\n")
    total = 0
    for line in data:
        nums = list(map(int, re.findall(r"\d+", line)))
        nums[-1] += 10000000000000; nums[-2] += 10000000000000
        eq = np.array([nums[0::2], nums[1::2]])
        sol = [round(x, 3) for x in linalg.solve(eq[:,0:2],eq[:,2])]
        if all(int(x) == x for x in sol):
            total += 3*sol[0] + sol[1]
            #print(total)
            
    print(total) 

if __name__ == "__main__":
    main("aoc24_dec13_data.txt")