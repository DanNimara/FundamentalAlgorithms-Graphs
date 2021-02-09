
def citire(nume_fisier="kruskal.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        la=[[] for i in range(n+1)]
        lista = []
        for i in range(m):
            x,y,z=(int(a) for a in f.readline().split())
            lista.append((x,y,z))

    return n, m, lista


n, m, lista = citire()
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