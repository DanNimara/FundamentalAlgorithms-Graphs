import math


def citire(nume_fisier="retea2.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        c, b, m = (int(z) for z in linie.split())
        lista = []
        coord = []
        for i in range(c+b):
            x,y=(int(a) for a in f.readline().split())
            coord.append((x,y))
        for i in range(m):
            x, y = (int(a) for a in f.readline().split())
            cost = math.sqrt(math.pow(coord[x-1][0]-coord[y-1][0],2)+math.pow(coord[x-1][1]-coord[y-1][1],2))
            lista.append((x,y,cost))
    return c, b, m, lista


c, b, m, lista = citire()
t = c+b
lista.sort(key=lambda e: e[2])
lm=[]
tata = [0]*(t+1)
h = [0]*(t+1)


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


for i in range(1,t+1):
    init(i)
for i in range(1,c):
    if c>1:
        union(i, i+1)
nrmsel = c-1
cost = 0
for i in range(m):
    if reprez(lista[i][0]) != reprez(lista[i][1]):
            cost += lista[i][2]
            lm.append((lista[i][0], lista[i][1]))
            union(lista[i][0], lista[i][1])
            nrmsel += 1
            if nrmsel == t - 1:
                break

print("Costul este",cost)
for i in lm:
    print(i[0],i[1])