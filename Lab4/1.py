from collections import deque

def citire(nume_fisier="activitati.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        n=int(f.readline())
        durata = [0]*(n+1)
        durate = [int(z) for z in f.readline().split()]
        for i in range(1,n+1):
            durata[i] = durate[i-1]
        m = int(f.readline())
        mat = [[0 for j in range(n+2)] for i in range(n+2)]
        la=[[] for i in range(n+1)]
        gri = [0]*(n+1)
        gre = [0]*(n+1)
        for linie in f:
            x,y=(int(z) for z in linie.split())
            gri[y] += 1
            gre[x] += 1
            la[x].append(y)
            mat[x][y] = durata[x]
    return n, la, durata, mat, gri, gre


n, la, durata, mat, gri, gre = citire()

def DFS(i):
    viz[i] = 1
    for v in la[i]:
        if viz[v] == 0:
            DFS(v)
    sortTop.append(i)


viz = [0] * (n + 1)
sortTop = deque()
for i in range(1, n+1):
    if viz[i] == 0:
        DFS(i)

sortTop.reverse()
for i in range(1,n+1):
    if gri[i] == 0:
        la[0].append(i)
    if gre[i] == 0:
        la[i].append(n+1)
        mat[i][n+1] = durata[i]
tata = [0]*(n+2)
d=[None]*(n+2)
sortTop.appendleft(0)
d[0] = 0

for u in sortTop:
    for v in la[u]:
        if d[v] is not None:
            if d[u]+mat[u][v] > d[v]:
                d[v] = d[u] + mat[u][v]
                tata[v] = u
        if d[v] is None:
            d[v] = d[u] + mat[u][v]
            tata[v] = u
print("Timp minim "+str(d[n+1]))
print("Activitati critice: ",end="")
vf=tata[n+1]
while vf!=0:
    print(vf,end=" ")
    vf = tata[vf]
print()
for i in range(1,n+1):
    print(str(i)+': '+str(d[i])+" "+str(d[i]+durata[i]))