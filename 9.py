for m in range(16, 23):
	for n in range(1, m):
		if m * (m + n) == 500:
			a = m **2 - n**2
			b = 2*m*n
			c = m **2 + n**2
			print(a*b*c)