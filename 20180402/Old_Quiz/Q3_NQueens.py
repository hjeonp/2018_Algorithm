global_count = 0

def promising(level):
    for i in range(1,level):
        if cols[level] == cols[i]: return False
        elif level-i==abs(cols[level]-cols[i]):return False
    return True

def queens(level):
    global global_count
    if not promising(level): return False
    elif level == N: global_count += 1
    else:
        for i in range(1,N+1):
            cols[level+1] = i
            queens(level+1)

arr = []
M = eval(input())
for i in range(M):
    N = eval(input())
    global_count = 0
    cols = [0 for i in range(N+1)]
    queens(0)
    arr.append(global_count)

for i in range(M): print(arr[i])
