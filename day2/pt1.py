import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt', 'r') as file:
    lines = file.read().splitlines()

horizontal_val = 0
depth_val = 0

for index, line in enumerate(lines):
    x = re.search(r"\D*\s(\d*)", line)
    crnt_val = int(x.group(1))
    if line.startswith('forward'):
        horizontal_val = horizontal_val + crnt_val
    elif line.startswith('down'):
        depth_val = depth_val + crnt_val
    elif line.startswith('up'):
        depth_val = depth_val - crnt_val

final_res = horizontal_val * depth_val

print(f'Final result = {final_res}')


    