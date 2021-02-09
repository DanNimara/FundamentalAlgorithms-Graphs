from collections import deque
from sys import maxsize

def citire(nume_fisier="secondbest.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        mat=[[0 for j in range(n+1)] for i in range(n+1)]
        lista = []
        much=[]
        for i in range(m):
            x,y,z=(int(a) for a in f.readline().split())
            lista.append((x,y,z))
            mat[x][y] = z
            mat[y][x] = z
            much.append((x,y))

    return n, m, lista, mat, much


n, m, lista, mat, much = citire()
lista.sort(key=lambda e: e[2])
lm=[]
tata = [0]*(n+1)
h = [0]*(n+1)


def init(u):
    tata[u] = h[u] = 0


def reprez(u):
    while tata[u] != 0:
        u = tata[u]
    return u


def union(u, v):
    ru=reprez(u)
    rv=reprez(v)
    if h[ru]>h[rv]:
        tata[rv] = ru
    else:
        tata[ru] = rv
        if h[ru] == h[rv]:
            h[rv] = h[ru]+1



for i in range(1,n+1):
    init(i)
cost = 0
nrmsel = 0
for i in range(m):
    if reprez(lista[i][0]) != reprez(lista[i][1]):
            cost += lista[i][2]
            lm.append((lista[i][0],lista[i][1]))
            union(lista[i][0],lista[i][1])
            nrmsel += 1
            if nrmsel == n-1:
                break

print("Costul este",cost)
for i in range(n-1):
    print(lm[i][0],lm[i][1])


def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))


def BFS(s):
    q = deque()
    q.append(s)
    viz[s]=1
    max[s][s][0]=0
    max[s][s][1]=0
    while len(q)>0:
        x = q.popleft()
        for y in la[x]:
            if viz[y] == 0:
                q.append(y)
                comp = mat[max[s][x][0]][max[s][x][1]]
                if mat[x][y] > comp:
                    max[s][y][0] = x
                    max[s][y][1]=y
                else:
                    max[s][y][0]=max[s][x][0]
                    max[s][y][1] = max[s][x][1]
                viz[y]=1

la=[[] for i in range(n+1)]
for i in lm:
    la[i[0]].append(i[1])
    la[i[1]].append(i[0])

max = [[[0, 0] for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    viz = [0] *(n+1)
    BFS(i)
minim = maxsize
muchramase = Diff(much,lm)
for i in muchramase:
    if mat[i[0]][i[1]]-mat[max[i[0]][i[1]][0]][max[i[0]][i[1]][1]]<maxsize:
        maxsize = mat[i[0]][i[1]]-mat[max[i[0]][i[1]][0]][max[i[0]][i[1]][1]]
        elim = (max[i[0]][i[1]][0], max[i[0]][i[1]][1])
        add = (i[0], i[1])

cost = cost - mat[elim[0]][elim[1]] + mat[add[0]][add[1]]
print("Noul cost este",cost)
lm.remove(elim)
lm.append(add)
for i in range(n-1):
    print(lm[i][0],lm[i][1])


