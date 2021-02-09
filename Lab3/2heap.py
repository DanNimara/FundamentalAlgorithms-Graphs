from sys import maxsize
import heapq

def citire(nume_fisier="grafpond.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        la=[[] for i in range(n+1)]
        lista = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(m):
            x, y, z = (int(a) for a in f.readline().split())
            la[x].append(y)
            la[y].append(x)
            lista[x][y] = z
            lista[y][x] = z

    return n, m, la, lista


n, m, la, lista = citire()
q = [0]*(n+1)
tata = [0]*(n+1)
d = [None]*(n+1)

d[1] = 0 # costul minim pentru 1 este 0, din el pornim
vf=n
cost=0
h=[]
heapq.heapify(h)
heapq.heappush(h,(0, 1)) #cost, apoi nod
while vf:
    ales = heapq.heappop(h)
    u = ales[1]
    while q[u] == 1:
        ales = heapq.heappop(h)
        u = ales[1]
    q[u] = 1
    for v in la[u]:
        if d[v] is not None and q[v] == 0 and lista[u][v] < d[v]:
            d[v] = lista[u][v]
            heapq.heappush(h,(lista[u][v],v))
            tata[v] = u
        elif q[v] == 0 and d[v] is None:
            d[v] = lista[u][v]
            heapq.heappush(h,(lista[u][v], v))
            tata[v] = u
    if u!=1:
        cost += lista[u][tata[u]]
        print(u, tata[u])
    vf -= 1
print(cost)