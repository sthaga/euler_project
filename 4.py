def check(lst):
	i = 0
	while i < len(lst)/2:
		if lst[i] != lst[len(lst)-i-1]:
			return False
		i += 1
	return True


max = 0

for i in range(100, 1001):
	for j in range(100, 1001):
		mx = i * j
		mx = str(mx)
		pals = mx[0:len(mx)]
		if check(pals):
			if i*j >= max:
				max = i*j

print(max)