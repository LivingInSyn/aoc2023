from typing import List
import re
import itertools
from functools import cache

input = ''
with open('./d12/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]

@cache
def check_replacements(ts: str, values: List[int]):
    springs = [s for s in ts.split('.') if s]
    if len(springs) != len(values):
        return False
    all_match = True
    for i in range(len(springs)):
        if len(springs[i]) != values[i]:
            all_match = False
            break
    return all_match
    a = 'foo'

@cache
def find_line_sol(springs: str, values: List[int]):
    unknowns = [m.start() for m in re.finditer('\?', springs)]
    possible_combinations = 0
    for l in range(0,len(unknowns)+1):
        for replace_indexs in itertools.combinations(unknowns, l):
            ts = springs
            # replace the indexes with '#'
            #print(replace_indexs)
            for ri in replace_indexs:
                ts = ts[:ri] + '#' + ts[ri+1:]
            # replace the rest with '.'
            ts = ts.replace('?', '.')
            # check
            if check_replacements(ts, values):
                possible_combinations = possible_combinations + 1
    #print(possible_combinations)
    return possible_combinations

def unfold(line, expansion = 5):
    springs,values = line.split(' ')
    new_springs = ''
    new_values = ''
    for _ in range(expansion):
        new_springs = new_springs + springs + '?'
        new_values = new_values + values + ','
    new_springs = new_springs[:-1]
    new_values = new_values[:-1]
    return f'{new_springs} {new_values}'


sum = 0
processed_lines = 0
for line in lines:
    line2 = unfold(line, 2)
    springs, values = line.split(' ')
    spring2, values2 = line2.split(' ')
    values = tuple([int(i) for i in values.split(',')])
    values2 = tuple([int(i) for i in values2.split(',')])
    c = find_line_sol(springs, values)
    c2 = find_line_sol(spring2, values2)
    m = c2/c
    # extrapolate
    for _ in range(3):
        c2 = c2 * m

    # print(c)
    sum = sum + c2
    processed_lines = processed_lines + 1
    print(processed_lines) 
print(sum)
