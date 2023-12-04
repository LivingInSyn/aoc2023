
input = ''
with open('./d4/input.txt', 'r') as f:
    input = f.read()

lines = [line.strip() for line in input.split('\n')]

# parse the lines into two lists, winning numbers and owned numbers
sum = 0
for line in lines:
    line = line.split(':')[1]
    winning_numbers, owned_numbers = line.split('|')
    winning_numbers = [int(num) for num in winning_numbers.split(' ') if num != '']
    owned_numbers = [int(num) for num in owned_numbers.split(' ') if num != '']
    
    intersection = set(winning_numbers) & set(owned_numbers)
    score = 2 ** (len(intersection)-1) if intersection else 0
    print(f'Score: {score}')
    sum = sum + score

    
    
print(sum)