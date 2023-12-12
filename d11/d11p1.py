from itertools import combinations

input = ''
with open('./d11/input.txt', 'r') as f:
    input = f.read()

lines = [list(line.strip()) for line in input.split('\n') if line]

# Find the expansions
expand_columns = []
expand_rows = []
for y in range(len(lines)):
    # check the row
    if '#' not in lines[y]:
        expand_rows.append(y)

for x in range(len(lines[y])):
    saw_galaxy = False
    for y in range(len(lines)):
        if lines[y][x] == '#':
            saw_galaxy = True
            break
    if not saw_galaxy:
        expand_columns.append(x)

# expand the rows first, 
# starting from the end to not mess stuff up
for e in reversed(expand_rows):
    new_row = list('.' * len(lines[0]))
    lines.insert(e+1, new_row)
# expand the columns
for y in range(len(lines)):
    for e in reversed(expand_columns):
        a = lines[y]
        b = e
        #print(e)
        lines[y].insert(e+1, '.')
# done expanding

# build the set
galaxies = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            galaxies.add((y,x))
# iterate 
sum = 0
for c in combinations(galaxies, 2):
    if (6,1) in c and (11,5) in c:
        a = 'foo'
    distance = abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])
    #print(distance)
    sum = sum + distance
print(sum)


# for line in lines:
#     print(''.join(line))
