from collections import deque
from sys import maxsize


def citire(nume_fisier="secvente.in"):
    n=0
    with open(nume_fisier) as f:
        n = int(f.readline())
        gr = [int(x) for x in f.readline().split()]
        gri = [0]*(n+1)
        gre = [0]*(n+1)
        for i in range(1, n+1):
            gri[i] = gr[i-1]
        gr = [int(x) for x in f.readline().split()]
        for i in range(1, n + 1):
            gre[i] = gr[i - 1]
    return n, gri, gre


n, gri, gre = citire()

tata = [0]*(2 * n+2)
viz = [0]*(2 * n+2)
s = 0
t = 2*n+1
le = [[] for i in range(2* n + 2)]
li = [[] for i in range(2* n + 2)]
# tratez graful ca un graf orientat, din s doar ies muchii ce merg intr-o bucata din graf care comunica cu cealalta bucata intr-un sens
# celelalte se reunesc apoi in t
mat = [[None for j in range(2 * n + 2)] for i in range(2 * n + 2)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            le[i].append(n+j)
            li[n+j].append(i)
            mat[i][n+j] = [0, 1]
for i in range(1, n+1):
    le[s].append(i)
    li[i].append(s)
    mat[s][i] = [0, gri[i]]
for i in range(n+1, 2*n+1):
    le[i].append(t)
    li[t].append(i)
    mat[i][t] = [0, gre[i-n]]

def build_unsat_BF(s, t):
    for i in range(0, 2*n+2):
        tata[i] = viz[i] = 0
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
            if viz[j] == 0 and mat[j][i][0] > 0:
                q.append(j)
                viz[j] = 1
                tata[j] = -i
                if j == t:
                    return True
    return False


q = deque()
P = []
while build_unsat_BF(s, t) is True:
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
    for i in range(len(P)-1):
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
sum = 0
for i in gri:
    sum += i
if flux == sum:
    for i in range(1, n+1):
        for j in le[i]:
            if mat[i][j][0] > 0 and v != t:
                u = i
                v = j
                if u > n:
                    u -= n
                if v > n:
                    v -= n
                print(u, v)
else:
    print("NU")


