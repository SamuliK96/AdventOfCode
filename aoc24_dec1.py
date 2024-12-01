# Advent of code 2024, December 1

def part1():
    left_list = []
    right_list = []
    with open("aoc24_dec1_data.txt") as file:
        for line in file:
            line = line.split()
            #print(line)
            left_list.append(int(line[0]))
            right_list.append(int(line[-1]))
    
    left_list.sort()
    right_list.sort()
    print(sum(left_list)-sum(right_list))
    sums = 0
    while left_list:
        sums += abs(left_list.pop(0) - right_list.pop(0))
        
    print(sums)

def part2():
    nums = {}
    left_list = []
    right_list = []
    with open("aoc24_dec1_data.txt") as file:
        for line in file:
            line = line.split()
            #print(line)
            left_list.append(int(line[0]))
            right_list.append(int(line[-1]))

    for num in left_list:
        if num not in nums.keys():
            nums[num] = [1, 0]
        elif num in nums.keys():
            nums[num][0] += 1
        
    for num in right_list:
        if num in nums.keys():
            nums[num][-1] += 1

    nsum = 0
    for num in nums:
        nsum += num * nums[num][0] * nums[num][-1]
    
    print(nsum)

def test():
    left_list = [3,4,2,1,3,3]
    right_list = [4,3,5,3,9,3]
    nums = {}

    for num in left_list:
        if num not in nums.keys():
            nums[num] = [1, 0]
        elif num in nums.keys():
            nums[num][0] += 1
        
    for num in right_list:
        if num in nums.keys():
            nums[num][-1] += 1
    
    nsum = 0
    for num in nums:
        nsum += num * nums[num][0] * nums[num][-1]
    
    print(nsum)

if __name__ == "__main__":
    part2()
    #test()


'''
def part2():
    nums = {}
    with open("aoc24_dec1_data.txt") as file:
        for line in file:
            lnum, rnum = line.split()
            lnum = int(lnum)
            rnum = int(rnum)
            #print(line)
            if lnum not in nums.keys():
                nums[lnum] = [1, 0]
            elif lnum in nums.keys():
                nums[lnum][0] += 1
            
            if rnum in nums.keys():
                nums[rnum][-1] += 1

    nsum = 0
    for num in nums:
        nsum += num * nums[num][0] * nums[num][-1]
'''
