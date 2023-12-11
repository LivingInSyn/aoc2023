
input = ''
with open('./d10/input.txt', 'r') as f:
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
    print(cc)

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
    

print(path)
print(len(path))
print((len(path) + 1)/2)