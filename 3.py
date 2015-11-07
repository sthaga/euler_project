mx = 600851475143
prime = []
prime_n = 2

while prime_n <= mx:
	if mx % prime_n == 0:
		prime.append(prime_n)
		mx /= prime_n
		prime_n = 2
	else:
		prime_n += 1

print(prime[len(prime)-1])