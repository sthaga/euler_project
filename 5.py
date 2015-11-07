def ck_prime(x, lst):
	for num in lst:
		if x%num == 0:
			return False

	return True

prime = [2]
result = 1

for i in range(3,21):
	if ck_prime(i, prime):
		prime.append(i)

for x in prime:
	var = 1
	while x ** var < 20:
		var += 1
	var -= 1
	result *= x ** var

print(result)