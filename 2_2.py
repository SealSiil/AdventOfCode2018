import itertools

def stripping(strippy):
    return strippy.strip()

file = open("Input2_1.txt")

lines = file.readlines()

lines = map(stripping, lines)


for combo in itertools.combinations(lines, 2):
    temp = []
    error = 0 
    for index in range(len(combo[0])):
        if combo[0][index] == combo[1][index]:
            temp.append(combo[0][index])
        else:
            error += 1
    if error < 2:        
        print("".join(temp))
        break