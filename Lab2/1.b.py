from collections import deque

def citire(orientat=False, nume_fisier="ex1.in"):
    n = 0
    la = []
    with open(nume_fisier) as f:
        linie = f.readline()
        n, m = (int(z) for z in linie.split())
        la = [[] for i in range(n + 1)]
        for linie in f:
            x, y = (int(z) for z in linie.split())
            la[x].append(y)
            if not orientat:
                la[y].append(x)
    return n, la


n, la = citire()

viz = [0] * (n + 1)

nivel = [None]*(n+1)
niv_min = [None]*(n+1)
tata = [None]*(n+1)
pc = set()
rad = 1
fii = 0
critice = False


def DFS(i):
    viz[i] = 1
    niv_min[i] = nivel[i]
    global fii, critice
    for j in la[i]:
        if viz[j] == 0:
            nivel[j] = nivel[i]+1
            tata[j]=i
            if i == rad:
                fii += 1
            DFS(j)
            niv_min[i] = min(niv_min[i], niv_min[j])
            if niv_min[j] >= nivel[i]:
                critice = True
                pc.add(i)
        else:
            if nivel[j]<nivel[i]-1:
                niv_min[i] = min(niv_min[i],nivel[j])

nivel[1] = 1
DFS(1)
if fii == 1 and rad in pc:
    pc.remove(rad)
elif fii == 2 and rad not in pc:
    pc.add(rad)

if critice == False:
    print("retea 2-muchie conexa")
else:
    print(pc)