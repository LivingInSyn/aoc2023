
input = ''
with open('./d10/einput4.txt', 'r') as f:
    input = f.read()

lines = [list(line.strip()) for line in input.split('\n') if line]

# find where s is today
sx = 0
sy = 0
for y in range(0,len(lines)):
    if sx > 0 and sy > 0:
        break
    for x in range(0, len(lines[y])):
        if lines[y][x] == 'S':
            sx = x
            sy = y
            break

print(sx, sy)
    

cx = sx
cy = sy
cc = 'S'
dir = 'any'
path = []
while True:
    cc = lines[cy][cx]
    # print(cc)

    if (dir == 'r' or dir == 'any') and cx+1 < len(lines[cy]):
        # keep going right
        if lines[cy][cx+1] == 'S':
            break
        elif lines[cy][cx+1] == '-':
            cx = cx+1 # cy didn't change
            path.append((cy,cx))
            dir = 'r'
            continue
        # change to up
        elif lines[cy][cx+1] == 'J':
            cx = cx+1 # cy didn't change
            path.append((cy,cx))
            dir = 'u'
            continue
        # change to down
        elif lines[cy][cx+1] == '7':
            cx = cx+1 # cy didn't change
            path.append((cy,cx))
            dir = 'd'
            continue
    elif (dir == 'l' or dir == 'any') and cx-1 >= 0:
        if lines[cy][cx-1] == 'S':
            break
        # keep going left
        elif lines[cy][cx-1] == '-':
            cx = cx-1 # cy didn't change
            path.append((cy,cx))
            dir = 'l'
            continue
        # change to up
        elif lines[cy][cx-1] == 'L':
            cx = cx-1 # cy didn't change
            path.append((cy,cx))
            dir = 'u'
            continue
        # change to down
        elif lines[cy][cx-1] == 'F':
            cx = cx-1 # cy didn't change
            path.append((cy,cx))
            dir = 'd'
            continue
    elif (dir == 'd' or dir == 'any') and cy+1 < len(lines):
        if lines[cy+1][cx] == 'S':
            break
        elif lines[cy+1][cx] == '|':
            cy = cy+1 # cx didn't change
            path.append((cy,cx))
            dir = 'd'
            continue
        elif lines[cy+1][cx] == 'J':
            cy = cy+1 # cx didn't change
            path.append((cy,cx))
            dir = 'l'
            continue
        elif lines[cy+1][cx] == 'L':
            cy = cy+1 # cx didn't change
            path.append((cy,cx))
            dir = 'r'
            continue
    elif (dir == 'u' or dir == 'any') and cy-1 >= 0:
        if lines[cy-1][cx] == 'S':
            break
        elif lines[cy-1][cx] == '|':
            cy = cy-1 # cx didn't change
            path.append((cy,cx))
            dir = 'u'
            continue
        elif lines[cy-1][cx] == 'F':
            cy = cy-1 # cx didn't change
            path.append((cy,cx))
            dir = 'r'
            continue
        elif lines[cy-1][cx] == '7':
            cy = cy-1 # cx didn't change
            path.append((cy,cx))
            dir = 'l'
            continue
    

path = set(path)


exclude = set()
#print(path)
# print(len(path))
# print((len(path) + 1)/2)

# build the top and bottom exclusions
for x in range(0, len(lines[0])):
    if (0, x) not in path:
        exclude.add((0, x))
    if (len(lines)-1, x) not in path:
        exclude.add((len(lines)-1, x))
# build the sides
for y in range(0, len(lines)):
    if (y, 0) not in path:
        exclude.add((y, 0))
    if (y, len(lines)-1) not in path:
        exclude.add((y, len(lines)-1))
# fill in everything touching an exclusion
while True:
    updated_something = False
    new_exc = []
    for exc in exclude:
        # check up
        upcheck = (exc[0]-1, exc[1])
        if exc[0]-1 >= 0 and upcheck not in exclude and upcheck not in path:
            new_exc.append(upcheck)
            updated_something = True
        # check down
        downcheck = (exc[0]+1, exc[1])
        if exc[0]+1 < len(lines) and downcheck not in exclude and downcheck not in path:
            new_exc.append(downcheck)
            updated_something = True
        # check right
        rcheck = (exc[0], exc[1]+1)
        if exc[1]+1 < len(lines[0]) and rcheck not in exclude and rcheck not in path:
            new_exc.append(rcheck)
            updated_something = True
        # check left
        lcheck = (exc[0], exc[1]-1)
        if exc[1]-1 >= 0 and lcheck not in exclude and lcheck not in path:
            new_exc.append(lcheck)
            updated_something = True
    for ne in new_exc:
        exclude.add(ne)
    if not updated_something:
        break

# for what's left, we'll follow straight up/down/right/left
# if we hit an edge or something in exclude, it's an exclude
# otherwise, we'll assume it's inside of the loop
inner = set()
for y in range(0,len(lines)):
    for x in range(0, len(lines[y])):
        if (y,x) in path or (y,x) in exclude:
            continue
        # go straight up
        up = True
        down = True
        left = True
        right = True
        for cy in reversed(range(0,y)):
            if lines[cy][x] == '-':
                up = False
                break
        # down
        for cy in range(y, len(lines)):
            if lines[cy][x] == '-':
                down = False
                break
        # right
        for cx in range(x, len(lines[y])):
            if lines[y][cx] == '|':
                right = False
                break
        # left 
        for cx in reversed(range(0,x)):
            if lines[y][cx] == '|':
                left = False
                break
        #if any are true
        if up or down or left or right:
            exclude.add((y,x))
        else:
            inner.add((y,x))

print(len(inner))
        


for y in range(0,len(lines)):
    drawline = ''
    for x in range(0, len(lines[y])):
        if (y,x) in exclude:
            drawline = drawline + 'O'
        elif (y,x) in path:
            drawline = drawline + lines[y][x]
        elif (y,x) in inner:
            drawline = drawline + 'I'
        else:
            drawline = drawline + '.'
    print(drawline)
            
