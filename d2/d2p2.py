
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


power_sum = 0
for game in games:
    if game == '':
        continue
    gid, pgame = parse_game(game)

    mins = {}
    for hid, vals in pgame.items():
        for color, count in vals.items():
            if color not in mins:
                mins[color] = 0
            mins[color] = max(mins[color], count)
    # print(gid)
    # for k,v in mins.items():
    #     print(f"{k}: {v}")
    power = 1
    for v in mins.values():
        power = power * v
    print(f'GID: {gid}, Power: {power}')
    power_sum = power_sum + power
    
    
print(f'Possible: {power_sum}')
