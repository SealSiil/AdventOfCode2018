file = open("Input1_1.txt")

Lines = file.readlines()

acum = sum(map(int, Lines))

print(acum)
