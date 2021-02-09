from collections import deque
from sys import maxsize

flux_corect = True

def citire(nume_fisier="retea.in"):
    n=0
    la=[]
    global flux_corect
    with open(nume_fisier) as f:
        n = int(f.readline())
        s, t = (int(x) for x in f.readline().split())
        m = int(f.readline())
        le = [[] for i in range(n+1)]
        li = [[] for i in range(n + 1)]
        mat = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(m):
            i, j, c, fl = (int(x) for x in f.readline().split())
            mat[i][j] = [fl, c]
            if fl > c:
                flux_corect = False
            le[i].append(j)
            li[j].append(i)
    return n, m, s, t, le, li, mat


n, m, s, t, le, li, mat = citire()

for i in range(1,n+1):
    flux_int = 0
    flux_ext = 0
    if i != s and i != t:
        for v in li[i]:
            flux_int += mat[v][i][0]
        for v in le[i]:
            flux_ext += mat[i][v][0]
        if flux_int != flux_ext:
            flux_corect = False
    elif i == s:
        for v in le[i]:
            flux_ext += mat[i][v][0]
        for v in li[t]:
            flux_int += mat[v][t][0]
        if flux_int != flux_ext:
            flux_corect = False

if flux_corect is True:
    print("DA")
    tata = [0]*(n+1)
    viz = [0]*(n+1)
    def build_unsat_BF():
        for i in range(1, n+1):
            tata[i] = viz[i] = 0
        global s, t
        q.clear()
        q.append(s)
        viz[s] = 1
        while len(q) > 0:
            i = q.pop()
            for j in le[i]:     #arc direct
                if viz[j]==0 and mat[i][j][1]-mat[i][j][0] > 0:
                    q.append(j)
                    viz[j] = 1
                    tata[j] = i
                    if j == t:
                        return True
                elif viz[j]==0 and mat[i][j][1]-mat[i][j][0] == 0:
                    vf_min_cut.append(j)
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
    vf_min_cut = []
    while build_unsat_BF() is True:
        pond = []
        P = []
        vf = t
        while vf != s:
            P.append(vf)
            if tata[vf] > 0:
                vf = tata[vf]
            else:
                vf = - tata[vf]

        P.append(s)
        P.reverse()
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
        vf_min_cut.clear()
    flux = 0
    for v in le[s]:
        flux += mat[s][v][0]
    print(flux)
    for i in range(1, n+1):
        for v in le[i]:
            print(i, v, mat[i][v][0])
    print(flux)     # min_cut = max_flow
    for i in vf_min_cut:
        for v in li[i]:
            if mat[v][i][1]-mat[v][i][0] == 0:
                # print(i, v)     # afiseaza invers arcele fiindca eu plec din punctul de oprire spre cel din care vin
                print(v, i)

else:
    print("NU")


