
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
current_locations = []
for k in dmap.keys():
    if k.endswith('A'):
        current_locations.append(k)
while True:
    # exit condition
    all_z = True
    for cl in current_locations:
        if not cl.endswith('Z'):
            all_z = False
            break
    if all_z:
        break
    # iterate next steps
    dir = steps[step_counter%len(steps)]
    step_counter = step_counter + 1
    for i in range(0,len(current_locations)):
        current_locations[i] = dmap[current_locations[i]][dir]
    if step_counter % 1000 == 0:
        print(step_counter)
    #print(f'step: {step_counter}, new locations: {current_locations}')

print(step_counter)
