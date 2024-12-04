import sys
import re

def multiply(match):
    match = match.strip('mul(').strip(')')
    match = match.split(',')
    return int(match[0]) * int(match[1])

f = open(sys.argv[1], "r")

memory = f.readlines()
sum = 0
for line in memory:
    matches = re.findall("mul\(\d+,\d+\)", line)
    #print(matches)
    for match in matches:
        sum += multiply(match)

print(sum)