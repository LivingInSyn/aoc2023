
input = ''
with open('./d6/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]

time = int(lines[0].split(':')[1].replace(' ',''))
dist = int(lines[1].split(':')[1].replace(' ',''))

#forward first
first_win = 0
for hold_time in range(0, int(time/2)):
    ms = hold_time
    move_time = time - hold_time
    distance = ms * move_time
    if distance > dist:
        first_win = hold_time
        break
# backwards
last_win = 0
for hold_time in reversed(range(0, time)):
    ms = hold_time
    move_time = time - hold_time
    distance = ms * move_time
    if distance > dist:
        last_win = hold_time
        break

total = (last_win - first_win)+1
print(total)
