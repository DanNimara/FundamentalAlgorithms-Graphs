from collections import deque

def citire(orientat=True, nume_fisier="eulerb.in"):
    n=0
    with open(nume_fisier) as f:
        n = int(f.readline())
        la=[[] for i in range(n+1)]
        gri = [0 for i in range(n + 1)]
        gre = [0 for i in range(n + 1)]
        for linie in f:
            x,y=(int(z) for z in linie.split())
            la[x].append(y)
            gre[x] += 1
            gri[y] += 1
            if not orientat:
                la[y].append(x)
                gr[y] += 1
    return n, la, gri, gre


n, la, gri, gre = citire()
viz = [0]*(n+1)


def BFS(s):
    q = deque()
    q.append(s)
    viz[s] = 1
    while len(q) > 0:
        x = q.popleft()
        for y in la[x]:
            if viz[y] == 0:
                q.append(y)
                viz[y] = 1


BFS(1)
eul = True
for i in range(1,n+1):
    if gri[i] != gre[i]:
        eul = False

if eul is True:

    st = []


    def Euler(v):

        for i in la[v]:
            la[v].remove(i)
            Euler(i)
        st.append(v)


    Euler(1)
    st.pop()
    st.reverse()
    print(len(st))
    print(st)
else:
    print("NU")

