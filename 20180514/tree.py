import os
import sys
import queue

class Node:
    def __init__(self, key = None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

A.left = B; A.right = C;
B.parent = A; B.left = D; C.parent = A; C.left = F;
D.parent = B; D.left = E; F.parent = C; F.left = G; F.right = H;
E.parent = C; G.parent = F; H.parent = F;

def preorder_tree_walk(ROOT):
    if ROOT !=  None:
        print(ROOT.key)
        preorder_tree_walk(ROOT.left)
        preorder_tree_walk(ROOT.right)

def level_order_tree_traversal(ROOT):
    q = queue.Queue()
    q.put(ROOT)
    while q.empty() != 0:
        v = q.get()
        print(v)
        if v.left != None: v.put(v.left)
        if v.right != None: v.put(v.right)

preorder_tree_walk(A)
level_order_tree_traversal(A)
