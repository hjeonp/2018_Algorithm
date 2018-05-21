x = [20, 10, 5, 9, 15, 17, 7]

class Node:
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

NodeArr = [Node for x in range(100)]

def completeBT(arr, n):
    for i in range(n):

