from collections import deque


def citire(orientat=False,nume_fisier="graf.in"):
    n=0
    la=[]
    pc=[]
    st=0
    with open(nume_fisier) as f:
        linie=f.readline()
        n,m=(int(z) for z in linie.split())
        la=[[] for i in range(n+1)]
        for i in range(m):
            linie=f.readline()
            x,y = (int(z) for z in linie.split())
            la[x].append(y)
            if not orientat:
                la[y].append(x)
        pc = [int(x) for x in f.readline().split()]
        st = int(f.readline())
    return n, la, pc, st


n, la, pc, st = citire()
# print(n)
# print(st)
# print(pc)
# for i in range(n):
#     print(str(i)+": ",end="")
#     print(la[i])

viz=[0]*(n+1)
tata=[None]*(n+1)
d=[None]*(n+1)
pcont=[None]*(n+1)
for i in range(1,n+1):
    if i in pc:
        pcont[i] = 1
    else: pcont[i] = 0
parc_bf = []

def BFS(s):

    q = deque()
    q.append(s)
    viz[s] = 1; d[s] = 0
    while len(q) > 0:
        x = q.popleft()
        parc_bf.append(x)
        for y in la[x]:
            if viz[y] == 0:
                q.append(y)
                viz[y] = 1
                tata[y] = x
                d[y] = d[x]+1
                if pcont[y] == 1:
                    return y


drum = []
found = BFS(st)
x = found
while x != st:
    print("Tatal lui: ", x, "este ", tata[x])
    drum.append(x)
    x = tata[x]
drum.append(x)
drum.reverse()
print(found)
print("Drumul este: ", drum)