# Adventure of code 2023
# December 1

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def main():
    sum = 0
    file = open('aoc1.txt', 'r')
    for row in file:
        for num in numbers:
            if num in row: row = row.replace(num, num[0]+str(numbers[num])+num[-1])

        nums = ""
        for ch in row:
            if ch.isnumeric(): nums += ch

        n = int(nums[0] + nums[-1])
        #print(n)
        sum += n
    

    print(sum)

main()