from collections import deque
from sys import maxsize


def citire(nume_fisier="graf.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        n, m = (int(x) for x in f.readline().split())
        la = [[] for i in range(n+2)]
        for i in range(m):
            i, j = (int(x) for x in f.readline().split())
            la[i].append(j)
            la[j].append(i)
    return n, m, la


n, m, la = citire()

viz = [0]*(n+1)
tata = [None]*(n+1)
d = [None]*(n+1)

ciclu = False

def DFS(s):
    viz[s]=1
    global nod, fin, ciclu
    for y in la[s]:
        if viz[y]==0:
            tata[y]=s
            d[y]=d[s]+1
            DFS(y)
        elif viz[y]==1 and y != tata[s]:
            if ciclu is False and (d[s]-d[y])%2 == 0:
                ciclu = True
                nod = s
                fin = y


nod = -1
fin = -1
for i in range(1, n+1):
    viz = [0] * (n + 1)
    tata = [None] * (n + 1)
    d = [None] * (n+1)
    d[i] = 0
    DFS(i)
    if ciclu is True:
        print("Graful nu este bipartit")
        c = []
        if d[nod] < d[fin]:
            nod,fin=fin,nod
        c.append(fin)
        while nod != fin:
            c.append(nod)
            nod = tata[nod]
        c.append(fin)
        print(c)
        break

if ciclu is not True:
    colorare = [-1]*(n+1)
    colorare[1] = 1
    q = deque()
    q.append(1)
    while q:
        u = q.pop()
        for v in la[u]:
            if colorare[v] == -1:
                colorare[v] = 1 - colorare[u]
                q.append(v)
    X = []
    Y = []
    for i in range(1,n+1):
        if colorare[i] == 1:
            X.append(i)
        else: Y.append(i)
    tata = [0]*(n+2)
    viz = [0]*(n+2)
    s = 0
    t = n+1
    le = [[] for i in range(n + 2)]
    li = [[] for i in range(n + 2)]
    # tratez graful ca un graf orientat, din s doar ies muchii ce merg intr-o bucata din graf care comunica cu cealalta bucata intr-un sens
    # celelalte se reunesc apoi in t
    mat = [[None for j in range(n + 2)] for i in range(n + 2)]
    for i in X:
        for v in la[i]:
            le[i].append(v)
            li[v].append(i)
            mat[i][v] = [0, 1]
    for i in X:
        le[s].append(i)
        li[i].append(s)
        mat[s][i] = [0, 1]
    for i in Y:
        le[i].append(t)
        li[t].append(i)
        mat[i][t] = [0, 1]


    def build_unsat_BF():
        for i in range(0, n+2):
            tata[i] = viz[i] = 0
        global s, t
        q.clear()
        q.append(s)
        viz[s] = 1
        while q:
            i = q.pop()
            for j in le[i]:     #arc direct
                if viz[j] == 0 and mat[i][j][1]-mat[i][j][0] > 0:
                    q.append(j)
                    viz[j] = 1
                    tata[j] = i
                    if j == t:
                        return True
            for j in li[i]:     #arc invers
                if viz[j]==0 and mat[j][i][0] > 0:
                    q.append(j)
                    viz[j] = 1
                    tata[j] = -i
                    if j == t:
                        return True
        return False


    q = deque()
    P = []
    a=0
    while build_unsat_BF() is True:
        P = []
        vf = t
        while vf != s:
            P.append(vf)
            if tata[vf] >= 0:
                vf = tata[vf]
            else:
                vf = - tata[vf]
        P.append(s)
        P.reverse()
        pond = []
        for i in range(len(P)-1):       # calculez I(P)
            if tata[P[i+1]] >= 0:
                pond.append(mat[P[i]][P[i+1]][1]-mat[P[i]][P[i+1]][0])
            else:
                pond.append(mat[P[i+1]][P[i]][0])
        val = min(pond)
        for i in range(len(P) - 1):
            if tata[P[i+1]] >= 0:
                mat[P[i]][P[i + 1]][0] = mat[P[i]][P[i+1]][0] + val # fluxul creste
            else:
                mat[P[i+1]][P[i]][0] = mat[P[i+1]][P[i]][0] - val
        P.clear()

    flux = 0
    for v in le[s]:
        flux += mat[s][v][0]
    print("Cuplajul maximal este "+str(flux))
    for i in range(1, n+1):
        for v in le[i]:
            if mat[i][v][0]>0 and v!=t:
                print(i, v)

else:
    print("Graful nu este bipartit")


