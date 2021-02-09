from collections import deque
MAX = 500

def BFS(n, m, pair):

	deplx = [-1, 1, 0, 0]
	deply = [0, 0, -1, 1]
	global dist
	viz = [[0 for j in range(m+2)] for i in range(n+2)]
	d = [[None for j in range(m + 2)] for i in range(n + 2)]
	# tata =[[[0, 0] for j in range(m+2)] for i in range(n+2)]
	q = deque()
	viz[pair[0]][pair[1]] = 1
	d[pair[0]][pair[1]] = 0
	q.append(pair)
	if mat[pair[0]][pair[1]] == 1:
		dist = d[pair[0]][pair[1]]
		return pair
	while q:
		curr_cell = q.popleft()
		x = curr_cell[0]
		y = curr_cell[1]
		for i in range(4):
			vx = x + deplx[i]
			vy = y + deply[i]
			neigh_cell = [vx, vy]
			if viz[vx][vy] == 0 and vx>=1 and vx<=m and vy>=1 and vy<=n:
				# tata[vx][vy] = curr_cell
				d[vx][vy] = d[x][y] + 1
				viz[vx][vy] = 1
				if mat[vx][vy] == 1:
					dist = d[neigh_cell[0]][neigh_cell[1]]
					return neigh_cell
				q.append(neigh_cell)
	return [0, 0]



with open("b2.in") as f:
	n,m=(int(l) for l in f.readline().split())
	mat = [[0 for i in range(0, m+1)] for j in range(0, n+1)]
	for i in range(1,n+1):
		linie = f.readline().split()
		for j in range(1, m+1):
			mat[i][j] = int(linie[j-1])
	linie = f.readline()
	while linie:
		x, y = (int(l) for l in linie.split())
		dist = 0
		coord = BFS(n, m, [x, y])
		print(dist, coord)
		linie = f.readline()

viz=[0]*(n+1)
tata=[None]*(n+1)
d=[None]*(n+1)

