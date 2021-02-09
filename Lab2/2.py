from collections import deque

def citire(orientat=False, nume_fisier="biconex.in"):
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
st = deque()
pct = set()
comp_bic = 0
comp_list = []


def DFS(i):
    viz[i] = 1
    niv_min[i] = nivel[i]
    global comp_bic
    for j in la[i]:
        if viz[j] == 0:
            st.append([i, j])
            nivel[j] = nivel[i]+1
            DFS(j)
            niv_min[i] = min(niv_min[i], niv_min[j])
            if niv_min[j] >= nivel[i]:
                comp_bic +=1
                while (not(st[len(st)-1][0] == i and st[len(st)-1][1] == j)) or (not(st[len(st)-1][0] == i and st[len(st)-1][1] == j)):
                    pct.add(st[len(st)-1][0])
                    pct.add(st[len(st)-1][0])
                    st.pop()
                pct.add(i)
                pct.add(j)
                comp_list.append(list(pct))
                st.pop()
                pct.clear()
        else:
            if nivel[j] < nivel[i]-1:
                niv_min[i] = min(niv_min[i], nivel[j])
                st.append([i, j])


nivel[1] = 1
DFS(1)
with open("biconex.out","w") as g:
    g.write(str(comp_bic)+"\n")
    for i in range(comp_bic):
        for j in comp_list[i]:
            g.write(str(j)+" ")
        g.write("\n")