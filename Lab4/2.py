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
k = int(input())
pc = [0]*(n+1)
for x in input().split():
    pc[int(x)] = 1
st = int(input())
q = [0]*(n+1)
tata = [0]*(n+1)
d = [None]*(n+1)

d[st] = 0 # costul minim pentru 1 este 0, din el pornim
vf=n
fin = 0
h=[]
heapq.heapify(h)
heapq.heappush(h,(0, st)) #cost, apoi nod
while h:
    ales = heapq.heappop(h)
    u = ales[1]
    # if d[u] is None:  #daca d[u] e inf, algoritmul se poate opri
    #     break
    while q[u] == 1:
        ales = heapq.heappop(h)
        u = ales[1]
    q[u] = 1
    for v in la[u]:
        if d[v] is not None and d[u] + lista[u][v] < d[v]:
            d[v] = d[u] + lista[u][v]
            heapq.heappush(h,(lista[u][v],v))
            tata[v] = u
            if pc[v] == 1:
                fin = v
                break
        elif d[v] is None:
            d[v] = d[u] + lista[u][v]
            heapq.heappush(h, (lista[u][v], v))
            tata[v] = u
            if pc[v] == 1:
                fin = v
                break

drum = []
print("Costul este",d[fin],"si drumul")
while fin != st:
    drum.append(fin)
    fin = tata[fin]
drum.append(st)
drum.reverse()

for i in drum:
    print(i, end=" ")