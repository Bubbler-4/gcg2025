def p(g):
	return [[min(g[r//3][c//3],g[r%3][c%3])for c in range(9)] for r in range(9)]