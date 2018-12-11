
with open("Input8_1.txt") as f:
    data = list(map(int,f.readline().split(" ")))

class Node:
    
    nodeDict = {}
    currentPos = 0

    def __init__(self, Data):
        self.n_kids = Data[Node.currentPos]
        self.n_meta = Data[Node.currentPos + 1]
        self.Data = Data
        for kid in range(0, self.n_kids):
            Node.currentPos += 2
            Node(self.Data)
        Node.nodeDict[Node.currentPos] = self.MetaData()
        Node.currentPos += self.n_meta
    
    
    def MetaData(self):
        subtotal = 0
        begin = Node.currentPos + 2
        end = begin + self.n_meta
        for index in range(begin, end):
            subtotal += self.Data[index]
        return  subtotal

Node(data)

print(sum(Node.nodeDict.values()))