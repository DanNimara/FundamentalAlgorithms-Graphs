from collections import deque

def citire(orientat=True,nume_fisier="top.in"):
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


def DFS(i):
    viz[i] = 1
    for v in la[i]:
        if viz[v] == 0:
            DFS(v)
    q.append(i)


viz = [0] * (n + 1)
q = deque()
for i in range(1, n+1):
    if viz[i] == 0:
        DFS(i)

with open("sortaret.out","w") as g:
    q.reverse()
    for i in q:
        g.write(str(i)+" ")
