# Advent of Code 2024, December 6

import numpy as np

class Guard():
    def __init__(self, position: list, laboratory: list):
        self.position = position
        self.laboratory = laboratory
        self.direction = [-1, 0]
        self.steps = 0
    
    def step(self):
        self.laboratory[*self.position] = "X"
        new_pos = [int(sum(x)) for x in zip(self.position, self.direction)]
        while self.laboratory[*new_pos] == "#":
            self.turn()
            new_pos = [int(sum(x)) for x in zip(self.position, self.direction)]
        self.position = new_pos
        
        if -1 in self.position:
            raise IndexError        
        return None

    def turn(self):
        if self.direction == [-1, 0]: # up -> right
            self.direction = [0, 1]
        elif self.direction == [0, 1]: # right -> down
            self.direction = [1, 0]
        elif self.direction == [1, 0]: # down -> left
            self.direction = [0, -1]
        elif self.direction == [0, -1]: # left -> up
            self.direction = [-1, 0]
        
        return None

def main():
    data = []
    with open("test_data_6.txt") as file:
        for line in file:
            data.append(list(line.strip()))
    
    lab = np.array(data)

    pos = np.where(lab == "^")
    guard = Guard(pos, lab)

    while True:
        try:
            guard.step()
        except IndexError:
            break
    
    print(np.sum(guard.laboratory == "X"))
    
    
    
    
    
if __name__ == "__main__":
    main()

