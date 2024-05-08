order = ['white', 'black', 'black']

num_hits = 0
for number in range(1,778):
    if '7' in str(number) and (number % 3 == 0 or number % 3 == 2):
        print(f'number {number} hit yes')
        num_hits += str(number).count('7')
    else:
        print(f'number {number} hit no')
    if number % 3 == 1:
        print('white can')
    else:
        print('black can')

print(num_hits)

