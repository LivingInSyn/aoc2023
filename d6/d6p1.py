
input = ''
with open('./d6/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]

times = [int(t) for t in lines[0].split(':')[1].strip().split(' ') if t]
dists = [int(d) for d in lines[1].split(':')[1].strip().split(' ') if d]

ways_to_win = []
for race in range(0, len(times)):
    race_win_count = 0
    for hold_time in range(0, times[race]):
        ms = hold_time
        move_time = times[race] - hold_time
        distance = ms * move_time
        if distance > dists[race]:
            race_win_count = race_win_count + 1
            #print(f'race: {race} - win with ht: {hold_time}, distance: {distance}')
    ways_to_win.append(race_win_count)
    #print(f'There are {race_win_count} ways to win race {race}')

product = 1
for w in ways_to_win:
    product = product * w
print(product)