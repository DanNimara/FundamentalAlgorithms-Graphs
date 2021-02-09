import heapq

def citire(nume_fisier="bellman.in"):
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
            lista[x][y] = z

    return n, m, la, lista


n, m, la, lista = citire()
s = int(input())
q = [0]*(n+1)
tata = [0]*(n+1)
d = [None]*(n+1)

d[s] = 0 # costul minim pentru 1 este 0, din el pornim
ciclu = False
for i in range(1, n+1):
    for u in range(1, n+1):
        for v in la[u]:
            if d[v] is not None and d[u] is not None and d[u] + lista[u][v] < d[v]:
                d[v] = d[u] + lista[u][v]
                if i == n and ciclu is False:
                    ciclu = True
                    vf = v
                tata[v] = u
            elif d[v] is None and d[u] is not None:
                d[v] = d[u] + lista[u][v]
                tata[v] = u

if ciclu is True:
    print("Graful are ciclu de cost negativ:",end=" ")
    # print("vf", vf)
    # for i in range(1, n+1):
    #     vf = tata[vf]
    x = vf
    # print("vf", vf)
    print(vf, end=" ")
    vf=tata[vf]
    while vf != x:
        print(vf, end=" ")
        vf = tata[vf]
    print(vf,end=" ")
else:
    for i in range(1,n+1):
        dad = i
        drum = []
        while dad != s:
            drum.append(dad)
            dad = tata[dad]
        drum.append(dad)
        drum.reverse()
        print(drum)