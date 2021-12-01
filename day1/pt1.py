import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    lines = file.read().splitlines()

increases = 0
decreases = 0

prev_value = -1

for index, line in enumerate(lines):
    line = int(line)
    if index == 0:
        print(f'{line} (N/A - no previous measurement)')
        prev_value = line
    else:
        if line > prev_value:
            print(f'{line} (increased)')
            increases = increases + 1
        else:
            print(f'{line} (decreased)')
            decreases = decreases + 1
        prev_value = line

print(f'Increases: {increases}')