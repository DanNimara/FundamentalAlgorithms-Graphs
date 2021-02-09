from collections import deque

def citire(orientat=False, nume_fisier="c6.in"):
    with open(nume_fisier) as f:
        linie=f.readline()
        n, m = (int(z) for z in linie.split())
        la=[[] for i in range(n+1)]
        gr = [0 for i in range(n + 1)]
        for linie in f:
            x,y=(int(z) for z in linie.split())
            la[x].append(y)
            gr[x] += 1
            if not orientat:
                la[y].append(x)
                gr[y] += 1
    return n, la, gr


n, la, gr = citire()
culoare = [0]*(n+1)
viz = [1]*(n+1)
viz[0] = 0


def colorare():
    culori = [1, 2, 3, 4, 5, 6]
    if sum(viz) <= 6:
        for i in range(1, n+1):
            if viz[i]:
                culoare[i] = culori.pop(0)
    else:
        for i in range(1,n+1):
            if gr[i] <= 5 and viz[i] == 1:  #daca gradul e <=5 si nu a fost vizitat
                x = i
                viz[x] = 0
                break
        for v in la[x]:
            gr[v] -= 1
        colorare()
        for v in la[x]:
            if culoare[v] in culori:
                culori.remove(culoare[v])
        culoare[x] = culori[0]


colorare()

for i in range(1, n+1):
    print(culoare[i], end=" ")
    for v in la[i]:
        if culoare[v] == culoare[i]:
            print("PROST REZOLVAT")