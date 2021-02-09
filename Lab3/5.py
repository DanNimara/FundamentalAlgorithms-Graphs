
def citire(nume_fisier="grafpond.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        mat=[[0] for j in range(n+1) for i in range(n+1)]
        lista = []
        for i in range(m):
            x, y, z = (int(a) for a in f.readline().split())
            lista.append((x,y,z))

    return n, m, lista, mat


n, m, lista, mat = citire()
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

print("Muchiile apcm in G:")
for i in range(n-1):
    print(lm[i][0],lm[i][1])
print("Cost", cost)

viz = [0]*(n+1)
parinti = [0]*(n+1)


def dfs(nod):
    viz[nod] = 1
    for vecin in lista:
        if vecin[0] == nod:
            if viz[vecin[1]] == 0:
                parinti[vecin[1]] = [nod, lista[nod][vecin[1]][2]]
                dfs(vecin[1])


#e1, e2, c=(int(x) for x in input().split())
e1,e2,c=int(3),int(5),int(4)
max = [0, 0 ,0]
dfs(e2)
nod = e2
muchie = parinti[nod]
while muchie != 0:
    if muchie[1] > max[2]:
        max = [muchie[0], nod, muchie[1]]
    nod = muchie[0]
    muchie = parinti[nod]
print(h[e1],h[e2])
#
# cost_max=0
# while e1 != e2:
#     for i in range(n-1):
#         if lm[i][0]==e1 or lm[i][1]==e1:
#             if mat[lm[i][0]][lm[i][1]]>cost_max:
#                 cost_max = mat[lm[i][0]][lm[i][1]]
#                 m1,m2=lm[i][0],lm[1][0]
#             if lm[i][0]==e1:
#