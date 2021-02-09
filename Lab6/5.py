from collections import deque

def citire(orientat=False, nume_fisier="euler.in"):
    n=0
    with open(nume_fisier) as f:
        n = int(f.readline())
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
    if viz[i] == 0 or gr[i] % 2 == 1:
        eul = False

if eul is True:

    st = []


    def Euler(v):

        for i in la[v]:
            la[v].remove(i)
            la[i].remove(v)
            Euler(i)
        st.append(v)


    Euler(1)
    print(len(st))
    print(st)