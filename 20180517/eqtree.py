stack = []
data = []
NodeArr = []

class Node:
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

#Input is via postfix order

raw_input = input()
for i in range(len(raw_input)):
    data.append(raw_input[i])
    if data[i].isdigit() == True:
        data[i] = int(stack[i])

print(data)

for i in range(len(stack)):
    if type(data[i]) == True:
        stack.append(data[i])

