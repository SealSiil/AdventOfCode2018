file = open("Input2_1.txt")

lines = file.readlines()

Multi = {2:0, 3:0}

for line in lines:
    tempdict = {}
    for letter in line:
        if letter in tempdict.keys():
            tempdict [letter] += 1
        else:
            tempdict [letter] = 1
    if 2 in tempdict.values():
        Multi[2] += 1
    if 3 in tempdict.values():
        Multi[3] += 1


print("-------------------")
print(Multi)
print(Multi[2] * Multi[3])