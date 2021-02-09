from collections import deque

def citire(orientat=False,nume_fisier="c1.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        la=[[] for i in range(n+1)]
        for linie in f:
            x,y=(int(z) for z in linie.split())
            la[x].append(y)
            if not orientat:
                la[y].append(x)
    return n, la


n, la = citire()
# print(n)
# for i in range(n):
#     print(str(i)+": ",end="")
#     print(la[i])



ciclu = False
nod = -1
fin = -1


def DFS(s):
    viz[s] = 1
    global ciclu, nod, fin
    for y in la[s]:
        if viz[y] == 0:
            tata[y] = s
            d[y] = d[s] + 1
            DFS(y)
        elif viz[y] == 1 and y != tata[s]:
            if ciclu == False:
                ciclu = True
                nod = s
                fin = y


for i in range(1, n+1):
    viz = [0] * (n + 1)
    tata = [None] * (n + 1)
    d = [None] * (n+1)
    d[i] = 0
    DFS(i)
    if ciclu == True:
        c = []
        if d[nod] < d[fin]:
            nod, fin = fin, nod
        c.append(fin)
        while nod != fin:
            c.append(nod)
            nod = tata[nod]
        c.append(fin)
        print(c)
        break

if not ciclu:
    print("Graful este aciclic")
