from collections import deque
from sys import maxsize


def citire(orientat=False,nume_fisier="b4.in"):
    n=0
    la=[]
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        la=[[] for i in range(n+1)]
        for i in range(m):
            x,y=(int(z) for z in f.readline().split())
            la[x].append(y)
            if not orientat:
                la[y].append(x)
        s, d = (int(z) for z in f.readline().split())

    return n, la, s, d


def find_paths(paths, path, parent, u):

    if u == -1:
        paths.append(path.copy())
        return

    for par in parent[u]:

        path.append(u)

        find_paths(paths, path, parent, par)

        path.pop()

n, la, s, d = citire()

# print(n)
# for i in range(n):
#     print(str(i)+": ",end="")
#     print(la[i])


def BFS(parent, n, start):
    dist = [maxsize for _ in range(n + 1)]
    q = deque()
    q.append(start)
    parent[start] = [-1]
    dist[start] = 0

    while len(q) > 0:
        u = q.popleft()
        for v in la[u]:
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                q.append(v)
                parent[v].clear()
                parent[v].append(u)
            elif dist[v] == dist[u] + 1:
                parent[v].append(u)


def intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


def intersect_paths(n, start, end):
    paths = []
    path = []
    parent = [[] for _ in range(n+1)]

    BFS(parent, n, start)

    find_paths(paths, path, parent, end)
    if len(paths)>1:
        inters = intersection(paths[0], paths[1])
    else:
        inters = paths[0]
    for i in range(1, len(paths)):
        inters = intersection(inters,paths[i])

    inters = reversed(inters)
    for i in inters:
        print(i, end=" ")


intersect_paths(n, s, d)