from collections import deque

def citire(orientat=False, nume_fisier="c6.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie = f.readline()
        n, m = (int(z) for z in linie.split())
        la = [[] for i in range(n+1)]
        gr = [0 for i in range(n + 1)]
        for linie in f:
            x, y = (int(z) for z in linie.split())
            la[x].append(y)
            gr[x] += 1
            if not orientat:
                la[y].append(x)
                gr[y] += 1
    return n, la, gr


n, la, gr = citire()

grt = [[0, 0] for i in range(n+1)]
for i in range(1, n+1):
    grt[i] = [i, gr[i]]
grt.sort(key=lambda e: e[1], reverse=True)
print(grt)

culoare = [-1]*(n+1)


def colorare(la, v):
    culoare[v[1]] = 1
    n = len(v)
    disp = [False]*(n)
    for i in range(2, n):
        for v in la[i]:
            if culoare[v] != -1:
                disp[culoare[v]] = True
        cul = 0
        for j in range(1, n+1):
            if disp[j] is False:
                cul = j
                break
        culoare[i] = cul
        for v in la[i]:
            if culoare[v] != -1:
                disp[culoare[v]] = False


va = [i for i in range(n+1)]
vb = [0]*(n+1)
vc = [0]*(n+1)
vd = []
ve = []
for i in range(1,n+1):
    vc[i] = grt[i-1][0]
# colorare(la, va)
# colorare(la, vb)

print(vc)
# for i in range(1, n+1):
#     print(culoare[i], end=" ")
#     for v in la[i]:
#         if culoare[v] == culoare[i]:
#             print("PROST REZOLVAT")