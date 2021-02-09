from collections import deque
from sys import maxsize


def BFS(mymat, n, m, pair):

    deplx = [-1, 1, 0, 0, 1, 1, -1, -1]
    deply = [0, 0, -1, 1, -1, 1, 1, -1]
    viz = [[0 for j in range(m+2)] for i in range(n+2)]
    d = [[None for j in range(m + 2)] for i in range(n + 2)]
    q = deque()
    viz[pair[0]][pair[1]] = 1
    d[pair[0]][pair[1]] = 1
    q.append(pair)
    while q:
        curr_cell = q.popleft()
        x = curr_cell[0]
        y = curr_cell[1]
        for i in range(8):
            vx = x + deplx[i]
            vy = y + deply[i]
            neigh_cell = [vx, vy]
            if mymat[vx][vy] == 0 and viz[vx][vy] == 0 and vx>=1 and vx<=n and vy>=1 and vy<=m:
                d[vx][vy] = d[x][y] + 1
                viz[vx][vy] = 1
                q.append(neigh_cell)
    return d



with open("rj.in") as f:
    n,m=(int(l) for l in f.readline().split())
    mat = [[0 for i in range(m+2)] for j in range(n+2)]
    r = [[0 for i in range(m+2)] for j in range(n+2)]
    jul = [[0 for i in range(m + 2)] for j in range(n + 2)]
    for i in range(1,n+1):
        linie = f.readline()
        for j in range(1, m+1):
            if linie[j-1] == "R":
                romeo = [i, j]
                #r[i][j] = 0
            elif linie[j-1] == "J":
                julieta = [i, j]
            elif linie[j-1] == "X":
                r[i][j] = 1
                jul[i][j] = 1

drum1 = BFS(r, n, m, romeo)
drum2 = BFS(jul, n, m, julieta)
tmin = maxsize
xi = 0
yi = 0
for k in range(1, n+1):
    for l in range(1, m+1):
        if drum1[k][l] is not None and drum2[k][l] is not None:
            if drum1[k][l] == drum2[k][l] and drum1[k][l] < tmin:
                xi = k
                yi = l
                tmin = drum1[k][l]
print(tmin, xi, yi)
