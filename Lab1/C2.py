from collections import deque


def citire(orientat=True,nume_fisier="c2.in"):
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
ciclu=False


def printCycle(q, v):
    global ciclu
    ciclu = True
    q2 = deque()
    lung = len(q)-1
    while q[lung] != v:
        q2.append(q[lung])
        lung -= 1
    q2.append(q[lung])
    while q2:
        print(q2[len(q2)-1], end=" ")
        q2.pop()


def DFS(q, viz):
    for v in la[q[len(q)-1]]:
        if viz[v] == 1:
            printCycle(q, v)
        elif viz[v] == 0:
            q.append(v)
            viz[v] = 1
            DFS(q, viz)
    viz[q[len(q)-1]] = 2
    q.pop()


viz = [0] * (n + 1)

for i in range(1, n+1):
    if viz[i] == 0:
        q = deque()
        q.append(i)
        viz[i] = 1
        DFS(q, viz)
if not ciclu:
    print("REALIZABIL")
