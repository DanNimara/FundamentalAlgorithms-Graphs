from collections import deque

def citire(orientat=False, nume_fisier="intervale.in"):
    n=0
    with open(nume_fisier) as f:
        m = int(f.readline())
        n = m
        v = [[0, 0] for i in range(n+1)]
        for i in range(1,n+1):
            a, b = (int(x) for x in f.readline().split())
            v[i] = (a, b)
    return n, v


n, v = citire()
v.sort(key=lambda e: e[0])
# print(v)

la = [[] for i in range(n + 1)]
for i in range(1, n):
    for j in range(i+1, n+1):
        if v[i][1] > v[j][0]:
            la[i].append(j)
            la[j].append(i)

# for i in range(1,n+1):
#     print(i, la[i])

culoare = [0]*(n+1)


def colorare(la, v):
    culoare[1] = 1
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


colorare(la, v)
for i in range(1, n+1):
    print(culoare[i], end=" ")
    for v in la[i]:
        if culoare[v] == culoare[i]:
            print("PROST REZOLVAT")