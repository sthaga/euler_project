sum = 0

x1 = 1
x2 = 2
x3 = 3

while x2 <= 4000000:
	x3 = x1 + x2
	x1 = x2
	x2 = x3
	if(x1 %2 == 0):
		sum += x1

print(sum)