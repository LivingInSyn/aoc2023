import sys

input = ''
with open('./d5/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]


seeds = []


range_vals = {
    'h_to_l': [],
    't_to_h': [],
    'l_to_t': [],
    'w_to_l': [],
    'f_to_w': [],
    's_to_f': [],
    's_to_s': []
}

key = None
for line in lines:
    if 'seeds:' in line:
        seeds = [int(seed) for seed in line.split(':')[1].strip().split(' ')]
    #parsing magic vals
    if 'seed-to-soil' in line:
        key = 's_to_s'
        continue
    elif 'soil-to-fertilizer' in line:
        key = 's_to_f'
        continue
    elif 'fertilizer-to-water' in line:
        key = 'f_to_w'
        continue
    elif 'water-to-light' in line:
        key = 'w_to_l'
        continue
    elif 'light-to-temperature' in line:
        key = 'l_to_t'
        continue
    elif 'temperature-to-humidity' in line:
        key = 't_to_h'
        continue
    elif 'humidity-to-location' in line:
        key = 'h_to_l'
        continue
    # load the dict
    if key:
        vals = [int(val) for val in line.split(' ')]
        range_vals[key].append(vals)

def get_map(key, input):
    for r in range_vals[key]:
        source_range = range(r[1], r[1]+r[2])
        if input in source_range:
            delta = input - r[1]
            return r[0]+delta
    return input

# t0 = get_map('s_to_s', 99)
# t0 = get_map('s_to_s', 53)
# t1 = get_map('s_to_s', 79)
# t2 = get_map('s_to_s', 14)
# t3 = get_map('s_to_s', 55)
# t4 = get_map( 's_to_s', 13)


lowest_number = sys.maxsize
seed_ranges = []
for x in range(0, len(seeds), 2):
    seed_ranges.append(range(seeds[x], seeds[x]+seeds[x+1]))

rr = 0
for seed_range in seed_ranges:
    print(f'running range {rr} of {len(seed_ranges)}')
    for seed in seed_range:
        soil = get_map('s_to_s', seed)
        fert = get_map('s_to_f', soil)
        wate = get_map('f_to_w', fert)
        lite = get_map('w_to_l', wate)
        temp = get_map('l_to_t', lite)
        humi = get_map('t_to_h', temp)
        loca = get_map('h_to_l', humi)
        lowest_number = min(lowest_number, loca)
    rr = rr + 1
print(lowest_number)
