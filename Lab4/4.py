import heapq

def citire(nume_fisier="catun.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie = f.readline()
        n, m, nrf = (int(z) for z in linie.split())
        fort = set()
        for i in f.readline().split():
            fort.add(int(i))
        la = [[] for i in range(n+1)]
        lista = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(m):
            x, y, z = (int(a) for a in f.readline().split())
            la[x].append(y)
            la[y].append(x)
            lista[x][y] = z
            lista[y][x] = z

    return n, m, la, lista, fort


n, m, la, lista, fort = citire()
q = [0]*(n+1)
tata = [0]*(n+1)
d = [None]*(n+1)

vf = n
fin = 0
h = []
heapq.heapify(h)
for i in fort:
    lista[0][i] = 0
    lista[i][0] = 0
    la[0].append(i)
    la[i].append(0)
d[0]=0
f=[0]*(n+1)
heapq.heappush(h,(0, 0)) #cost, apoi nod
while h:
    ales = heapq.heappop(h)
    u = ales[1]
    while q[u] == 1 and len(h) > 0:
        ales = heapq.heappop(h)
        u = ales[1]
    q[u] = 1
    for v in la[u]:
        if d[v] is not None:
            if d[u] + lista[u][v] < d[v]:
                d[v] = d[u] + lista[u][v]
                heapq.heappush(h, (lista[u][v], v))
                tata[v] = u
            elif d[u] + lista[u][v] == d[v] and u < tata[v]: #aici fac pentru nodul precedent verificarea, nu pentru fortareata
                tata[v] = u
        elif d[v] is None:
            d[v] = d[u] + lista[u][v]
            heapq.heappush(h, (lista[u][v], v))
            tata[v] = u

for i in range(1,n+1):
    while tata[i] not in fort and tata[i] != 0:
        tata[i] = tata[tata[i]]
with open("catun.out", "w") as g:
    for i in range(1,n+1):
        g.write(str(tata[i])+" ")