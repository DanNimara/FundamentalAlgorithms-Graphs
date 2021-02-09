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
st = deque()    #stiva de muchii
pct = set()
comp = deque()
nod_max = 0
noduri = []
muchii = deque()


def DFS(i):
    viz[i] = 1
    niv_min[i] = nivel[i]
    global nod_max
    for j in la[i]:
        if viz[j] == 0:
            st.append([i, j])
            nivel[j] = nivel[i]+1
            DFS(j)
            niv_min[i] = min(niv_min[i], niv_min[j])
            if niv_min[j] >= nivel[i]:
                while (not(st[len(st)-1][0] == i and st[len(st)-1][1] == j)) or (not(st[len(st)-1][0] == i and st[len(st)-1][1] == j)):#scot muchiile din stiva
                    pct.add(st[len(st)-1][0])   #retin varfurile distincte din fiecare componenta in O(1)
                    pct.add(st[len(st)-1][0])
                    comp.append([st[len(st)-1][0], st[len(st)-1][1]])
                    st.pop()
                pct.add(i)
                pct.add(j)
                comp.append([st[len(st) - 1][0], st[len(st) - 1][1]])
                st.pop()
                if len(pct) > nod_max:  #daca subreteaua are numar mai mare de noduri decat cea anterioara
                    nod_max = len(pct)
                    noduri.clear()
                    noduri.extend(list(pct))
                    muchii.clear()
                    muchii.extend(comp)
                comp.clear()
                pct.clear()

        else:
            if nivel[j]<nivel[i]-1:
                niv_min[i] = min(niv_min[i],nivel[j])
                st.append([i, j])


nivel[1] = 1
DFS(1)

for i in range(nod_max):
    print(noduri[i],end=" ")
print()
for i in muchii:
    print(i[0],i[1])