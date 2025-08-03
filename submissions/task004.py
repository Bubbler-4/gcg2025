def p(g):
	for r,R in enumerate(g):
		for c,C in enumerate(R):
			if 0<C==g[r][c-1]==g[r-1][c]:
				g[r-1][c-1]=C;g[r-1][c]=0;g[r][c]=0;c-=1
				while g[r][c]:c-=1
				g[r][c]=C
	return[[0]+r[:-1]for r in g]