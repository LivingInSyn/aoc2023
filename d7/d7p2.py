
input = ''
with open('./d7/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]

hands = {}
for line in lines:
    hands[line.split(' ')[0]] = line.split(' ')[1]

# just checking for dups
# jh = list(hands.keys())
# for i in range(0, len(jh)):
#     for y in range(i+1, len(jh)):
#         if jh[i] == jh[y]:
#             print(f"DUP: {jh[i]}")


def get_hand_type(hand):
    freq = {}
    for c in hand:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] = freq[c] + 1
    shand = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    
    # greedily assign the jokers to the highest
    if 'J' in freq:
        num_jokers = freq['J']
        freq[shand[0][0]] = freq[shand[0][0]] + num_jokers
        freq['J'] = 0
        shand = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    
    
    if shand[0][1] == 5:
        return 7
    elif shand[0][1] == 4:
        return 6
    elif shand[0][1] == 3 and shand[1][1] == 2:
        return 5
    elif shand[0][1] == 3 and shand[1][1] == 1:
        return 4
    elif shand[0][1] == 2 and shand[1][1] == 2:
        return 3
    elif shand[0][1] == 2 and shand[1][1] == 1:
        return 2
    return 1
    
t1 = get_hand_type('32T3K')
t2 = get_hand_type('T55J5')
t3 = get_hand_type('KK677')
t4 = get_hand_type('KTJJT')
t5 = get_hand_type('QQQJA')


cdict = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7, 
    '8':8,
    '9':9,
    'T':10,
    'J':1,  #note now == 1, not 11
    'Q':12,
    'K':13,
    'A':14
}

def compare_hands(cw, nh):
    if cw is None:
        return nh
    cws = get_hand_type(cw)
    nhs = get_hand_type(nh)
    if nhs < cws:
        return nh
    elif nhs == cws:
        for i in range(0,5):
            if cw[i] == nh[i]:
                continue
            # if cw is stronger, return nh
            elif cdict[cw[i]] > cdict[nh[i]]:
                return nh
            # otherwise nh is stronger, return cw
            else:
                return cw
    else:
        return cw

t0 = compare_hands('KK677', 'KTJJT') 
a = 'foo'

ranked = []
while True:
    if len(hands) == 0:
        break
    weakest_key = None
    for hand, bid in hands.items():
        weakest_key = compare_hands(weakest_key, hand)
    ranked.append((weakest_key, hands[weakest_key]))
    del hands[weakest_key]

sum = 0
for i in range(0, len(ranked)):
    m = i + 1
    sum = sum + (m * int(ranked[i][1]))
print(sum)
