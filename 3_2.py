import numpy as np
import re


def cleaning(data):
    match = pattern.match(data)
    Claims[int(match.group(1))] = ([int(match.group(2)),int(match.group(3))], [int(match.group(4)),int(match.group(5))])

def stake(marker, edgePos, edgeSize):
    for w in range((edgePos[0] + 1),(edgePos[0] + 1 + edgeSize[0])) :
        for h in range((edgePos[1] + 1),(edgePos[1] + 1 + edgeSize[1])):
            if fabric[w,h] == 0:
                fabric[w,h] = marker
            else:
                fabric[w,h] = -1
            

with open("Input3_1.txt") as f:
    lines = f.readlines()

fabric = np.zeros((2000,2000))
Claims = {}

pattern = r"[#](\d*)\s[@]\s(\d*)[,](\d*)[:]\s(\d*)[x](\d*)\s*"
pattern = re.compile(pattern)

for line in lines:
    cleaning(line)


for key in Claims.keys():
    marker = key
    edgePos, edgeSize = Claims[key]
    stake(marker, edgePos, edgeSize)


ClaimAreas = dict(zip(*np.unique(fabric, return_counts=True)))

for key in Claims.keys():
    edgeSize = Claims[key][1]
    try:
        if edgeSize[0]*edgeSize[1] == ClaimAreas[key]:
            print(key)
            break
    except:
        pass

