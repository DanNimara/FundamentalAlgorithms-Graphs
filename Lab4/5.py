from sys import maxsize


def citire(nume_fisier="floyd.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie = f.readline()
        n, m = (int(z) for z in linie.split())
        la = [[] for i in range(n+1)]
        mat = [[None for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n+1):
            mat[i][i] = 0
        for i in range(m):
            x, y, z = (int(a) for a in f.readline().split())
            la[x].append(y)
            mat[x][y] = z

    return n, m, la, mat
# 4 4 --pt ciclu de cost neg
# 1 2 1
# 2 3 -1
# 3 4 -1
# 4 1 -1

n, m, la, mat = citire()
q = [0]*(n+1)
tata = [0]*(n+1)
d = [[None for j in range(n+1)]for i in range(n+1)]
p = [[0 for j in range(n+1)]for i in range(n+1)]

def drum(i, j):
    if i != j:
        drum(i, p[i][j])
    print(j, end=" ")

for i in range(1,n+1):
    for j in range(1,n+1):
        if mat[i][j] is None:
            p[i][j] = 0
        else:
            d[i][j] = mat[i][j]
            if i!=j:
                p[i][j] = i
ciclu = False
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][j] is not None and d[i][k] is not None and d[k][j] is not None:
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j] = d[i][k]+d[k][j]
                    p[i][j] = p[k][j]
                    if d[i][j] < 0:
                        vf = i
                        ciclu = True
                        break
            elif d[i][j] is None and d[i][k] is not None and d[k][j] is not None:
                d[i][j] = d[i][k] + d[k][j]
                p[i][j] = p[k][j]
        if ciclu:
            break
    if ciclu:
        break


if ciclu:
    print("Un ciclu de cost negativ:",end=" ")
    drum(i, p[i][i])
    print(i)

else:
        exc = [0]*(n+1)

        for i in range(1,n+1):
            currmax=0
            for j in range(1,n+1):
                if d[i][j] is not None:
                    if d[i][j] > currmax:
                        currmax = d[i][j]
            exc[i] = currmax
        print(exc)
        raza = maxsize
        for i in range(1, n+1):
            if exc[i]<raza:
                raza = exc[i]
        print("Raza grafului: "+str(raza))

        centru=[]
        for i in range(1, n+1):
            if exc[i]==raza:
                centru.append(i)
        print(centru)
        diam = max(exc)
        print("Diametrul grafului: "+str(diam))
        lant = False
        for i in range(1, n+1):
            for j in range(1, n+1):
                if lant is False and d[i][j] == diam:
                    lant = True
                    drum(i,j)