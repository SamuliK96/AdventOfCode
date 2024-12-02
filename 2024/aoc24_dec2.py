# Advent of Code 2024, December 2
import numpy as np

def main():
    with open("aoc24_dec2_data.txt") as file:
        data = file.readlines()


    safe = 0
    for line in data:
        line = list(map(int, line.split()))
        diffs = np.diff(line)

        if is_safe(diffs):
             safe += 1
             continue
        
        for i in range(len(line)):
            line2 = line[:]
            line2.pop(i)
            print(line2)
            diffs = np.diff(line2)

            if is_safe(diffs):
                safe += 1
                break

    print(safe)  

def is_safe(report: list):
        if not(all(n > 0 for n in report) or all(n < 0 for n in report)):
            return False
        elif all(abs(n) <= 3 for n in report):
            return True
        else:
            return False
            
    



if __name__ == "__main__":
    main()