
input = ''
with open('./d2/input.txt', 'r') as f:
    input = f.read()
games = [game.strip() for game in input.split('\n')]


def parse_game(game):
    gid = game.split(':')[0].split(' ')[1]
    dhands = game.split(':')[1].split(';')
    # cleanup the hands
    dhands = [hand.strip() for hand in dhands]
    # parse the hands
    hands = {}
    for i in range(0,len(dhands)):
        balls = [b.strip() for b in dhands[i].split(',')]
        hands[i] = {}
        for b in balls:
            num = int(b.split(' ')[0])
            color = b.split(' ')[1]
            hands[i][color] = num
    return gid, hands


possible_counter = 0
for game in games:
    if game == '':
        continue
    gid, pgame = parse_game(game)
    LIMITS = {
        'red': 12,
        'green': 13,
        'blue':  14
    }
    possible = True
    for hid, vals in pgame.items():
        for k,v in LIMITS.items():
            if k in vals:
                if vals[k] > LIMITS[k]:
                    possible = False
                    print(f'GID: {gid} impossible. {k} == {vals[k]}')
                    break      
    if possible:
        possible_counter = possible_counter + int(gid)
print(f'Possible: {possible_counter}')
