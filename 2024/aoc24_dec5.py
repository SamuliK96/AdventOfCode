# Advent of Code 2024. December 5

import itertools

def get_data():
    rules = {}
    with open("aoc24_dec5_rules.txt") as file:
        for line in file:
            line = [int(_) for _ in line.split("|")]
            if line[0] not in rules:
                rules[line[0]] = [line[1]]
            else:
                rules[line[0]].append(line[1])
    
    updates = []
    with open("aoc24_dec5_updates.txt") as file:
        for line in file:
            updates.append([int(x) for x in line.split(",")])
    
    return rules, updates

def main():
    rules, updates = get_data()
    silver_middles = 0
    gold_middles = 0
    for up in updates:
        if is_correct(up, rules):
            silver_middles += up[len(up)//2]
        else:
            pass #gold_middles += order(up, rules)
    print(silver_middles)
    print(gold_middles)

# ~Nth attempt for part 2 lol
'''def order(update: list, rules: dict):
    new = [update[0]]
    for element in update[1:]:
        for el in new:
'''
        



def is_correct(update: list, rules: dict):
    for i, el in enumerate(update):  
        if el in rules:
            rule = rules[el]

            for r in rule:
                if r in update and (update.index(r) < i):
                    return False
    
    return True


if __name__ == "__main__":
    main()
