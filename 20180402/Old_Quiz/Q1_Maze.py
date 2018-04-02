n, m=map(int, input().split())
check=[[10000 for i in range(m)] for j in range(n)]
board=[]

for i in range(n):
    s=input(); row=[]
    for ch in s: row.append(int(ch))
    board.append(row)

def check_maze(board, x, y ,tmp, check):
    check[x][y]=tmp
    if x+1<n and board[x+1][y]==0 and check[x+1][y]>tmp+1: check_maze(board, x+1, y, tmp+1, check)
    if y+1<m and board[x][y+1]==0 and check[x][y+1]>tmp+1: check_maze(board, x, y+1, tmp+1, check)
    if x-1>=0 and board[x-1][y]==0 and check[x-1][y]>tmp+1: check_maze(board, x-1, y, tmp+1, check)
    if y-1>=0 and board[x][y-1]==0 and check[x][y-1]>tmp+1: check_maze(board, x, y-1, tmp+1, check)
    
check_maze(board, n-1, 0, 1, check); print(check[0][m-1])
