# Advent of Code 2024, December 3
import re

def main():
    with open("aoc24_dec3_data.txt") as file:
        raw_data = ''.join(file.readlines())

    do_data = raw_data.split("do()")
    new_data = []

    for item in do_data:
        try:
            lst = item.split("don't()")
            new_data.append(lst[0])
        except:
            new_data.append(item)
    
    processed = ''.join(new_data)

    data = re.findall(r"mul\((\d+),(\d+)\)",processed)
    mul_sum = 0
    for item in data:
        x, y = item
        mul_sum += int(x) * int(y)
    
    print(mul_sum)


if __name__ == "__main__":
    main()