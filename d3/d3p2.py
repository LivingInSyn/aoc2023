
NUMBERS = '1234567890'
SYMBOLS = '!@#$%^&*()+-/='

input = ''
with open('./d3/input.txt', 'r') as f:
    input = f.read()

#load the input into a 2d array
lines = [line.strip() for line in input.split('\n')]
schematic = []
for line in lines:
    schematic.append(list(line))
# gather the coordinates for the symbols and numbers
numbers = []
symbols = []

isNumber = False
running_number = ''

schema_max_y = len(schematic)
schema_max_x = len(schematic[0])

for y in range(0,len(schematic)):
    for x in range(0, len(schematic[y])):
        # find numbers
        t = schematic[y][x]
        if schematic[y][x] in NUMBERS:
            isNumber = True
            running_number = running_number + schematic[y][x]
            if x == len(schematic[y])-1:
                numbers.append((running_number,(y,x)))
                isNumber = False
                running_number = ''
        elif schematic[y][x] not in NUMBERS:
            if running_number != '':
                px = x-1
                numbers.append((running_number,(y,px)))
            isNumber = False
            running_number = ''
        # find symbols
        if schematic[y][x] in SYMBOLS:
            symbols.append((schematic[y][x],(y,x)))
a = 'foo'

sum = 0
for symbol in symbols:
    if symbol[0] != '*':
        continue
    maxx = min(symbol[1][1]+1, schema_max_x)
    maxy = min(symbol[1][0]+1, schema_max_y)
    minx = max(0, symbol[1][1]-len(symbol[0]))
    miny = max(0, symbol[1][0]-1)

    touchnumbers = []
    for cy in range(miny, maxy+1):
        for cx in range(minx, maxx+1):
            for number in numbers:
                # check if the number is already in touchnumbers
                seen = False
                for n in touchnumbers:
                    if n[1] == number[1]:
                        seen = True
                        break
                if seen:
                    continue
                # end checking tn

                # check the x's. It should be <= the x from the tuple but > the x from the tuple minus the len
                if cx <= number[1][1] and cx > number[1][1] - len(number[0]):
                    # the y must be the same as the the check number
                    if cy == number[1][0]:
                        touchnumbers.append((number[0], number[1]))
    if len(touchnumbers) == 2:
        gear_ratio = int(touchnumbers[0][0]) * int(touchnumbers[1][0])
        print(f'symbol at {symbol[1]} touches exactly two. Gear Ratio: {gear_ratio}')
        sum = sum + gear_ratio
    
    a = 'foo'
print(sum)

