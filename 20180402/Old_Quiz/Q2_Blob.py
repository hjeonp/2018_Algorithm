array = []

def maze(array, a, b):
    global n
    dir=[[1,0],[-1,0],[0,-1],[0, -1],[1,1],[1,-1],[-1,1],[-1,-1]]
    if a<0 or b<0 or a>=n or b>=n or array[a][b] == 0: return 0
    array[a][b]=0; sum=1
    for i in range(8): sum += maze(array, a + dir[i][0], b + dir[i][1])
    return sum

n=int(input())
list=[]

for i in range(n):
    list=[]; line=input()
    for j in range(n): list.append(int(line[j]))
    array.append(list)

for i in range(n):
    for j in range(n):
        S  = maze(array, i, j)
        if(S): list.append(S)

length = len(list)
print(length)
for i in list: print(i, end=" ")
