file = open("Input1_1.txt")

Lines = file.readlines()

Frq = {0 :1}
acum = 0 

while Frq[acum] < 2 :
    for line in Lines:
        acum += int(line)
        if acum in Frq.keys():
            Frq[acum] += 1
            print(acum)
            break
        else:
            Frq[acum] = 1

