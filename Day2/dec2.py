# Advent of code 2023
# December 2

available = {
    'red': 12,
    'green': 13,
    'blue': 14 
}

def is_valid(sets: list):
    for set in sets:
        set = set.split(', ')
        for ball in set:
            num, color = ball.split()
            num = int(num)

            if      color == 'blue' and num > available['blue']: return False
            elif    color == 'green' and num > available['green']: return False
            elif    color == 'red' and num > available['red']: return False
            else:   continue
    
    return True

def set_power(sets: list):
    red = []
    green = []
    blue = []
    for set in sets:
        set = set.split(', ')      
        for ball in set:
            num, color = ball.split()
            #print(color, num)
            num = int(num)

            if color == 'blue': blue.append(num)
            elif color == 'green': green.append(num)
            elif color == 'red': red.append(num)
    
    #print(gmin, bmin, rmin)
    '''
    print('Red:', red)
    print('Blue:', blue)
    print('Green:', green)
    '''
    bmax = max(blue)
    rmax = max(red)
    gmax = max(green)
    #print(rmin, bmin, gmin)
    pow = gmax * bmax * rmax
    return pow

def main():
    sum = 0
    pow = 0
    file = open('aoc2.txt', 'r')
    for row in file:
        game = row.split(':')
        id = int(game[0].split(' ')[1])
        sets = game[1].split(';')
        pow += set_power(sets)
        if is_valid(sets):
            sum += id
        else:
            continue
    
    print(sum, pow)

main()