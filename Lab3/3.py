from sys import maxsize


def lev(a, b):
    if len(b) == 0:
        return len(a)
    elif len(a) == 0:
        return len(b)
    elif a[0] == b[0]:
        return lev(a[1:], b[1:])
    else:
        c1 = lev(a[1:], b)
        c2 = lev(a, b[1:])
        c3 = lev(a[1:], b[1:])
        return 1 + min(c1, c2, c3)


def init(u):
    tata[u] = h[u] = 0


def reprez(u):
    while tata[u] != 0:
        u = tata[u]
    return u


def union(u, v):
    ru = reprez(u)
    rv = reprez(v)
    if h[ru] > h[rv]:
        cluster[ru] = cluster[ru] + cluster[rv]
        cluster[rv].clear()
        tata[rv] = ru
    else:
        tata[ru] = rv
        cluster[rv] = cluster[rv] + cluster[ru]
        cluster[ru].clear()
        if h[ru] == h[rv]:
            h[rv] = h[ru]+1


with open("cuvinte.in") as f:
    v=[]
    for i in f.readline().split():
        v.append(i)
    n = len(v)
    tata = [0] * (n + 1)
    h = [0] * (n + 1)
    lista = []
    cluster = []
    for i in range(n-1):
        for j in range(i+1, n):
            dist = lev(v[i], v[j])
            lista.append((i, j, dist))
    lista.sort(key=lambda e: e[2])

    for i in range(n):
        init(i)
        cluster.append([i])
    k = 3
    grad = 0
    for i in lista:
        if reprez(i[0]) != reprez(i[1]):
            union(i[0], i[1])
            grad += 1
            if grad == n-k:
                break

grad_sep = maxsize    #muchia de cost minim care uneste doua componente conexe din T'
for i in range(n-1):
    for j in range(i,n):
        if reprez(i) != reprez(j) and lev(v[i], v[j]) < grad_sep:
            grad_sep = lev(v[i], v[j])

print("Gradul de separare este "+str(grad_sep)+", iar clusterele sunt:")

for i in range(n):
    if cluster[i]:
        for w in cluster[i]:
            print(v[w], end=" ")
        print()