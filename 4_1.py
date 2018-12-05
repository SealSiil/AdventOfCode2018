import pandas as pd

with open("Input4_1.txt") as f:
    lines = f.readlines()

for index in range(0, len(lines)):
    temp = lines[index].split(sep="]")
    temp[0] = temp[0] + "]"
    lines[index] = ",".join(temp)

with open("Input4_1Del.txt", "w") as f:
    f.writelines(lines)


df = pd.read_table("Input4_1Del.txt", header=None, names= ["Action"], delimiter=",", parse_dates=True)


df.sort_index(inplace=True)
print("-------")
print(df.head(20))



