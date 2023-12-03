
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
for number in numbers:
    maxx = min(number[1][1]+1, schema_max_x)
    maxy = min(number[1][0]+1, schema_max_y)
    minx = max(0, number[1][1]-len(number[0]))
    miny = max(0, number[1][0]-1)

    touches_symbol = False
    for cy in range(miny, maxy+1):
        if touches_symbol:
            break
        for cx in range(minx, maxx+1):
            for symbol in symbols:
                if symbol[1][0] == cy and symbol[1][1] == cx:
                    touches_symbol = True
                    break
    if touches_symbol:
        print(f'{number[0]} touches a symbol')
        sum = sum + int(number[0])
    else:
        print(f'{number[0]} touches NO symbol')
    a = 'foo'
print(sum)

