sum = 2
x = 2000000

for i in range(3, x, 2):
	j = 3
	while j < i ** 0.5:
		if i%j == 0:
			break
		j += 2
	if j > i ** 0.5:
		sum += i

print(sum)