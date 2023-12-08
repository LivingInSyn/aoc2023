
input = ''
with open('./d8/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]

steps = lines[0]
ts = []
for s in steps:
    if s == 'R':
        ts.append(1)
    else:
        ts.append(0)
steps = ts

lines = lines[1:]

def parse_line(line):
    id = line.split('=')[0].strip()
    tuple = line.split('=')[1].strip().replace('(', '').replace(')', '').split(',')
    tuple[0]=tuple[0].strip()
    tuple[1]=tuple[1].strip()
    return id, (tuple[0], tuple[1])

dmap = {}
for line in lines:
    id, t = parse_line(line)
    dmap[id] = t

dir_counter = 0
step_counter = 0
current_location = 'AAA'
while True:
    if current_location == 'ZZZ':
        break
    dir = steps[step_counter%len(steps)]
    step_counter = step_counter + 1
    current_location = dmap[current_location][dir]
    print(f'step: {step_counter}, new location: {current_location}')

print(step_counter)
