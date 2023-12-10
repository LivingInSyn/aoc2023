

input = ''
with open('./d9/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]



def extrapolate(rows):
    exv = 0
    for ri in reversed(range(0, len(rows))):
        # if we're on row 0, we've already extrapolated, return the 
        # last index
        if ri == 0:
            return rows[0][-1]
        # A - 3 = 0
        # A - rows[ri-1][-1] = rows[ri][-1]
        # A = rows[ri][-1] + rows[ri-1][-1]
        ev = rows[ri][-1] + rows[ri-1][-1]
        rows[ri-1].append(ev)


tosum = []
for line in lines:
    initial_values = [int(v) for v in line.split(' ')]
    rows = [initial_values,]
    while True:
        rvals = []
        comprow = rows[-1]
        # exit condition
        all_zero = True
        for v in comprow:
            if v != 0:
                all_zero = False
                break
        if all_zero:
            break
        # built the next row
        for i in range(0, len(comprow) - 1):
            nval = comprow[i+1]-comprow[i]
            rvals.append(nval)
        rows.append(rvals)
        # print(rvals)
    ev = extrapolate(rows)
    print(ev)
    tosum.append(ev)

sum = 0
for t in tosum:
    sum = sum + t
print(sum)
