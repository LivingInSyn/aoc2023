
input = ''
with open('./d4/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n')]

# parse the lines into two lists, winning numbers and owned numbers

#LAST_CARD = 6
LAST_CARD = 197

seen = {}
for x in range(1,LAST_CARD+1):
    seen[x] = 0
hands = {}



hand = 1
for line in lines:
    line = line.split(':')[1]
    winning_numbers, owned_numbers = line.split('|')
    winning_numbers = set([int(num) for num in winning_numbers.split(' ') if num != ''])
    owned_numbers = set([int(num) for num in owned_numbers.split(' ') if num != ''])
    intersection_len = len(winning_numbers & owned_numbers)

    # hands[hand] = (winning_numbers, owned_numbers, intersection_len)
    
    # we definitely saw hand this hand so add it:
    seen[hand] = seen[hand] + 1
    # add the next winning cards
    for times_process in range(0, seen[hand]):
        for i in range(1, intersection_len+1):
            if hand+i > LAST_CARD:
                continue
            seen[hand+i] = seen[hand+i] + 1
    hand = hand + 1

total_cards = 0
for h,v in seen.items():
    total_cards = total_cards + v
    
print(total_cards)