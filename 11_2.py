import numpy as np 



Input = 2568
sampleSize = 3

def calc_power(x,y,input):
    ID = x + 10
    return (((((ID*y)+input)*ID)%1000)//100)-5

def power_Grid(size, input = 2568):
    grid = np.zeros((size,size))
    for x in range(1,size +1):
        for y in range(1,size +1):
            grid[x-1,y-1] = calc_power(x,y,input)
    return grid

def square_sum(TLx,TLy,grid, size = 3):
    endx = TLx + size 
    endy = TLy + size 
    return np.sum(grid[TLx:endx,TLy:endy])

grid = power_Grid(300, Input)
MostPowerLoc = []
MostPower = 0 

for sampleSize in range(1,301):
    redoxSize = len(grid) - (sampleSize- 1)


    for x in range(redoxSize):
        for y in range(redoxSize):
            currentPower = square_sum(x,y,grid,sampleSize)
            if currentPower > MostPower:
                MostPower = currentPower
                MostPowerLoc = [x + 1,y + 1,sampleSize]

print(MostPowerLoc, MostPower)

