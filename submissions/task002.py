def p(g):
	h=[[4-x%2 for x in r]for r in g]
	d,e=len(h),len(h[0])
	z=[(x,y)for x in range(d)for y in range(e)if x in[0,d-1]or y in[0,e-1]]
	while z:
		a,b=z.pop();a%=len(h);b%=len(h[0])
		if h[a][b]>3:h[a][b]=0;z+=[(a+1,b),(a-1,b),(a,b+1),(a,b-1)]
	return h