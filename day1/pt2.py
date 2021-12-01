import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    lines = file.read().splitlines()

increases = 0
decreases = 0

prev_value = 1000

for index, line in enumerate(lines):
    if index < 2:
        print(f'{line} (N/A - no previous measurement)')
    else:
        a = int(lines[index - 2])
        b = int(lines[index - 1])
        c = int(lines[index])
        sum = a + b + c
        if sum > prev_value:
            print(f'{sum} (increased)')
            increases = increases + 1
        else:
            print(f'{sum} (decreased)')
            decreases = decreases + 1
        prev_value = sum

print(f'Increases: {increases}')