
input = ''
with open('./d7/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n') if line]

hands = {}
for line in lines:
    hands[line.split(' ')[0]] = line.split(' ')[1]


def get_hand_type(hand):
    freq = {}
    for c in hand:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] = freq[c] + 1
    shand = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    # greedily assign the jokers to the highest freq
    if 'J' in freq:
        print(f'shand before: {shand}')
        num_jokers = freq['J']
        if num_jokers == 5:
            freq = {'A': 5}
        elif shand[0][0] != 'J':
            freq[shand[0][0]] = freq[shand[0][0]] + num_jokers
            del freq['J']
        else:
            freq[shand[1][0]] = freq[shand[1][0]] + num_jokers
            del freq['J']
        shand = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        print(f'shand after: {shand}')
        a = 'foo'
    # return the val using the joker replacement
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
